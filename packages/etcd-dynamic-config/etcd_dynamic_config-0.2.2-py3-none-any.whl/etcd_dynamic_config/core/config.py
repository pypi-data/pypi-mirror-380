"""Etcd configuration manager with caching and watching capabilities."""

import asyncio
import builtins
import logging
import threading
import time
from typing import Callable, Dict, Optional

from .logging import setup_logging


class EtcdConfig:
    """Universal etcd configuration manager with caching and real-time updates.

    This class is completely generic and works with any BaseEtcdClient subclass.

    Features:
    - In-memory caching for performance
    - Real-time watching for configuration changes
    - Thread-safe operations
    - Graceful error handling
    - Works with any BaseEtcdClient implementation
    """

    def __init__(self, client) -> None:
        """Initialize EtcdConfig with a client.

        Args:
            client: An instance of BaseEtcdClient or its subclass
        """
        if client is None:
            raise ValueError("client parameter is required")

        self._client = client

        # In-memory cache for configs
        self._cache: Dict[str, builtins.object] = {}
        self._lock = threading.RLock()
        self._logger = logging.getLogger("app.config")
        self._watch_cancel: Optional[Callable[[], None]] = None
        self._last_watcher_event_time = time.time()
        self._watcher_check_task: Optional[asyncio.Task] = None
        self._auth_error_detected = False

    def _load_initial(self) -> bool:
        """Load initial configuration from etcd. Returns True if successful."""
        # Validate etcd connection first
        if not self._client.validate_connection_settings():
            self._logger.error(
                "etcd_config_validation_failed",
                extra={
                    "event": {"category": ["config"], "action": "validation_failed"},
                    "etcd": {"validation_passed": False},
                },
            )
            return False

        try:
            # Synchronous initial load
            configs = self._client.get_config({})
            with self._lock:
                self._cache = dict(configs)
        except Exception as e:
            self._logger.error(
                "etcd_config_load_failed",
                extra={
                    "event": {"category": ["config"], "action": "load_failed"},
                    "error": {"message": str(e), "type": type(e).__name__},
                },
                exc_info=True,
            )
            return False
        # Enrich init log with diagnostic context
        prefix = self._client.get_config_prefix()
        key_map = self._client.get_etcd_key_map()
        expected_count = len(key_map)
        loaded_count = sum(
            1 for name in key_map.values() if configs.get(name) is not None
        )
        missing_names = [name for name in key_map.values() if configs.get(name) is None]

        # Log initialization result
        success = loaded_count > 0 and loaded_count == expected_count
        log_level = "info" if success else "warning"
        getattr(self._logger, log_level)(
            "etcd_config_initialized",
            extra={
                "event": {"category": ["config"], "action": "initialized"},
                "etcd": {
                    "prefix": prefix,
                    "initialization_success": success,
                },
                "config": {
                    "keys_expected": expected_count,
                    "keys_loaded": loaded_count,
                    "keys_missing": missing_names,
                },
            },
        )

        return success

    async def start(self) -> bool:
        """Start etcd configuration manager. Returns True if successful."""
        # Initial load in a thread to avoid blocking loop with CPU-bound work
        loop = asyncio.get_running_loop()
        success = await loop.run_in_executor(None, self._load_initial)

        if not success:
            self._logger.error(
                "etcd_config_start_failed",
                extra={
                    "event": {"category": ["config"], "action": "start_failed"},
                    "etcd": {"initial_load_success": False},
                },
            )
            return False

        # Attempt to start watcher for the control unit prefix
        watcher_started = False
        try:
            prefix = self._client.get_config_prefix()

            cancel = self._client.start_watch_prefix(prefix, self._get_event_handler())
            if cancel is not None:
                self._watch_cancel = cancel
                watcher_started = True
        except Exception:
            self._logger.warning(
                "etcd_watcher_start_failed",
                extra={
                    "event": {"category": ["config"], "action": "watcher_start_failed"},
                    "etcd": {"watcher_enabled": False},
                },
                exc_info=True,
            )

        self._logger.info(
            "etcd_config_started",
            extra={
                "event": {"category": ["config"], "action": "started"},
                "etcd": {
                    "watcher_started": watcher_started,
                    "mode": "watch" if watcher_started else "stub",
                },
            },
        )

        # Start watcher health check task
        if watcher_started:
            self._watcher_check_task = asyncio.create_task(self._watcher_health_check())

        return True

    async def _watcher_health_check(self):
        """Periodically check if watcher is still receiving events and restart if needed."""
        while True:
            try:
                await asyncio.sleep(300)  # Check every 5 minutes

                # If no events received in last 10 minutes, watcher might be dead
                time_since_last_event = time.time() - self._last_watcher_event_time
                if time_since_last_event > 600:  # 10 minutes
                    self._logger.debug(
                        "Watcher appears inactive, attempting restart",
                        extra={
                            "etcd": {
                                "time_since_last_event": int(time_since_last_event)
                            },
                            "event": {
                                "category": ["config"],
                                "action": "watcher_restart",
                            },
                        },
                    )

                    # Restart watcher
                    try:
                        if self._watch_cancel:
                            self._watch_cancel()
                            self._watch_cancel = None

                        # Force reconnection
                        self._client._client = None

                        # Restart watcher
                        prefix = self._client.get_config_prefix()
                        cancel = self._client.start_watch_prefix(
                            prefix, self._get_event_handler()
                        )
                        if cancel:
                            self._watch_cancel = cancel
                            self._last_watcher_event_time = time.time()
                            self._logger.debug(
                                "Watcher restarted successfully",
                                extra={
                                    "event": {
                                        "category": ["config"],
                                        "action": "watcher_restarted",
                                    }
                                },
                            )
                    except Exception:
                        self._logger.error(
                            "Failed to restart watcher",
                            exc_info=True,
                            extra={
                                "event": {
                                    "category": ["config"],
                                    "action": "watcher_restart_failed",
                                }
                            },
                        )

            except asyncio.CancelledError:
                break
            except Exception:
                self._logger.warning(
                    "watcher_health_check_error",
                    extra={
                        "event": {
                            "category": ["config"],
                            "action": "health_check_error",
                        },
                        "etcd": {"watcher_active": True},
                    },
                    exc_info=True,
                )

    def _get_event_handler(self):
        """Get the event handler function for watcher."""

        def _on_event(absolute_key: str) -> None:
            try:
                # Update last event time
                self._last_watcher_event_time = time.time()

                self._logger.info(
                    "etcd_watch_event",
                    extra={
                        "event": {"category": ["config"], "action": "watch_event"},
                        "etcd": {"key": absolute_key},
                    },
                )
                # Only handle keys we care about
                key_map = self._client.get_etcd_key_map()
                internal_name = key_map.get(absolute_key)
                if not internal_name:
                    self._logger.debug(
                        "etcd_watch_event_skipped",
                        extra={"etcd": {"key": absolute_key}},
                    )
                    return
                values = self._client.get_values_by_keys([absolute_key])
                raw_value = values.get(absolute_key)

                # Apply type coercion using client's method
                processed_value = self._client._coerce_config_value(
                    internal_name, raw_value
                )

                with self._lock:
                    self._cache[internal_name] = processed_value

                self._logger.info(
                    "etcd_config_key_updated",
                    extra={
                        "event": {"category": ["config"], "action": "key_updated"},
                        "etcd": {
                            "key": absolute_key,
                            "internal_name": internal_name,
                        },
                    },
                )

                # Apply dynamic log level changes immediately
                if internal_name in ("log_level", "log_sql_level"):
                    try:
                        # Read both levels from cache (with fallback defaults)
                        level = str(self._cache.get("log_level", "INFO")).upper()
                        sql_level = str(
                            self._cache.get("log_sql_level", "WARNING")
                        ).upper()
                        setup_logging(
                            level,
                            sql_level=sql_level,
                        )
                        self._logger.info(
                            "log_levels_reconfigured",
                            extra={
                                "event": {
                                    "category": ["config"],
                                    "action": "log_reconfigured",
                                },
                                "logging": {"level": level, "sql_level": sql_level},
                            },
                        )
                    except Exception:
                        self._logger.warning(
                            "log_level_apply_failed",
                            extra={
                                "event": {
                                    "category": ["config"],
                                    "action": "log_reconfigure_failed",
                                },
                                "logging": {"level": level, "sql_level": sql_level},
                            },
                            exc_info=True,
                        )
            except Exception as e:
                self._logger.warning(
                    "etcd_config_watch_callback_failed",
                    extra={
                        "event": {
                            "category": ["config"],
                            "action": "watch_cb_failed",
                        },
                        "error": {"message": str(e), "type": type(e).__name__},
                    },
                    exc_info=True,
                )

        return _on_event

    async def stop(self) -> None:
        try:
            if self._watcher_check_task is not None:
                self._watcher_check_task.cancel()
                try:
                    await self._watcher_check_task
                except asyncio.CancelledError:
                    pass
                self._watcher_check_task = None

            if self._watch_cancel is not None:
                self._watch_cancel()
                self._watch_cancel = None
        finally:
            return None

    async def get_all_configs(self) -> dict:
        # Return a copy to protect internal dict
        with self._lock:
            if self._cache:
                # Cache hit: return immediately and log it
                try:
                    self._logger.debug(
                        "etcd_config_cache_hit",
                        extra={
                            "event": {"category": ["config"], "action": "cache_hit"},
                            "config": {"keys_loaded": len(self._cache)},
                        },
                    )
                except Exception:
                    pass
                return dict(self._cache)
        # Fallback: if cache empty (e.g., before start), load synchronously in executor
        loop = asyncio.get_running_loop()
        try:
            result = await loop.run_in_executor(
                None, lambda: self._client.get_config({})
            )
            with self._lock:
                if not self._cache:
                    self._cache = dict(result)
                    # Cache miss: populated from etcd synchronously
                    try:
                        self._logger.info(
                            "etcd_config_cache_miss_loaded",
                            extra={
                                "event": {
                                    "category": ["config"],
                                    "action": "cache_miss_loaded",
                                },
                                "config": {"keys_loaded": len(self._cache)},
                            },
                        )
                    except Exception:
                        pass
            return dict(self._cache)
        except Exception as e:
            self._logger.error(
                "etcd_config_fallback_failed",
                extra={
                    "event": {"category": ["config"], "action": "fallback_failed"},
                    "error": {"message": str(e), "type": type(e).__name__},
                },
                exc_info=True,
            )
            return {}


__all__ = ["EtcdConfig"]
