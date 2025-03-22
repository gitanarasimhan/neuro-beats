"""
Health check endpoint for monitoring service status.
"""
from flask import Blueprint, jsonify

bp = Blueprint('health', __name__)

@bp.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint.
    """
    return jsonify({
        'status': 'healthy',
        'service': 'neuro-beats-backend'
    }) 