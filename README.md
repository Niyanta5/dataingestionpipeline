# Data Ingestion Pipeline (CSV → PostgreSQL)

A Python-based pipeline to ingest CSV data into PostgreSQL, designed for scalability and error handling. Containerized with Docker for easy deployment.

---

## Features
- **Batch Ingestion**: Load CSV files into PostgreSQL.
- **Error Handling**: Logs failures and missing files.
- **PostgreSQL Integration**: Uses SQLAlchemy for robust database operations.
- **Docker Support**: Run PostgreSQL and the pipeline in containers.
- **Logging**: Detailed logs for debugging.

---

## Prerequisites
- Docker and Docker Compose
- Python 3.9+
- Git
- PostgreSQL client (e.g., pgAdmin)

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Niyanta5/data-ingestion-pipeline.git
   cd data-ingestion-pipeline
   ```
2. Create a .env file

## Try it yourself

1. Build and start the containers
   ```bash
   docker-compose up --build -d
   ```
2. Run the pipeline:
   ```bash
   docker-compose up ingestion
   ```
3. Verify the data in postgreSQL:
   ```bash
   docker exec -it data-ingestion-pipeline-postgres-1 psql -U postgres -d sales_db -c "SELECT * FROM sales;"
   ```
4. Run the tests
   ```bash
   docker exec -it data-ingestion-pipeline-ingestion-1 python -m pytest tests/
   ```
### Expected Output
🟢 Starting ingestion for file: /app/data/raw/sales_data.csv
✅ File exists: /app/data/raw/sales_data.csv
📊 DataFrame loaded. Rows: 2
💾 Data written to table: sales
INFO: Ingestion successful. 2 rows ingested from /app/data/raw/sales_data.csv


