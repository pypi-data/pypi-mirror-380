"""Basic tests for etcd-dynamic-config."""

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from etcd_dynamic_config import (
    BaseEtcdClient,
    EtcdClient,
    EtcdConfig,
    etcd_client,
    etcd_config,
)


class TestImports:
    """Test that all imports work correctly."""

    def test_can_import_base_client(self):
        """Test that BaseEtcdClient can be imported."""
        assert BaseEtcdClient is not None

    def test_can_import_client(self):
        """Test that EtcdClient can be imported (backward compatibility)."""
        assert EtcdClient is not None
        assert EtcdClient == BaseEtcdClient  # Should be alias

    def test_can_import_config(self):
        """Test that EtcdConfig can be imported."""
        assert EtcdConfig is not None

    def test_can_import_instances(self):
        """Test that default instances can be imported."""
        assert etcd_client is not None
        assert etcd_config is not None

    def test_instances_are_correct_type(self):
        """Test that instances are of correct types."""
        # etcd_client is now a wrapper, test its actual type
        from etcd_dynamic_config.core.client import _get_default_client

        actual_client = _get_default_client()
        assert isinstance(actual_client, BaseEtcdClient)
        assert isinstance(etcd_config, EtcdConfig)


class TestBaseEtcdClient:
    """Test BaseEtcdClient functionality."""

    def create_test_config(self):
        """Create a test YAML configuration."""
        config = {
            "etcd_key_map": [
                {"key": "DatabaseUrl", "type": "str"},
                {"key": "DebugMode", "type": "bool"},
                {"key": "MaxConnections", "type": "int"},
                {"key": "Timeout", "type": "float"},
            ],
            "env_var_map": [
                {"key": "DatabaseUrl", "type": "str"},
                {"key": "DebugMode", "type": "bool"},
                {"key": "MaxConnections", "type": "int"},
                {"key": "Timeout", "type": "float"},
            ],
        }

        # Create temporary file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            yaml.dump(config, f)
            return f.name

    def test_client_initialization(self):
        """Test that client initializes correctly with YAML config."""
        config_file = self.create_test_config()

        try:
            client = BaseEtcdClient(
                config_file_path=config_file, root_key="/APPS/TestService"
            )

            assert client._logger is not None
            assert client._config_file_path == config_file
            assert client._root_key == "/APPS/TestService"
            assert client._yaml_config is not None

        finally:
            Path(config_file).unlink()

    def test_yaml_config_loading(self):
        """Test YAML configuration loading."""
        config_file = self.create_test_config()

        try:
            client = BaseEtcdClient(
                config_file_path=config_file, root_key="/APPS/TestService"
            )

            # Check that YAML config was loaded
            assert "etcd_key_map" in client._yaml_config
            assert "env_var_map" in client._yaml_config
            assert len(client._yaml_config["etcd_key_map"]) == 4

        finally:
            Path(config_file).unlink()

    def test_config_file_not_found(self):
        """Test error handling when config file doesn't exist."""
        with pytest.raises(FileNotFoundError):
            BaseEtcdClient(
                config_file_path="/nonexistent/config.yaml",
                root_key="/APPS/TestService",
            )

    def test_key_map_generation(self):
        """Test that key map is generated correctly from YAML."""
        config_file = self.create_test_config()

        try:
            client = BaseEtcdClient(
                config_file_path=config_file, root_key="/APPS/TestService"
            )

            key_map = client.get_etcd_key_map()

            assert isinstance(key_map, dict)
            assert len(key_map) == 4

            # Check specific keys
            expected_keys = [
                "/APPS/TestService/DatabaseUrl",
                "/APPS/TestService/DebugMode",
                "/APPS/TestService/MaxConnections",
                "/APPS/TestService/Timeout",
            ]

            for expected_key in expected_keys:
                assert expected_key in key_map

            # Check mappings - now keys map to themselves
            assert key_map["/APPS/TestService/DatabaseUrl"] == "DatabaseUrl"
            assert key_map["/APPS/TestService/DebugMode"] == "DebugMode"

        finally:
            Path(config_file).unlink()

    def test_env_var_map_generation(self):
        """Test that environment variable map is generated correctly from YAML."""
        config_file = self.create_test_config()

        try:
            client = BaseEtcdClient(
                config_file_path=config_file, root_key="/APPS/TestService"
            )

            env_map = client.get_env_var_map()

            assert isinstance(env_map, dict)
            assert len(env_map) == 4

            # Check mappings - now keys map to environment variables (auto-generated from key names)
            assert env_map["DatabaseUrl"] == "DATABASEURL"
            assert env_map["DebugMode"] == "DEBUGMODE"
            assert env_map["MaxConnections"] == "MAXCONNECTIONS"
            assert env_map["Timeout"] == "TIMEOUT"

        finally:
            Path(config_file).unlink()

    def test_type_coercion(self):
        """Test automatic type coercion based on YAML types."""
        config_file = self.create_test_config()

        try:
            client = BaseEtcdClient(
                config_file_path=config_file, root_key="/APPS/TestService"
            )

            # Test string coercion
            result = client._coerce_config_value("DatabaseUrl", "postgres://localhost")
            assert result == "postgres://localhost"
            assert isinstance(result, str)

            # Test boolean coercion
            result = client._coerce_config_value("DebugMode", "true")
            assert result is True
            assert isinstance(result, bool)

            result = client._coerce_config_value("DebugMode", "false")
            assert result is False

            result = client._coerce_config_value("DebugMode", "1")
            assert result is True

            # Test integer coercion
            result = client._coerce_config_value("MaxConnections", "10")
            assert result == 10
            assert isinstance(result, int)

            # Test float coercion
            result = client._coerce_config_value("Timeout", "30.5")
            assert result == 30.5
            assert isinstance(result, float)

        finally:
            Path(config_file).unlink()

    def test_config_prefix_generation(self):
        """Test config prefix generation."""
        config_file = self.create_test_config()

        try:
            # Test without dev mode
            client = BaseEtcdClient(
                config_file_path=config_file, root_key="/APPS/TestService"
            )

            prefix = client.get_config_prefix()
            assert prefix == "/APPS/TestService"

            # Test with dev mode
            with patch.dict("os.environ", {"EtcdSettings__Dev": "true"}):
                client = BaseEtcdClient(
                    config_file_path=config_file, root_key="/APPS/TestService"
                )

                prefix = client.get_config_prefix()
                assert prefix == "/dev/APPS/TestService"

            # Test with root key that doesn't start with /
            client = BaseEtcdClient(
                config_file_path=config_file, root_key="APPS/TestService"
            )

            prefix = client.get_config_prefix()
            assert prefix == "/APPS/TestService"

        finally:
            Path(config_file).unlink()

    def test_parse_host_port(self):
        """Test host/port parsing."""
        config_file = self.create_test_config()

        try:
            client = BaseEtcdClient(
                config_file_path=config_file, root_key="/APPS/TestService"
            )

            host, port, scheme = client._parse_host_port(
                "https://etcd.example.com:2379"
            )

            assert host == "etcd.example.com"
            assert port == 2379
            assert scheme == "https"

        finally:
            Path(config_file).unlink()


class TestEtcdClient:
    """Test backward compatibility with EtcdClient alias."""

    def test_etcd_client_is_alias(self):
        """Test that EtcdClient is an alias for BaseEtcdClient."""
        assert EtcdClient == BaseEtcdClient


class TestEtcdConfig:
    """Test EtcdConfig functionality."""

    def test_config_initialization(self):
        """Test that config manager initializes correctly."""
        config = EtcdConfig()
        assert config._logger is not None
        assert config._cache == {}
        assert config._watch_cancel is None

    def test_load_initial_success(self):
        """Test successful initial load."""
        from unittest.mock import MagicMock

        # Create a mock client
        mock_client = MagicMock()
        mock_client.validate_connection_settings.return_value = True
        mock_client.get_config.return_value = {"test_key": "test_value"}

        # Create config with mock client
        config = EtcdConfig(client=mock_client)
        success = config._load_initial()

        assert success is True
        assert config._cache == {"test_key": "test_value"}

    def test_load_initial_validation_failure(self):
        """Test initial load with validation failure."""
        from unittest.mock import MagicMock

        # Create a mock client
        mock_client = MagicMock()
        mock_client.validate_connection_settings.return_value = False

        # Create config with mock client
        config = EtcdConfig(client=mock_client)
        success = config._load_initial()

        assert success is False


class TestIntegration:
    """Integration tests."""

    @pytest.mark.asyncio
    async def test_config_lifecycle(self):
        """Test full config lifecycle."""
        config = EtcdConfig()

        # Should be able to start (might fail due to no etcd, but shouldn't crash)
        try:
            success = await config.start()
            # Success depends on etcd availability, but should not raise
            assert isinstance(success, bool)
        except Exception:
            # If etcd is not available, that's expected in test environment
            pass
        finally:
            # Should always be able to stop
            await config.stop()

    def test_get_all_configs_empty_cache(self):
        """Test getting configs with empty cache."""
        import asyncio

        async def test_async():
            config = EtcdConfig()
            # With empty cache, should return empty dict
            configs = await config.get_all_configs()
            assert isinstance(configs, dict)

        asyncio.run(test_async())
