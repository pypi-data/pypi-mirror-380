"""Etcd Configuration Provider - A Python library for managing etcd-based configurations."""

__version__ = "0.1.2"
__author__ = "Anton Irshenko"
__email__ = "a_irshenko@example.com"

# Import base classes and implementations
from .core.base import BaseEtcdClient
from .core.client import (  # Backward compatibility
    EtcdClient,
    create_default_client,
    etcd_client,
)
from .core.config import EtcdConfig, etcd_config
from .core.logging import setup_logging

__all__ = [
    "BaseEtcdClient",
    "EtcdClient",  # Backward compatibility alias for BaseEtcdClient
    "etcd_client",  # Backward compatibility
    "create_default_client",
    "EtcdConfig",
    "etcd_config",
    "setup_logging",
]
