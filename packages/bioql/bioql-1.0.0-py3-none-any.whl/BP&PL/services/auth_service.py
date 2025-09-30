"""
Authentication service for user management and API key authentication.
"""

import secrets
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from ..models.user import User, APIKey, UserPlanEnum
from ..models.subscription import Subscription, SubscriptionStatusEnum


class AuthService:
    """
    Service for user authentication, registration, and API key management.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def register_user(self, email: str, username: str, password: str,
                     first_name: str = None, last_name: str = None,
                     organization: str = None) -> Tuple[User, str]:
        """
        Register a new user.

        Args:
            email: User's email address
            username: Unique username
            password: User's password
            first_name: User's first name
            last_name: User's last name
            organization: User's organization

        Returns:
            Tuple of (User instance, verification_token)

        Raises:
            ValueError: If user already exists or validation fails
        """
        # Validate input
        if not email or not username or not password:
            raise ValueError("Email, username, and password are required")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        # Check if user already exists
        existing_user = self.db_session.query(User).filter(
            or_(User.email == email, User.username == username)
        ).first()

        if existing_user:
            if existing_user.email == email:
                raise ValueError("Email address already registered")
            else:
                raise ValueError("Username already taken")

        # Create new user
        user = User(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            organization=organization,
            current_plan=UserPlanEnum.FREE,
            is_active=True,
            is_verified=False
        )

        user.set_password(password)
        verification_token = user.generate_verification_token()

        self.db_session.add(user)
        self.db_session.commit()

        return user, verification_token

    def authenticate_user(self, login: str, password: str) -> Optional[User]:
        """
        Authenticate user with email/username and password.

        Args:
            login: Email or username
            password: User's password

        Returns:
            User instance if authentication successful, None otherwise
        """
        user = self.db_session.query(User).filter(
            and_(
                or_(User.email == login, User.username == login),
                User.is_active == True
            )
        ).first()

        if user and user.check_password(password):
            user.last_login = datetime.utcnow()
            self.db_session.commit()
            return user

        return None

    def authenticate_api_key(self, api_key: str) -> Optional[Tuple[User, APIKey]]:
        """
        Authenticate using API key.

        Args:
            api_key: API key string

        Returns:
            Tuple of (User, APIKey) if valid, None otherwise
        """
        # Find API key by prefix (first 8 characters)
        if len(api_key) < 8:
            return None

        key_prefix = api_key[:8]

        api_key_obj = self.db_session.query(APIKey).filter(
            and_(
                APIKey.key_prefix == key_prefix,
                APIKey.is_active == True
            )
        ).first()

        if not api_key_obj:
            return None

        # Verify full key
        if not api_key_obj.check_key(api_key):
            return None

        # Check if key is expired
        if api_key_obj.is_expired():
            return None

        # Get user
        user = self.db_session.query(User).filter(
            and_(
                User.id == api_key_obj.user_id,
                User.is_active == True
            )
        ).first()

        if not user:
            return None

        # Record usage
        api_key_obj.record_usage()
        self.db_session.commit()

        return user, api_key_obj

    def verify_email(self, verification_token: str) -> bool:
        """
        Verify user's email address using verification token.

        Args:
            verification_token: Email verification token

        Returns:
            True if verification successful, False otherwise
        """
        user = self.db_session.query(User).filter_by(
            verification_token=verification_token
        ).first()

        if user:
            user.is_verified = True
            user.verification_token = None
            self.db_session.commit()
            return True

        return False

    def create_api_key(self, user_id: str, key_name: str,
                      rate_limit_per_minute: int = 60,
                      rate_limit_per_hour: int = 1000,
                      rate_limit_per_day: int = 10000,
                      expires_days: int = None) -> Tuple[APIKey, str]:
        """
        Create a new API key for a user.

        Args:
            user_id: User ID
            key_name: Name for the API key
            rate_limit_per_minute: Rate limit per minute
            rate_limit_per_hour: Rate limit per hour
            rate_limit_per_day: Rate limit per day
            expires_days: Days until expiration (None for no expiration)

        Returns:
            Tuple of (APIKey instance, actual_key_string)

        Raises:
            ValueError: If user not found or validation fails
        """
        user = self.db_session.query(User).filter_by(id=user_id).first()
        if not user:
            raise ValueError("User not found")

        # Generate API key
        api_key_string = APIKey.generate_key()

        # Set expiration if specified
        expires_at = None
        if expires_days:
            expires_at = datetime.utcnow() + timedelta(days=expires_days)

        # Create API key record
        api_key = APIKey(
            user_id=user_id,
            key_name=key_name,
            rate_limit_per_minute=rate_limit_per_minute,
            rate_limit_per_hour=rate_limit_per_hour,
            rate_limit_per_day=rate_limit_per_day,
            expires_at=expires_at
        )

        api_key.set_key(api_key_string)

        self.db_session.add(api_key)
        self.db_session.commit()

        return api_key, api_key_string

    def revoke_api_key(self, api_key_id: str, user_id: str = None) -> bool:
        """
        Revoke an API key.

        Args:
            api_key_id: API key ID to revoke
            user_id: Optional user ID for additional security

        Returns:
            True if revocation successful, False otherwise
        """
        query = self.db_session.query(APIKey).filter_by(id=api_key_id)

        if user_id:
            query = query.filter_by(user_id=user_id)

        api_key = query.first()

        if api_key:
            api_key.is_active = False
            self.db_session.commit()
            return True

        return False

    def list_user_api_keys(self, user_id: str) -> List[Dict[str, Any]]:
        """
        List all API keys for a user.

        Args:
            user_id: User ID

        Returns:
            List of API key information dictionaries
        """
        api_keys = self.db_session.query(APIKey).filter_by(user_id=user_id).all()

        return [
            {
                'id': key.id,
                'key_name': key.key_name,
                'key_display': f"{key.key_prefix}...",
                'is_active': key.is_active,
                'created_at': key.created_at.isoformat(),
                'last_used': key.last_used.isoformat() if key.last_used else None,
                'expires_at': key.expires_at.isoformat() if key.expires_at else None,
                'is_expired': key.is_expired(),
                'total_requests': key.total_requests,
                'rate_limits': {
                    'per_minute': key.rate_limit_per_minute,
                    'per_hour': key.rate_limit_per_hour,
                    'per_day': key.rate_limit_per_day
                }
            }
            for key in api_keys
        ]

    def initiate_password_reset(self, email: str) -> Optional[str]:
        """
        Initiate password reset process.

        Args:
            email: User's email address

        Returns:
            Reset token if user found, None otherwise
        """
        user = self.db_session.query(User).filter_by(email=email).first()

        if user:
            reset_token = user.generate_reset_token()
            self.db_session.commit()
            return reset_token

        return None

    def reset_password(self, reset_token: str, new_password: str) -> bool:
        """
        Reset user password using reset token.

        Args:
            reset_token: Password reset token
            new_password: New password

        Returns:
            True if reset successful, False otherwise
        """
        if len(new_password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        user = self.db_session.query(User).filter_by(reset_token=reset_token).first()

        if user and user.is_reset_token_valid():
            user.set_password(new_password)
            user.reset_token = None
            user.reset_token_expires = None
            self.db_session.commit()
            return True

        return False

    def change_password(self, user_id: str, current_password: str, new_password: str) -> bool:
        """
        Change user password.

        Args:
            user_id: User ID
            current_password: Current password for verification
            new_password: New password

        Returns:
            True if change successful, False otherwise
        """
        if len(new_password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        user = self.db_session.query(User).filter_by(id=user_id).first()

        if user and user.check_password(current_password):
            user.set_password(new_password)
            self.db_session.commit()
            return True

        return False

    def update_user_profile(self, user_id: str, **kwargs) -> bool:
        """
        Update user profile information.

        Args:
            user_id: User ID
            **kwargs: Fields to update

        Returns:
            True if update successful, False otherwise
        """
        user = self.db_session.query(User).filter_by(id=user_id).first()

        if not user:
            return False

        # List of allowed fields to update
        allowed_fields = [
            'first_name', 'last_name', 'organization', 'username'
        ]

        updated = False
        for field, value in kwargs.items():
            if field in allowed_fields and hasattr(user, field):
                setattr(user, field, value)
                updated = True

        if updated:
            user.updated_at = datetime.utcnow()
            self.db_session.commit()

        return updated

    def deactivate_user(self, user_id: str) -> bool:
        """
        Deactivate a user account.

        Args:
            user_id: User ID to deactivate

        Returns:
            True if deactivation successful, False otherwise
        """
        user = self.db_session.query(User).filter_by(id=user_id).first()

        if user:
            user.is_active = False

            # Deactivate all API keys
            api_keys = self.db_session.query(APIKey).filter_by(user_id=user_id).all()
            for key in api_keys:
                key.is_active = False

            # Cancel active subscriptions
            active_subscriptions = self.db_session.query(Subscription).filter(
                and_(
                    Subscription.user_id == user_id,
                    Subscription.status == SubscriptionStatusEnum.ACTIVE
                )
            ).all()

            for subscription in active_subscriptions:
                subscription.cancel(at_period_end=False)

            self.db_session.commit()
            return True

        return False

    def reactivate_user(self, user_id: str) -> bool:
        """
        Reactivate a user account.

        Args:
            user_id: User ID to reactivate

        Returns:
            True if reactivation successful, False otherwise
        """
        user = self.db_session.query(User).filter_by(id=user_id).first()

        if user:
            user.is_active = True
            self.db_session.commit()
            return True

        return False

    def get_user_permissions(self, user_id: str) -> Dict[str, Any]:
        """
        Get user permissions and plan limits.

        Args:
            user_id: User ID

        Returns:
            Dictionary with user permissions and limits
        """
        user = self.db_session.query(User).filter_by(id=user_id).first()

        if not user:
            return {}

        # Get current subscription
        active_subscription = self.db_session.query(Subscription).filter(
            and_(
                Subscription.user_id == user_id,
                Subscription.status == SubscriptionStatusEnum.ACTIVE
            )
        ).first()

        plan = active_subscription.plan if active_subscription else None

        return {
            'user_id': user_id,
            'is_admin': user.is_admin,
            'is_verified': user.is_verified,
            'current_plan': user.current_plan.value,
            'subscription': {
                'active': active_subscription is not None,
                'plan_name': plan.name if plan else None,
                'hardware_access': plan.allow_hardware_access if plan else False,
                'max_qubits': plan.max_qubits if plan else 4,  # Free tier limit
                'max_circuit_depth': plan.max_circuit_depth if plan else 100,
                'monthly_shot_limit': plan.monthly_shot_limit if plan else 1000,
                'api_limits': {
                    'calls_per_minute': plan.api_calls_per_minute if plan else 10,
                    'calls_per_hour': plan.api_calls_per_hour if plan else 100,
                    'calls_per_day': plan.api_calls_per_day if plan else 1000
                }
            }
        }

    def check_user_access(self, user_id: str, required_plan: str = None,
                         hardware_access: bool = False,
                         admin_only: bool = False) -> Tuple[bool, str]:
        """
        Check if user has required access level.

        Args:
            user_id: User ID to check
            required_plan: Minimum required plan
            hardware_access: Whether hardware access is required
            admin_only: Whether admin access is required

        Returns:
            Tuple of (has_access, reason)
        """
        user = self.db_session.query(User).filter_by(id=user_id).first()

        if not user:
            return False, "User not found"

        if not user.is_active:
            return False, "User account is inactive"

        if admin_only and not user.is_admin:
            return False, "Admin access required"

        permissions = self.get_user_permissions(user_id)

        if hardware_access and not permissions['subscription']['hardware_access']:
            return False, "Hardware access not available in current plan"

        if required_plan:
            plan_hierarchy = ['free', 'basic', 'pro', 'enterprise']
            current_plan_level = plan_hierarchy.index(permissions['current_plan'])
            required_plan_level = plan_hierarchy.index(required_plan.lower())

            if current_plan_level < required_plan_level:
                return False, f"Plan upgrade required (minimum: {required_plan})"

        return True, "Access granted"

    def get_user_stats(self, user_id: str) -> Dict[str, Any]:
        """
        Get user statistics and activity summary.

        Args:
            user_id: User ID

        Returns:
            Dictionary with user statistics
        """
        user = self.db_session.query(User).filter_by(id=user_id).first()

        if not user:
            return {}

        # Get API key stats
        api_keys = self.db_session.query(APIKey).filter_by(user_id=user_id).all()
        active_api_keys = [key for key in api_keys if key.is_active and not key.is_expired()]

        # Calculate total API requests
        total_api_requests = sum(key.total_requests for key in api_keys)

        return {
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'full_name': user.full_name,
                'organization': user.organization,
                'created_at': user.created_at.isoformat(),
                'last_login': user.last_login.isoformat() if user.last_login else None,
                'is_verified': user.is_verified,
                'current_plan': user.current_plan.value
            },
            'api_access': {
                'total_api_keys': len(api_keys),
                'active_api_keys': len(active_api_keys),
                'total_requests': total_api_requests
            },
            'account_status': {
                'is_active': user.is_active,
                'is_admin': user.is_admin,
                'total_spent': user.total_spent
            }
        }