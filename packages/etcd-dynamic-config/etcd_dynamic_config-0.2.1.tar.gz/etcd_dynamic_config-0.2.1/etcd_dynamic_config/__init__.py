"""Etcd Configuration Provider - A Python library for managing etcd-based configurations."""

__version__ = "0.2.1"
__author__ = "Anton Irshenko"
__email__ = "a_irshenko@proton.me"

# Import base classes and implementations
from .core.client import EtcdClient
from .core.config import EtcdConfig
from .core.logging import setup_logging

__all__ = [
    "EtcdClient",
    "EtcdConfig",
    "setup_logging",
]
