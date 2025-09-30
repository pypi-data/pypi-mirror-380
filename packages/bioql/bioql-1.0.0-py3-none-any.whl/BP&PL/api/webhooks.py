"""
Webhook endpoints for external service integrations.
"""

from flask import Blueprint, request, current_app
import hmac
import hashlib

from ..integrations.stripe_integration import StripeService
from ..config import get_stripe_config
from .main import get_db_session
from .utils import api_response


webhooks_bp = Blueprint('webhooks', __name__)


@webhooks_bp.route('/stripe', methods=['POST'])
def stripe_webhook():
    """Handle Stripe webhook events."""
    try:
        payload = request.data
        sig_header = request.headers.get('Stripe-Signature')

        if not sig_header:
            current_app.logger.warning("Stripe webhook received without signature")
            return api_response(None, "Missing signature", 400)

        # Get Stripe configuration
        stripe_config = get_stripe_config()
        if not stripe_config['enabled']:
            return api_response(None, "Stripe integration not enabled", 503)

        # Initialize Stripe service
        db_session = get_db_session()
        stripe_service = StripeService(
            db_session,
            stripe_config['secret_key'],
            stripe_config['webhook_secret']
        )

        # Handle webhook
        result = stripe_service.handle_webhook(payload.decode('utf-8'), sig_header)

        current_app.logger.info(f"Stripe webhook processed: {result}")
        return api_response(result)

    except Exception as e:
        current_app.logger.error(f"Stripe webhook error: {str(e)}")
        return api_response(None, f"Webhook processing failed: {str(e)}", 400)


@webhooks_bp.route('/internal', methods=['POST'])
def internal_webhook():
    """Handle internal webhook events."""
    try:
        # Verify internal webhook signature
        payload = request.data
        sig_header = request.headers.get('X-Webhook-Signature')

        if not sig_header:
            return api_response(None, "Missing signature", 400)

        # Get webhook secret from config
        from ..config import get_api_config
        api_config = get_api_config()
        webhook_secret = api_config.get('webhooks', {}).get('internal', {}).get('secret_key')

        if not webhook_secret:
            return api_response(None, "Webhook not configured", 503)

        # Verify signature
        expected_signature = hmac.new(
            webhook_secret.encode('utf-8'),
            payload,
            hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(f"sha256={expected_signature}", sig_header):
            current_app.logger.warning("Invalid internal webhook signature")
            return api_response(None, "Invalid signature", 401)

        # Process webhook event
        event_data = request.get_json()
        event_type = event_data.get('type')

        if event_type == 'user.plan_changed':
            result = handle_plan_change_webhook(event_data)
        elif event_type == 'billing.monthly_cycle':
            result = handle_monthly_billing_webhook(event_data)
        elif event_type == 'quota.limit_exceeded':
            result = handle_quota_exceeded_webhook(event_data)
        else:
            result = {'status': 'ignored', 'event_type': event_type}

        current_app.logger.info(f"Internal webhook processed: {result}")
        return api_response(result)

    except Exception as e:
        current_app.logger.error(f"Internal webhook error: {str(e)}")
        return api_response(None, f"Webhook processing failed: {str(e)}", 400)


def handle_plan_change_webhook(event_data):
    """Handle user plan change webhook."""
    try:
        user_id = event_data.get('user_id')
        old_plan = event_data.get('old_plan')
        new_plan = event_data.get('new_plan')

        current_app.logger.info(f"User {user_id} plan changed from {old_plan} to {new_plan}")

        # Update user quotas based on new plan
        db_session = get_db_session()
        from ..services.quota_manager import QuotaManager

        quota_manager = QuotaManager(db_session)

        # Here you could implement plan-specific quota updates
        # For now, just log the event

        return {
            'status': 'processed',
            'event_type': 'user.plan_changed',
            'user_id': user_id
        }

    except Exception as e:
        current_app.logger.error(f"Plan change webhook error: {str(e)}")
        raise


def handle_monthly_billing_webhook(event_data):
    """Handle monthly billing cycle webhook."""
    try:
        billing_date = event_data.get('billing_date')
        user_id = event_data.get('user_id')  # Optional, if for specific user

        current_app.logger.info(f"Processing monthly billing for date: {billing_date}")

        # Process monthly billing
        db_session = get_db_session()
        from ..services.billing_engine import BillingEngine
        from ..config import get_pricing_config

        pricing_config = get_pricing_config()
        billing_engine = BillingEngine(db_session, pricing_config)

        result = billing_engine.process_monthly_billing(user_id)

        return {
            'status': 'processed',
            'event_type': 'billing.monthly_cycle',
            'billing_result': result
        }

    except Exception as e:
        current_app.logger.error(f"Monthly billing webhook error: {str(e)}")
        raise


def handle_quota_exceeded_webhook(event_data):
    """Handle quota limit exceeded webhook."""
    try:
        user_id = event_data.get('user_id')
        quota_type = event_data.get('quota_type')
        current_usage = event_data.get('current_usage')
        limit = event_data.get('limit')

        current_app.logger.warning(
            f"Quota exceeded for user {user_id}: {quota_type} "
            f"({current_usage}/{limit})"
        )

        # Here you could implement notifications, service limitations, etc.
        # For now, just log the event

        return {
            'status': 'processed',
            'event_type': 'quota.limit_exceeded',
            'user_id': user_id,
            'quota_type': quota_type
        }

    except Exception as e:
        current_app.logger.error(f"Quota exceeded webhook error: {str(e)}")
        raise


@webhooks_bp.route('/test', methods=['POST'])
def test_webhook():
    """Test webhook endpoint for development and testing."""
    try:
        event_data = request.get_json()

        current_app.logger.info(f"Test webhook received: {event_data}")

        return api_response({
            'received_data': event_data,
            'timestamp': event_data.get('timestamp'),
            'event_type': event_data.get('type', 'unknown')
        }, "Test webhook received successfully")

    except Exception as e:
        current_app.logger.error(f"Test webhook error: {str(e)}")
        return api_response(None, f"Test webhook failed: {str(e)}", 400)