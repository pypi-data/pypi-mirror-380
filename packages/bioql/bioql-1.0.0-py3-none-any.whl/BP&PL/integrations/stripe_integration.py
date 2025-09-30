"""
Stripe payment gateway integration for BioQL billing system.
"""

import stripe
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List
from sqlalchemy.orm import Session
from decimal import Decimal

from ..models.user import User
from ..models.billing import Bill, Payment, PaymentMethod, PaymentStatusEnum, PaymentMethodTypeEnum, BillStatusEnum
from ..models.subscription import Subscription, Plan, SubscriptionStatusEnum, BillingIntervalEnum


class StripeService:
    """
    Service for integrating with Stripe payment processing.
    """

    def __init__(self, db_session: Session, stripe_secret_key: str,
                 webhook_secret: str = None):
        """
        Initialize Stripe service.

        Args:
            db_session: Database session
            stripe_secret_key: Stripe secret API key
            webhook_secret: Stripe webhook endpoint secret
        """
        self.db_session = db_session
        self.webhook_secret = webhook_secret
        stripe.api_key = stripe_secret_key

    def create_customer(self, user: User) -> str:
        """
        Create a Stripe customer for a user.

        Args:
            user: User instance

        Returns:
            Stripe customer ID

        Raises:
            Exception: If customer creation fails
        """
        try:
            customer = stripe.Customer.create(
                email=user.email,
                name=user.full_name,
                description=f"BioQL Customer - {user.username}",
                metadata={
                    'user_id': user.id,
                    'username': user.username,
                    'bioql_customer': 'true'
                }
            )

            # Update user with Stripe customer ID
            user.stripe_customer_id = customer.id
            self.db_session.commit()

            return customer.id

        except stripe.error.StripeError as e:
            raise Exception(f"Failed to create Stripe customer: {str(e)}")

    def get_or_create_customer(self, user: User) -> str:
        """
        Get existing Stripe customer ID or create new customer.

        Args:
            user: User instance

        Returns:
            Stripe customer ID
        """
        if user.stripe_customer_id:
            try:
                # Verify customer still exists in Stripe
                stripe.Customer.retrieve(user.stripe_customer_id)
                return user.stripe_customer_id
            except stripe.error.StripeError:
                # Customer doesn't exist, create new one
                pass

        return self.create_customer(user)

    def create_payment_intent(self, user: User, amount: Decimal,
                            currency: str = 'USD', bill: Bill = None,
                            description: str = None) -> Dict[str, Any]:
        """
        Create a Stripe Payment Intent.

        Args:
            user: User making the payment
            amount: Payment amount
            currency: Currency code
            bill: Optional bill being paid
            description: Payment description

        Returns:
            Payment Intent details
        """
        try:
            customer_id = self.get_or_create_customer(user)

            # Convert amount to cents (Stripe uses smallest currency unit)
            amount_cents = int(amount * 100)

            metadata = {
                'user_id': user.id,
                'bioql_payment': 'true'
            }

            if bill:
                metadata['bill_id'] = bill.id
                metadata['bill_number'] = bill.bill_number

            payment_intent = stripe.PaymentIntent.create(
                amount=amount_cents,
                currency=currency.lower(),
                customer=customer_id,
                description=description or f"BioQL payment for {user.email}",
                metadata=metadata,
                automatic_payment_methods={'enabled': True}
            )

            # Create Payment record
            payment = Payment(
                bill_id=bill.id if bill else None,
                user_id=user.id,
                amount=str(amount),
                currency=currency.upper(),
                status=PaymentStatusEnum.PENDING,
                stripe_payment_intent_id=payment_intent.id
            )

            self.db_session.add(payment)

            # Update bill with payment intent ID
            if bill:
                bill.payment_intent_id = payment_intent.id

            self.db_session.commit()

            return {
                'payment_intent_id': payment_intent.id,
                'client_secret': payment_intent.client_secret,
                'payment_id': payment.id,
                'amount': amount,
                'currency': currency
            }

        except stripe.error.StripeError as e:
            raise Exception(f"Failed to create payment intent: {str(e)}")

    def confirm_payment(self, payment_intent_id: str) -> Dict[str, Any]:
        """
        Confirm payment and update records.

        Args:
            payment_intent_id: Stripe Payment Intent ID

        Returns:
            Payment confirmation details
        """
        try:
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

            # Find payment record
            payment = self.db_session.query(Payment).filter_by(
                stripe_payment_intent_id=payment_intent_id
            ).first()

            if not payment:
                raise Exception("Payment record not found")

            if payment_intent.status == 'succeeded':
                # Mark payment as succeeded
                payment.mark_succeeded(
                    stripe_charge_id=payment_intent.latest_charge,
                    processor_fee=str(Decimal(payment_intent.latest_charge.fee if payment_intent.latest_charge else 0) / 100)
                )

                # Mark bill as paid if associated
                if payment.bill:
                    payment.bill.mark_paid(payment)

                self.db_session.commit()

                return {
                    'status': 'succeeded',
                    'payment_id': payment.id,
                    'amount': payment.amount_float,
                    'currency': payment.currency
                }

            elif payment_intent.status == 'payment_failed':
                failure_reason = payment_intent.last_payment_error.message if payment_intent.last_payment_error else "Payment failed"
                payment.mark_failed(reason=failure_reason)
                self.db_session.commit()

                return {
                    'status': 'failed',
                    'payment_id': payment.id,
                    'error': failure_reason
                }

            else:
                return {
                    'status': payment_intent.status,
                    'payment_id': payment.id
                }

        except stripe.error.StripeError as e:
            raise Exception(f"Failed to confirm payment: {str(e)}")

    def create_subscription(self, user: User, plan: Plan,
                          billing_interval: BillingIntervalEnum,
                          payment_method_id: str = None) -> Dict[str, Any]:
        """
        Create a Stripe subscription.

        Args:
            user: User subscribing
            plan: Subscription plan
            billing_interval: Billing interval
            payment_method_id: Stripe payment method ID

        Returns:
            Subscription creation details
        """
        try:
            customer_id = self.get_or_create_customer(user)

            # Get Stripe price ID for the plan and interval
            stripe_price_id = plan.get_stripe_price_id(billing_interval)
            if not stripe_price_id:
                raise Exception(f"No Stripe price configured for plan {plan.name} ({billing_interval.value})")

            subscription_params = {
                'customer': customer_id,
                'items': [{'price': stripe_price_id}],
                'metadata': {
                    'user_id': user.id,
                    'plan_id': plan.id,
                    'billing_interval': billing_interval.value,
                    'bioql_subscription': 'true'
                }
            }

            if payment_method_id:
                subscription_params['default_payment_method'] = payment_method_id

            stripe_subscription = stripe.Subscription.create(**subscription_params)

            # Create Subscription record
            subscription = Subscription(
                user_id=user.id,
                plan_id=plan.id,
                status=SubscriptionStatusEnum.ACTIVE,
                billing_interval=billing_interval,
                current_period_start=datetime.fromtimestamp(stripe_subscription.current_period_start),
                current_period_end=datetime.fromtimestamp(stripe_subscription.current_period_end),
                price=plan.price_monthly if billing_interval == BillingIntervalEnum.MONTHLY else plan.price_yearly,
                stripe_subscription_id=stripe_subscription.id,
                stripe_customer_id=customer_id
            )

            self.db_session.add(subscription)

            # Update user's current plan
            user.current_plan = plan.plan_type

            self.db_session.commit()

            return {
                'subscription_id': subscription.id,
                'stripe_subscription_id': stripe_subscription.id,
                'status': stripe_subscription.status,
                'current_period_end': subscription.current_period_end.isoformat()
            }

        except stripe.error.StripeError as e:
            raise Exception(f"Failed to create subscription: {str(e)}")

    def cancel_subscription(self, subscription: Subscription,
                          at_period_end: bool = True) -> Dict[str, Any]:
        """
        Cancel a Stripe subscription.

        Args:
            subscription: Subscription to cancel
            at_period_end: Whether to cancel at period end

        Returns:
            Cancellation details
        """
        try:
            if at_period_end:
                stripe_subscription = stripe.Subscription.modify(
                    subscription.stripe_subscription_id,
                    cancel_at_period_end=True
                )
            else:
                stripe_subscription = stripe.Subscription.delete(
                    subscription.stripe_subscription_id
                )

            # Update subscription record
            subscription.cancel(at_period_end=at_period_end)
            self.db_session.commit()

            return {
                'subscription_id': subscription.id,
                'status': 'cancelled',
                'at_period_end': at_period_end,
                'ends_at': subscription.current_period_end.isoformat() if at_period_end else datetime.utcnow().isoformat()
            }

        except stripe.error.StripeError as e:
            raise Exception(f"Failed to cancel subscription: {str(e)}")

    def add_payment_method(self, user: User, payment_method_id: str) -> PaymentMethod:
        """
        Add a payment method for a user.

        Args:
            user: User adding payment method
            payment_method_id: Stripe payment method ID

        Returns:
            PaymentMethod instance
        """
        try:
            customer_id = self.get_or_create_customer(user)

            # Attach payment method to customer
            stripe.PaymentMethod.attach(
                payment_method_id,
                customer=customer_id
            )

            # Retrieve payment method details
            stripe_pm = stripe.PaymentMethod.retrieve(payment_method_id)

            # Create PaymentMethod record
            payment_method = PaymentMethod(
                user_id=user.id,
                type=PaymentMethodTypeEnum.CREDIT_CARD,  # Default to credit card
                stripe_payment_method_id=payment_method_id,
                is_active=True
            )

            # Extract card details if available
            if stripe_pm.card:
                payment_method.card_brand = stripe_pm.card.brand
                payment_method.card_last4 = stripe_pm.card.last4
                payment_method.card_exp_month = stripe_pm.card.exp_month
                payment_method.card_exp_year = stripe_pm.card.exp_year

            self.db_session.add(payment_method)
            self.db_session.commit()

            return payment_method

        except stripe.error.StripeError as e:
            raise Exception(f"Failed to add payment method: {str(e)}")

    def remove_payment_method(self, payment_method: PaymentMethod) -> bool:
        """
        Remove a payment method.

        Args:
            payment_method: PaymentMethod to remove

        Returns:
            True if successful
        """
        try:
            if payment_method.stripe_payment_method_id:
                stripe.PaymentMethod.detach(payment_method.stripe_payment_method_id)

            payment_method.is_active = False
            self.db_session.commit()

            return True

        except stripe.error.StripeError as e:
            raise Exception(f"Failed to remove payment method: {str(e)}")

    def sync_subscription_status(self, subscription: Subscription) -> Dict[str, Any]:
        """
        Sync subscription status with Stripe.

        Args:
            subscription: Subscription to sync

        Returns:
            Sync results
        """
        try:
            stripe_subscription = stripe.Subscription.retrieve(
                subscription.stripe_subscription_id
            )

            # Update subscription status
            status_mapping = {
                'active': SubscriptionStatusEnum.ACTIVE,
                'past_due': SubscriptionStatusEnum.PAST_DUE,
                'canceled': SubscriptionStatusEnum.CANCELLED,
                'unpaid': SubscriptionStatusEnum.UNPAID,
                'trialing': SubscriptionStatusEnum.TRIALING,
                'incomplete': SubscriptionStatusEnum.INCOMPLETE
            }

            new_status = status_mapping.get(stripe_subscription.status, SubscriptionStatusEnum.ACTIVE)

            if new_status != subscription.status:
                subscription.status = new_status

            # Update period dates
            subscription.current_period_start = datetime.fromtimestamp(
                stripe_subscription.current_period_start
            )
            subscription.current_period_end = datetime.fromtimestamp(
                stripe_subscription.current_period_end
            )

            # Update cancellation status
            if stripe_subscription.cancel_at_period_end:
                subscription.cancel_at_period_end = True

            self.db_session.commit()

            return {
                'subscription_id': subscription.id,
                'status': subscription.status.value,
                'synced': True
            }

        except stripe.error.StripeError as e:
            raise Exception(f"Failed to sync subscription: {str(e)}")

    def handle_webhook(self, payload: str, sig_header: str) -> Dict[str, Any]:
        """
        Handle Stripe webhook events.

        Args:
            payload: Webhook payload
            sig_header: Stripe signature header

        Returns:
            Event handling results
        """
        if not self.webhook_secret:
            raise Exception("Webhook secret not configured")

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, self.webhook_secret
            )

            event_type = event['type']
            event_data = event['data']['object']

            if event_type == 'payment_intent.succeeded':
                return self._handle_payment_succeeded(event_data)
            elif event_type == 'payment_intent.payment_failed':
                return self._handle_payment_failed(event_data)
            elif event_type == 'invoice.payment_succeeded':
                return self._handle_invoice_payment_succeeded(event_data)
            elif event_type == 'customer.subscription.updated':
                return self._handle_subscription_updated(event_data)
            elif event_type == 'customer.subscription.deleted':
                return self._handle_subscription_deleted(event_data)
            else:
                return {'status': 'ignored', 'event_type': event_type}

        except ValueError:
            raise Exception("Invalid payload")
        except stripe.error.SignatureVerificationError:
            raise Exception("Invalid signature")

    def _handle_payment_succeeded(self, payment_intent) -> Dict[str, Any]:
        """Handle successful payment webhook."""
        payment = self.db_session.query(Payment).filter_by(
            stripe_payment_intent_id=payment_intent['id']
        ).first()

        if payment:
            payment.mark_succeeded(
                stripe_charge_id=payment_intent.get('latest_charge'),
                processor_fee=str(Decimal(payment_intent.get('fee', 0)) / 100)
            )

            if payment.bill:
                payment.bill.mark_paid(payment)

            self.db_session.commit()

        return {'status': 'processed', 'payment_id': payment.id if payment else None}

    def _handle_payment_failed(self, payment_intent) -> Dict[str, Any]:
        """Handle failed payment webhook."""
        payment = self.db_session.query(Payment).filter_by(
            stripe_payment_intent_id=payment_intent['id']
        ).first()

        if payment:
            error_message = payment_intent.get('last_payment_error', {}).get('message', 'Payment failed')
            payment.mark_failed(reason=error_message)
            self.db_session.commit()

        return {'status': 'processed', 'payment_id': payment.id if payment else None}

    def _handle_invoice_payment_succeeded(self, invoice) -> Dict[str, Any]:
        """Handle successful invoice payment webhook."""
        subscription_id = invoice.get('subscription')
        if not subscription_id:
            return {'status': 'ignored', 'reason': 'No subscription ID'}

        subscription = self.db_session.query(Subscription).filter_by(
            stripe_subscription_id=subscription_id
        ).first()

        if subscription:
            # Renew subscription period if this is a recurring payment
            if invoice.get('billing_reason') == 'subscription_cycle':
                subscription.renew_period()
                self.db_session.commit()

        return {'status': 'processed', 'subscription_id': subscription.id if subscription else None}

    def _handle_subscription_updated(self, subscription_data) -> Dict[str, Any]:
        """Handle subscription update webhook."""
        subscription = self.db_session.query(Subscription).filter_by(
            stripe_subscription_id=subscription_data['id']
        ).first()

        if subscription:
            self.sync_subscription_status(subscription)

        return {'status': 'processed', 'subscription_id': subscription.id if subscription else None}

    def _handle_subscription_deleted(self, subscription_data) -> Dict[str, Any]:
        """Handle subscription deletion webhook."""
        subscription = self.db_session.query(Subscription).filter_by(
            stripe_subscription_id=subscription_data['id']
        ).first()

        if subscription:
            subscription.status = SubscriptionStatusEnum.CANCELLED
            subscription.ended_at = datetime.utcnow()
            self.db_session.commit()

        return {'status': 'processed', 'subscription_id': subscription.id if subscription else None}

    def get_usage_charges(self, subscription: Subscription) -> List[Dict[str, Any]]:
        """
        Get usage-based charges for a subscription billing period.

        Args:
            subscription: Subscription to get charges for

        Returns:
            List of usage charges
        """
        from ..models.usage import UsageLog

        # Get unbilled usage for the current period
        usage_logs = self.db_session.query(UsageLog).filter(
            and_(
                UsageLog.user_id == subscription.user_id,
                UsageLog.billed == False,
                UsageLog.success == True,
                UsageLog.created_at >= subscription.current_period_start,
                UsageLog.created_at < subscription.current_period_end
            )
        ).all()

        charges = []
        for log in usage_logs:
            if log.cost_float > 0:
                charges.append({
                    'description': f"Quantum computation - {log.shots_executed} shots",
                    'amount': log.cost_float,
                    'quantity': 1,
                    'usage_log_id': log.id
                })

        return charges

    def create_usage_invoice(self, subscription: Subscription) -> Optional[str]:
        """
        Create a Stripe invoice for usage charges.

        Args:
            subscription: Subscription to invoice

        Returns:
            Stripe invoice ID if created
        """
        charges = self.get_usage_charges(subscription)

        if not charges:
            return None

        try:
            # Create invoice items for each charge
            for charge in charges:
                stripe.InvoiceItem.create(
                    customer=subscription.stripe_customer_id,
                    amount=int(charge['amount'] * 100),  # Convert to cents
                    currency='usd',
                    description=charge['description'],
                    metadata={
                        'usage_log_id': charge['usage_log_id'],
                        'subscription_id': subscription.id
                    }
                )

            # Create and finalize invoice
            invoice = stripe.Invoice.create(
                customer=subscription.stripe_customer_id,
                auto_advance=True,  # Automatically finalize
                metadata={
                    'subscription_id': subscription.id,
                    'billing_period_start': subscription.current_period_start.isoformat(),
                    'billing_period_end': subscription.current_period_end.isoformat()
                }
            )

            return invoice.id

        except stripe.error.StripeError as e:
            raise Exception(f"Failed to create usage invoice: {str(e)}")