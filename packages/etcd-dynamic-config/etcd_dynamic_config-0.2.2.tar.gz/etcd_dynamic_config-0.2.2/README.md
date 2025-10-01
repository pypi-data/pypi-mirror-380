# etcd-dynamic-config

Python library for managing etcd-based configurations with caching and real-time updates.

## Installation

```bash
pip install etcd-dynamic-config
```

## Quick Start

### Basic Usage

```python
from etcd_dynamic_config import BaseEtcdClient

# Create client
client = BaseEtcdClient(
        endpoint=os.getenv("EtcdSettings__HostName"),
        username=os.getenv("EtcdSettings__UserName"),
        password=os.getenv("EtcdSettings__Password"),
        root_key=os.getenv("EtcdSettings__RootKey", "/APPS/ControlUnit"),
        use_snake_case=True, # transform values that we got under rootkey to python format
        auto_discover_keys=True, # search those values, if stated False you should redifine _build_etcd_key_map method
    )

# Get configuration
config = client.get_config()

# Use values
api_url = config.get('categorization_api_url')
db_dsn = config.get('postgres_dsn')
```

### Async Usage

```python
import asyncio
from etcd_dynamic_config import EtcdConfig, ControlUnitEtcdClient

async def main():
    client = ControlUnitEtcdClient()
    config_manager = EtcdConfig(client=client)

    await config_manager.start()
    configs = await config_manager.get_all_configs()
    await config_manager.stop()

asyncio.run(main())
```

## Environment Variables

Set these to configure etcd connection:

```bash
export EtcdSettings__HostName="http://localhost:2379"
export EtcdSettings__UserName="username"
export EtcdSettings__Password="password"
export EtcdSettings__RootKey="/APPS/ControlUnit"
```

## Features

- In-memory caching for fast access
- Real-time updates via etcd watch
- Automatic type coercion (bool, int, float, tuple)
- Snake case conversion (CamelCase → snake_case)
- Environment variable fallback
- Thread-safe operations
