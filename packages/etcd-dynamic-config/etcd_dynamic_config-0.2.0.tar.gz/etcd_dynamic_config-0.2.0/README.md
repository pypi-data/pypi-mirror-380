# Etcd Dynamic Config

[![PyPI version](https://badge.fury.io/py/etcd-dynamic-config.svg)](https://pypi.org/project/etcd-dynamic-config/)
[![Python versions](https://img.shields.io/pypi/pyversions/etcd-dynamic-config.svg)](https://pypi.org/project/etcd-dynamic-config/)
[![License](https://img.shields.io/pypi/l/etcd-dynamic-config.svg)](https://github.com/ton5169/etcd-dynamic-config/blob/main/LICENSE)

A robust Python library for managing etcd-based configurations with caching, real-time updates, and graceful fallbacks.

## Key Features

- 🚀 **High Performance**: In-memory caching for fast configuration access
- 🔄 **Real-time Updates**: Automatic watching for configuration changes
- 🛡️ **Reliability**: Graceful fallbacks to local environment variables
- 🔒 **Security**: Support for TLS and authentication
- 🧵 **Thread-safe**: Safe concurrent access to configuration data
- 📊 **Observability**: Structured logging and monitoring support
- 🎯 **Type-safe**: Built-in type coercion and validation

## Installation

```bash
pip install etcd-dynamic-config
```

For development with extra tools:

```bash
pip install etcd-dynamic-config[dev]
```

## Quick Start

### Basic Usage

```python
import asyncio
import os

from etcd_dynamic_config import EtcdClient, EtcdConfig, setup_logging

# It's recommended to set up logging first
setup_logging(level="INFO")

# Define your custom client by inheriting from EtcdClient
class MyAppClient(EtcdClient):
    """A custom client for 'MyApp' with specific configurations."""

    def get_config_prefix(self) -> str:
        """Define a custom prefix for this application."""
        return "/apps/myapp"

    def _build_etcd_key_map(self):
        """Map etcd keys to user-friendly internal names."""
        prefix = self.get_config_prefix()
        return {
            f"{prefix}/database_url": "db_url",
            f"{prefix}/api_key": "api_key",
        }

    def _build_env_var_map(self):
        """Map internal names to environment variables for local development."""
        return {
            "db_url": "MYAPP_DB_URL",
            "api_key": "MYAPP_API_KEY",
        }

async def main():
    # For local testing, set environment variables
    os.environ["USE_LOCAL_CONFIG"] = "true"
    os.environ["MYAPP_DB_URL"] = "postgresql://user:pass@localhost/db"
    os.environ["MYAPP_API_KEY"] = "local-secret-key"

    # 1. Create an instance of your custom client
    my_app_client = MyAppClient()

    # 2. Inject the client into EtcdConfig
    config_manager = EtcdConfig(client=my_app_client)

    try:
        # Start the configuration manager
        await config_manager.start()

        # Get all configurations
        configs = await config_manager.get_all_configs()
        print(f"Database URL: {configs.get('db_url')}")
        print(f"API Key: {configs.get('api_key')}")

    finally:
        # Clean shutdown
        await config_manager.stop()

asyncio.run(main())
```

### Environment Variables

Set these environment variables to configure etcd connection:

```bash
# Etcd connection settings
export EtcdSettings__HostName="http://localhost:2379"
export EtcdSettings__UserName="your-username"
export EtcdSettings__Password="your-password"
export EtcdSettings__RootKey="/APPS/ControlUnit"

# Optional: Use local environment variables instead of etcd
export USE_LOCAL_CONFIG="false"

# Optional: TLS settings
export EtcdSettings__CaCertPath="/path/to/ca-cert.pem"
```

### Local Development

For local development, set `USE_LOCAL_CONFIG=true` and define configurations as environment variables:

```bash
export USE_LOCAL_CONFIG="true"
export MYAPP_DB_URL="postgresql://user:pass@localhost:5432/db"
export MYAPP_API_KEY="your-secret-key"
```

## Detailed Usage Examples

### EtcdClient - Creating Custom Clients

`EtcdClient` is a concrete class for creating custom etcd clients. You can either instantiate it directly with configuration maps, or extend it to define your application-specific configuration schema.

#### Complete EtcdClient Example

```python
from typing import Dict
from etcd_dynamic_config import EtcdClient

class MyApplicationClient(EtcdClient):
    """Custom client for MyApplication."""

    def __init__(
        self,
        endpoint: str = None,
        username: str = None,
        password: str = None,
        root_key: str = None,
        ca_cert_path: str = None,
        use_local_config: bool = None,
        app_environment: str = "production"
    ):
        """Initialize MyApplication client.

        Args:
            endpoint: etcd server address (http://localhost:2379)
            username: Username for authentication
            password: Password for authentication
            root_key: Root key prefix (/APPS/MyApp)
            ca_cert_path: Path to CA certificate for TLS
            use_local_config: Whether to use local variables instead of etcd
            app_environment: Application environment (production/staging/dev)
        """
        # Pass all parameters to base class
        super().__init__(
            endpoint=endpoint,
            username=username,
            password=password,
            root_key=root_key,
            ca_cert_path=ca_cert_path,
            use_local_config=use_local_config
        )

        self.app_environment = app_environment

    def get_config_prefix(self) -> str:
        """Get the configuration keys prefix."""
        # Add environment to path
        dev_prefix = "/dev" if self.app_environment == "dev" else ""
        root = self._root_key or f"/APPS/MyApplication/{self.app_environment}"
        return f"{dev_prefix}{root}"

    def _build_etcd_key_map(self) -> Dict[str, str]:
        """Build etcd keys to internal names mapping."""
        base = self.get_config_prefix()
        return {
            f"{base}/Database/Host": "database_host",
            f"{base}/Database/Port": "database_port",
            f"{base}/Database/Name": "database_name",
            f"{base}/Database/User": "database_user",
            f"{base}/Database/Password": "database_password",
            f"{base}/Redis/Url": "redis_url",
            f"{base}/API/BaseUrl": "api_base_url",
            f"{base}/API/SecretKey": "api_secret_key",
            f"{base}/Cache/Enabled": "cache_enabled",
            f"{base}/Cache/TTL": "cache_ttl_seconds",
            f"{base}/Logging/Level": "log_level",
            f"{base}/Monitoring/Enabled": "monitoring_enabled",
        }

    def _build_env_var_map(self) -> Dict[str, str]:
        """Build internal names to environment variables mapping."""
        return {
            "database_host": "MYAPP_DB_HOST",
            "database_port": "MYAPP_DB_PORT",
            "database_name": "MYAPP_DB_NAME",
            "database_user": "MYAPP_DB_USER",
            "database_password": "MYAPP_DB_PASSWORD",
            "redis_url": "MYAPP_REDIS_URL",
            "api_base_url": "MYAPP_API_BASE_URL",
            "api_secret_key": "MYAPP_API_SECRET_KEY",
            "cache_enabled": "MYAPP_CACHE_ENABLED",
            "cache_ttl_seconds": "MYAPP_CACHE_TTL_SECONDS",
            "log_level": "MYAPP_LOG_LEVEL",
            "monitoring_enabled": "MYAPP_MONITORING_ENABLED",
        }

    def _coerce_config_value(self, internal_name: str, value):
        """Apply custom type coercion."""
        # Application-specific type coercion
        if internal_name == "database_port":
            try:
                return int(value) if value else 5432
            except (ValueError, TypeError):
                return 5432
        elif internal_name in ("cache_enabled", "monitoring_enabled"):
            if isinstance(value, str):
                return value.lower() in ("1", "true", "yes", "on", "enabled")
            return bool(value)
        elif internal_name == "cache_ttl_seconds":
            try:
                return int(value) if value else 3600
            except (ValueError, TypeError):
                return 3600
        elif internal_name == "api_secret_key":
            # Don't log secret keys
            return str(value) if value else ""

        # Use default coercion for other values
        return super()._coerce_config_value(internal_name, value)

# Client usage
def main():
    # Example 1: Using with etcd
    print("=== Using with etcd ===")
    client_etcd = MyApplicationClient(
        endpoint="https://etcd-cluster.example.com:2379",
        username="myapp-user",
        password="secure-password",
        root_key="/APPS/MyApplication/production",
        ca_cert_path="/etc/ssl/certs/ca-bundle.pem",
        use_local_config=False,
        app_environment="production"
    )

    # Get configuration
    config = client_etcd.get_config()
    print(f"Database Host: {config.get('database_host')}")
    print(f"Cache Enabled: {config.get('cache_enabled')} (type: {type(config.get('cache_enabled'))})")

    # Example 2: Local development
    print("\n=== Local development example ===")
    client_local = MyApplicationClient(
        use_local_config=True,
        app_environment="dev"
    )

    config_local = client_local.get_config()
    print(f"Local Database Host: {config_local.get('database_host')}")
    print(f"Local Log Level: {config_local.get('log_level')}")

    # Example 3: Minimal configuration
    print("\n=== Minimal configuration example ===")
    client_minimal = MyApplicationClient()  # All parameters default from env
    config_minimal = client_minimal.get_config()
    print(f"Minimal config keys: {list(config_minimal.keys())}")

if __name__ == "__main__":
    main()
```

### Synchronous Configuration Retrieval

```python
from etcd_dynamic_config import EtcdClient

# Create client
client = EtcdClient(use_local_config=True)

# Get all configurations
config = client.get_config()

# Access specific values
api_url = config.get('categorization_api_url')
database_dsn = config.get('postgres_dsn')

print(f"API URL: {api_url}")
print(f"Database: {database_dsn}")
```

### Asynchronous Configuration Management

```python
import asyncio
from etcd_dynamic_config import EtcdConfig, EtcdClient

async def async_config_example():
    # Create custom client
    client = EtcdClient(
        endpoint="https://etcd.example.com:2379",
        username="my-user",
        password="my-password"
    )

    # Create configuration manager
    config_manager = EtcdConfig(client=client)

    try:
        # Start manager
        success = await config_manager.start()
        if success:
            print("✅ Configuration manager started")

            # Get configurations
            configs = await config_manager.get_all_configs()

            # Work with configurations
            api_token = configs.get('categorization_api_token')
            if api_token:
                print(f"API Token received: {len(api_token)} characters")

            # Work loop
            for i in range(5):
                await asyncio.sleep(2)
                current_configs = await config_manager.get_all_configs()
                log_level = current_configs.get('log_level', 'INFO')
                print(f"[{i+1}/5] Current log level: {log_level}")

    except Exception as e:
        print(f"❌ Configuration error: {e}")

    finally:
        # Clean shutdown
        await config_manager.stop()
        print("👋 Configuration manager stopped")

asyncio.run(async_config_example())
```

### Error Handling

```python
from etcd_dynamic_config import EtcdClient

def safe_config_access():
    try:
        client = EtcdClient(
            endpoint="https://etcd.example.com:2379",
            username="wrong-user",
            password="wrong-password"
        )

        config = client.get_config()

        # Safe access with default values
        timeout = config.get('ai_http_timeout_seconds') or 30.0
        max_conn = config.get('ai_http_max_connections') or 10
        log_level = config.get('log_level') or 'INFO'

        print(f"✅ Configuration loaded successfully")
        print(f"Timeout: {timeout}s, Max connections: {max_conn}")
        print(f"Log level: {log_level}")

    except Exception as e:
        print(f"❌ Configuration access error: {e}")
        print("🔄 Using fallback values...")

        # Fallback values
        timeout = 30.0
        max_conn = 10
        log_level = 'INFO'

    return {
        'timeout': timeout,
        'max_connections': max_conn,
        'log_level': log_level
    }

# Usage
config = safe_config_access()
print(f"Final configuration: {config}")
```

## Configuration Schema

The library doesn't impose any specific configuration schema - **you define your own keys!**

### Creating Your Own Configuration Schema

```python
from typing import Dict
from etcd_dynamic_config import EtcdClient

class MyServiceClient(EtcdClient):
    """Client for your service with custom configuration schema."""

    def get_config_prefix(self) -> str:
        """Returns the configuration keys prefix."""
        return "/services/my-service/prod"

    def _build_etcd_key_map(self) -> Dict[str, str]:
        """Builds etcd keys to internal names mapping."""
        base = self.get_config_prefix()
        return {
            # Your custom etcd keys -> internal names
            f"{base}/Database/Host": "db_host",
            f"{base}/Database/Port": "db_port",
            f"{base}/Database/Name": "db_name",
            f"{base}/Database/Credentials/User": "db_user",
            f"{base}/Database/Credentials/Password": "db_password",
            f"{base}/Redis/Url": "redis_url",
            f"{base}/Redis/Password": "redis_password",
            f"{base}/API/BaseUrl": "api_base_url",
            f"{base}/API/SecretKey": "api_secret_key",
            f"{base}/Features/Cache/Enabled": "cache_enabled",
            f"{base}/Features/Cache/TTL": "cache_ttl_seconds",
            f"{base}/Monitoring/LogLevel": "log_level",
            f"{base}/Monitoring/Metrics/Enabled": "metrics_enabled",
            f"{base}/Limits/MaxConnections": "max_connections",
            f"{base}/Limits/Timeout": "request_timeout",
        }

    def _build_env_var_map(self) -> Dict[str, str]:
        """Builds internal names to environment variables mapping."""
        return {
            # Internal names -> environment variables
            "db_host": "MYSERVICE_DB_HOST",
            "db_port": "MYSERVICE_DB_PORT",
            "db_name": "MYSERVICE_DB_NAME",
            "db_user": "MYSERVICE_DB_USER",
            "db_password": "MYSERVICE_DB_PASSWORD",
            "redis_url": "MYSERVICE_REDIS_URL",
            "redis_password": "MYSERVICE_REDIS_PASSWORD",
            "api_base_url": "MYSERVICE_API_BASE_URL",
            "api_secret_key": "MYSERVICE_API_SECRET_KEY",
            "cache_enabled": "MYSERVICE_CACHE_ENABLED",
            "cache_ttl_seconds": "MYSERVICE_CACHE_TTL",
            "log_level": "MYSERVICE_LOG_LEVEL",
            "metrics_enabled": "MYSERVICE_METRICS_ENABLED",
            "max_connections": "MYSERVICE_MAX_CONNECTIONS",
            "request_timeout": "MYSERVICE_REQUEST_TIMEOUT",
        }

    def _coerce_config_value(self, internal_name: str, value):
        """Applies custom type coercion."""
        # Type coercion for numeric values
        if internal_name in ("db_port", "max_connections", "cache_ttl_seconds"):
            try:
                return int(value) if value else self._get_default_value(internal_name)
            except (ValueError, TypeError):
                return self._get_default_value(internal_name)

        # Type coercion for timeouts
        elif internal_name == "request_timeout":
            try:
                return float(value) if value else 30.0
            except (ValueError, TypeError):
                return 30.0

        # Type coercion for boolean values
        elif internal_name in ("cache_enabled", "metrics_enabled"):
            if isinstance(value, str):
                return value.lower() in ("1", "true", "yes", "on", "enabled")
            return bool(value)

        # Don't log secret values
        elif internal_name in ("db_password", "redis_password", "api_secret_key"):
            return str(value) if value else ""

        # Use default coercion for other values
        return super()._coerce_config_value(internal_name, value)

    def _get_default_value(self, internal_name: str):
        """Returns default values."""
        defaults = {
            "db_port": 5432,
            "max_connections": 10,
            "cache_ttl_seconds": 3600,
        }
        return defaults.get(internal_name, 0)
```

### Documenting Your Configuration Schema

Create documentation for your configuration keys:

| Etcd Key | Environment Variable | Type | Default | Description |
|----------|---------------------|------|---------|-------------|
| `/services/my-service/prod/Database/Host` | `MYSERVICE_DB_HOST` | str | - | Database host |
| `/services/my-service/prod/Database/Port` | `MYSERVICE_DB_PORT` | int | 5432 | Database port |
| `/services/my-service/prod/Database/Name` | `MYSERVICE_DB_NAME` | str | - | Database name |
| `/services/my-service/prod/Redis/Url` | `MYSERVICE_REDIS_URL` | str | - | Redis server URL |
| `/services/my-service/prod/Features/Cache/Enabled` | `MYSERVICE_CACHE_ENABLED` | bool | false | Enable caching |
| `/services/my-service/prod/Limits/MaxConnections` | `MYSERVICE_MAX_CONNECTIONS` | int | 10 | Maximum connections |
| `/services/my-service/prod/Monitoring/LogLevel` | `MYSERVICE_LOG_LEVEL` | str | INFO | Log level |

## Architecture

### Components

1. **EtcdClient**: Base client for etcd operations
   - Connection management
   - Authentication and TLS
   - Key-value operations
   - Change watching capabilities

2. **EtcdConfig**: High-level configuration manager
   - Caching layer
   - Type coercion
   - Real-time updates
   - Health monitoring

### Thread Safety

All operations are thread-safe:

- Configuration cache uses `threading.RLock()`
- Async operations properly handle concurrency
- Watcher callbacks are serialized

### Error Recovery

The library implements several recovery mechanisms:

- Automatic reconnection on authentication failures
- Watcher restart on inactivity
- Fallback to local environment variables
- Graceful degradation when etcd is unavailable

## Available Classes

| Class | Purpose | Usage |
|-------|---------|-------|
| `EtcdClient` | Concrete base class | For creating custom clients or direct instantiation |
| `EtcdConfig` | Configuration manager | For async configuration management |

## Development

### Development Setup

```bash
# Clone the repository
git clone https://github.com/ton5169/etcd-dynamic-config.git
cd etcd-dynamic-config

# Install development dependencies
pip install -e .[dev]

# Run tests
pytest

# Format code
black etcd_dynamic_config/
isort etcd_dynamic_config/

# Type checking
mypy etcd_dynamic_config/
```

### Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=etcd_dynamic_config --cov-report=html

# Specific test file
pytest tests/test_client.py

# Integration tests
pytest -m integration
```

### Building Documentation

```bash
# Install docs dependencies
pip install -e .[docs]

# Build documentation
cd docs
make html
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Usage Examples

Check out complete examples in the [examples/](examples/) directory:

- [basic_usage.py](examples/basic_usage.py) - basic usage
- [advanced_usage.py](examples/advanced_usage.py) - advanced features
- [custom_client_example.py](examples/custom_client_example.py) - custom client
- [schema_documentation_example.py](examples/schema_documentation_example.py) - schema documentation

## License

MIT License - see [LICENSE](LICENSE) file.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.
