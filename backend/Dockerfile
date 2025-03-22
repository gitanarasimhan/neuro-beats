# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production \
    SSL_CERT=/app/certs/localhost+2.pem \
    SSL_KEY=/app/certs/localhost+2-key.pem

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        openssl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create directory for certificates
RUN mkdir -p /app/certs

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--certfile", "/app/certs/localhost+2.pem", "--keyfile", "/app/certs/localhost+2-key.pem", "app:create_app()"] 