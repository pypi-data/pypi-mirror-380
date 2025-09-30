"""
Subscription and plan models.
"""

from datetime import datetime, timedelta
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text, JSON, Enum
from sqlalchemy.orm import relationship
import enum

from .base import BaseModel


class PlanTypeEnum(enum.Enum):
    """Enum for plan types."""
    FREE = "free"
    BASIC = "basic"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class SubscriptionStatusEnum(enum.Enum):
    """Enum for subscription status."""
    ACTIVE = "active"
    CANCELLED = "cancelled"
    PAST_DUE = "past_due"
    UNPAID = "unpaid"
    TRIALING = "trialing"
    INCOMPLETE = "incomplete"


class BillingIntervalEnum(enum.Enum):
    """Enum for billing intervals."""
    MONTHLY = "monthly"
    YEARLY = "yearly"


class Plan(BaseModel):
    """Subscription plans available to users."""

    __tablename__ = 'plans'

    # Plan identification
    name = Column(String(100), nullable=False)
    plan_type = Column(Enum(PlanTypeEnum), nullable=False, unique=True)
    description = Column(Text)

    # Pricing
    price_monthly = Column(String(20), default='0.00')  # Monthly price
    price_yearly = Column(String(20), default='0.00')   # Yearly price
    currency = Column(String(3), default='USD', nullable=False)

    # Plan limits and features
    monthly_shot_limit = Column(Integer)  # null = unlimited
    daily_shot_limit = Column(Integer)    # null = unlimited
    hourly_shot_limit = Column(Integer)   # null = unlimited

    # API limits
    api_calls_per_minute = Column(Integer, default=60)
    api_calls_per_hour = Column(Integer, default=1000)
    api_calls_per_day = Column(Integer, default=10000)

    # Hardware access
    allow_hardware_access = Column(Boolean, default=False)
    max_qubits = Column(Integer)  # null = unlimited
    max_circuit_depth = Column(Integer)  # null = unlimited

    # Support and features
    priority_support = Column(Boolean, default=False)
    analytics_access = Column(Boolean, default=False)
    api_access = Column(Boolean, default=True)

    # Plan status
    is_active = Column(Boolean, default=True)
    is_public = Column(Boolean, default=True)  # Visible to customers

    # Stripe integration
    stripe_price_id_monthly = Column(String(100))
    stripe_price_id_yearly = Column(String(100))
    stripe_product_id = Column(String(100))

    # Metadata
    plan_metadata = Column(JSON)
    sort_order = Column(Integer, default=0)

    # Relationships
    subscriptions = relationship("Subscription", back_populates="plan")
    features = relationship("PlanFeature", back_populates="plan", cascade="all, delete-orphan")

    @property
    def price_monthly_float(self):
        """Get monthly price as float."""
        try:
            return float(self.price_monthly) if self.price_monthly else 0.0
        except (ValueError, TypeError):
            return 0.0

    @property
    def price_yearly_float(self):
        """Get yearly price as float."""
        try:
            return float(self.price_yearly) if self.price_yearly else 0.0
        except (ValueError, TypeError):
            return 0.0

    @property
    def yearly_savings(self):
        """Calculate yearly savings compared to monthly billing."""
        monthly_annual = self.price_monthly_float * 12
        yearly_price = self.price_yearly_float
        if monthly_annual > 0 and yearly_price < monthly_annual:
            return monthly_annual - yearly_price
        return 0.0

    @property
    def yearly_savings_percentage(self):
        """Calculate yearly savings percentage."""
        monthly_annual = self.price_monthly_float * 12
        savings = self.yearly_savings
        if monthly_annual > 0:
            return (savings / monthly_annual) * 100
        return 0.0

    def get_stripe_price_id(self, interval):
        """Get Stripe price ID for billing interval."""
        if interval == BillingIntervalEnum.MONTHLY:
            return self.stripe_price_id_monthly
        elif interval == BillingIntervalEnum.YEARLY:
            return self.stripe_price_id_yearly
        return None

    def check_shot_limit(self, shots, period='monthly'):
        """Check if shots are within plan limits."""
        if period == 'monthly' and self.monthly_shot_limit:
            return shots <= self.monthly_shot_limit
        elif period == 'daily' and self.daily_shot_limit:
            return shots <= self.daily_shot_limit
        elif period == 'hourly' and self.hourly_shot_limit:
            return shots <= self.hourly_shot_limit
        return True  # No limit or unlimited

    def check_circuit_limits(self, qubits, depth):
        """Check if circuit is within plan limits."""
        if self.max_qubits and qubits > self.max_qubits:
            return False
        if self.max_circuit_depth and depth > self.max_circuit_depth:
            return False
        return True


class PlanFeature(BaseModel):
    """Individual features available in plans."""

    __tablename__ = 'plan_features'

    plan_id = Column(String(36), ForeignKey('plans.id'), nullable=False)

    # Feature details
    name = Column(String(100), nullable=False)
    description = Column(Text)
    included = Column(Boolean, default=True)

    # Feature limits
    limit_value = Column(Integer)  # null = unlimited
    limit_unit = Column(String(50))  # shots, qubits, calls, etc.

    # Display order
    sort_order = Column(Integer, default=0)

    # Relationships
    plan = relationship("Plan", back_populates="features")


class Subscription(BaseModel):
    """User subscriptions to plans."""

    __tablename__ = 'subscriptions'

    # Subscription identification
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    plan_id = Column(String(36), ForeignKey('plans.id'), nullable=False)

    # Subscription details
    status = Column(Enum(SubscriptionStatusEnum), default=SubscriptionStatusEnum.ACTIVE, nullable=False)
    billing_interval = Column(Enum(BillingIntervalEnum), default=BillingIntervalEnum.MONTHLY, nullable=False)

    # Timing
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    current_period_start = Column(DateTime, default=datetime.utcnow, nullable=False)
    current_period_end = Column(DateTime, nullable=False)
    cancel_at_period_end = Column(Boolean, default=False)
    cancelled_at = Column(DateTime)
    ended_at = Column(DateTime)

    # Trial information
    trial_start = Column(DateTime)
    trial_end = Column(DateTime)

    # Pricing
    price = Column(String(20), nullable=False)
    currency = Column(String(3), default='USD', nullable=False)

    # Stripe integration
    stripe_subscription_id = Column(String(100), unique=True)
    stripe_customer_id = Column(String(100))

    # Usage tracking for billing period
    current_period_shots = Column(Integer, default=0)
    current_period_api_calls = Column(Integer, default=0)
    current_period_cost = Column(String(20), default='0.00')

    # Metadata
    subscription_metadata = Column(JSON)

    # Relationships
    user = relationship("User", back_populates="subscriptions")
    plan = relationship("Plan", back_populates="subscriptions")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.current_period_end:
            if self.billing_interval == BillingIntervalEnum.MONTHLY:
                self.current_period_end = self.current_period_start + timedelta(days=30)
            else:  # yearly
                self.current_period_end = self.current_period_start + timedelta(days=365)

    @property
    def is_active(self):
        """Check if subscription is currently active."""
        return (self.status == SubscriptionStatusEnum.ACTIVE and
                self.current_period_end > datetime.utcnow() and
                (not self.ended_at or self.ended_at > datetime.utcnow()))

    @property
    def is_trial(self):
        """Check if subscription is in trial period."""
        if not self.trial_start or not self.trial_end:
            return False
        now = datetime.utcnow()
        return self.trial_start <= now <= self.trial_end

    @property
    def days_until_renewal(self):
        """Calculate days until next renewal."""
        if self.current_period_end:
            delta = self.current_period_end - datetime.utcnow()
            return max(0, delta.days)
        return 0

    @property
    def days_in_trial(self):
        """Calculate remaining days in trial."""
        if self.is_trial:
            delta = self.trial_end - datetime.utcnow()
            return max(0, delta.days)
        return 0

    @property
    def price_float(self):
        """Get price as float."""
        try:
            return float(self.price) if self.price else 0.0
        except (ValueError, TypeError):
            return 0.0

    def check_usage_limits(self, shots=0, api_calls=0):
        """Check if usage is within subscription limits."""
        # Check shot limits
        if self.plan.monthly_shot_limit:
            if self.current_period_shots + shots > self.plan.monthly_shot_limit:
                return False, f"Monthly shot limit ({self.plan.monthly_shot_limit}) would be exceeded"

        # Check API call limits (you'd need to track current period API calls)
        # This is a simplified version
        return True, "Usage within limits"

    def record_usage(self, shots=0, cost=0.0, api_calls=0):
        """Record usage for the current billing period."""
        self.current_period_shots += shots
        self.current_period_api_calls += api_calls

        current_cost = float(self.current_period_cost) if self.current_period_cost else 0.0
        self.current_period_cost = str(current_cost + cost)

    def renew_period(self):
        """Renew the subscription for the next billing period."""
        if self.billing_interval == BillingIntervalEnum.MONTHLY:
            self.current_period_start = self.current_period_end
            self.current_period_end = self.current_period_start + timedelta(days=30)
        else:  # yearly
            self.current_period_start = self.current_period_end
            self.current_period_end = self.current_period_start + timedelta(days=365)

        # Reset period usage counters
        self.current_period_shots = 0
        self.current_period_api_calls = 0
        self.current_period_cost = '0.00'

    def cancel(self, at_period_end=True):
        """Cancel the subscription."""
        if at_period_end:
            self.cancel_at_period_end = True
        else:
            self.status = SubscriptionStatusEnum.CANCELLED
            self.cancelled_at = datetime.utcnow()
            self.ended_at = datetime.utcnow()

    def reactivate(self):
        """Reactivate a cancelled subscription."""
        if self.status == SubscriptionStatusEnum.CANCELLED:
            self.status = SubscriptionStatusEnum.ACTIVE
            self.cancel_at_period_end = False
            self.cancelled_at = None
            self.ended_at = None