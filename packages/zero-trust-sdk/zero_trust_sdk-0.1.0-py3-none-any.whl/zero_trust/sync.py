"""Sync manager for the Zero Trust SDK."""

import asyncio
import time
from typing import Any, Dict, List, Optional, Callable
from dataclasses import dataclass

from .http_client import HttpClient
from .types import SyncConfig, SyncStatus, ZeroTrustError


@dataclass
class SyncResult:
    """Result of a sync operation."""
    records_synced: int
    errors: List[str]
    duration_ms: int
    last_sync_time: str


class SyncManager:
    """Sync manager for Zero Trust API."""

    def __init__(self, http_client: HttpClient) -> None:
        """Initialize sync manager.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client
        self._running_syncs: Dict[str, asyncio.Task] = {}

    async def create_sync_config(
        self,
        name: str,
        source_type: str,
        source: str,
        target: str,
        interval: int,
    ) -> SyncConfig:
        """Create a new sync configuration.
        
        Args:
            name: Sync configuration name
            source_type: Source type (e.g., "database", "api", "file")
            source: Source connection string or URL
            target: Target database name
            interval: Sync interval in seconds
            
        Returns:
            Created sync configuration
            
        Raises:
            ZeroTrustError: If creation fails
        """
        if not all([name, source_type, source, target]):
            raise ZeroTrustError.validation("All sync configuration fields are required")
        
        if interval < 10:
            raise ZeroTrustError.validation("Sync interval must be at least 10 seconds")

        payload = {
            "name": name,
            "source_type": source_type,
            "source": source,
            "target": target,
            "interval": interval,
        }

        try:
            response = await self.http_client.post("/api/v1/sync/configs", payload)
            
            return SyncConfig(
                name=response.get("name"),
                source_type=response.get("source_type"),
                source=response.get("source"),
                target=response.get("target"),
                interval=response.get("interval"),
                created_at=response.get("created_at"),
                last_sync=response.get("last_sync"),
                status=SyncStatus.STOPPED,
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to create sync config: {e}", "SYNC_CONFIG_ERROR")

    async def list_sync_configs(self) -> List[SyncConfig]:
        """List all sync configurations.
        
        Returns:
            List of sync configurations
            
        Raises:
            ZeroTrustError: If request fails
        """
        try:
            response = await self.http_client.get("/api/v1/sync/configs")
            
            configs = []
            for config_data in response.get("configs", []):
                config = SyncConfig(
                    name=config_data.get("name"),
                    source_type=config_data.get("source_type"),
                    source=config_data.get("source"),
                    target=config_data.get("target"),
                    interval=config_data.get("interval"),
                    created_at=config_data.get("created_at"),
                    last_sync=config_data.get("last_sync"),
                    status=SyncStatus(config_data.get("status", "STOPPED")),
                )
                configs.append(config)
                
            return configs
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to list sync configs: {e}", "SYNC_LIST_ERROR")

    async def get_sync_config(self, name: str) -> SyncConfig:
        """Get sync configuration by name.
        
        Args:
            name: Sync configuration name
            
        Returns:
            Sync configuration
            
        Raises:
            ZeroTrustError: If config not found or request fails
        """
        if not name:
            raise ZeroTrustError.validation("Sync config name is required")

        try:
            response = await self.http_client.get(f"/api/v1/sync/configs/{name}")
            
            return SyncConfig(
                name=response.get("name"),
                source_type=response.get("source_type"),
                source=response.get("source"),
                target=response.get("target"),
                interval=response.get("interval"),
                created_at=response.get("created_at"),
                last_sync=response.get("last_sync"),
                status=SyncStatus(response.get("status", "STOPPED")),
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to get sync config: {e}", "SYNC_GET_ERROR")

    async def update_sync_config(
        self,
        name: str,
        **kwargs: Any,
    ) -> SyncConfig:
        """Update sync configuration.
        
        Args:
            name: Sync configuration name
            **kwargs: Fields to update
            
        Returns:
            Updated sync configuration
            
        Raises:
            ZeroTrustError: If update fails
        """
        if not name:
            raise ZeroTrustError.validation("Sync config name is required")
        
        if not kwargs:
            raise ZeroTrustError.validation("At least one field to update is required")

        # Validate interval if provided
        if "interval" in kwargs and kwargs["interval"] < 10:
            raise ZeroTrustError.validation("Sync interval must be at least 10 seconds")

        try:
            response = await self.http_client.put(f"/api/v1/sync/configs/{name}", kwargs)
            
            return SyncConfig(
                name=response.get("name"),
                source_type=response.get("source_type"),
                source=response.get("source"),
                target=response.get("target"),
                interval=response.get("interval"),
                created_at=response.get("created_at"),
                last_sync=response.get("last_sync"),
                status=SyncStatus(response.get("status", "STOPPED")),
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to update sync config: {e}", "SYNC_UPDATE_ERROR")

    async def delete_sync_config(self, name: str) -> bool:
        """Delete sync configuration.
        
        Args:
            name: Sync configuration name
            
        Returns:
            True if deletion successful
            
        Raises:
            ZeroTrustError: If deletion fails
        """
        if not name:
            raise ZeroTrustError.validation("Sync config name is required")

        # Stop sync if running
        if name in self._running_syncs:
            await self.stop_sync(name)

        try:
            await self.http_client.delete(f"/api/v1/sync/configs/{name}")
            return True
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to delete sync config: {e}", "SYNC_DELETE_ERROR")

    async def start_sync(
        self,
        name: str,
        callback: Optional[Callable[[SyncResult], None]] = None,
    ) -> bool:
        """Start sync process.
        
        Args:
            name: Sync configuration name
            callback: Optional callback for sync results
            
        Returns:
            True if sync started successfully
            
        Raises:
            ZeroTrustError: If start fails
        """
        if not name:
            raise ZeroTrustError.validation("Sync config name is required")
        
        if name in self._running_syncs:
            raise ZeroTrustError.validation(f"Sync '{name}' is already running")

        try:
            # Get sync configuration
            config = await self.get_sync_config(name)
            
            # Start sync task
            task = asyncio.create_task(self._run_sync_loop(config, callback))
            self._running_syncs[name] = task
            
            return True
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to start sync: {e}", "SYNC_START_ERROR")

    async def stop_sync(self, name: str) -> bool:
        """Stop sync process.
        
        Args:
            name: Sync configuration name
            
        Returns:
            True if sync stopped successfully
            
        Raises:
            ZeroTrustError: If stop fails
        """
        if not name:
            raise ZeroTrustError.validation("Sync config name is required")
        
        if name not in self._running_syncs:
            return True  # Already stopped

        try:
            # Cancel the sync task
            task = self._running_syncs[name]
            task.cancel()
            
            try:
                await task
            except asyncio.CancelledError:
                pass  # Expected
            
            del self._running_syncs[name]
            return True
            
        except Exception as e:
            raise ZeroTrustError(f"Failed to stop sync: {e}", "SYNC_STOP_ERROR")

    async def sync_once(
        self,
        name: str,
    ) -> SyncResult:
        """Run sync once.
        
        Args:
            name: Sync configuration name
            
        Returns:
            Sync result
            
        Raises:
            ZeroTrustError: If sync fails
        """
        if not name:
            raise ZeroTrustError.validation("Sync config name is required")

        try:
            # Get sync configuration
            config = await self.get_sync_config(name)
            
            # Run sync once
            return await self._perform_sync(config)
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to run sync: {e}", "SYNC_RUN_ERROR")

    async def get_sync_status(self, name: str) -> Dict[str, Any]:
        """Get sync process status.
        
        Args:
            name: Sync configuration name
            
        Returns:
            Sync status information
            
        Raises:
            ZeroTrustError: If status request fails
        """
        if not name:
            raise ZeroTrustError.validation("Sync config name is required")

        try:
            # Check if sync is running locally
            is_running = name in self._running_syncs
            
            # Get config for additional info
            config = await self.get_sync_config(name)
            
            return {
                "name": name,
                "status": "RUNNING" if is_running else "STOPPED",
                "last_sync": config.last_sync,
                "interval": config.interval,
                "source": config.source,
                "target": config.target,
            }
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to get sync status: {e}", "SYNC_STATUS_ERROR")

    async def from_api(
        self,
        url: str,
        database: str,
        table_name: str,
        headers: Optional[Dict[str, str]] = None,
    ) -> SyncResult:
        """Sync data from external API.
        
        Args:
            url: API endpoint URL
            database: Target database name
            table_name: Target table name
            headers: Optional HTTP headers
            
        Returns:
            Sync result
            
        Raises:
            ZeroTrustError: If API sync fails
        """
        if not all([url, database, table_name]):
            raise ZeroTrustError.validation("URL, database, and table name are required")

        try:
            import aiohttp
            
            # Fetch data from API
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers or {}) as response:
                    if response.status != 200:
                        raise ZeroTrustError.server_error(
                            response.status, f"API returned {response.status}"
                        )
                    
                    data = await response.json()
            
            # Import data
            from .migration import MigrationManager
            migration = MigrationManager(self.http_client)
            
            start_time = time.time()
            
            if isinstance(data, list):
                records = data
            elif isinstance(data, dict) and "data" in data:
                records = data["data"]
            else:
                records = [data]  # Single record
            
            # Import records
            if records:
                await migration.import_dataframe(database, table_name, pd.DataFrame(records))
            
            duration_ms = int((time.time() - start_time) * 1000)
            
            return SyncResult(
                records_synced=len(records),
                errors=[],
                duration_ms=duration_ms,
                last_sync_time=str(int(time.time())),
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"API sync failed: {e}", "API_SYNC_ERROR")

    async def _run_sync_loop(
        self,
        config: SyncConfig,
        callback: Optional[Callable[[SyncResult], None]] = None,
    ) -> None:
        """Run sync loop for a configuration.
        
        Args:
            config: Sync configuration
            callback: Optional callback for sync results
        """
        while True:
            try:
                # Perform sync
                result = await self._perform_sync(config)
                
                # Call callback if provided
                if callback:
                    try:
                        callback(result)
                    except Exception:
                        pass  # Don't let callback errors stop sync
                
                # Wait for next interval
                await asyncio.sleep(config.interval)
                
            except asyncio.CancelledError:
                break
            except Exception:
                # Log error and continue
                await asyncio.sleep(config.interval)

    async def _perform_sync(self, config: SyncConfig) -> SyncResult:
        """Perform actual sync operation.
        
        Args:
            config: Sync configuration
            
        Returns:
            Sync result
        """
        start_time = time.time()
        errors = []
        records_synced = 0
        
        try:
            if config.source_type == "api":
                # Sync from API
                result = await self.from_api(config.source, config.target, "synced_data")
                records_synced = result.records_synced
                errors = result.errors
            else:
                # Other sync types would be implemented here
                errors.append(f"Sync type '{config.source_type}' not yet implemented")
                
        except Exception as e:
            errors.append(str(e))
        
        duration_ms = int((time.time() - start_time) * 1000)
        
        return SyncResult(
            records_synced=records_synced,
            errors=errors,
            duration_ms=duration_ms,
            last_sync_time=str(int(time.time())),
        )

    def get_running_syncs(self) -> List[str]:
        """Get list of currently running sync names.
        
        Returns:
            List of running sync names
        """
        return list(self._running_syncs.keys())

    async def stop_all_syncs(self) -> bool:
        """Stop all running syncs.
        
        Returns:
            True if all syncs stopped successfully
        """
        try:
            for name in list(self._running_syncs.keys()):
                await self.stop_sync(name)
            return True
        except Exception:
            return False