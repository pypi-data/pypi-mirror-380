#!/usr/bin/env python3
"""
Basic usage example of etcd-dynamic-config library.

This example shows how to use the new YAML-based configuration approach.
"""

import asyncio
import os
from pathlib import Path

# Import the library
from etcd_dynamic_config import BaseEtcdClient, EtcdConfig


async def main():
    """Demonstrate basic usage of the etcd configuration client."""

    # Get the path to the config file (relative to this script)
    script_dir = Path(__file__).parent
    config_file = script_dir / "web_service_config.yaml"

    print(f"Using config file: {config_file}")

    # Create a client instance
    # You need to specify:
    # 1. config_file_path - path to your YAML configuration file
    # 2. root_key - the root key prefix for your application in etcd
    client = BaseEtcdClient(
        config_file_path=str(config_file),
        root_key=os.getenv(
            "EtcdSettings__RootKey", "/APPS/MyService"
        ),  # This will be prefixed with /dev if EtcdSettings__Dev=true
        endpoint=os.getenv("EtcdSettings__HostName", "http://localhost:2379"),
        username=os.getenv("EtcdSettings__UserName"),
        password=os.getenv("EtcdSettings__Password"),
        use_local_config=os.getenv("USE_LOCAL_CONFIG", "false").lower() == "true",
    )

    print(f"Client created with prefix: {client.get_config_prefix()}")

    # Get configuration values
    config = client.get_config()

    print("\nConfiguration values:")
    for key, value in config.items():
        print(f"  {key}: {value} (type: {type(value).__name__})")

    # Demonstrate direct key access
    print("\nDirect key access examples:")
    try:
        database_url = config.get("DatabaseUrl", "Not configured")
        print(f"  DatabaseUrl: {database_url}")

        debug_mode = config.get("DebugMode", False)
        print(f"  DebugMode: {debug_mode} (type: {type(debug_mode).__name__})")

        max_connections = config.get("MaxConnections", 10)
        print(
            f"  MaxConnections: {max_connections} (type: {type(max_connections).__name__})"
        )
    except Exception as e:
        print(f"  Error accessing config values: {e}")

    # Create and start the configuration manager
    config_manager = EtcdConfig(client)

    try:
        # Start the config manager (loads initial config and starts watching)
        success = await config_manager.start()

        if success:
            print("\nConfiguration manager started successfully!")

            # Get all configurations (from cache)
            cached_config = await config_manager.get_all_configs()
            print(f"\nCached configurations ({len(cached_config)} items):")

            for key, value in list(cached_config.items())[:5]:  # Show first 5 items
                print(f"  {key}: {value}")

            if len(cached_config) > 5:
                print(f"  ... and {len(cached_config) - 5} more items")

            # Demonstrate accessing cached values by key
            print("\nAccessing cached values by key:")
            try:
                cached_db_url = cached_config.get("DatabaseUrl", "Not in cache")
                print(f"  Cached DatabaseUrl: {cached_db_url}")

                cached_debug = cached_config.get("DebugMode", "Not in cache")
                print(f"  Cached DebugMode: {cached_debug}")
            except Exception as e:
                print(f"  Error accessing cached values: {e}")

            # Keep running for a while to demonstrate watching
            print("\nWatching for configuration changes... (press Ctrl+C to stop)")
            await asyncio.sleep(30)

        else:
            print("Failed to start configuration manager")

    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        await config_manager.stop()
        print("Configuration manager stopped")


if __name__ == "__main__":
    asyncio.run(main())
