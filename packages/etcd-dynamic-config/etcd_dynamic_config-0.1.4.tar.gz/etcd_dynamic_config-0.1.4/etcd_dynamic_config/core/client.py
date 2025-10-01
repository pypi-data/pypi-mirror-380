"""Etcd client for configuration management."""

import os

from .base import BaseEtcdClient


# Create default client instance using the existing config file
def create_default_client() -> BaseEtcdClient:
    """Create a default client instance using etcd_config.yaml"""
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "etcd_config.yaml"
    )
    root_key = os.getenv("EtcdSettings__RootKey", "/APPS")

    # Ensure root_key is not None
    if root_key is None:
        root_key = "/APPS"

    return BaseEtcdClient(
        config_file_path=config_path,
        root_key=root_key,
        endpoint=os.getenv("EtcdSettings__HostName"),
        username=os.getenv("EtcdSettings__UserName"),
        password=os.getenv("EtcdSettings__Password"),
        use_local_config=str(os.getenv("USE_LOCAL_CONFIG", "false")).lower() == "true",
    )


# Create default instance lazily
def _get_default_client():
    """Get or create the default client instance."""
    if not hasattr(_get_default_client, "_instance"):
        _get_default_client._instance = create_default_client()
    return _get_default_client._instance


# Use property-like access
class _DefaultClientWrapper:
    def __getattr__(self, name):
        return getattr(_get_default_client(), name)


etcd_client = _DefaultClientWrapper()

# For backward compatibility
EtcdClient = BaseEtcdClient

__all__ = ["EtcdClient", "etcd_client", "create_default_client"]
