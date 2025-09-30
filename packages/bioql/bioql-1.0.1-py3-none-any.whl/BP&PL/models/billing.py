"""
Billing and payment models.
"""

from datetime import datetime, timedelta
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text, JSON, Enum
from sqlalchemy.orm import relationship
from decimal import Decimal
import enum

from .base import BaseModel


class BillStatusEnum(enum.Enum):
    """Enum for bill status."""
    DRAFT = "draft"
    PENDING = "pending"
    PAID = "paid"
    OVERDUE = "overdue"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"


class PaymentStatusEnum(enum.Enum):
    """Enum for payment status."""
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"


class PaymentMethodTypeEnum(enum.Enum):
    """Enum for payment method types."""
    CREDIT_CARD = "credit_card"
    BANK_TRANSFER = "bank_transfer"
    PAYPAL = "paypal"
    CRYPTO = "crypto"


class Bill(BaseModel):
    """Customer bill/invoice."""

    __tablename__ = 'bills'

    # Bill identification
    bill_number = Column(String(50), unique=True, nullable=False, index=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)

    # Billing period
    period_start = Column(DateTime, nullable=False)
    period_end = Column(DateTime, nullable=False)

    # Bill status
    status = Column(Enum(BillStatusEnum), default=BillStatusEnum.DRAFT, nullable=False)

    # Amounts (stored as strings to avoid floating point issues)
    subtotal = Column(String(20), default='0.00')
    tax_amount = Column(String(20), default='0.00')
    discount_amount = Column(String(20), default='0.00')
    total_amount = Column(String(20), default='0.00')

    # Currency
    currency = Column(String(3), default='USD', nullable=False)

    # Due dates
    issued_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    due_at = Column(DateTime, nullable=False)
    paid_at = Column(DateTime)

    # Billing details
    billing_email = Column(String(255))
    billing_address = Column(JSON)
    tax_rate = Column(Float, default=0.0)

    # Payment information
    stripe_invoice_id = Column(String(100), unique=True)
    payment_intent_id = Column(String(100))

    # Notes and metadata
    notes = Column(Text)
    bill_metadata = Column(JSON)

    # Relationships
    user = relationship("User", back_populates="bills")
    bill_items = relationship("BillItem", back_populates="bill", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="bill", cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.bill_number:
            self.bill_number = self.generate_bill_number()
        if not self.due_at:
            self.due_at = datetime.utcnow() + timedelta(days=30)

    @classmethod
    def generate_bill_number(cls):
        """Generate unique bill number."""
        from datetime import datetime
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f"BIOQL-{timestamp}"

    def calculate_totals(self):
        """Calculate bill totals from line items."""
        subtotal = sum(Decimal(item.total_amount) for item in self.bill_items)

        # Apply discount
        discount = Decimal(self.discount_amount) if self.discount_amount else Decimal('0.00')
        subtotal_after_discount = subtotal - discount

        # Calculate tax
        tax = subtotal_after_discount * Decimal(str(self.tax_rate))

        # Calculate total
        total = subtotal_after_discount + tax

        # Update fields
        self.subtotal = str(subtotal)
        self.tax_amount = str(tax)
        self.total_amount = str(total)

        return float(total)

    @property
    def is_overdue(self):
        """Check if bill is overdue."""
        return (self.status == BillStatusEnum.PENDING and
                self.due_at < datetime.utcnow())

    @property
    def days_overdue(self):
        """Calculate days overdue."""
        if self.is_overdue:
            return (datetime.utcnow() - self.due_at).days
        return 0

    @property
    def total_float(self):
        """Get total amount as float."""
        try:
            return float(self.total_amount) if self.total_amount else 0.0
        except (ValueError, TypeError):
            return 0.0

    def add_usage_charges(self, usage_logs):
        """Add usage charges to the bill."""
        for usage_log in usage_logs:
            if not usage_log.billed and usage_log.success:
                bill_item = BillItem(
                    bill_id=self.id,
                    description=f"Quantum computation - {usage_log.shots_executed} shots on {usage_log.backend_used}",
                    quantity=1,
                    unit_price=usage_log.total_cost or '0.00',
                    total_amount=usage_log.total_cost or '0.00',
                    usage_log_id=usage_log.id
                )
                self.bill_items.append(bill_item)
                usage_log.billed = True
                usage_log.bill_id = self.id

    def finalize(self):
        """Finalize the bill."""
        self.calculate_totals()
        if self.status == BillStatusEnum.DRAFT:
            self.status = BillStatusEnum.PENDING

    def mark_paid(self, payment):
        """Mark bill as paid."""
        self.status = BillStatusEnum.PAID
        self.paid_at = datetime.utcnow()
        if payment:
            self.payments.append(payment)


class BillItem(BaseModel):
    """Individual line item on a bill."""

    __tablename__ = 'bill_items'

    bill_id = Column(String(36), ForeignKey('bills.id'), nullable=False)

    # Item details
    description = Column(String(500), nullable=False)
    quantity = Column(Float, default=1.0)
    unit_price = Column(String(20), nullable=False)
    total_amount = Column(String(20), nullable=False)

    # Optional links to usage
    usage_log_id = Column(String(36), ForeignKey('usage_logs.id'))
    subscription_id = Column(String(36))

    # Metadata
    bill_metadata = Column(JSON)

    # Relationships
    bill = relationship("Bill", back_populates="bill_items")
    usage_log = relationship("UsageLog", foreign_keys=[usage_log_id])

    @property
    def unit_price_float(self):
        """Get unit price as float."""
        try:
            return float(self.unit_price) if self.unit_price else 0.0
        except (ValueError, TypeError):
            return 0.0

    @property
    def total_amount_float(self):
        """Get total amount as float."""
        try:
            return float(self.total_amount) if self.total_amount else 0.0
        except (ValueError, TypeError):
            return 0.0


class PaymentMethod(BaseModel):
    """Stored payment methods for users."""

    __tablename__ = 'payment_methods'

    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)

    # Payment method details
    type = Column(Enum(PaymentMethodTypeEnum), nullable=False)
    is_default = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    # Stripe integration
    stripe_payment_method_id = Column(String(100))

    # Card details (last 4 digits, brand, etc.)
    card_last4 = Column(String(4))
    card_brand = Column(String(20))
    card_exp_month = Column(Integer)
    card_exp_year = Column(Integer)

    # Bank details
    bank_name = Column(String(100))
    account_last4 = Column(String(4))

    # Other details
    nickname = Column(String(100))
    bill_metadata = Column(JSON)

    # Relationships
    user = relationship("User")
    payments = relationship("Payment", back_populates="payment_method")

    @property
    def display_name(self):
        """Get display-friendly name for payment method."""
        if self.nickname:
            return self.nickname
        elif self.type == PaymentMethodTypeEnum.CREDIT_CARD and self.card_brand and self.card_last4:
            return f"{self.card_brand.title()} ending in {self.card_last4}"
        elif self.type == PaymentMethodTypeEnum.BANK_TRANSFER and self.bank_name and self.account_last4:
            return f"{self.bank_name} ending in {self.account_last4}"
        else:
            return self.type.value.replace('_', ' ').title()

    @property
    def is_expired(self):
        """Check if payment method is expired (for cards)."""
        if self.type == PaymentMethodTypeEnum.CREDIT_CARD and self.card_exp_month and self.card_exp_year:
            now = datetime.utcnow()
            return (self.card_exp_year < now.year or
                   (self.card_exp_year == now.year and self.card_exp_month < now.month))
        return False


class Payment(BaseModel):
    """Payment records."""

    __tablename__ = 'payments'

    # Payment identification
    payment_number = Column(String(50), unique=True, nullable=False)
    bill_id = Column(String(36), ForeignKey('bills.id'), nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    payment_method_id = Column(String(36), ForeignKey('payment_methods.id'))

    # Payment details
    amount = Column(String(20), nullable=False)
    currency = Column(String(3), default='USD', nullable=False)
    status = Column(Enum(PaymentStatusEnum), default=PaymentStatusEnum.PENDING, nullable=False)

    # Payment processor details
    stripe_payment_intent_id = Column(String(100))
    stripe_charge_id = Column(String(100))
    processor_fee = Column(String(20), default='0.00')

    # Timing
    processed_at = Column(DateTime)
    failed_at = Column(DateTime)
    refunded_at = Column(DateTime)

    # Failure information
    failure_reason = Column(String(255))
    failure_code = Column(String(50))

    # Notes and metadata
    notes = Column(Text)
    bill_metadata = Column(JSON)

    # Relationships
    bill = relationship("Bill", back_populates="payments")
    user = relationship("User")
    payment_method = relationship("PaymentMethod", back_populates="payments")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.payment_number:
            self.payment_number = self.generate_payment_number()

    @classmethod
    def generate_payment_number(cls):
        """Generate unique payment number."""
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f"PAY-{timestamp}"

    @property
    def amount_float(self):
        """Get amount as float."""
        try:
            return float(self.amount) if self.amount else 0.0
        except (ValueError, TypeError):
            return 0.0

    def mark_succeeded(self, **kwargs):
        """Mark payment as succeeded."""
        self.status = PaymentStatusEnum.SUCCEEDED
        self.processed_at = datetime.utcnow()

        # Update additional fields
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def mark_failed(self, reason=None, code=None):
        """Mark payment as failed."""
        self.status = PaymentStatusEnum.FAILED
        self.failed_at = datetime.utcnow()
        if reason:
            self.failure_reason = reason
        if code:
            self.failure_code = code

    def mark_refunded(self, **kwargs):
        """Mark payment as refunded."""
        self.status = PaymentStatusEnum.REFUNDED
        self.refunded_at = datetime.utcnow()

        # Update additional fields
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)