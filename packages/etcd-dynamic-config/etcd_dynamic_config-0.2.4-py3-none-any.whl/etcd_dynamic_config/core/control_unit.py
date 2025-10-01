"""ControlUnit-specific etcd client implementation."""

import os
from typing import Optional

from .base import BaseEtcdClient


class ControlUnitEtcdClient(BaseEtcdClient):
    """Etcd client specifically configured for ControlUnit application.

    This class uses automatic key discovery from etcd.
    All keys under the configured prefix are automatically discovered and mapped.
    Keys are converted to snake_case by default (CategorizationApiUrl -> categorization_api_url).
    """

    def __init__(
        self,
        endpoint: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        root_key: Optional[str] = None,
        ca_cert_path: Optional[str] = None,
        use_snake_case: bool = True,
        auto_discover_keys: bool = True,
    ):
        """Initialize ControlUnit etcd client.

        Args:
            endpoint: etcd server endpoint
            username: etcd username
            password: etcd password
            root_key: root key prefix
            ca_cert_path: path to CA certificate
            use_snake_case: convert keys to snake_case (default: True)
            auto_discover_keys: auto-discover keys from etcd (default: True)
        """
        super().__init__(
            endpoint=endpoint,
            username=username,
            password=password,
            root_key=root_key,
            ca_cert_path=ca_cert_path,
            use_snake_case=use_snake_case,
            auto_discover_keys=auto_discover_keys,
        )

    def get_config_prefix(self) -> str:
        """Get the etcd key prefix for ControlUnit."""
        dev_enabled = str(os.getenv("EtcdSettings__Dev", "false")).lower() == "true"
        root = self._root_key or "/APPS/ControlUnit"
        root = root.strip()
        if not root.startswith("/"):
            root = f"/{root}"
        root = root.rstrip("/")
        return f"{'/dev' if dev_enabled else ''}{root}"


# Create default ControlUnit client instance
control_unit_client = ControlUnitEtcdClient(
    endpoint=os.getenv("EtcdSettings__HostName"),
    username=os.getenv("EtcdSettings__UserName"),
    password=os.getenv("EtcdSettings__Password"),
    root_key=os.getenv("EtcdSettings__RootKey"),
    auto_discover_keys=True,
)

__all__ = ["ControlUnitEtcdClient", "control_unit_client"]
