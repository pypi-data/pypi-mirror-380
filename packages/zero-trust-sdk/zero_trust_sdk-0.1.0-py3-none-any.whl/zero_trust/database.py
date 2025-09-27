"""Database manager for the Zero Trust SDK."""

from typing import Any, Dict, List, Optional
import pandas as pd

from .http_client import HttpClient
from .types import Database, Table, Column, QueryResult, QueryOptions, ZeroTrustError


class DatabaseManager:
    """Database manager for Zero Trust API."""

    def __init__(self, http_client: HttpClient) -> None:
        """Initialize database manager.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client

    async def list_databases(self) -> List[Database]:
        """List all databases.
        
        Returns:
            List of databases
            
        Raises:
            ZeroTrustError: If request fails
        """
        try:
            response = await self.http_client.get("/api/v1/databases")
            
            databases = []
            for db_data in response.get("databases", []):
                database = Database(
                    name=db_data.get("name"),
                    tables=db_data.get("tables", []),
                    created_at=db_data.get("created_at"),
                    size=db_data.get("size"),
                    record_count=db_data.get("record_count"),
                )
                databases.append(database)
                
            return databases
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to list databases: {e}", "DATABASE_LIST_ERROR")

    async def create_database(self, name: str) -> Database:
        """Create a new database.
        
        Args:
            name: Database name
            
        Returns:
            Created database information
            
        Raises:
            ZeroTrustError: If creation fails
        """
        if not name:
            raise ZeroTrustError.validation("Database name is required")

        payload = {"name": name}

        try:
            response = await self.http_client.post("/api/v1/databases", payload)
            
            return Database(
                name=response.get("name"),
                tables=response.get("tables", []),
                created_at=response.get("created_at"),
                size=response.get("size"),
                record_count=response.get("record_count"),
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to create database: {e}", "DATABASE_CREATE_ERROR")

    async def get_database(self, name: str) -> Database:
        """Get database information.
        
        Args:
            name: Database name
            
        Returns:
            Database information
            
        Raises:
            ZeroTrustError: If database not found or request fails
        """
        if not name:
            raise ZeroTrustError.validation("Database name is required")

        try:
            response = await self.http_client.get(f"/api/v1/databases/{name}")
            
            return Database(
                name=response.get("name"),
                tables=response.get("tables", []),
                created_at=response.get("created_at"),
                size=response.get("size"),
                record_count=response.get("record_count"),
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to get database: {e}", "DATABASE_GET_ERROR")

    async def delete_database(self, name: str) -> bool:
        """Delete a database.
        
        Args:
            name: Database name
            
        Returns:
            True if deletion successful
            
        Raises:
            ZeroTrustError: If deletion fails
        """
        if not name:
            raise ZeroTrustError.validation("Database name is required")

        try:
            await self.http_client.delete(f"/api/v1/databases/{name}")
            return True
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to delete database: {e}", "DATABASE_DELETE_ERROR")

    async def create_table(
        self,
        database: str,
        table_name: str,
        columns: List[Column],
    ) -> Table:
        """Create a new table.
        
        Args:
            database: Database name
            table_name: Table name
            columns: Table columns
            
        Returns:
            Created table information
            
        Raises:
            ZeroTrustError: If creation fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")
        
        if not columns:
            raise ZeroTrustError.validation("At least one column is required")

        # Convert columns to API format
        column_names = [col.name for col in columns]
        column_types = [col.data_type for col in columns]

        payload = {
            "name": table_name,
            "columns": column_names,
            "types": column_types,
        }

        try:
            response = await self.http_client.post(
                f"/api/v1/databases/{database}/tables", payload
            )
            
            # Parse column information
            parsed_columns = []
            for i, col_name in enumerate(column_names):
                parsed_columns.append(Column(
                    name=col_name,
                    data_type=column_types[i],
                    nullable=columns[i].nullable,
                    default_value=columns[i].default_value,
                    is_primary_key=columns[i].is_primary_key,
                ))
            
            return Table(
                name=response.get("name", table_name),
                columns=parsed_columns,
                row_count=response.get("row_count", 0),
                size=response.get("size"),
                created_at=response.get("created_at"),
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to create table: {e}", "TABLE_CREATE_ERROR")

    async def get_table(self, database: str, table_name: str) -> Table:
        """Get table information.
        
        Args:
            database: Database name
            table_name: Table name
            
        Returns:
            Table information
            
        Raises:
            ZeroTrustError: If table not found or request fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")

        try:
            response = await self.http_client.get(
                f"/api/v1/databases/{database}/tables/{table_name}"
            )
            
            # Parse column information
            columns = []
            column_data = response.get("columns", [])
            for col in column_data:
                columns.append(Column(
                    name=col.get("name"),
                    data_type=col.get("data_type"),
                    nullable=col.get("nullable", True),
                    default_value=col.get("default_value"),
                    is_primary_key=col.get("is_primary_key", False),
                ))
            
            return Table(
                name=response.get("name"),
                columns=columns,
                row_count=response.get("row_count"),
                size=response.get("size"),
                created_at=response.get("created_at"),
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to get table: {e}", "TABLE_GET_ERROR")

    async def insert_data(
        self,
        database: str,
        table_name: str,
        data: List[Dict[str, Any]],
    ) -> int:
        """Insert data into a table.
        
        Args:
            database: Database name
            table_name: Table name
            data: List of records to insert
            
        Returns:
            Number of inserted records
            
        Raises:
            ZeroTrustError: If insertion fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")
        
        if not data:
            raise ZeroTrustError.validation("Data is required")

        payload = {
            "database": database,
            "table": table_name,
            "data": data,
        }

        try:
            response = await self.http_client.post("/api/v1/data", payload)
            return response.get("inserted_count", len(data))
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to insert data: {e}", "DATA_INSERT_ERROR")

    async def query_data(
        self,
        database: str,
        table_name: str,
        offset: int = 0,
        limit: int = 100,
    ) -> QueryResult:
        """Query table data with pagination.
        
        Args:
            database: Database name
            table_name: Table name
            offset: Row offset for pagination
            limit: Maximum number of rows to return
            
        Returns:
            Query result with data and metadata
            
        Raises:
            ZeroTrustError: If query fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")

        params = {
            "offset": offset,
            "limit": limit,
        }

        try:
            response = await self.http_client.get(
                f"/api/v1/databases/{database}/tables/{table_name}/data",
                params=params,
            )
            
            from .types import QueryData, QueryMeta, OperationType
            
            query_data = QueryData(
                columns=response.get("columns"),
                rows=response.get("rows", []),
            )
            
            query_meta = QueryMeta(
                row_count=response.get("total_rows", len(query_data.rows)),
                execution_time_ms=response.get("execution_time_ms"),
                operation_type=OperationType.READ,
            )
            
            return QueryResult(data=query_data, meta=query_meta)
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to query data: {e}", "DATA_QUERY_ERROR")

    async def search_table(
        self,
        database: str,
        table_name: str,
        column: str,
        value: str,
        limit: int = 100,
    ) -> QueryResult:
        """Search table data by column value.
        
        Args:
            database: Database name
            table_name: Table name
            column: Column to search in
            value: Value to search for
            limit: Maximum number of rows to return
            
        Returns:
            Query result with matching data
            
        Raises:
            ZeroTrustError: If search fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")
        
        if not column or not value:
            raise ZeroTrustError.validation("Column and value are required for search")

        params = {
            "column": column,
            "value": value,
            "limit": limit,
        }

        try:
            response = await self.http_client.get(
                f"/api/v1/databases/{database}/tables/{table_name}/search",
                params=params,
            )
            
            from .types import QueryData, QueryMeta, OperationType
            
            query_data = QueryData(
                columns=response.get("columns"),
                rows=response.get("rows", []),
            )
            
            query_meta = QueryMeta(
                row_count=len(query_data.rows),
                execution_time_ms=response.get("execution_time_ms"),
                operation_type=OperationType.READ,
            )
            
            return QueryResult(data=query_data, meta=query_meta)
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to search table: {e}", "SEARCH_ERROR")

    def query(self, database: str) -> "QueryBuilder":
        """Create a query builder for the database.
        
        Args:
            database: Database name
            
        Returns:
            Query builder instance
        """
        return QueryBuilder(self.http_client, database)

    async def to_dataframe(
        self,
        database: str,
        table_name: str,
        limit: Optional[int] = None,
    ) -> pd.DataFrame:
        """Convert table data to pandas DataFrame.
        
        Args:
            database: Database name
            table_name: Table name
            limit: Maximum number of rows (None for all)
            
        Returns:
            pandas DataFrame with table data
            
        Raises:
            ZeroTrustError: If conversion fails
        """
        try:
            # Query all data in batches if no limit specified
            if limit is None:
                # First, get total row count
                result = await self.query_data(database, table_name, offset=0, limit=1)
                total_rows = result.meta.row_count
                
                # Query all data in batches
                all_rows = []
                batch_size = 1000
                for offset in range(0, total_rows, batch_size):
                    batch_result = await self.query_data(
                        database, table_name, offset=offset, limit=batch_size
                    )
                    all_rows.extend(batch_result.data.rows)
                
                # Create DataFrame
                if all_rows and result.data.columns:
                    return pd.DataFrame(all_rows, columns=result.data.columns)
                else:
                    return pd.DataFrame()
            else:
                # Query limited data
                result = await self.query_data(database, table_name, limit=limit)
                if result.data.rows and result.data.columns:
                    return pd.DataFrame(result.data.rows, columns=result.data.columns)
                else:
                    return pd.DataFrame()
                    
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to create DataFrame: {e}", "DATAFRAME_ERROR")


class QueryBuilder:
    """SQL query builder for Zero Trust databases."""

    def __init__(self, http_client: HttpClient, database: str) -> None:
        """Initialize query builder.
        
        Args:
            http_client: HTTP client instance
            database: Database name
        """
        self.http_client = http_client
        self.database = database

    async def execute(self, sql: str, options: Optional[QueryOptions] = None) -> QueryResult:
        """Execute SQL query.
        
        Args:
            sql: SQL query string
            options: Query execution options
            
        Returns:
            Query result
            
        Raises:
            ZeroTrustError: If query execution fails
        """
        if not sql:
            raise ZeroTrustError.validation("SQL query is required")

        payload = {
            "sql": sql,
            "database": self.database,
        }
        
        if options:
            if options.max_rows:
                payload["max_rows"] = options.max_rows
            if options.timeout_ms:
                payload["timeout_ms"] = options.timeout_ms
            payload["include_meta"] = options.include_meta

        try:
            response = await self.http_client.post("/api/v1/query/execute", payload)
            
            from .types import QueryData, QueryMeta, OperationType
            
            query_data = QueryData(
                columns=response.get("columns"),
                rows=response.get("rows", []),
            )
            
            query_meta = QueryMeta(
                row_count=response.get("row_count", len(query_data.rows)),
                execution_time_ms=response.get("execution_time_ms"),
                operation_type=OperationType.READ if sql.strip().upper().startswith("SELECT") else OperationType.WRITE,
            )
            
            return QueryResult(data=query_data, meta=query_meta)
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to execute query: {e}", "QUERY_EXECUTION_ERROR")

    async def to_dataframe(self, sql: str) -> pd.DataFrame:
        """Execute SQL query and return results as DataFrame.
        
        Args:
            sql: SQL query string
            
        Returns:
            pandas DataFrame with query results
            
        Raises:
            ZeroTrustError: If query execution fails
        """
        try:
            result = await self.execute(sql)
            if result.data.rows and result.data.columns:
                return pd.DataFrame(result.data.rows, columns=result.data.columns)
            else:
                return pd.DataFrame()
                
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Failed to create DataFrame from query: {e}", "QUERY_DATAFRAME_ERROR")