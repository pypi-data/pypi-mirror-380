"""
Billing API routes for invoices, payments, and subscriptions.
"""

from flask import Blueprint, request, jsonify, current_app
from datetime import datetime

from ...services.billing_engine import BillingEngine
from ...services.auth_service import AuthService
from ...integrations.stripe_integration import StripeService
from ...models.billing import Bill, Payment, BillStatusEnum
from ...models.subscription import Subscription, Plan, SubscriptionStatusEnum
from ...config import get_pricing_config, get_stripe_config
from ..main import get_db_session
from ..utils import api_response, validate_json, paginate_query, get_pagination_params, parse_date_range
from ..auth.routes import token_required, api_key_required


billing_bp = Blueprint('billing', __name__)


@billing_bp.route('/summary', methods=['GET'])
@token_required
def get_billing_summary(current_user_id):
    """Get billing summary for the current user."""
    try:
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        start_date, end_date = parse_date_range(start_date_str, end_date_str)

        db_session = get_db_session()
        pricing_config = get_pricing_config()
        billing_engine = BillingEngine(db_session, pricing_config)

        summary = billing_engine.get_billing_summary(current_user_id, start_date, end_date)

        return api_response(summary)

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Billing summary error: {str(e)}")
        return api_response(None, "Failed to retrieve billing summary", 500)


@billing_bp.route('/bills', methods=['GET'])
@token_required
def list_bills(current_user_id):
    """List bills for the current user."""
    try:
        page, per_page = get_pagination_params()
        status = request.args.get('status')

        db_session = get_db_session()
        query = db_session.query(Bill).filter_by(user_id=current_user_id)

        if status:
            try:
                status_enum = BillStatusEnum(status)
                query = query.filter_by(status=status_enum)
            except ValueError:
                return api_response(None, f"Invalid status: {status}", 400)

        query = query.order_by(Bill.created_at.desc())
        result = paginate_query(query, page, per_page)

        return api_response(result)

    except Exception as e:
        current_app.logger.error(f"Bills listing error: {str(e)}")
        return api_response(None, "Failed to retrieve bills", 500)


@billing_bp.route('/bills/<bill_id>', methods=['GET'])
@token_required
def get_bill_details(current_user_id, bill_id):
    """Get detailed information for a specific bill."""
    try:
        db_session = get_db_session()
        bill = db_session.query(Bill).filter_by(id=bill_id, user_id=current_user_id).first()

        if not bill:
            return api_response(None, "Bill not found", 404)

        bill_data = bill.to_dict()
        bill_data['bill_items'] = [item.to_dict() for item in bill.bill_items]
        bill_data['payments'] = [payment.to_dict() for payment in bill.payments]

        return api_response(bill_data)

    except Exception as e:
        current_app.logger.error(f"Bill details error: {str(e)}")
        return api_response(None, "Failed to retrieve bill details", 500)


@billing_bp.route('/bills/<bill_id>/pay', methods=['POST'])
@token_required
def create_payment_intent(current_user_id, bill_id):
    """Create a payment intent for a bill."""
    try:
        db_session = get_db_session()
        bill = db_session.query(Bill).filter_by(id=bill_id, user_id=current_user_id).first()

        if not bill:
            return api_response(None, "Bill not found", 404)

        if bill.status != BillStatusEnum.PENDING:
            return api_response(None, "Bill is not payable", 400)

        # Get user
        auth_service = AuthService(db_session)
        user = db_session.query(User).filter_by(id=current_user_id).first()

        # Create Stripe payment intent
        stripe_config = get_stripe_config()
        if not stripe_config['enabled']:
            return api_response(None, "Payment processing not available", 503)

        stripe_service = StripeService(db_session, stripe_config['secret_key'], stripe_config['webhook_secret'])

        payment_intent = stripe_service.create_payment_intent(
            user=user,
            amount=bill.total_float,
            bill=bill,
            description=f"Payment for bill {bill.bill_number}"
        )

        return api_response(payment_intent)

    except Exception as e:
        current_app.logger.error(f"Payment intent creation error: {str(e)}")
        return api_response(None, "Failed to create payment intent", 500)


@billing_bp.route('/payments', methods=['GET'])
@token_required
def list_payments(current_user_id):
    """List payments for the current user."""
    try:
        page, per_page = get_pagination_params()

        db_session = get_db_session()
        query = db_session.query(Payment).filter_by(user_id=current_user_id)
        query = query.order_by(Payment.created_at.desc())

        result = paginate_query(query, page, per_page)

        return api_response(result)

    except Exception as e:
        current_app.logger.error(f"Payments listing error: {str(e)}")
        return api_response(None, "Failed to retrieve payments", 500)


@billing_bp.route('/payments/<payment_id>', methods=['GET'])
@token_required
def get_payment_details(current_user_id, payment_id):
    """Get detailed information for a specific payment."""
    try:
        db_session = get_db_session()
        payment = db_session.query(Payment).filter_by(id=payment_id, user_id=current_user_id).first()

        if not payment:
            return api_response(None, "Payment not found", 404)

        payment_data = payment.to_dict()

        # Include bill information if available
        if payment.bill:
            payment_data['bill'] = {
                'id': payment.bill.id,
                'bill_number': payment.bill.bill_number,
                'total_amount': payment.bill.total_amount
            }

        return api_response(payment_data)

    except Exception as e:
        current_app.logger.error(f"Payment details error: {str(e)}")
        return api_response(None, "Failed to retrieve payment details", 500)


@billing_bp.route('/subscriptions', methods=['GET'])
@token_required
def list_subscriptions(current_user_id):
    """List subscriptions for the current user."""
    try:
        db_session = get_db_session()
        subscriptions = db_session.query(Subscription).filter_by(user_id=current_user_id).all()

        subscription_data = []
        for sub in subscriptions:
            sub_dict = sub.to_dict()
            sub_dict['plan'] = sub.plan.to_dict() if sub.plan else None
            subscription_data.append(sub_dict)

        return api_response({
            'subscriptions': subscription_data,
            'total': len(subscription_data)
        })

    except Exception as e:
        current_app.logger.error(f"Subscriptions listing error: {str(e)}")
        return api_response(None, "Failed to retrieve subscriptions", 500)


@billing_bp.route('/subscriptions', methods=['POST'])
@token_required
@validate_json(['plan_id', 'billing_interval'])
def create_subscription(current_user_id):
    """Create a new subscription."""
    data = request.get_json()

    try:
        db_session = get_db_session()

        # Get plan
        plan = db_session.query(Plan).filter_by(id=data['plan_id']).first()
        if not plan:
            return api_response(None, "Plan not found", 404)

        # Get user
        from ...models.user import User
        user = db_session.query(User).filter_by(id=current_user_id).first()

        # Validate billing interval
        from ...models.subscription import BillingIntervalEnum
        try:
            billing_interval = BillingIntervalEnum(data['billing_interval'])
        except ValueError:
            return api_response(None, "Invalid billing interval", 400)

        # Create Stripe subscription
        stripe_config = get_stripe_config()
        if not stripe_config['enabled']:
            return api_response(None, "Subscription service not available", 503)

        stripe_service = StripeService(db_session, stripe_config['secret_key'], stripe_config['webhook_secret'])

        subscription_result = stripe_service.create_subscription(
            user=user,
            plan=plan,
            billing_interval=billing_interval,
            payment_method_id=data.get('payment_method_id')
        )

        return api_response(subscription_result)

    except Exception as e:
        current_app.logger.error(f"Subscription creation error: {str(e)}")
        return api_response(None, "Failed to create subscription", 500)


@billing_bp.route('/subscriptions/<subscription_id>/cancel', methods=['POST'])
@token_required
def cancel_subscription(current_user_id, subscription_id):
    """Cancel a subscription."""
    try:
        at_period_end = request.get_json().get('at_period_end', True) if request.is_json else True

        db_session = get_db_session()
        subscription = db_session.query(Subscription).filter_by(
            id=subscription_id,
            user_id=current_user_id
        ).first()

        if not subscription:
            return api_response(None, "Subscription not found", 404)

        if subscription.status != SubscriptionStatusEnum.ACTIVE:
            return api_response(None, "Subscription is not active", 400)

        # Cancel in Stripe
        stripe_config = get_stripe_config()
        if stripe_config['enabled']:
            stripe_service = StripeService(db_session, stripe_config['secret_key'], stripe_config['webhook_secret'])
            result = stripe_service.cancel_subscription(subscription, at_period_end)
        else:
            # Cancel locally only
            subscription.cancel(at_period_end)
            db_session.commit()
            result = {
                'subscription_id': subscription.id,
                'status': 'cancelled',
                'at_period_end': at_period_end
            }

        return api_response(result)

    except Exception as e:
        current_app.logger.error(f"Subscription cancellation error: {str(e)}")
        return api_response(None, "Failed to cancel subscription", 500)


@billing_bp.route('/plans', methods=['GET'])
def list_plans():
    """List available subscription plans."""
    try:
        db_session = get_db_session()
        plans = db_session.query(Plan).filter_by(is_active=True, is_public=True).order_by(Plan.sort_order).all()

        plan_data = []
        for plan in plans:
            plan_dict = plan.to_dict()
            plan_dict['features'] = [feature.to_dict() for feature in plan.features]
            plan_data.append(plan_dict)

        return api_response({
            'plans': plan_data,
            'total': len(plan_data)
        })

    except Exception as e:
        current_app.logger.error(f"Plans listing error: {str(e)}")
        return api_response(None, "Failed to retrieve plans", 500)


@billing_bp.route('/plans/<plan_id>', methods=['GET'])
def get_plan_details(plan_id):
    """Get detailed information for a specific plan."""
    try:
        db_session = get_db_session()
        plan = db_session.query(Plan).filter_by(id=plan_id, is_active=True).first()

        if not plan:
            return api_response(None, "Plan not found", 404)

        plan_data = plan.to_dict()
        plan_data['features'] = [feature.to_dict() for feature in plan.features]

        return api_response(plan_data)

    except Exception as e:
        current_app.logger.error(f"Plan details error: {str(e)}")
        return api_response(None, "Failed to retrieve plan details", 500)


@billing_bp.route('/cost-estimate', methods=['POST'])
@token_required
@validate_json(['backend_type', 'shots', 'qubits'])
def estimate_cost(current_user_id):
    """Estimate cost for a quantum computation."""
    data = request.get_json()

    try:
        db_session = get_db_session()
        pricing_config = get_pricing_config()
        billing_engine = BillingEngine(db_session, pricing_config)

        # Parse backend type
        from ...models.usage import BackendTypeEnum, AlgorithmTypeEnum
        try:
            backend_type = BackendTypeEnum(data['backend_type'])
        except ValueError:
            return api_response(None, "Invalid backend type", 400)

        # Parse algorithm type
        algorithm_type_str = data.get('algorithm_type', 'basic')
        try:
            algorithm_type = AlgorithmTypeEnum(algorithm_type_str)
        except ValueError:
            algorithm_type = AlgorithmTypeEnum.BASIC

        cost_breakdown = billing_engine.calculate_shot_cost(
            backend_type=backend_type,
            shots=data['shots'],
            qubits=data['qubits'],
            algorithm_type=algorithm_type
        )

        return api_response(cost_breakdown)

    except Exception as e:
        current_app.logger.error(f"Cost estimation error: {str(e)}")
        return api_response(None, "Failed to estimate cost", 500)


@billing_bp.route('/monthly-estimate', methods=['GET'])
@token_required
def get_monthly_estimate(current_user_id):
    """Get estimated monthly cost based on usage patterns."""
    try:
        db_session = get_db_session()
        pricing_config = get_pricing_config()
        billing_engine = BillingEngine(db_session, pricing_config)

        estimate = billing_engine.estimate_monthly_cost(current_user_id)

        return api_response(estimate)

    except Exception as e:
        current_app.logger.error(f"Monthly estimate error: {str(e)}")
        return api_response(None, "Failed to get monthly estimate", 500)


@billing_bp.route('/payment-methods', methods=['GET'])
@token_required
def list_payment_methods(current_user_id):
    """List payment methods for the current user."""
    try:
        db_session = get_db_session()
        from ...models.billing import PaymentMethod

        payment_methods = db_session.query(PaymentMethod).filter_by(
            user_id=current_user_id,
            is_active=True
        ).all()

        method_data = []
        for method in payment_methods:
            method_dict = method.to_dict()
            method_dict['display_name'] = method.display_name
            method_dict['is_expired'] = method.is_expired
            method_data.append(method_dict)

        return api_response({
            'payment_methods': method_data,
            'total': len(method_data)
        })

    except Exception as e:
        current_app.logger.error(f"Payment methods listing error: {str(e)}")
        return api_response(None, "Failed to retrieve payment methods", 500)


@billing_bp.route('/payment-methods', methods=['POST'])
@token_required
@validate_json(['payment_method_id'])
def add_payment_method(current_user_id):
    """Add a new payment method."""
    data = request.get_json()

    try:
        db_session = get_db_session()

        # Get user
        from ...models.user import User
        user = db_session.query(User).filter_by(id=current_user_id).first()

        # Add payment method via Stripe
        stripe_config = get_stripe_config()
        if not stripe_config['enabled']:
            return api_response(None, "Payment service not available", 503)

        stripe_service = StripeService(db_session, stripe_config['secret_key'], stripe_config['webhook_secret'])

        payment_method = stripe_service.add_payment_method(
            user=user,
            payment_method_id=data['payment_method_id']
        )

        payment_method_dict = payment_method.to_dict()
        payment_method_dict['display_name'] = payment_method.display_name

        return api_response(payment_method_dict)

    except Exception as e:
        current_app.logger.error(f"Payment method addition error: {str(e)}")
        return api_response(None, "Failed to add payment method", 500)


@billing_bp.route('/payment-methods/<method_id>', methods=['DELETE'])
@token_required
def remove_payment_method(current_user_id, method_id):
    """Remove a payment method."""
    try:
        db_session = get_db_session()
        from ...models.billing import PaymentMethod

        payment_method = db_session.query(PaymentMethod).filter_by(
            id=method_id,
            user_id=current_user_id
        ).first()

        if not payment_method:
            return api_response(None, "Payment method not found", 404)

        # Remove payment method via Stripe
        stripe_config = get_stripe_config()
        if stripe_config['enabled']:
            stripe_service = StripeService(db_session, stripe_config['secret_key'], stripe_config['webhook_secret'])
            success = stripe_service.remove_payment_method(payment_method)
        else:
            payment_method.is_active = False
            db_session.commit()
            success = True

        if success:
            return api_response(None, "Payment method removed successfully")
        else:
            return api_response(None, "Failed to remove payment method", 500)

    except Exception as e:
        current_app.logger.error(f"Payment method removal error: {str(e)}")
        return api_response(None, "Failed to remove payment method", 500)