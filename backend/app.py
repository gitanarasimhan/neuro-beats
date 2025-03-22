"""
Main application entry point.
"""
from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

from src.routes.recommendation import bp as recommendation_bp
from src.routes.health import bp as health_bp
from src.config import (
    DEBUG, HOST, PORT, CORS_ORIGINS,
    SSL_CERT, SSL_KEY
)

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app, origins=CORS_ORIGINS)
    
    # Register blueprints
    app.register_blueprint(recommendation_bp)
    app.register_blueprint(health_bp)
    
    # Configure proxy settings
    app.wsgi_app = ProxyFix(app.wsgi_app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    # For local development with self-signed SSL certs
    app.run(
        host=HOST,
        port=PORT,
        ssl_context=(SSL_CERT, SSL_KEY),
        debug=DEBUG
    )