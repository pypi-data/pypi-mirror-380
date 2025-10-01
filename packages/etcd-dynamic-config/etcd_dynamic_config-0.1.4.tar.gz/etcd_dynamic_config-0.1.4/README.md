# etcd-dynamic-config

A Python library for managing etcd-based configurations with YAML configuration files, automatic type coercion, and real-time watching capabilities.



## Installation

```bash
pip install etcd-dynamic-config
```

## Quick Start

### 1. Create a YAML Configuration File

Create a `config.yaml` file for your service:

```yaml
etcd_key_map:
  - key: "DatabaseUrl"
    type: "str"
  - key: "DebugMode"
    type: "bool"
  - key: "MaxConnections"
    type: "int"
  - key: "RequestTimeout"
    type: "float"

env_var_map:
  - key: "DatabaseUrl"
    type: "str"
  - key: "DebugMode"
    type: "bool"
  - key: "MaxConnections"
    type: "int"
  - key: "RequestTimeout"
    type: "float"
```

### 2. Use the Client

```python
import asyncio
from etcd_dynamic_config import BaseEtcdClient, EtcdConfig

async def main():
    # Create a client
    client = BaseEtcdClient(
        config_file_path="config.yaml",
        root_key="/APPS/MyService",
        endpoint="http://localhost:2379",
        username="myuser",
        password="mypassword"
    )

    # Get configuration values
    config = client.get_config()
    print(f"Database URL: {config['DatabaseUrl']}")
    print(f"Debug Mode: {config['DebugMode']}")

    # Use with configuration manager for real-time updates
    config_manager = EtcdConfig(client)
    await config_manager.start()

    # Get cached configuration
    cached_config = await config_manager.get_all_configs()

    await config_manager.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

## Configuration File Format

### etcd_key_map

Defines the etcd keys and their types. Keys are used directly as configuration names:

```yaml
etcd_key_map:
  - key: "DatabaseUrl"        # The key name in etcd (without prefix)
    type: "str"               # Type for automatic coercion (str, int, float, bool)
```

### env_var_map

Defines environment variable mappings for fallback when etcd is not available. Environment variable names are automatically generated from keys:

```yaml
env_var_map:
  - key: "DatabaseUrl"        # Configuration key name
    type: "str"               # Type for automatic coercion
```


## Supported Types

- **str**: String values (default)
- **int**: Integer values
- **float**: Floating point values
- **bool**: Boolean values (supports "true", "false", "1", "0", "yes", "no", "on", "off")

## Environment Variables

The library uses the following environment variables for configuration:

- `EtcdSettings__HostName`: etcd server endpoint
- `EtcdSettings__UserName`: etcd username
- `EtcdSettings__Password`: etcd password
- `EtcdSettings__RootKey`: default root key (used by create_default_client)
- `EtcdSettings__Dev`: if set to "true", adds "/dev" prefix to all keys
- `USE_LOCAL_CONFIG`: if set to "true", uses environment variables instead of etcd

## Examples

### Basic Usage

```python
from etcd_dynamic_config import BaseEtcdClient

client = BaseEtcdClient(
    config_file_path="my_config.yaml",
    root_key="/APPS/MyService"
)

config = client.get_config()
database_url = config["DatabaseUrl"]
debug_mode = config["DebugMode"]  # Automatically converted to bool
```

### With Real-time Updates

```python
import asyncio
from etcd_dynamic_config import BaseEtcdClient, EtcdConfig

async def main():
    client = BaseEtcdClient(
        config_file_path="my_config.yaml",
        root_key="/APPS/MyService"
    )

    config_manager = EtcdConfig(client)
    await config_manager.start()

    # Configuration will automatically update when etcd values change
    while True:
        config = await config_manager.get_all_configs()
        print(f"Current config: {config}")
        await asyncio.sleep(1)

asyncio.run(main())
```

### Custom Configuration

```python
from etcd_dynamic_config import BaseEtcdClient

# Create client with custom configuration
client = BaseEtcdClient(
    config_file_path="custom_config.yaml",
    root_key="/APPS/CustomService",
    endpoint="https://etcd.example.com:2379",
    username="admin",
    password="secret",
    ca_cert_path="/path/to/ca.pem"
)

# Get configuration with automatic type coercion
config = client.get_config()
max_connections = config["MaxConnections"]  # int
timeout = config["RequestTimeout"]  # float
debug = config["DebugMode"]  # bool
```


## API Reference

### BaseEtcdClient

The main client class for etcd configuration management.

#### Constructor

```python
BaseEtcdClient(
    config_file_path: str,        # Path to YAML configuration file (required)
    root_key: str,                # Root key prefix (e.g., "/APPS/MyService") (required)
    endpoint: Optional[str] = None,      # etcd endpoint
    username: Optional[str] = None,      # etcd username
    password: Optional[str] = None,      # etcd password
    ca_cert_path: Optional[str] = None,  # CA certificate path
    use_local_config: Optional[bool] = None  # Use env vars instead of etcd
)
```

#### Methods

- `get_config(defaults: Optional[Dict] = None) -> Dict`: Get all configuration values
- `get_config_prefix() -> str`: Get the etcd key prefix
- `get_etcd_key_map() -> Dict[str, str]`: Get etcd key mappings
- `get_env_var_map() -> Dict[str, str]`: Get environment variable mappings