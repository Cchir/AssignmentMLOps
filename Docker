# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run when container starts
CMD ["python", "scripts/schedular.py"]
