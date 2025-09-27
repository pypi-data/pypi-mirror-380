"""
Zero Trust SDK for Python

A powerful Python SDK for interacting with Zero Trust Blockchain Databases with pandas integration.

Example:
    >>> from zero_trust import ZeroTrustClient, Config
    >>> 
    >>> # Initialize client
    >>> client = ZeroTrustClient.create("https://api.zerotrust.com")
    >>> 
    >>> # Authenticate
    >>> client.auth.login("user@example.com", "password")
    >>> 
    >>> # Query data as pandas DataFrame
    >>> df = client.databases.query("my-app-db").to_dataframe("SELECT * FROM users")
    >>> 
    >>> # Export DataFrame to Zero Trust database
    >>> client.migration.import_dataframe(df, "my-app-db", "users_backup")
"""

from .client import ZeroTrustClient
from .config import Config
from .types import (
    User,
    AuthResponse,
    Database,
    Table,
    Column,
    QueryResult,
    QueryOptions,
    HealthStatus,
    SystemStats,
    MigrationStatus,
    SyncConfig,
    ZeroTrustError,
)
from .auth import AuthManager
from .database import DatabaseManager, QueryBuilder
from .migration import MigrationManager
from .sync import SyncManager

__version__ = "0.1.0"
__author__ = "Zero Trust Team"
__email__ = "dev@zerotrust.com"

__all__ = [
    # Main classes
    "ZeroTrustClient",
    "Config",
    # Managers
    "AuthManager",
    "DatabaseManager",
    "QueryBuilder",
    "MigrationManager",
    "SyncManager",
    # Types
    "User",
    "AuthResponse",
    "Database",
    "Table",
    "Column",
    "QueryResult",
    "QueryOptions",
    "HealthStatus",
    "SystemStats",
    "MigrationStatus",
    "SyncConfig",
    "ZeroTrustError",
    # Metadata
    "__version__",
]