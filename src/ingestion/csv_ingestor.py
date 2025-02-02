import pandas as pd
import os
from typing import Optional
from sqlalchemy.exc import SQLAlchemyError
from ..connectors.postgresql import PostgreSQLConnector
from ..utils.logger import logger

class CSVIngestor:
    def __init__(self):
        self.connector = PostgreSQLConnector()
        self.engine = self.connector.get_engine()

    def ingest(self, file_path: str, table_name: str, dtype: Optional[dict] = None, parse_dates: Optional[list] = None):
        try:  # FIXED: Indent this block under the method
            print(f"🟢 Starting ingestion for file: {file_path}")

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"{file_path} does not exist")
            print(f"✅ File exists: {file_path}")

            df = pd.read_csv(file_path, dtype=dtype, parse_dates=parse_dates)
            print(f"📊 DataFrame loaded. Rows: {len(df)}")

            df.to_sql(
                table_name,
                self.engine,
                if_exists="append",
                index=False
            )
            print(f"💾 Data written to table: {table_name}")
            logger.info(f"Ingested {len(df)} rows from {file_path}")

            return True
        except (FileNotFoundError, pd.errors.ParserError, SQLAlchemyError) as e:
            logger.error(f"CSV ingestion failed: {str(e)}")
            return False

# Add this to test the script directly
if __name__ == "__main__":
    ingestor = CSVIngestor()
    ingestor.ingest(
        file_path="/app/data/raw/sales_data.csv",  # Use absolute Docker path
        table_name="sales",
        parse_dates=["sale_date"]  # Explicitly pass date columns
    )