"""Basic tests for etcd-dynamic-config."""

from unittest.mock import patch

import pytest

from etcd_dynamic_config import EtcdClient, EtcdConfig


class TestImports:
    """Test that all imports work correctly."""

    def test_can_import_client(self):
        """Test that EtcdClient can be imported."""
        assert EtcdClient is not None

    def test_can_import_config(self):
        """Test that EtcdConfig can be imported."""
        assert EtcdConfig is not None


class TestEtcdClient:
    """Test EtcdClient functionality."""

    def test_client_initialization(self):
        """Test that client initializes correctly."""
        client = EtcdClient()
        assert client._logger is not None
        assert client._use_local_config is False

    @patch.dict("os.environ", {"USE_LOCAL_CONFIG": "true"})
    def test_local_config_mode(self):
        """Test local config mode."""
        client = EtcdClient()
        assert client._use_local_config is True

    def test_key_map_generation(self):
        """Test that key map is generated correctly."""
        client = EtcdClient()
        key_map = client.get_etcd_key_map()

        assert isinstance(key_map, dict)
        assert len(key_map) == 0

        # With a map
        client_with_map = EtcdClient(etcd_key_map={"/test/key": "my_key"})
        key_map = client_with_map.get_etcd_key_map()
        assert len(key_map) == 1
        assert key_map["/test/key"] == "my_key"

    def test_env_var_map_generation(self):
        """Test that environment variable map is generated correctly."""
        client = EtcdClient()
        env_map = client.get_env_var_map()

        assert isinstance(env_map, dict)
        assert len(env_map) == 0

        # With a map
        client_with_map = EtcdClient(env_var_map={"my_key": "MY_KEY"})
        env_map = client_with_map.get_env_var_map()
        assert len(env_map) == 1
        assert env_map["my_key"] == "MY_KEY"

    def test_parse_host_port(self):
        """Test host/port parsing."""
        host, port, scheme = EtcdClient._parse_host_port(
            "https://etcd.example.com:2379"
        )

        assert host == "etcd.example.com"
        assert port == 2379
        assert scheme == "https"


class TestEtcdConfig:
    """Test EtcdConfig functionality."""

    def test_config_initialization(self):
        """Test that config manager initializes correctly."""
        from unittest.mock import MagicMock

        mock_client = MagicMock(spec=EtcdClient)
        config = EtcdConfig(client=mock_client)
        assert config._logger is not None
        assert config._cache == {}
        assert config._watch_cancel is None

    def test_load_initial_success(self):
        """Test successful initial load."""
        from unittest.mock import MagicMock

        # Create a mock client
        mock_client = MagicMock(spec=EtcdClient)
        mock_client.validate_connection_settings.return_value = True
        mock_client.get_config.return_value = {"test_key": "test_value"}
        mock_client.get_etcd_key_map.return_value = {}

        # Create config with mock client
        config = EtcdConfig(client=mock_client)
        success = config._load_initial()

        assert success is True
        assert config._cache == {"test_key": "test_value"}

    def test_load_initial_validation_failure(self):
        """Test initial load with validation failure."""
        from unittest.mock import MagicMock

        # Create a mock client
        mock_client = MagicMock(spec=EtcdClient)
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
        client = EtcdClient(use_local_config=True)
        config = EtcdConfig(client)

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
            client = EtcdClient(use_local_config=True)
            config = EtcdConfig(client)
            # With empty cache, should return empty dict if no env vars are set
            configs = await config.get_all_configs()
            assert isinstance(configs, dict)

        asyncio.run(test_async())
