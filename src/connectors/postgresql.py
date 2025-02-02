import os
from sqlalchemy import create_engine, exc
from dotenv import load_dotenv

load_dotenv() #load environment variables from .env

class PostgreSQLConnector:
    def __init__(self):
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.host = os.getenv("POSTGRES_HOST")
        self.db = os.getenv("POSTGRES_DB")
        self.engine = create_engine(
            f"postgresql://{self.user}:{self.password}@{self.host}/{self.db}"
        )
    def get_engine(self):
        return self.engine
    
    def test_connection(self):
        try:
            with self.engine.connect():
                print("PostgreSQl connection successful")
                return True

        except exc.SQLAlchemyError as e:
            print(f"Connection failed: {str(e)}")
            return False