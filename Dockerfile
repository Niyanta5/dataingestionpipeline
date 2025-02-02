# Python base image
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

CMD ["python", "-m", "src.ingestion.csv_ingestor"]