"""
User management models for the BioQL billing system.
"""

from datetime import datetime, timedelta
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text, Integer, Enum
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import enum

from .base import BaseModel


class UserPlanEnum(enum.Enum):
    """Enum for user plans."""
    FREE = "free"
    BASIC = "basic"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class User(BaseModel):
    """User model for authentication and billing."""

    __tablename__ = 'users'

    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    organization = Column(String(255))

    # Account status
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    # Billing information
    stripe_customer_id = Column(String(100), unique=True, index=True)
    current_plan = Column(Enum(UserPlanEnum), default=UserPlanEnum.FREE, nullable=False)

    # Account limits and usage
    total_spent = Column(String(20), default='0.00')  # Store as string to avoid floating point issues
    last_login = Column(DateTime)
    verification_token = Column(String(100))
    reset_token = Column(String(100))
    reset_token_expires = Column(DateTime)

    # Relationships
    api_keys = relationship("APIKey", back_populates="user", cascade="all, delete-orphan")
    subscriptions = relationship("Subscription", back_populates="user", cascade="all, delete-orphan")
    usage_logs = relationship("UsageLog", back_populates="user", cascade="all, delete-orphan")
    bills = relationship("Bill", back_populates="user", cascade="all, delete-orphan")
    quota_usage = relationship("QuotaUsage", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password):
        """Set password hash."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check password against hash."""
        return check_password_hash(self.password_hash, password)

    def generate_verification_token(self):
        """Generate email verification token."""
        self.verification_token = secrets.token_urlsafe(32)
        return self.verification_token

    def generate_reset_token(self, expires_hours=24):
        """Generate password reset token."""
        self.reset_token = secrets.token_urlsafe(32)
        self.reset_token_expires = datetime.utcnow() + timedelta(hours=expires_hours)
        return self.reset_token

    def is_reset_token_valid(self):
        """Check if reset token is still valid."""
        return (self.reset_token and
                self.reset_token_expires and
                self.reset_token_expires > datetime.utcnow())

    @property
    def full_name(self):
        """Get user's full name."""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    @property
    def current_subscription(self):
        """Get user's current active subscription."""
        active_subs = [sub for sub in self.subscriptions if sub.is_active]
        return active_subs[0] if active_subs else None

    def to_dict(self, include_sensitive=False):
        """Convert to dictionary, optionally excluding sensitive data."""
        data = super().to_dict()
        if not include_sensitive:
            data.pop('password_hash', None)
            data.pop('verification_token', None)
            data.pop('reset_token', None)
            data.pop('stripe_customer_id', None)
        return data


class APIKey(BaseModel):
    """API key model for user authentication."""

    __tablename__ = 'api_keys'

    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    key_name = Column(String(100), nullable=False)
    key_hash = Column(String(255), nullable=False, unique=True, index=True)
    key_prefix = Column(String(10), nullable=False)  # First 8 chars for display

    # Key permissions and limits
    is_active = Column(Boolean, default=True, nullable=False)
    rate_limit_per_minute = Column(Integer, default=60)
    rate_limit_per_hour = Column(Integer, default=1000)
    rate_limit_per_day = Column(Integer, default=10000)

    # Usage tracking
    last_used = Column(DateTime)
    total_requests = Column(Integer, default=0)

    # Expiration
    expires_at = Column(DateTime)

    # Relationships
    user = relationship("User", back_populates="api_keys")

    @classmethod
    def generate_key(cls):
        """Generate a new API key."""
        key = f"bioql_{secrets.token_urlsafe(32)}"
        return key

    def set_key(self, key):
        """Set the API key hash and prefix."""
        self.key_hash = generate_password_hash(key)
        self.key_prefix = key[:8]

    def check_key(self, key):
        """Check if provided key matches the stored hash."""
        return check_password_hash(self.key_hash, key)

    def is_expired(self):
        """Check if the API key has expired."""
        return self.expires_at and self.expires_at < datetime.utcnow()

    def is_valid(self):
        """Check if the API key is valid and active."""
        return self.is_active and not self.is_expired()

    def record_usage(self):
        """Record API key usage."""
        self.last_used = datetime.utcnow()
        self.total_requests += 1

    def to_dict(self, include_sensitive=False):
        """Convert to dictionary, optionally excluding sensitive data."""
        data = super().to_dict()
        if not include_sensitive:
            data.pop('key_hash', None)
            # Only show prefix for security
            data['key_display'] = f"{self.key_prefix}..."
        return data


class UserPlan(BaseModel):
    """User plan history and changes."""

    __tablename__ = 'user_plans'

    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    plan = Column(Enum(UserPlanEnum), nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    ended_at = Column(DateTime)

    # Reason for plan change
    change_reason = Column(String(255))
    changed_by = Column(String(36))  # User ID who made the change

    # Relationships
    user = relationship("User", foreign_keys=[user_id])

    @property
    def is_active(self):
        """Check if this plan period is currently active."""
        now = datetime.utcnow()
        return self.started_at <= now and (self.ended_at is None or self.ended_at > now)