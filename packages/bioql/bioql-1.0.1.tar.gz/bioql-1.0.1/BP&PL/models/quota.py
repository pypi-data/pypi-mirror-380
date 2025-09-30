"""
Quota and rate limiting models.
"""

from datetime import datetime, timedelta
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

from .base import BaseModel


class QuotaTypeEnum(enum.Enum):
    """Enum for quota types."""
    SHOTS_PER_HOUR = "shots_per_hour"
    SHOTS_PER_DAY = "shots_per_day"
    SHOTS_PER_MONTH = "shots_per_month"
    API_CALLS_PER_MINUTE = "api_calls_per_minute"
    API_CALLS_PER_HOUR = "api_calls_per_hour"
    API_CALLS_PER_DAY = "api_calls_per_day"
    CONCURRENT_JOBS = "concurrent_jobs"
    SPENDING_PER_DAY = "spending_per_day"
    SPENDING_PER_MONTH = "spending_per_month"


class Quota(BaseModel):
    """Quota definitions for users or plans."""

    __tablename__ = 'quotas'

    # Quota identification
    name = Column(String(100), nullable=False)
    quota_type = Column(Enum(QuotaTypeEnum), nullable=False)

    # Quota applies to
    user_id = Column(String(36), ForeignKey('users.id'))  # User-specific quota
    plan_id = Column(String(36), ForeignKey('plans.id'))  # Plan-level quota
    api_key_id = Column(String(36), ForeignKey('api_keys.id'))  # API key quota

    # Quota limits
    limit_value = Column(Integer, nullable=False)
    period_seconds = Column(Integer, nullable=False)  # Time window for the quota

    # Quota status
    is_active = Column(Boolean, default=True)
    is_hard_limit = Column(Boolean, default=True)  # Hard limit vs warning

    # Relationships
    user = relationship("User", foreign_keys=[user_id])
    plan = relationship("Plan", foreign_keys=[plan_id])
    api_key = relationship("APIKey", foreign_keys=[api_key_id])
    usage_records = relationship("QuotaUsage", back_populates="quota", cascade="all, delete-orphan")

    @property
    def period_hours(self):
        """Get period in hours."""
        return self.period_seconds / 3600

    @property
    def period_days(self):
        """Get period in days."""
        return self.period_seconds / (3600 * 24)

    def get_current_usage(self, user_id=None, api_key_id=None):
        """Get current usage for this quota within the time window."""
        cutoff_time = datetime.utcnow() - timedelta(seconds=self.period_seconds)

        query_filters = [
            QuotaUsage.quota_id == self.id,
            QuotaUsage.created_at >= cutoff_time
        ]

        if user_id:
            query_filters.append(QuotaUsage.user_id == user_id)
        if api_key_id:
            query_filters.append(QuotaUsage.api_key_id == api_key_id)

        # This would need to be implemented with actual database session
        # For now, return 0 as placeholder
        return 0

    def check_limit(self, requested_amount, user_id=None, api_key_id=None):
        """Check if requested amount would exceed quota."""
        current_usage = self.get_current_usage(user_id, api_key_id)
        return current_usage + requested_amount <= self.limit_value

    def get_remaining(self, user_id=None, api_key_id=None):
        """Get remaining quota amount."""
        current_usage = self.get_current_usage(user_id, api_key_id)
        return max(0, self.limit_value - current_usage)


class QuotaUsage(BaseModel):
    """Records of quota usage."""

    __tablename__ = 'quota_usage'

    # Usage identification
    quota_id = Column(String(36), ForeignKey('quotas.id'), nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    api_key_id = Column(String(36), ForeignKey('api_keys.id'))
    usage_log_id = Column(String(36), ForeignKey('usage_logs.id'))

    # Usage amount
    amount = Column(Integer, nullable=False)

    # Context
    operation_type = Column(String(50))  # quantum_execution, api_call, etc.
    usage_metadata = Column(String(500))

    # Relationships
    quota = relationship("Quota", back_populates="usage_records")
    user = relationship("User", back_populates="quota_usage")
    api_key = relationship("APIKey", foreign_keys=[api_key_id])
    usage_log = relationship("UsageLog", foreign_keys=[usage_log_id])

    @classmethod
    def record_usage(cls, quota_id, user_id, amount, api_key_id=None, usage_log_id=None, operation_type=None, usage_metadata=None):
        """Record quota usage."""
        usage_record = cls(
            quota_id=quota_id,
            user_id=user_id,
            api_key_id=api_key_id,
            usage_log_id=usage_log_id,
            amount=amount,
            operation_type=operation_type,
            usage_metadata=usage_metadata
        )
        return usage_record