# tests/test_csv_ingestor.py
import pytest
from src.ingestion.csv_ingestor import CSVIngestor

def test_csv_ingestion_success():
    ingestor = CSVIngestor()
    assert ingestor.ingest("data/raw/test.csv", "sales") is True