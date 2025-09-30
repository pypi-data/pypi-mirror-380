"""Core components for etcd configuration management."""

from .client import EtcdClient, etcd_client
from .config import EtcdConfig
from .logging import setup_logging

etcd_config = EtcdConfig(client=etcd_client)


__all__ = ["EtcdClient", "etcd_client", "EtcdConfig", "etcd_config", "setup_logging"]
