"""Migration manager for the Zero Trust SDK."""

import csv
import io
import json
from typing import Any, Dict, List, Optional, Union
import pandas as pd

from .http_client import HttpClient
from .types import MigrationStatus, BatchResult, ZeroTrustError


class MigrationManager:
    """Migration manager for Zero Trust API."""

    def __init__(self, http_client: HttpClient) -> None:
        """Initialize migration manager.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client

    async def import_csv(
        self,
        database: str,
        table_name: str,
        csv_content: str,
        has_header: bool = True,
        batch_size: int = 1000,
    ) -> MigrationStatus:
        """Import data from CSV content.
        
        Args:
            database: Database name
            table_name: Table name
            csv_content: CSV content as string
            has_header: Whether CSV has header row
            batch_size: Number of records per batch
            
        Returns:
            Migration status
            
        Raises:
            ZeroTrustError: If import fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")
        
        if not csv_content:
            raise ZeroTrustError.validation("CSV content is required")

        try:
            # Parse CSV content
            csv_reader = csv.reader(io.StringIO(csv_content))
            rows = list(csv_reader)
            
            if not rows:
                raise ZeroTrustError.validation("CSV contains no data")
            
            # Extract headers and data
            if has_header:
                headers = rows[0]
                data_rows = rows[1:]
            else:
                headers = [f"column_{i}" for i in range(len(rows[0]))]
                data_rows = rows
            
            # Convert to list of dictionaries
            records = []
            for row in data_rows:
                if len(row) != len(headers):
                    continue  # Skip malformed rows
                record = {headers[i]: row[i] for i in range(len(headers))}
                records.append(record)
            
            # Import in batches
            total_imported = 0
            for i in range(0, len(records), batch_size):
                batch = records[i:i + batch_size]
                
                payload = {
                    "database": database,
                    "table": table_name,
                    "data": batch,
                }
                
                response = await self.http_client.post("/api/v1/data", payload)
                total_imported += response.get("inserted_count", len(batch))
            
            return MigrationStatus(
                id=f"csv_import_{table_name}",
                status="Completed",
                records_processed=total_imported,
                total_records=len(records),
                started_at="",  # Would be populated by server
                completed_at="",  # Would be populated by server
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"CSV import failed: {e}", "CSV_IMPORT_ERROR")

    async def import_json(
        self,
        database: str,
        table_name: str,
        json_content: str,
        batch_size: int = 1000,
    ) -> MigrationStatus:
        """Import data from JSON content.
        
        Args:
            database: Database name
            table_name: Table name
            json_content: JSON content as string
            batch_size: Number of records per batch
            
        Returns:
            Migration status
            
        Raises:
            ZeroTrustError: If import fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")
        
        if not json_content:
            raise ZeroTrustError.validation("JSON content is required")

        try:
            # Parse JSON content
            data = json.loads(json_content)
            
            # Handle different JSON structures
            if isinstance(data, list):
                records = data
            elif isinstance(data, dict) and "data" in data:
                records = data["data"]
            elif isinstance(data, dict) and "records" in data:
                records = data["records"]
            else:
                raise ZeroTrustError.validation("Unsupported JSON structure")
            
            if not records:
                raise ZeroTrustError.validation("JSON contains no data")
            
            # Ensure all records are dictionaries
            if not all(isinstance(record, dict) for record in records):
                raise ZeroTrustError.validation("All records must be objects")
            
            # Import in batches
            total_imported = 0
            for i in range(0, len(records), batch_size):
                batch = records[i:i + batch_size]
                
                payload = {
                    "database": database,
                    "table": table_name,
                    "data": batch,
                }
                
                response = await self.http_client.post("/api/v1/data", payload)
                total_imported += response.get("inserted_count", len(batch))
            
            return MigrationStatus(
                id=f"json_import_{table_name}",
                status="Completed",
                records_processed=total_imported,
                total_records=len(records),
                started_at="",  # Would be populated by server
                completed_at="",  # Would be populated by server
            )
            
        except ZeroTrustError:
            raise
        except json.JSONDecodeError as e:
            raise ZeroTrustError.validation(f"Invalid JSON: {e}")
        except Exception as e:
            raise ZeroTrustError(f"JSON import failed: {e}", "JSON_IMPORT_ERROR")

    async def import_dataframe(
        self,
        database: str,
        table_name: str,
        df: pd.DataFrame,
        batch_size: int = 1000,
    ) -> MigrationStatus:
        """Import data from pandas DataFrame.
        
        Args:
            database: Database name
            table_name: Table name
            df: pandas DataFrame
            batch_size: Number of records per batch
            
        Returns:
            Migration status
            
        Raises:
            ZeroTrustError: If import fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")
        
        if df is None or df.empty:
            raise ZeroTrustError.validation("DataFrame is empty")

        try:
            # Convert DataFrame to records
            records = df.to_dict('records')
            
            # Import in batches
            total_imported = 0
            for i in range(0, len(records), batch_size):
                batch = records[i:i + batch_size]
                
                payload = {
                    "database": database,
                    "table": table_name,
                    "data": batch,
                }
                
                response = await self.http_client.post("/api/v1/data", payload)
                total_imported += response.get("inserted_count", len(batch))
            
            return MigrationStatus(
                id=f"dataframe_import_{table_name}",
                status="Completed",
                records_processed=total_imported,
                total_records=len(records),
                started_at="",  # Would be populated by server
                completed_at="",  # Would be populated by server
            )
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"DataFrame import failed: {e}", "DATAFRAME_IMPORT_ERROR")

    async def export_to_csv(
        self,
        database: str,
        table_name: str,
        include_header: bool = True,
    ) -> str:
        """Export table data to CSV format.
        
        Args:
            database: Database name
            table_name: Table name
            include_header: Whether to include header row
            
        Returns:
            CSV content as string
            
        Raises:
            ZeroTrustError: If export fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")

        try:
            # Query all data from table
            from .database import DatabaseManager
            db_manager = DatabaseManager(self.http_client)
            
            # Get all data in batches
            all_rows = []
            columns = None
            offset = 0
            batch_size = 1000
            
            while True:
                result = await db_manager.query_data(
                    database, table_name, offset=offset, limit=batch_size
                )
                
                if not result.data.rows:
                    break
                    
                if columns is None:
                    columns = result.data.columns
                    
                all_rows.extend(result.data.rows)
                
                if len(result.data.rows) < batch_size:
                    break
                    
                offset += batch_size
            
            # Convert to CSV
            output = io.StringIO()
            writer = csv.writer(output)
            
            if include_header and columns:
                writer.writerow(columns)
                
            for row in all_rows:
                writer.writerow(row)
            
            return output.getvalue()
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"CSV export failed: {e}", "CSV_EXPORT_ERROR")

    async def export_to_json(
        self,
        database: str,
        table_name: str,
        format_type: str = "records",
    ) -> str:
        """Export table data to JSON format.
        
        Args:
            database: Database name
            table_name: Table name
            format_type: JSON format ("records", "values", "index")
            
        Returns:
            JSON content as string
            
        Raises:
            ZeroTrustError: If export fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")

        try:
            # Query all data from table
            from .database import DatabaseManager
            db_manager = DatabaseManager(self.http_client)
            
            # Get all data in batches
            all_rows = []
            columns = None
            offset = 0
            batch_size = 1000
            
            while True:
                result = await db_manager.query_data(
                    database, table_name, offset=offset, limit=batch_size
                )
                
                if not result.data.rows:
                    break
                    
                if columns is None:
                    columns = result.data.columns
                    
                all_rows.extend(result.data.rows)
                
                if len(result.data.rows) < batch_size:
                    break
                    
                offset += batch_size
            
            # Convert to different JSON formats
            if format_type == "records":
                # List of objects
                records = []
                if columns:
                    for row in all_rows:
                        record = {columns[i]: row[i] for i in range(len(columns))}
                        records.append(record)
                return json.dumps(records, indent=2)
                
            elif format_type == "values":
                # Just the values
                return json.dumps(all_rows, indent=2)
                
            elif format_type == "index":
                # Object with numeric indices
                indexed = {}
                if columns:
                    for i, row in enumerate(all_rows):
                        record = {columns[j]: row[j] for j in range(len(columns))}
                        indexed[str(i)] = record
                return json.dumps(indexed, indent=2)
                
            else:
                raise ZeroTrustError.validation(f"Unsupported format type: {format_type}")
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"JSON export failed: {e}", "JSON_EXPORT_ERROR")

    async def export_to_dataframe(
        self,
        database: str,
        table_name: str,
    ) -> pd.DataFrame:
        """Export table data to pandas DataFrame.
        
        Args:
            database: Database name
            table_name: Table name
            
        Returns:
            pandas DataFrame with table data
            
        Raises:
            ZeroTrustError: If export fails
        """
        if not database or not table_name:
            raise ZeroTrustError.validation("Database and table names are required")

        try:
            from .database import DatabaseManager
            db_manager = DatabaseManager(self.http_client)
            return await db_manager.to_dataframe(database, table_name)
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"DataFrame export failed: {e}", "DATAFRAME_EXPORT_ERROR")

    async def backup_database(
        self,
        database: str,
        include_data: bool = True,
        format_type: str = "json",
    ) -> str:
        """Create a backup of the entire database.
        
        Args:
            database: Database name
            include_data: Whether to include data or just schema
            format_type: Backup format ("json", "csv")
            
        Returns:
            Backup content as string
            
        Raises:
            ZeroTrustError: If backup fails
        """
        if not database:
            raise ZeroTrustError.validation("Database name is required")

        try:
            from .database import DatabaseManager
            db_manager = DatabaseManager(self.http_client)
            
            # Get database information
            db_info = await db_manager.get_database(database)
            
            backup_data = {
                "database": database,
                "created_at": db_info.created_at,
                "tables": {},
            }
            
            # Backup each table
            for table_name in db_info.tables:
                table_info = await db_manager.get_table(database, table_name)
                
                table_backup = {
                    "name": table_name,
                    "columns": [
                        {
                            "name": col.name,
                            "data_type": col.data_type,
                            "nullable": col.nullable,
                            "default_value": col.default_value,
                            "is_primary_key": col.is_primary_key,
                        }
                        for col in table_info.columns
                    ],
                }
                
                if include_data:
                    # Export table data
                    if format_type == "json":
                        result = await db_manager.query_data(database, table_name, limit=None)
                        table_backup["data"] = result.data.rows
                    else:
                        # For CSV, include as string
                        csv_data = await self.export_to_csv(database, table_name)
                        table_backup["data"] = csv_data
                
                backup_data["tables"][table_name] = table_backup
            
            return json.dumps(backup_data, indent=2)
            
        except ZeroTrustError:
            raise
        except Exception as e:
            raise ZeroTrustError(f"Database backup failed: {e}", "BACKUP_ERROR")

    async def restore_database(
        self,
        backup_content: str,
        target_database: str,
        overwrite: bool = False,
    ) -> MigrationStatus:
        """Restore database from backup.
        
        Args:
            backup_content: Backup content as JSON string
            target_database: Target database name
            overwrite: Whether to overwrite existing database
            
        Returns:
            Migration status
            
        Raises:
            ZeroTrustError: If restore fails
        """
        if not backup_content or not target_database:
            raise ZeroTrustError.validation("Backup content and target database are required")

        try:
            # Parse backup content
            backup_data = json.loads(backup_content)
            
            from .database import DatabaseManager
            from .types import Column
            db_manager = DatabaseManager(self.http_client)
            
            # Create target database
            try:
                await db_manager.create_database(target_database)
            except ZeroTrustError as e:
                if not overwrite and "already exists" in str(e):
                    raise ZeroTrustError.validation(
                        f"Database {target_database} already exists. Use overwrite=True to replace it."
                    )
            
            total_restored = 0
            
            # Restore each table
            for table_name, table_data in backup_data.get("tables", {}).items():
                # Create table with schema
                columns = []
                for col_data in table_data.get("columns", []):
                    column = Column(
                        name=col_data["name"],
                        data_type=col_data["data_type"],
                        nullable=col_data.get("nullable", True),
                        default_value=col_data.get("default_value"),
                        is_primary_key=col_data.get("is_primary_key", False),
                    )
                    columns.append(column)
                
                await db_manager.create_table(target_database, table_name, columns)
                
                # Import data if present
                if "data" in table_data:
                    data = table_data["data"]
                    if isinstance(data, str):
                        # CSV format
                        await self.import_csv(target_database, table_name, data)
                    elif isinstance(data, list):
                        # JSON format
                        if data:  # Only import if there's data
                            await db_manager.insert_data(target_database, table_name, data)
                            total_restored += len(data)
            
            return MigrationStatus(
                id=f"restore_{target_database}",
                status="Completed",
                records_processed=total_restored,
                total_records=total_restored,
                started_at="",  # Would be populated by server
                completed_at="",  # Would be populated by server
            )
            
        except ZeroTrustError:
            raise
        except json.JSONDecodeError as e:
            raise ZeroTrustError.validation(f"Invalid backup format: {e}")
        except Exception as e:
            raise ZeroTrustError(f"Database restore failed: {e}", "RESTORE_ERROR")