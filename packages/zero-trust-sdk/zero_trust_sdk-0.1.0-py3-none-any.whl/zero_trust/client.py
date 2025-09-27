"""
Main client for the Zero Trust SDK
"""

from typing import Optional

from .config import Config
from .http_client import HttpClient
from .auth import AuthManager
from .database import DatabaseManager
from .migration import MigrationManager
from .sync import SyncManager
from .types import HealthStatus, SystemStats, ZeroTrustError


class ZeroTrustClient:
    """Main Zero Trust SDK client."""

    def __init__(self, config: Config) -> None:
        """Initialize the client with configuration.
        
        Args:
            config: Client configuration
        """
        self._config = config
        self._http_client = HttpClient(config)
        self._auth = AuthManager(self._http_client)
        self._databases = DatabaseManager(self._http_client)
        self._migration = MigrationManager(self._http_client)
        self._sync = SyncManager(self._http_client)

    @classmethod
    async def create(cls, api_url: str, token: Optional[str] = None) -> "ZeroTrustClient":
        """Create a new Zero Trust client.
        
        Args:
            api_url: API base URL
            token: Authentication token (optional)
            
        Returns:
            Initialized client
            
        Raises:
            ZeroTrustError: If connection fails
        """
        config = Config(api_url=api_url, token=token)
        client = cls(config)
        
        # Test connectivity
        try:
            await client.health()
        except ZeroTrustError as e:
            if e.code == 'NETWORK_ERROR':
                raise ZeroTrustError.network(
                    f"Could not connect to Zero Trust API at {api_url}. "
                    f"Please check the URL and network connectivity."
                )
            raise e
        
        return client

    @classmethod
    async def create_with_defaults(cls) -> "ZeroTrustClient":
        """Create a client with default configuration from environment.
        
        Returns:
            Initialized client
        """
        config = Config.from_env()
        return await cls.create(config.api_url, config.token)

    @property
    def auth(self) -> AuthManager:
        """Get the authentication manager."""
        return self._auth

    @property
    def databases(self) -> DatabaseManager:
        """Get the database manager."""
        return self._databases

    @property
    def migration(self) -> MigrationManager:
        """Get the migration manager."""
        return self._migration

    @property
    def sync(self) -> SyncManager:
        """Get the sync manager."""
        return self._sync

    async def health(self) -> HealthStatus:
        """Check system health.
        
        Returns:
            Health status information
            
        Raises:
            ZeroTrustError: If health check fails
        """
        try:
            response = await self._http_client.get("/health")
            return HealthStatus(**response)
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Health check failed: {e}", "HEALTH_CHECK_ERROR")

    async def stats(self) -> SystemStats:
        """Get system statistics.
        
        Returns:
            System statistics
            
        Raises:
            ZeroTrustError: If stats request fails
        """
        try:
            response = await self._http_client.get("/api/v1/stats")
            return SystemStats(**response)
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to get system stats: {e}", "STATS_ERROR")

    def get_config(self) -> Config:
        """Get the current configuration.
        
        Returns:
            Current configuration
        """
        return self._config

    def set_token(self, token: str) -> None:
        """Update the authentication token.
        
        Args:
            token: New authentication token
        """
        self._config = self._config.with_token(token)
        self._http_client.set_token(token)

    def is_authenticated(self) -> bool:
        """Check if the client is authenticated.
        
        Returns:
            True if authenticated, False otherwise
        """
        return self._config.is_authenticated()

    async def test_connection(self) -> bool:
        """Test the connection to the API.
        
        Returns:
            True if connection successful, False otherwise
        """
        return await self._http_client.test_connection()

    async def version(self) -> dict:
        """Get API version information.
        
        Returns:
            Version information
            
        Raises:
            ZeroTrustError: If version request fails
        """
        try:
            return await self._http_client.get("/api/v1/version")
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to get version info: {e}", "VERSION_ERROR")

    async def ping(self) -> dict:
        """Ping the API server.
        
        Returns:
            Ping response with message and timestamp
            
        Raises:
            ZeroTrustError: If ping fails
        """
        try:
            return await self._http_client.get("/api/v1/ping")
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Ping failed: {e}", "PING_ERROR")