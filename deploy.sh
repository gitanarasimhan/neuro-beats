#!/bin/bash

# Exit on error
set -e

echo "🚀 Deploying Neuro-Beats application..."

# Check if .env files exist
if [ ! -f "./backend/.env" ]; then
    echo "❌ Error: backend/.env file not found!"
    echo "Please create the .env file from .env.template"
    exit 1
fi

# Check for SSL certificates
if [ ! -f "./backend/certs/localhost+2.pem" ] || [ ! -f "./backend/certs/localhost+2-key.pem" ]; then
    echo "⚠️  SSL certificates not found in ./backend/certs/"
    echo "🔒 Generating self-signed certificates..."
    
    # Create certs directory if it doesn't exist
    mkdir -p ./backend/certs
    
    # Generate self-signed certificates using mkcert if available
    if command -v mkcert &> /dev/null; then
        mkcert -install
        mkcert -key-file ./backend/certs/localhost+2-key.pem -cert-file ./backend/certs/localhost+2.pem localhost 127.0.0.1
    else
        echo "❌ Error: mkcert not found! Please install mkcert or provide SSL certificates manually."
        echo "Visit https://github.com/FiloSottile/mkcert for installation instructions."
        exit 1
    fi
fi

# Build and start containers
echo "🏗️  Building containers..."
docker-compose build

echo "🚀 Starting services..."
docker-compose up -d

echo "🔍 Checking service health..."
sleep 10

# Check if services are running
if docker-compose ps | grep -q "neuro-beats-backend.*running"; then
    echo "✅ Backend is running"
else
    echo "❌ Backend failed to start"
    docker-compose logs backend
    exit 1
fi

if docker-compose ps | grep -q "neuro-beats-frontend.*running"; then
    echo "✅ Frontend is running"
else
    echo "❌ Frontend failed to start"
    docker-compose logs frontend
    exit 1
fi

echo "✨ Deployment completed successfully!"
echo "📝 Application logs can be viewed with: docker-compose logs -f"
echo "🌍 Frontend is available at: https://localhost"
echo "🔌 Backend API is available at: https://localhost/api"
echo "🔒 Using SSL certificates from: ./backend/certs/" 