"""
Configuration settings for the application.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask settings
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 5000))

# Spotify API credentials
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# CORS settings
CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'https://localhost:3000').split(',')

# SSL settings for development
SSL_CERT = os.getenv('SSL_CERT', 'localhost+2.pem')
SSL_KEY = os.getenv('SSL_KEY', 'localhost+2-key.pem')

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    API_PREFIX = '/api/v1'
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')
    CACHE_DEFAULT_TIMEOUT = int(os.getenv('CACHE_DEFAULT_TIMEOUT', 300))
    RATELIMIT_DEFAULT = os.getenv('RATELIMIT_DEFAULT', '100 per day')
    
class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    
class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    
class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    
# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
} 