"""
Main Flask application factory for BioQL billing API.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import redis
import logging
from datetime import datetime

from ..config import get_api_config, get_database_config, get_redis_config
from ..models.base import Base


# Global database session
db_session = None
redis_client = None


def create_app(config_name='production'):
    """
    Create and configure Flask application.

    Args:
        config_name: Configuration environment name

    Returns:
        Configured Flask application
    """
    app = Flask(__name__)

    # Load configuration
    api_config = get_api_config()
    db_config = get_database_config()
    redis_config = get_redis_config()

    # Configure Flask app
    app.config['SECRET_KEY'] = api_config['authentication']['jwt']['secret_key']
    app.config['SQLALCHEMY_DATABASE_URI'] = db_config['database']['primary']['url']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    init_database(app, db_config)

    # Initialize Redis
    init_redis(redis_config)

    # Configure CORS
    if api_config['cors']['enabled']:
        CORS(app,
             origins=api_config['cors']['origins'],
             methods=api_config['cors']['methods'],
             allow_headers=api_config['cors']['headers'])

    # Configure logging
    configure_logging(api_config)

    # Register blueprints
    register_blueprints(app, api_config)

    # Register error handlers
    register_error_handlers(app)

    # Register middleware
    register_middleware(app, api_config)

    return app


def init_database(app, db_config):
    """Initialize database connection."""
    global db_session

    try:
        engine = create_engine(
            db_config['database']['primary']['url'],
            pool_size=db_config.get('pooling', {}).get('pool_size', 20),
            max_overflow=db_config.get('pooling', {}).get('max_overflow', 30),
            pool_timeout=db_config.get('pooling', {}).get('pool_timeout', 30),
            pool_recycle=db_config.get('pooling', {}).get('pool_recycle', 3600),
            pool_pre_ping=db_config.get('pooling', {}).get('pool_pre_ping', True),
            echo=db_config['database']['primary'].get('echo', False)
        )

        # Create all tables
        Base.metadata.create_all(engine)

        # Create session factory
        Session = sessionmaker(bind=engine)
        db_session = Session()

        app.logger.info("Database initialized successfully")

    except Exception as e:
        app.logger.error(f"Failed to initialize database: {str(e)}")
        raise


def init_redis(redis_config):
    """Initialize Redis connection."""
    global redis_client

    if redis_config['enabled']:
        try:
            redis_client = redis.from_url(redis_config['url'])
            redis_client.ping()  # Test connection
            logging.info("Redis initialized successfully")
        except Exception as e:
            logging.warning(f"Failed to initialize Redis: {str(e)}")
            redis_client = None


def configure_logging(api_config):
    """Configure application logging."""
    log_config = api_config.get('logging', {})

    # Set log level
    log_level = getattr(logging, log_config.get('level', 'INFO'))
    logging.basicConfig(level=log_level, format=log_config.get('format'))

    # File logging
    if log_config.get('file_logging', {}).get('enabled', False):
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler(
            log_config['file_logging']['filename'],
            maxBytes=log_config['file_logging'].get('max_bytes', 10485760),
            backupCount=log_config['file_logging'].get('backup_count', 5)
        )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter(log_config.get('format')))
        logging.getLogger().addHandler(file_handler)


def register_blueprints(app, api_config):
    """Register API blueprints."""
    base_path = api_config['endpoints']['base_path']

    # Import blueprints
    from .auth.routes import auth_bp
    from .billing.routes import billing_bp
    from .usage.routes import usage_bp
    from .admin.routes import admin_bp
    from .webhooks import webhooks_bp

    # Register blueprints
    if api_config['endpoints']['auth']['enabled']:
        app.register_blueprint(auth_bp, url_prefix=f"{base_path}{api_config['endpoints']['auth']['path']}")

    if api_config['endpoints']['billing']['enabled']:
        app.register_blueprint(billing_bp, url_prefix=f"{base_path}{api_config['endpoints']['billing']['path']}")

    if api_config['endpoints']['usage']['enabled']:
        app.register_blueprint(usage_bp, url_prefix=f"{base_path}{api_config['endpoints']['usage']['path']}")

    if api_config['endpoints']['admin']['enabled']:
        app.register_blueprint(admin_bp, url_prefix=f"{base_path}{api_config['endpoints']['admin']['path']}")

    if api_config['endpoints']['webhooks']['enabled']:
        app.register_blueprint(webhooks_bp, url_prefix=f"{base_path}{api_config['endpoints']['webhooks']['path']}")

    # Health check endpoint
    @app.route('/health')
    def health_check():
        """Health check endpoint."""
        status = {'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()}

        # Check database
        try:
            db_session.execute('SELECT 1')
            status['database'] = 'connected'
        except Exception:
            status['database'] = 'disconnected'
            status['status'] = 'unhealthy'

        # Check Redis
        if redis_client:
            try:
                redis_client.ping()
                status['redis'] = 'connected'
            except Exception:
                status['redis'] = 'disconnected'
        else:
            status['redis'] = 'not_configured'

        return jsonify(status), 200 if status['status'] == 'healthy' else 503


def register_error_handlers(app):
    """Register global error handlers."""

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 'Not Found',
            'message': 'The requested resource was not found',
            'status_code': 404
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'error': 'Bad Request',
            'message': 'Invalid request data',
            'status_code': 400
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'error': 'Unauthorized',
            'message': 'Authentication required',
            'status_code': 401
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'error': 'Forbidden',
            'message': 'Insufficient permissions',
            'status_code': 403
        }), 403

    @app.errorhandler(429)
    def rate_limit_exceeded(error):
        return jsonify({
            'error': 'Rate Limit Exceeded',
            'message': 'Too many requests. Please try again later.',
            'status_code': 429
        }), 429

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f"Internal server error: {str(error)}")
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred',
            'status_code': 500
        }), 500


def register_middleware(app, api_config):
    """Register application middleware."""

    @app.before_request
    def before_request():
        """Middleware executed before each request."""
        # Log requests if enabled
        if api_config.get('logging', {}).get('log_requests', False):
            app.logger.info(f"{request.method} {request.path} - {request.remote_addr}")

        # Force HTTPS in production
        if api_config.get('security', {}).get('force_https', False):
            if not request.is_secure and request.headers.get('X-Forwarded-Proto', 'http') != 'https':
                return jsonify({
                    'error': 'HTTPS Required',
                    'message': 'All requests must use HTTPS'
                }), 400

    @app.after_request
    def after_request(response):
        """Middleware executed after each request."""
        # Add security headers
        security_config = api_config.get('security', {}).get('security_headers', {})
        if security_config.get('enabled', False):
            for header, value in security_config.get('headers', {}).items():
                response.headers[header] = value

        return response


def get_db_session():
    """Get the global database session."""
    return db_session


def get_redis_client():
    """Get the global Redis client."""
    return redis_client


if __name__ == '__main__':
    # Development server
    app = create_app('development')
    api_config = get_api_config()

    app.run(
        host=api_config['server']['host'],
        port=api_config['server']['port'],
        debug=api_config['server']['debug']
    )