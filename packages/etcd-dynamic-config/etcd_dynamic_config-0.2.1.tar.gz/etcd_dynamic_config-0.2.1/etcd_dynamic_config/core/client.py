"""Etcd client for configuration management."""

from .base import EtcdClient

etcd_client = EtcdClient()

__all__ = ["EtcdClient", "etcd_client"]
