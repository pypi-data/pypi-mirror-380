"""Type definitions for the Zero Trust SDK."""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from enum import Enum


class MigrationState(Enum):
    """Migration state enumeration."""
    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELLED = "Cancelled"


class SyncStatus(Enum):
    """Sync status enumeration."""
    STOPPED = "Stopped"
    RUNNING = "Running"


class OperationType(Enum):
    """Database operation type."""
    READ = "Read"
    WRITE = "Write"
    SCHEMA = "Schema"


@dataclass
class User:
    """User information."""
    id: str
    email: str
    role: str
    created_at: str
    wallet_address: Optional[str] = None


@dataclass
class AuthResponse:
    """Authentication response."""
    token: str
    user: User
    expires_at: Optional[str] = None


@dataclass
class Column:
    """Column definition."""
    name: str
    data_type: str
    nullable: bool
    default_value: Optional[str] = None
    is_primary_key: bool = False


@dataclass
class Table:
    """Table information."""
    name: str
    columns: List[Column]
    row_count: Optional[int] = None
    size: Optional[int] = None
    created_at: Optional[str] = None


@dataclass
class Database:
    """Database information."""
    name: str
    tables: List[str]
    created_at: Optional[str] = None
    size: Optional[int] = None
    record_count: Optional[int] = None


@dataclass
class QueryMeta:
    """Query execution metadata."""
    row_count: int
    execution_time_ms: Optional[int] = None
    operation_type: OperationType = OperationType.READ


@dataclass
class QueryData:
    """Query result data."""
    columns: Optional[List[str]] = None
    rows: List[List[Any]] = None

    def __post_init__(self) -> None:
        if self.rows is None:
            self.rows = []


@dataclass
class QueryResult:
    """Query result with data and metadata."""
    data: QueryData
    meta: QueryMeta


@dataclass
class QueryOptions:
    """Query execution options."""
    max_rows: Optional[int] = None
    timeout_ms: Optional[int] = None
    include_meta: bool = False


@dataclass
class HealthStatus:
    """System health status."""
    status: str
    version: str
    database: str
    blockchain: str
    uptime: Optional[int] = None


@dataclass
class SystemStats:
    """System statistics."""
    databases: int
    tables: int
    rows: int
    storage_bytes: Optional[int] = None
    active_connections: Optional[int] = None


@dataclass
class MigrationStatus:
    """Migration status."""
    id: str
    status: MigrationState
    records_processed: int
    total_records: Optional[int] = None
    started_at: str
    completed_at: Optional[str] = None
    error: Optional[str] = None


@dataclass
class SyncConfig:
    """Sync configuration."""
    name: str
    source_type: str
    source: str
    target: str
    interval: int
    created_at: str
    last_sync: Optional[str] = None
    status: Union[SyncStatus, Dict[str, Any]] = SyncStatus.STOPPED


@dataclass
class BatchResult:
    """Batch operation result."""
    successful: int
    failed: int
    errors: List[Dict[str, Union[int, str]]]


class ZeroTrustError(Exception):
    """Base exception for Zero Trust SDK errors."""

    def __init__(
        self,
        message: str,
        code: str = "UNKNOWN_ERROR",
        status: Optional[int] = None,
        is_retryable: bool = False,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.status = status
        self.is_retryable = is_retryable

    @classmethod
    def auth(cls, message: str) -> "ZeroTrustError":
        """Create an authentication error."""
        return cls(message, "AUTH_ERROR", 401, False)

    @classmethod
    def validation(cls, message: str) -> "ZeroTrustError":
        """Create a validation error."""
        return cls(message, "VALIDATION_ERROR", 400, False)

    @classmethod
    def not_found(cls, resource: str) -> "ZeroTrustError":
        """Create a not found error."""
        return cls(f"Resource not found: {resource}", "NOT_FOUND", 404, False)

    @classmethod
    def permission_denied(cls, operation: str) -> "ZeroTrustError":
        """Create a permission denied error."""
        return cls(f"Permission denied: {operation}", "PERMISSION_DENIED", 403, False)

    @classmethod
    def server_error(cls, status: int, message: str) -> "ZeroTrustError":
        """Create a server error."""
        return cls(message, "SERVER_ERROR", status, status >= 500)

    @classmethod
    def client_error(cls, status: int, message: str) -> "ZeroTrustError":
        """Create a client error."""
        return cls(message, "CLIENT_ERROR", status, False)

    @classmethod
    def rate_limit(cls, retry_after: int) -> "ZeroTrustError":
        """Create a rate limit error."""
        return cls(
            f"Rate limit exceeded. Try again in {retry_after} seconds",
            "RATE_LIMIT",
            429,
            True,
        )

    @classmethod
    def timeout(cls) -> "ZeroTrustError":
        """Create a timeout error."""
        return cls("Request timed out", "TIMEOUT", None, True)

    @classmethod
    def network(cls, message: str) -> "ZeroTrustError":
        """Create a network error."""
        return cls(f"Network error: {message}", "NETWORK_ERROR", None, True)

    def __str__(self) -> str:
        return f"ZeroTrustError[{self.code}]: {self.message}"

    def __repr__(self) -> str:
        return (
            f"ZeroTrustError(message={self.message!r}, code={self.code!r}, "
            f"status={self.status}, is_retryable={self.is_retryable})"
        )