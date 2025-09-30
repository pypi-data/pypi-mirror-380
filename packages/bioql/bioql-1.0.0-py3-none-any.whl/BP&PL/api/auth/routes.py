"""
Authentication API routes for user management and API keys.
"""

from flask import Blueprint, request, jsonify, current_app
from functools import wraps
import jwt
from datetime import datetime, timedelta

from ...services.auth_service import AuthService
from ..main import get_db_session
from ..utils import validate_json, rate_limit, api_response


auth_bp = Blueprint('auth', __name__)


def token_required(f):
    """Decorator to require JWT token authentication."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')

        if auth_header:
            try:
                token = auth_header.split(" ")[1]  # Bearer <token>
            except IndexError:
                return api_response(None, "Invalid token format", 401)

        if not token:
            return api_response(None, "Token is missing", 401)

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user_id = data['user_id']
        except jwt.ExpiredSignatureError:
            return api_response(None, "Token has expired", 401)
        except jwt.InvalidTokenError:
            return api_response(None, "Token is invalid", 401)

        return f(current_user_id, *args, **kwargs)

    return decorated


def api_key_required(f):
    """Decorator to require API key authentication."""
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')

        if not api_key:
            return api_response(None, "API key is missing", 401)

        db_session = get_db_session()
        auth_service = AuthService(db_session)

        result = auth_service.authenticate_api_key(api_key)
        if not result:
            return api_response(None, "Invalid API key", 401)

        user, api_key_obj = result
        return f(user.id, api_key_obj.id, *args, **kwargs)

    return decorated


@auth_bp.route('/register', methods=['POST'])
@rate_limit('auth_register', 5, 300)  # 5 registrations per 5 minutes
@validate_json(['email', 'username', 'password'])
def register():
    """Register a new user."""
    data = request.get_json()

    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        user, verification_token = auth_service.register_user(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            organization=data.get('organization')
        )

        # In production, send verification email here
        current_app.logger.info(f"User registered: {user.email} (verification token: {verification_token})")

        return api_response({
            'user_id': user.id,
            'email': user.email,
            'username': user.username,
            'verification_required': True
        }, "User registered successfully")

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Registration error: {str(e)}")
        return api_response(None, "Registration failed", 500)


@auth_bp.route('/login', methods=['POST'])
@rate_limit('auth_login', 10, 300)  # 10 login attempts per 5 minutes
@validate_json(['login', 'password'])
def login():
    """Authenticate user and return JWT token."""
    data = request.get_json()

    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        user = auth_service.authenticate_user(data['login'], data['password'])
        if not user:
            return api_response(None, "Invalid credentials", 401)

        if not user.is_verified:
            return api_response(None, "Email verification required", 403)

        # Generate JWT token
        token_payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=30),
            'iat': datetime.utcnow()
        }

        token = jwt.encode(token_payload, current_app.config['SECRET_KEY'], algorithm='HS256')

        return api_response({
            'access_token': token,
            'token_type': 'Bearer',
            'expires_in': 1800,  # 30 minutes
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'full_name': user.full_name,
                'current_plan': user.current_plan.value
            }
        }, "Login successful")

    except Exception as e:
        current_app.logger.error(f"Login error: {str(e)}")
        return api_response(None, "Login failed", 500)


@auth_bp.route('/verify-email', methods=['POST'])
@validate_json(['verification_token'])
def verify_email():
    """Verify user's email address."""
    data = request.get_json()

    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        success = auth_service.verify_email(data['verification_token'])
        if success:
            return api_response(None, "Email verified successfully")
        else:
            return api_response(None, "Invalid verification token", 400)

    except Exception as e:
        current_app.logger.error(f"Email verification error: {str(e)}")
        return api_response(None, "Verification failed", 500)


@auth_bp.route('/forgot-password', methods=['POST'])
@rate_limit('forgot_password', 3, 3600)  # 3 attempts per hour
@validate_json(['email'])
def forgot_password():
    """Initiate password reset process."""
    data = request.get_json()

    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        reset_token = auth_service.initiate_password_reset(data['email'])

        # Always return success to prevent email enumeration
        return api_response(None, "Password reset email sent (if email exists)")

    except Exception as e:
        current_app.logger.error(f"Password reset error: {str(e)}")
        return api_response(None, "Password reset failed", 500)


@auth_bp.route('/reset-password', methods=['POST'])
@validate_json(['reset_token', 'new_password'])
def reset_password():
    """Reset user password."""
    data = request.get_json()

    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        success = auth_service.reset_password(data['reset_token'], data['new_password'])
        if success:
            return api_response(None, "Password reset successfully")
        else:
            return api_response(None, "Invalid or expired reset token", 400)

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Password reset error: {str(e)}")
        return api_response(None, "Password reset failed", 500)


@auth_bp.route('/change-password', methods=['POST'])
@token_required
@validate_json(['current_password', 'new_password'])
def change_password(current_user_id):
    """Change user password."""
    data = request.get_json()

    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        success = auth_service.change_password(
            current_user_id,
            data['current_password'],
            data['new_password']
        )

        if success:
            return api_response(None, "Password changed successfully")
        else:
            return api_response(None, "Invalid current password", 400)

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Password change error: {str(e)}")
        return api_response(None, "Password change failed", 500)


@auth_bp.route('/profile', methods=['GET'])
@token_required
def get_profile(current_user_id):
    """Get user profile information."""
    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        user_stats = auth_service.get_user_stats(current_user_id)
        permissions = auth_service.get_user_permissions(current_user_id)

        return api_response({
            'user': user_stats['user_info'],
            'permissions': permissions,
            'api_access': user_stats['api_access'],
            'account_status': user_stats['account_status']
        })

    except Exception as e:
        current_app.logger.error(f"Profile retrieval error: {str(e)}")
        return api_response(None, "Failed to retrieve profile", 500)


@auth_bp.route('/profile', methods=['PUT'])
@token_required
@validate_json([])
def update_profile(current_user_id):
    """Update user profile information."""
    data = request.get_json()

    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        success = auth_service.update_user_profile(current_user_id, **data)

        if success:
            return api_response(None, "Profile updated successfully")
        else:
            return api_response(None, "Profile update failed", 400)

    except Exception as e:
        current_app.logger.error(f"Profile update error: {str(e)}")
        return api_response(None, "Profile update failed", 500)


@auth_bp.route('/api-keys', methods=['GET'])
@token_required
def list_api_keys(current_user_id):
    """List user's API keys."""
    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        api_keys = auth_service.list_user_api_keys(current_user_id)

        return api_response({
            'api_keys': api_keys,
            'total': len(api_keys)
        })

    except Exception as e:
        current_app.logger.error(f"API keys retrieval error: {str(e)}")
        return api_response(None, "Failed to retrieve API keys", 500)


@auth_bp.route('/api-keys', methods=['POST'])
@token_required
@validate_json(['key_name'])
def create_api_key(current_user_id):
    """Create a new API key."""
    data = request.get_json()

    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        api_key, key_string = auth_service.create_api_key(
            user_id=current_user_id,
            key_name=data['key_name'],
            rate_limit_per_minute=data.get('rate_limit_per_minute', 60),
            rate_limit_per_hour=data.get('rate_limit_per_hour', 1000),
            rate_limit_per_day=data.get('rate_limit_per_day', 10000),
            expires_days=data.get('expires_days')
        )

        return api_response({
            'api_key_id': api_key.id,
            'key_name': api_key.key_name,
            'api_key': key_string,  # Only shown once
            'expires_at': api_key.expires_at.isoformat() if api_key.expires_at else None,
            'rate_limits': {
                'per_minute': api_key.rate_limit_per_minute,
                'per_hour': api_key.rate_limit_per_hour,
                'per_day': api_key.rate_limit_per_day
            }
        }, "API key created successfully")

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"API key creation error: {str(e)}")
        return api_response(None, "API key creation failed", 500)


@auth_bp.route('/api-keys/<api_key_id>', methods=['DELETE'])
@token_required
def revoke_api_key(current_user_id, api_key_id):
    """Revoke an API key."""
    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        success = auth_service.revoke_api_key(api_key_id, current_user_id)

        if success:
            return api_response(None, "API key revoked successfully")
        else:
            return api_response(None, "API key not found", 404)

    except Exception as e:
        current_app.logger.error(f"API key revocation error: {str(e)}")
        return api_response(None, "API key revocation failed", 500)


@auth_bp.route('/permissions', methods=['GET'])
@token_required
def get_permissions(current_user_id):
    """Get user permissions and access levels."""
    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        permissions = auth_service.get_user_permissions(current_user_id)

        return api_response(permissions)

    except Exception as e:
        current_app.logger.error(f"Permissions retrieval error: {str(e)}")
        return api_response(None, "Failed to retrieve permissions", 500)