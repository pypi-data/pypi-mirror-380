"""InterceptedDataFrame entity for wrapped DataFrames."""

from dataclasses import dataclass
from datetime import datetime
from typing import Any
import pandas as pd
from ..models.catalog_reference import CatalogReference


@dataclass
class InterceptedDataFrame:
    """Wrapper that maintains DataFrame API compatibility."""

    data: pd.DataFrame
    source_table: CatalogReference
    fetch_time: datetime = None
    from_cache: bool = False
    _spark_df: Any = None

    def __post_init__(self):
        """Initialize fetch time if not provided."""
        if self.fetch_time is None:
            self.fetch_time = datetime.now()

        # Try to create Spark DataFrame
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
            self._spark_df = spark.createDataFrame(self.data)
        except:
            self._spark_df = None

    @property
    def spark_df(self):
        """Get the Spark DataFrame if available."""
        return self._spark_df if self._spark_df else self

    # Implement common DataFrame methods
    def select(self, *cols):
        """Select columns."""
        if self._spark_df:
            return self._spark_df.select(*cols)
        selected_data = self.data[list(cols)]
        return InterceptedDataFrame(selected_data, self.source_table, from_cache=self.from_cache)

    def filter(self, condition):
        """Filter rows."""
        if self._spark_df:
            return self._spark_df.filter(condition)
        # Simple filtering for pandas
        return self

    def where(self, condition):
        """Alias for filter."""
        return self.filter(condition)

    def groupBy(self, *cols):
        """Group by columns."""
        if self._spark_df:
            return self._spark_df.groupBy(*cols)
        return self.data.groupby(list(cols))

    def agg(self, *exprs):
        """Aggregate functions."""
        if self._spark_df:
            return self._spark_df.agg(*exprs)
        return self

    def join(self, other, on, how='inner'):
        """Join with another DataFrame."""
        if self._spark_df and hasattr(other, '_spark_df'):
            return self._spark_df.join(other._spark_df, on, how)
        # Pandas join
        if isinstance(other, InterceptedDataFrame):
            joined_data = pd.merge(self.data, other.data, on=on, how=how)
            return InterceptedDataFrame(joined_data, self.source_table, from_cache=False)
        return self

    def show(self, n=20, truncate=True):
        """Display rows."""
        if self._spark_df:
            return self._spark_df.show(n, truncate)
        print(self.data.head(n))

    def collect(self):
        """Collect all rows."""
        if self._spark_df:
            return self._spark_df.collect()
        return self.data.to_dict('records')

    def count(self):
        """Count rows."""
        if self._spark_df:
            return self._spark_df.count()
        return len(self.data)

    @property
    def schema(self):
        """Get schema."""
        if self._spark_df:
            return self._spark_df.schema
        return str(self.data.dtypes)

    @property
    def columns(self):
        """Get column names."""
        if self._spark_df:
            return self._spark_df.columns
        return list(self.data.columns)

    @property
    def dtypes(self):
        """Get column data types."""
        if self._spark_df:
            return self._spark_df.dtypes
        return list(zip(self.data.columns, self.data.dtypes.astype(str)))