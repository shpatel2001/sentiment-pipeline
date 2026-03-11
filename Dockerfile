# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code and create the data directory
COPY . .

# Run both scripts in sequence when the container starts
CMD ["sh", "-c", "python ingest.py && python transform.py && python gold_summary.py"]