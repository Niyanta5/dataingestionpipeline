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

    def ingest(self, file_path: str, table_name: str, dtype: Optional[dict]= None):
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"{file_path}" does not exist)

            df = pd.read_csv(file_path, dtype=dtype, parse_dates=True)
            df.to_sql(
                table_name, 
                self.engine,
                if_exists="append",
                index=False
            )
            logger.info(f"Ingested {len(df)} rows from file_path")
            return True
        except (FileNotFoundError, pd.errors.ParserError, SQlAlchemyError) as e:
            logger.error(f"CSV ingestion failed: {str(e)}")
            return False