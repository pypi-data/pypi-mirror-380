"""
Billing engine with hybrid pricing model implementation.
"""

from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from decimal import Decimal, ROUND_HALF_UP
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from ..models.billing import Bill, BillItem, BillStatusEnum
from ..models.usage import UsageLog, BackendTypeEnum, AlgorithmTypeEnum
from ..models.user import User
from ..models.subscription import Subscription, SubscriptionStatusEnum


class BillingEngine:
    """
    Core billing engine implementing the hybrid pricing model.

    Pricing Model:
    - Simulators: $0.001 per shot
    - Real hardware: $0.01 per shot
    - Complexity multiplier: 1x (≤4 qubits), 2x (5-8 qubits), 5x (9+ qubits)
    - Algorithm premium: VQE/Grover 3x, basic gates 1x
    - Subscription plans: Basic ($99/mo), Pro ($499/mo), Enterprise ($2999/mo)
    """

    def __init__(self, db_session: Session, pricing_config: Dict[str, Any]):
        self.db_session = db_session
        self.pricing_config = pricing_config

    def calculate_shot_cost(self, backend_type: BackendTypeEnum, shots: int,
                          qubits: int, algorithm_type: AlgorithmTypeEnum) -> Dict[str, Any]:
        """
        Calculate cost for quantum shots using hybrid pricing model.

        Args:
            backend_type: Type of backend (simulator or real hardware)
            shots: Number of shots
            qubits: Number of qubits in circuit
            algorithm_type: Type of algorithm being executed

        Returns:
            Dictionary with cost breakdown
        """
        # Base cost per shot
        if backend_type == BackendTypeEnum.SIMULATOR:
            base_cost_per_shot = Decimal(self.pricing_config.get('simulator_cost_per_shot', '0.001'))
        else:
            base_cost_per_shot = Decimal(self.pricing_config.get('hardware_cost_per_shot', '0.01'))

        # Complexity multiplier based on qubits
        if qubits <= 4:
            complexity_multiplier = Decimal('1.0')
        elif qubits <= 8:
            complexity_multiplier = Decimal('2.0')
        else:
            complexity_multiplier = Decimal('5.0')

        # Algorithm multiplier
        algorithm_multipliers = self.pricing_config.get('algorithm_multipliers', {
            'basic': 1.0,
            'vqe': 3.0,
            'grover': 3.0,
            'shor': 3.0,
            'qaoa': 2.0,
            'custom': 1.5
        })

        algorithm_multiplier = Decimal(str(algorithm_multipliers.get(algorithm_type.value, 1.0)))

        # Calculate total cost
        base_cost = base_cost_per_shot * Decimal(str(shots))
        total_cost = base_cost * complexity_multiplier * algorithm_multiplier

        return {
            'base_cost_per_shot': float(base_cost_per_shot),
            'shots': shots,
            'base_cost': float(base_cost),
            'complexity_multiplier': float(complexity_multiplier),
            'algorithm_multiplier': float(algorithm_multiplier),
            'total_cost': float(total_cost.quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)),
            'cost_breakdown': {
                'base': float(base_cost),
                'complexity_adjustment': float(base_cost * (complexity_multiplier - Decimal('1.0'))),
                'algorithm_premium': float(base_cost * complexity_multiplier * (algorithm_multiplier - Decimal('1.0')))
            }
        }

    def calculate_subscription_pricing(self, plan_type: str, billing_interval: str) -> Dict[str, Any]:
        """Calculate subscription pricing based on plan and interval."""
        subscription_prices = self.pricing_config.get('subscription_plans', {
            'basic': {'monthly': 99.00, 'yearly': 990.00},
            'pro': {'monthly': 499.00, 'yearly': 4990.00},
            'enterprise': {'monthly': 2999.00, 'yearly': 29990.00}
        })

        plan_pricing = subscription_prices.get(plan_type, {})
        price = plan_pricing.get(billing_interval, 0.0)

        # Calculate savings for yearly billing
        monthly_price = plan_pricing.get('monthly', 0.0)
        yearly_price = plan_pricing.get('yearly', 0.0)

        yearly_savings = 0.0
        savings_percentage = 0.0

        if billing_interval == 'yearly' and monthly_price > 0:
            annual_monthly_cost = monthly_price * 12
            yearly_savings = annual_monthly_cost - yearly_price
            savings_percentage = (yearly_savings / annual_monthly_cost) * 100

        return {
            'plan_type': plan_type,
            'billing_interval': billing_interval,
            'price': price,
            'currency': 'USD',
            'yearly_savings': yearly_savings,
            'savings_percentage': savings_percentage
        }

    def create_usage_bill(self, user_id: str, period_start: datetime,
                         period_end: datetime) -> Bill:
        """
        Create a bill for usage-based charges in a given period.

        Args:
            user_id: User ID to bill
            period_start: Start of billing period
            period_end: End of billing period

        Returns:
            Created Bill instance
        """
        # Get unbilled usage logs for the period
        unbilled_usage = self.db_session.query(UsageLog).filter(
            and_(
                UsageLog.user_id == user_id,
                UsageLog.billed == False,
                UsageLog.success == True,
                UsageLog.created_at >= period_start,
                UsageLog.created_at < period_end
            )
        ).all()

        if not unbilled_usage:
            return None  # No charges to bill

        # Create bill
        bill = Bill(
            user_id=user_id,
            period_start=period_start,
            period_end=period_end,
            status=BillStatusEnum.DRAFT
        )

        self.db_session.add(bill)
        self.db_session.flush()  # Get bill ID

        # Add line items for each usage log
        total_shots = 0
        for usage_log in unbilled_usage:
            if usage_log.total_cost and float(usage_log.total_cost) > 0:
                description = self._generate_usage_description(usage_log)

                bill_item = BillItem(
                    bill_id=bill.id,
                    description=description,
                    quantity=1,
                    unit_price=usage_log.total_cost,
                    total_amount=usage_log.total_cost,
                    usage_log_id=usage_log.id
                )

                bill.bill_items.append(bill_item)
                usage_log.billed = True
                usage_log.bill_id = bill.id
                total_shots += usage_log.shots_executed

        # Add summary line item if multiple usage logs
        if len(unbilled_usage) > 1:
            summary_item = BillItem(
                bill_id=bill.id,
                description=f"Usage Summary: {len(unbilled_usage)} quantum computations, {total_shots:,} total shots",
                quantity=0,  # Summary item
                unit_price='0.00',
                total_amount='0.00'
            )
            bill.bill_items.insert(0, summary_item)

        # Calculate totals and finalize
        bill.finalize()
        self.db_session.commit()

        return bill

    def create_subscription_bill(self, subscription: Subscription) -> Bill:
        """
        Create a bill for subscription charges.

        Args:
            subscription: Subscription to bill

        Returns:
            Created Bill instance
        """
        bill = Bill(
            user_id=subscription.user_id,
            period_start=subscription.current_period_start,
            period_end=subscription.current_period_end,
            status=BillStatusEnum.DRAFT
        )

        self.db_session.add(bill)
        self.db_session.flush()

        # Add subscription line item
        plan_name = subscription.plan.name
        interval_display = "Monthly" if subscription.billing_interval.value == "monthly" else "Annual"

        description = f"{plan_name} Plan - {interval_display} Subscription"

        bill_item = BillItem(
            bill_id=bill.id,
            description=description,
            quantity=1,
            unit_price=subscription.price,
            total_amount=subscription.price,
            subscription_id=subscription.id
        )

        bill.bill_items.append(bill_item)

        # Add any usage overages if applicable
        self._add_usage_overages(bill, subscription)

        # Calculate totals and finalize
        bill.finalize()
        self.db_session.commit()

        return bill

    def _add_usage_overages(self, bill: Bill, subscription: Subscription):
        """Add usage overage charges to subscription bill."""
        plan = subscription.plan

        # Check if plan has usage limits
        if not plan.monthly_shot_limit:
            return  # Unlimited plan, no overages

        # Get usage for current billing period
        current_usage = self.db_session.query(UsageLog).filter(
            and_(
                UsageLog.user_id == subscription.user_id,
                UsageLog.success == True,
                UsageLog.created_at >= subscription.current_period_start,
                UsageLog.created_at < subscription.current_period_end
            )
        ).all()

        total_shots = sum(log.shots_executed for log in current_usage)

        if total_shots > plan.monthly_shot_limit:
            overage_shots = total_shots - plan.monthly_shot_limit
            overage_rate = Decimal(self.pricing_config.get('overage_rate_per_shot', '0.005'))
            overage_cost = overage_rate * Decimal(str(overage_shots))

            overage_item = BillItem(
                bill_id=bill.id,
                description=f"Usage Overage: {overage_shots:,} shots over {plan.monthly_shot_limit:,} limit",
                quantity=overage_shots,
                unit_price=str(overage_rate),
                total_amount=str(overage_cost)
            )

            bill.bill_items.append(overage_item)

    def _generate_usage_description(self, usage_log: UsageLog) -> str:
        """Generate a human-readable description for usage log."""
        backend_display = usage_log.backend_used.replace('_', ' ').title()
        algorithm_display = usage_log.algorithm_type.value.upper() if usage_log.algorithm_type != AlgorithmTypeEnum.BASIC else "Standard"

        description = (
            f"{algorithm_display} quantum computation - "
            f"{usage_log.shots_executed:,} shots on {backend_display} "
            f"({usage_log.circuit_qubits} qubits, depth {usage_log.circuit_depth})"
        )

        if usage_log.biological_context and usage_log.biological_context != 'general':
            context_display = usage_log.biological_context.replace('_', ' ').title()
            description = f"{context_display} - {description}"

        return description

    def get_billing_summary(self, user_id: str, start_date: datetime = None,
                           end_date: datetime = None) -> Dict[str, Any]:
        """Get comprehensive billing summary for a user."""
        if not start_date:
            start_date = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if not end_date:
            end_date = datetime.utcnow()

        # Get bills in period
        bills_query = self.db_session.query(Bill).filter(
            and_(
                Bill.user_id == user_id,
                Bill.issued_at >= start_date,
                Bill.issued_at <= end_date
            )
        )
        bills = bills_query.all()

        # Calculate totals
        total_billed = sum(bill.total_float for bill in bills)
        total_paid = sum(bill.total_float for bill in bills if bill.status == BillStatusEnum.PAID)
        total_outstanding = sum(bill.total_float for bill in bills
                              if bill.status in [BillStatusEnum.PENDING, BillStatusEnum.OVERDUE])

        # Get usage summary
        usage_query = self.db_session.query(UsageLog).filter(
            and_(
                UsageLog.user_id == user_id,
                UsageLog.created_at >= start_date,
                UsageLog.created_at <= end_date,
                UsageLog.success == True
            )
        )
        usage_logs = usage_query.all()

        total_shots = sum(log.shots_executed for log in usage_logs)
        total_usage_cost = sum(log.cost_float for log in usage_logs)

        # Backend breakdown
        backend_costs = {}
        for log in usage_logs:
            backend = log.backend_used
            if backend not in backend_costs:
                backend_costs[backend] = {'shots': 0, 'cost': 0.0, 'jobs': 0}
            backend_costs[backend]['shots'] += log.shots_executed
            backend_costs[backend]['cost'] += log.cost_float
            backend_costs[backend]['jobs'] += 1

        # Current subscription
        active_subscription = self.db_session.query(Subscription).filter(
            and_(
                Subscription.user_id == user_id,
                Subscription.status == SubscriptionStatusEnum.ACTIVE
            )
        ).first()

        return {
            'period': {
                'start': start_date.isoformat(),
                'end': end_date.isoformat()
            },
            'billing_totals': {
                'total_billed': total_billed,
                'total_paid': total_paid,
                'total_outstanding': total_outstanding,
                'bill_count': len(bills)
            },
            'usage_totals': {
                'total_shots': total_shots,
                'total_usage_cost': total_usage_cost,
                'job_count': len(usage_logs),
                'average_cost_per_job': total_usage_cost / len(usage_logs) if usage_logs else 0
            },
            'backend_breakdown': backend_costs,
            'current_subscription': {
                'plan_name': active_subscription.plan.name if active_subscription else None,
                'monthly_cost': float(active_subscription.price) if active_subscription else 0,
                'billing_interval': active_subscription.billing_interval.value if active_subscription else None,
                'next_billing_date': active_subscription.current_period_end.isoformat() if active_subscription else None
            },
            'bills': [
                {
                    'id': bill.id,
                    'bill_number': bill.bill_number,
                    'amount': bill.total_float,
                    'status': bill.status.value,
                    'issued_at': bill.issued_at.isoformat(),
                    'due_at': bill.due_at.isoformat(),
                    'paid_at': bill.paid_at.isoformat() if bill.paid_at else None
                }
                for bill in bills
            ]
        }

    def process_monthly_billing(self, user_id: str = None) -> Dict[str, Any]:
        """
        Process monthly billing for all users or a specific user.

        Args:
            user_id: Optional specific user ID to process

        Returns:
            Summary of billing processing results
        """
        results = {
            'processed_users': 0,
            'usage_bills_created': 0,
            'subscription_bills_created': 0,
            'total_amount_billed': 0.0,
            'errors': []
        }

        # Define billing period (previous month)
        today = datetime.utcnow().date()
        first_day_current_month = today.replace(day=1)
        period_end = datetime.combine(first_day_current_month, datetime.min.time())

        if first_day_current_month.month == 1:
            period_start = first_day_current_month.replace(year=first_day_current_month.year - 1, month=12)
        else:
            period_start = first_day_current_month.replace(month=first_day_current_month.month - 1)
        period_start = datetime.combine(period_start, datetime.min.time())

        # Get users to process
        if user_id:
            users = [self.db_session.query(User).filter_by(id=user_id).first()]
            if not users[0]:
                results['errors'].append(f"User {user_id} not found")
                return results
        else:
            users = self.db_session.query(User).filter_by(is_active=True).all()

        for user in users:
            try:
                # Create usage bill
                usage_bill = self.create_usage_bill(user.id, period_start, period_end)
                if usage_bill:
                    results['usage_bills_created'] += 1
                    results['total_amount_billed'] += usage_bill.total_float

                # Process subscription billing
                active_subscriptions = self.db_session.query(Subscription).filter(
                    and_(
                        Subscription.user_id == user.id,
                        Subscription.status == SubscriptionStatusEnum.ACTIVE,
                        Subscription.current_period_end <= datetime.utcnow()
                    )
                ).all()

                for subscription in active_subscriptions:
                    subscription_bill = self.create_subscription_bill(subscription)
                    results['subscription_bills_created'] += 1
                    results['total_amount_billed'] += subscription_bill.total_float

                    # Renew subscription period
                    subscription.renew_period()

                results['processed_users'] += 1

            except Exception as e:
                results['errors'].append(f"Error processing user {user.id}: {str(e)}")

        return results

    def apply_discount(self, bill: Bill, discount_code: str = None,
                      discount_percentage: float = None,
                      discount_amount: float = None) -> bool:
        """
        Apply discount to a bill.

        Args:
            bill: Bill to apply discount to
            discount_code: Discount code (for validation)
            discount_percentage: Percentage discount (0-100)
            discount_amount: Fixed amount discount

        Returns:
            True if discount was applied successfully
        """
        if bill.status != BillStatusEnum.DRAFT:
            return False

        current_discount = float(bill.discount_amount) if bill.discount_amount else 0.0
        subtotal = float(bill.subtotal) if bill.subtotal else 0.0

        if discount_percentage:
            discount_amount = subtotal * (discount_percentage / 100)
        elif not discount_amount:
            return False

        # Apply discount
        new_discount = current_discount + discount_amount
        bill.discount_amount = str(new_discount)

        # Recalculate totals
        bill.calculate_totals()
        self.db_session.commit()

        return True

    def estimate_monthly_cost(self, user_id: str) -> Dict[str, Any]:
        """
        Estimate monthly cost based on current usage patterns.

        Args:
            user_id: User ID to analyze

        Returns:
            Cost estimation breakdown
        """
        # Analyze last 30 days of usage
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)

        usage_logs = self.db_session.query(UsageLog).filter(
            and_(
                UsageLog.user_id == user_id,
                UsageLog.created_at >= thirty_days_ago,
                UsageLog.success == True
            )
        ).all()

        if not usage_logs:
            return {
                'estimated_monthly_cost': 0.0,
                'confidence': 'low',
                'reason': 'No usage data available'
            }

        # Calculate averages
        total_shots = sum(log.shots_executed for log in usage_logs)
        total_cost = sum(log.cost_float for log in usage_logs)
        days_with_usage = len(set(log.created_at.date() for log in usage_logs))

        # Project to monthly
        if days_with_usage > 0:
            daily_average_cost = total_cost / days_with_usage
            estimated_monthly_cost = daily_average_cost * 30
        else:
            estimated_monthly_cost = 0.0

        # Confidence level based on data availability
        if days_with_usage >= 20:
            confidence = 'high'
        elif days_with_usage >= 10:
            confidence = 'medium'
        else:
            confidence = 'low'

        # Backend breakdown
        backend_usage = {}
        for log in usage_logs:
            backend = log.backend_used
            if backend not in backend_usage:
                backend_usage[backend] = {'shots': 0, 'cost': 0.0}
            backend_usage[backend]['shots'] += log.shots_executed
            backend_usage[backend]['cost'] += log.cost_float

        return {
            'estimated_monthly_cost': round(estimated_monthly_cost, 2),
            'confidence': confidence,
            'analysis_period_days': days_with_usage,
            'total_usage_analyzed': {
                'shots': total_shots,
                'cost': total_cost,
                'jobs': len(usage_logs)
            },
            'daily_averages': {
                'cost': round(daily_average_cost, 2) if days_with_usage > 0 else 0,
                'shots': round(total_shots / days_with_usage) if days_with_usage > 0 else 0
            },
            'backend_breakdown': backend_usage
        }