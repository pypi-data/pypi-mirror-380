"""Unity Catalog connector for data access."""

from typing import Any, Optional
import pandas as pd
from ..models.unity_catalog_connection import UnityCatalogConnection
from ..models.catalog_reference import CatalogReference


class UnityCatalogConnector:
    """Handles Unity Catalog connections and data fetching."""

    def __init__(self, connection: UnityCatalogConnection):
        """Initialize with a Unity Catalog connection."""
        self.connection = connection

    def fetch_table(self, table_ref: CatalogReference) -> pd.DataFrame:
        """Fetch entire table from Unity Catalog."""
        query = f"SELECT * FROM {table_ref.full_name}"
        return self.execute_query(query)

    def fetch_table_with_limit(self, table_ref: CatalogReference, limit: int) -> pd.DataFrame:
        """Fetch table with row limit."""
        query = f"SELECT * FROM {table_ref.full_name} LIMIT {limit}"
        return self.execute_query(query)

    def fetch_table_schema(self, table_ref: CatalogReference) -> Any:
        """Fetch table schema information."""
        query = f"DESCRIBE TABLE {table_ref.full_name}"
        return self.execute_query(query)

    def table_exists(self, table_ref: CatalogReference) -> bool:
        """Check if table exists in Unity Catalog."""
        try:
            query = f"SHOW TABLES IN {table_ref.catalog}.{table_ref.schema} LIKE '{table_ref.table}'"
            result = self.execute_query(query)
            return len(result) > 0 if result is not None else False
        except:
            return False

    def execute_query(self, query: str) -> pd.DataFrame:
        """Execute a SQL query and return results as DataFrame."""
        if not self.connection.is_connected:
            self.connection.connect()

        try:
            result = self.connection.execute_query(query)

            # Convert to pandas DataFrame
            if result:
                # Get column names from cursor description if available
                if hasattr(self.connection.connection, 'cursor'):
                    cursor = self.connection.connection.cursor()
                    cursor.execute(query)
                    columns = [desc[0] for desc in cursor.description] if cursor.description else None
                    data = cursor.fetchall()
                    cursor.close()
                    return pd.DataFrame(data, columns=columns)
                else:
                    return pd.DataFrame(result)

            return pd.DataFrame()
        except Exception as e:
            from ..exceptions import TableNotFoundError
            if "table" in str(e).lower() and "not found" in str(e).lower():
                raise TableNotFoundError(f"Table not found: {query}")
            raise

    def test_connection(self) -> bool:
        """Test the Unity Catalog connection."""
        try:
            query = "SELECT 1"
            result = self.execute_query(query)
            return result is not None
        except:
            return False