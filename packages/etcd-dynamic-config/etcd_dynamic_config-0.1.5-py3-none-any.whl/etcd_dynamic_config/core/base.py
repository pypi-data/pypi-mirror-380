"""Base classes for etcd configuration management."""

import builtins
import logging
import os
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Optional, Tuple
from urllib.parse import urlparse

import yaml

try:
    import etcd3
except ImportError:
    etcd3 = None


class BaseEtcdClient:
    """Universal etcd client with YAML-based configuration management.

    This class provides the foundation for etcd configuration management
    using YAML configuration files for key mappings and type definitions.
    """

    def __init__(
        self,
        config_file_path: str,
        root_key: str,
        endpoint: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        ca_cert_path: Optional[str] = None,
        use_local_config: Optional[bool] = None,
    ):
        """Initialize the etcd client.

        Args:
            config_file_path: path to YAML configuration file
            root_key: root key prefix for etcd keys (e.g., "/APPS/MyService")
            endpoint: etcd server endpoint (defaults to EtcdSettings__HostName env var)
            username: etcd username (defaults to EtcdSettings__UserName env var)
            password: etcd password (defaults to EtcdSettings__Password env var)
            ca_cert_path: path to CA certificate
            use_local_config: whether to use local env vars instead of etcd
        """
        self._logger = logging.getLogger("app.base")

        # Load YAML configuration
        self._config_file_path = config_file_path
        self._root_key = root_key
        self._yaml_config = self._load_yaml_config()

        # Configuration from parameters or environment
        self._endpoint = endpoint or os.getenv("EtcdSettings__HostName")
        self._username = username or os.getenv("EtcdSettings__UserName")
        self._password = password or os.getenv("EtcdSettings__Password")

        # CA cert path with fallback
        if ca_cert_path:
            self._ca_pem_path = ca_cert_path
        else:
            env_path = os.getenv("EtcdSettings__CaCertPath")
            if env_path:
                self._ca_pem_path = env_path
            else:
                # Fallback to local pem directory
                self._ca_pem_path = str(
                    Path(__file__).resolve().parent / "pem" / "cag-ca-bundle.pem"
                )

        # Local config mode
        if use_local_config is not None:
            self._use_local_config = use_local_config
        else:
            self._use_local_config = (
                str(os.getenv("USE_LOCAL_CONFIG", "false")).lower() == "true"
            )

        self._client: Optional[builtins.object] = None

        # Initialize key mappings from YAML config
        self._etcd_key_map = self._build_etcd_key_map_from_yaml()
        self._env_var_map = self._build_env_var_map_from_yaml()
        self._type_map = self._build_type_map_from_yaml()

    def _load_yaml_config(self) -> Dict[str, Any]:
        """Load YAML configuration from file."""
        try:
            config_path = Path(self._config_file_path)
            if not config_path.exists():
                raise FileNotFoundError(
                    f"Configuration file not found: {self._config_file_path}"
                )

            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)

            if not isinstance(config, dict):
                raise ValueError("YAML configuration must be a dictionary")

            self._logger.info(
                "yaml_config_loaded",
                extra={
                    "event": {"category": ["config"], "action": "yaml_loaded"},
                    "config": {
                        "file_path": str(config_path),
                        "keys_count": len(config.get("etcd_key_map", [])),
                    },
                },
            )
            return config

        except Exception as e:
            self._logger.error(
                "yaml_config_load_failed",
                extra={
                    "event": {"category": ["config"], "action": "yaml_load_failed"},
                    "error": {"message": str(e), "type": type(e).__name__},
                },
                exc_info=True,
            )
            raise

    def _build_etcd_key_map_from_yaml(self) -> Dict[str, str]:
        """Build etcd key mappings from YAML config."""
        keys = self._yaml_config.get("key_map", [])
        base_prefix = self.get_config_prefix()

        key_map = {}
        for item in keys:
            if not isinstance(item, dict) or "key" not in item:
                continue
            etcd_key = f"{base_prefix}/{item['key']}"
            # Use the key directly as the internal name
            internal_name = item["key"]
            key_map[etcd_key] = internal_name

        return key_map

    def _build_env_var_map_from_yaml(self) -> Dict[str, str]:
        """Build environment variable mappings from YAML config."""
        keys = self._yaml_config.get("key_map", [])

        env_map = {}
        for item in keys:
            if not isinstance(item, dict) or "key" not in item:
                continue
            # Use the key directly as the internal name
            internal_name = item["key"]
            # Use the key name as the environment variable name
            env_map[internal_name] = internal_name

        return env_map

    def _build_type_map_from_yaml(self) -> Dict[str, str]:
        """Build type mappings from YAML config."""
        keys = self._yaml_config.get("key_map", [])

        type_map = {}
        for item in keys:
            if not isinstance(item, dict) or "key" not in item:
                continue
            # Use the key directly as the internal name
            internal_name = item["key"]
            type_str = item.get("type", "str")
            type_map[internal_name] = type_str

        return type_map

    def get_config_prefix(self) -> str:
        """Get the etcd key prefix for this configuration set.

        Returns:
            The prefix path in etcd (e.g., '/APPS/MyService')
        """
        dev_enabled = str(os.getenv("EtcdSettings__Dev", "false")).lower() == "true"

        root = self._root_key.strip()
        if not root.startswith("/"):
            root = f"/{root}"
        root = root.rstrip("/")
        return f"{'/dev' if dev_enabled else ''}{root}"

    def get_etcd_key_map(self) -> Dict[str, str]:
        """Get the mapping of etcd keys to internal names."""
        return dict(self._etcd_key_map)

    def get_env_var_map(self) -> Dict[str, str]:
        """Get the mapping of internal names to environment variables."""
        return dict(self._env_var_map)

    @staticmethod
    def _parse_host_port(endpoint: str) -> Tuple[str, int, str]:
        """Parse host, port, and scheme from endpoint URL."""
        parsed = urlparse(str(endpoint))
        host = parsed.hostname or "etcd-client"
        port = parsed.port or 2379
        scheme = parsed.scheme or "http"
        return host, int(port), scheme

    def validate_connection_settings(self) -> bool:
        """Validate etcd connection settings."""
        if self._use_local_config:
            self._logger.info(
                "using_local_config",
                extra={
                    "event": {"category": ["config"], "action": "local_config_enabled"},
                    "etcd": {"mode": "local_env"},
                },
            )
            return True
        if not self._endpoint:
            self._logger.error(
                "etcd_endpoints_not_configured",
                extra={
                    "event": {"category": ["config"], "action": "validation_failed"},
                    "etcd": {"endpoint_configured": False},
                },
            )
            return False
        return True

    def connect(self) -> Optional[builtins.object]:
        """Establish connection to etcd server."""
        if etcd3 is None:
            self._logger.error(
                "etcd3_package_not_installed",
                extra={
                    "event": {"category": ["config"], "action": "dependency_missing"},
                    "etcd": {"package_available": False},
                },
            )
            return None

        if self._client is None:
            if not self.validate_connection_settings():
                return None

            try:
                if not self._endpoint:
                    raise ValueError("Endpoint is required for connection")
                host, port, scheme = self._parse_host_port(self._endpoint)

                client_kwargs = {"host": host, "port": port, "protocol": scheme}

                if scheme == "https":
                    client_kwargs["verify"] = self._ca_pem_path
                    self._logger.info(
                        "Using TLS for etcd connection",
                        extra={"etcd": {"ca_cert_path": self._ca_pem_path}},
                    )

                self._client = etcd3.client(**client_kwargs)

                # Authentication setup (same as before)
                if self._username and self._password:
                    try:
                        # Try different import paths for etcd3-py
                        try:
                            from etcd3 import etcdrpc as _rpc
                        except ImportError:
                            try:
                                import etcd3.etcdrpc as _rpc
                            except ImportError:
                                raise ImportError("Cannot find etcdrpc module")

                        import grpc

                        auth_stub = _rpc.AuthStub(self._client.channel)
                        auth_request = _rpc.AuthenticateRequest(
                            name=self._username, password=self._password
                        )
                        resp = auth_stub.Authenticate(auth_request, None)

                        # Set up credentials for gRPC watch API
                        self._client.metadata = (("token", resp.token),)

                        # Create token call credentials
                        class EtcdTokenCallCredentials(grpc.AuthMetadataPlugin):
                            def __init__(self, access_token):
                                self._access_token = access_token

                            def __call__(self, context, callback):
                                metadata = (("token", self._access_token),)
                                callback(metadata, None)

                        self._client.call_credentials = grpc.metadata_call_credentials(
                            EtcdTokenCallCredentials(resp.token)
                        )

                        self._logger.info(
                            "etcd_client_authenticated",
                            extra={
                                "event": {
                                    "category": ["config"],
                                    "action": "authenticated",
                                },
                                "etcd": {
                                    "auth_method": "grpc",
                                    "username": self._username,
                                },
                            },
                        )
                    except Exception as e:
                        # Fallback to HTTP-only auth
                        self._logger.debug(
                            "grpc_auth_failed_fallback_to_http",
                            extra={
                                "event": {
                                    "category": ["config"],
                                    "action": "auth_fallback",
                                },
                                "etcd": {
                                    "auth_method": "http",
                                    "original_error": str(e),
                                },
                                "error": {"message": str(e), "type": type(e).__name__},
                            },
                            exc_info=True,
                        )
                        self._client.auth(self._username, self._password)
                        self._logger.debug(
                            "etcd_client_authenticated_http",
                            extra={
                                "event": {
                                    "category": ["config"],
                                    "action": "authenticated",
                                },
                                "etcd": {
                                    "auth_method": "http",
                                    "username": self._username,
                                },
                            },
                        )

                # Verify connection
                version_info = self._client.version()
                self._logger.debug(
                    "ETCD client initialized",
                    extra={
                        "etcd": {
                            "endpoint": self._endpoint,
                            "host": host,
                            "port": port,
                            "scheme": scheme,
                            "version": str(version_info),
                        },
                    },
                )
            except Exception:
                self._logger.error(
                    "Failed to initialize etcd client",
                    exc_info=True,
                )
                return None
        return self._client

    def start_watch_prefix(
        self,
        prefix: str,
        on_event: Callable[[str], None],
    ) -> Optional[Callable[[], None]]:
        """Start a background watcher for a given prefix."""
        # Implementation remains the same as before
        if etcd3 is None:
            self._logger.error(
                "etcd3_package_not_installed",
                extra={
                    "event": {"category": ["config"], "action": "dependency_missing"},
                    "etcd": {"package_available": False},
                },
            )
            return None

        client = self.connect()

        if client is None:
            self._logger.error(
                "etcd_watcher_start_failed",
                extra={
                    "event": {"category": ["config"], "action": "watcher_start_failed"},
                    "etcd": {"client_connected": False},
                },
            )
            return None

        # The watching implementation remains the same
        # (keeping the existing complex logic for compatibility)

        # Prefer low-level Watcher
        try:
            try:
                from etcd3 import etcdrpc as _rpc
            except ImportError:
                import etcd3.etcdrpc as _rpc
            from etcd3.watch import Watcher as LowLevelWatcher

            channel = getattr(client, "channel", None) or getattr(
                client, "_channel", None
            )
            if channel is not None:
                try:
                    watch_stub = _rpc.WatchStub(channel)
                    low = LowLevelWatcher(
                        watchstub=watch_stub,
                        timeout=None,
                        call_credentials=getattr(client, "call_credentials", None),
                        metadata=getattr(client, "metadata", None),
                    )

                    def _ll_callback(resp_or_err) -> None:
                        try:
                            if isinstance(resp_or_err, BaseException):
                                self._logger.warning(
                                    "etcd low-level watcher error",
                                    extra={"error": str(resp_or_err)},
                                    exc_info=True,
                                )
                                return

                            evs = getattr(resp_or_err, "events", None) or []
                            for ev in evs:
                                key_bytes = getattr(ev, "key", None)
                                if key_bytes is None and hasattr(ev, "kv"):
                                    key_bytes = getattr(ev.kv, "key", None)
                                key_str = (
                                    key_bytes.decode("utf-8", errors="ignore")
                                    if isinstance(key_bytes, (bytes, bytearray))
                                    else str(key_bytes)
                                    if key_bytes is not None
                                    else ""
                                )
                                if key_str and key_str.startswith(prefix):
                                    self._logger.debug(
                                        f"etcd watcher calling on_event for key: {key_str}"
                                    )
                                    on_event(key_str)
                        except Exception:
                            self._logger.warning(
                                "Error in low-level watch callback", exc_info=True
                            )

                    try:
                        from etcd3 import utils as _utils

                        range_end = _utils.increment_last_byte(prefix.encode("utf-8"))
                    except Exception:
                        range_end = None

                    watch_id = low.add_callback(
                        prefix,
                        _ll_callback,
                        range_end=range_end,
                        progress_notify=True,
                        prev_kv=True,
                    )

                    try:
                        self._logger.debug(
                            "etcd_watch_started",
                            extra={
                                "etcd": {
                                    "method": "low",
                                    "prefix": prefix,
                                    "watch_id": watch_id,
                                }
                            },
                        )
                    except Exception:
                        pass

                    def _cancel() -> None:
                        try:
                            low.cancel(watch_id)
                        except Exception:
                            self._logger.debug(
                                "Low-level watcher cancel raised", exc_info=True
                            )

                    return _cancel
                except Exception:
                    pass
        except Exception:
            pass

        # Try stateful watcher
        try:
            from etcd3 import utils as _utils
            from etcd3.stateful.watch import Watcher as StatefulWatcher

            try:
                range_end = _utils.increment_last_byte(prefix.encode("utf-8"))
            except Exception as e:
                try:
                    prefix_bytes = prefix.encode("utf-8")
                    if len(prefix_bytes) == 0:
                        range_end = b"\x00"
                    else:
                        for i in range(len(prefix_bytes) - 1, -1, -1):
                            if prefix_bytes[i] < 0xFF:
                                range_end = prefix_bytes[:i] + bytes(
                                    [prefix_bytes[i] + 1]
                                )
                                break
                        else:
                            range_end = prefix_bytes + b"\x00"
                except Exception as manual_ex:
                    self._logger.warning(
                        "etcd_watcher_range_end_failed",
                        extra={
                            "event": {
                                "category": ["config"],
                                "action": "watcher_setup_failed",
                            },
                            "etcd": {"prefix": prefix},
                            "error": {
                                "message": f"Both etcd3.utils and manual range_end failed: {e}, {manual_ex}",
                                "utils_error": str(e),
                                "manual_error": str(manual_ex),
                            },
                        },
                        exc_info=True,
                    )
                    range_end = None

            try:
                watcher = StatefulWatcher(
                    client,
                    key=prefix,
                    range_end=range_end,
                    progress_notify=True,
                    prev_kv=True,
                )
            except TypeError:
                self._logger.warning(
                    "etcd_watcher_fallback_to_basic",
                    extra={
                        "event": {"category": ["config"], "action": "watcher_fallback"},
                        "etcd": {"watcher_type": "basic", "prefix": prefix},
                    },
                )
                watcher = StatefulWatcher(
                    client,
                    progress_notify=True,
                    prev_kv=True,
                )

            def _handle_event(event) -> None:
                try:
                    key_bytes = getattr(event, "key", None)
                    if key_bytes is None and hasattr(event, "kv"):
                        key_bytes = getattr(event.kv, "key", None)
                    key_str = (
                        key_bytes.decode("utf-8", errors="ignore")
                        if isinstance(key_bytes, (bytes, bytearray))
                        else str(key_bytes)
                        if key_bytes is not None
                        else ""
                    )
                    if not key_str:
                        return
                    if not key_str.startswith(prefix):
                        return
                    self._logger.debug(
                        f"etcd stateful watcher calling on_event for key: {key_str}"
                    )
                    on_event(key_str)
                except Exception:
                    self._logger.warning(
                        "etcd_watch_event_error",
                        extra={
                            "event": {
                                "category": ["config"],
                                "action": "watch_event_error",
                            },
                            "etcd": {"key": key_str, "watcher_type": "stateful"},
                        },
                        exc_info=True,
                    )

            try:
                watcher.onEvent(".*", _handle_event)
            except (TypeError, AttributeError):
                try:
                    watcher.onEvent(_handle_event)
                except (TypeError, AttributeError):
                    try:
                        watcher.callback = _handle_event
                    except (TypeError, AttributeError):
                        self._logger.error(
                            "etcd_watcher_registration_failed",
                            extra={
                                "event": {
                                    "category": ["config"],
                                    "action": "watcher_registration_failed",
                                },
                                "etcd": {"watcher_type": "stateful", "prefix": prefix},
                            },
                        )
                        raise

            watcher.runDaemon()

            try:
                self._logger.debug(
                    "etcd_watch_started",
                    extra={
                        "etcd": {
                            "method": "stateful",
                            "prefix": prefix,
                        }
                    },
                )
            except Exception:
                pass

            def _cancel() -> None:
                try:
                    watcher.stop()
                except Exception:
                    self._logger.debug("Stateful watcher stop raised", exc_info=True)

            return _cancel

        except Exception:
            self._logger.warning(
                "Skipping stateful watcher fallback to avoid RBAC issues; watcher disabled",
                extra={"etcd": {"prefix": prefix}},
            )
            return None

    def get_values_by_keys(self, keys: Iterable[str]) -> Dict[str, Optional[str]]:
        """Get values for multiple etcd keys."""
        result: Dict[str, Optional[str]] = {}
        client = self.connect()

        # Convert to list to get length
        keys_list = list(keys)

        if client is None:
            self._logger.error(
                "etcd_values_retrieval_failed",
                extra={
                    "event": {
                        "category": ["config"],
                        "action": "values_retrieval_failed",
                    },
                    "etcd": {
                        "client_connected": False,
                        "keys_requested": len(keys_list),
                    },
                },
            )
            return {str(key): None for key in keys_list}

        for key in keys:
            try:
                response = client.range(key)
                if response and response.kvs:
                    value = response.kvs[0].value
                    result[str(key)] = (
                        value.decode("utf-8") if value is not None else None
                    )
                else:
                    result[str(key)] = None
            except Exception as e:
                if "invalid auth token" in str(e).lower():
                    self._logger.warning(
                        "etcd_auth_token_expired",
                        extra={
                            "event": {
                                "category": ["config"],
                                "action": "auth_token_expired",
                            },
                            "etcd": {"key": key, "action": "reconnect_attempt"},
                        },
                    )
                    try:
                        self._client = None
                        client = self.connect()
                        if client:
                            response = client.range(key)
                            if response and response.kvs:
                                value = response.kvs[0].value
                                result[str(key)] = (
                                    value.decode("utf-8") if value is not None else None
                                )
                            else:
                                result[str(key)] = None
                            continue
                    except Exception:
                        pass

                result[str(key)] = None
                self._logger.warning(
                    "etcd_key_retrieval_failed",
                    extra={
                        "event": {
                            "category": ["config"],
                            "action": "key_retrieval_failed",
                        },
                        "etcd": {"key": key},
                    },
                    exc_info=True,
                )
        return result

    def _get_local_config_values(self) -> Dict[str, Optional[str]]:
        """Get configuration values from environment variables."""
        result: Dict[str, Optional[str]] = {}
        for internal_name, env_var in self._env_var_map.items():
            result[internal_name] = os.getenv(env_var)
        return result

    def get_mapped_values(self, key_map: Dict[str, str]) -> Dict[str, Optional[str]]:
        """Get values using a key mapping."""
        raw = self.get_values_by_keys(key_map.keys())
        mapped: Dict[str, Optional[str]] = {}
        for absolute_key, internal_name in key_map.items():
            mapped[internal_name] = raw.get(absolute_key)
        return mapped

    def get_config(
        self, defaults: Optional[Dict[str, builtins.object]] = None
    ) -> Dict[str, builtins.object]:
        """Get configuration with optional defaults and type coercion."""
        if defaults is None:
            defaults = {}

        if self._use_local_config:
            self._logger.info(
                "loading_config_from_env",
                extra={
                    "event": {"category": ["config"], "action": "loading_from_env"},
                    "config": {"source": "environment_variables"},
                },
            )
            mapped = self._get_local_config_values()
        else:
            mapped = self.get_mapped_values(self._etcd_key_map)

        result: Dict[str, object] = {}
        internal_names = set(self._etcd_key_map.values()) | set(
            self._env_var_map.keys()
        )

        for internal_name in internal_names:
            value = mapped.get(internal_name)
            if value is None:
                value = defaults.get(internal_name)

            # Apply type coercion (can be overridden by subclasses)
            result[internal_name] = self._coerce_config_value(internal_name, value)

        return result

    def _coerce_config_value(
        self, internal_name: str, value: builtins.object
    ) -> builtins.object:
        """Apply type coercion to configuration values based on YAML type definitions."""
        if value is None:
            return value

        type_str = self._type_map.get(internal_name, "str")

        try:
            if type_str == "bool":
                if isinstance(value, bool):
                    return value
                if isinstance(value, str):
                    lowered = value.strip().lower()
                    return lowered in ("1", "true", "yes", "y", "on")
                return bool(value)

            elif type_str == "int":
                if isinstance(value, int):
                    return value
                return int(str(value))

            elif type_str == "float":
                if isinstance(value, (int, float)):
                    return float(value)
                return float(str(value))

            elif type_str == "str":
                return str(value)

            elif type_str == "tuple":
                # Handle comma-separated strings and lists/tuples
                if isinstance(value, str):
                    return tuple(s.strip() for s in value.split(",") if s.strip())
                elif isinstance(value, (list, tuple)):
                    return tuple(value)
                else:
                    return tuple() if value is None else (str(value),)

            # Unknown type, return as-is
            return value

        except (ValueError, TypeError) as e:
            self._logger.warning(
                "config_value_coercion_failed",
                extra={
                    "event": {"category": ["config"], "action": "coercion_failed"},
                    "config": {
                        "internal_name": internal_name,
                        "expected_type": type_str,
                        "value": str(value),
                        "error": str(e),
                    },
                },
            )
            return value
