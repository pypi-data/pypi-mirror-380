"""
Admin API routes for system management and analytics.
"""

from flask import Blueprint, request, current_app
from datetime import datetime, timedelta
from sqlalchemy import func, and_, or_

from ...services.auth_service import AuthService
from ...services.billing_engine import BillingEngine
from ...services.usage_tracker import UsageTracker
from ...services.quota_manager import QuotaManager
from ...models.user import User, UserPlanEnum
from ...models.billing import Bill, Payment, BillStatusEnum, PaymentStatusEnum
from ...models.usage import UsageLog, BackendTypeEnum
from ...models.subscription import Subscription, Plan
from ...config import get_pricing_config
from ..main import get_db_session
from ..utils import (api_response, paginate_query, get_pagination_params,
                     parse_date_range, create_csv_response, validate_json)
from ..auth.routes import token_required


admin_bp = Blueprint('admin', __name__)


def admin_required(f):
    """Decorator to require admin privileges."""
    from functools import wraps

    @wraps(f)
    def decorated(current_user_id, *args, **kwargs):
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        has_access, reason = auth_service.check_user_access(
            current_user_id,
            admin_only=True
        )

        if not has_access:
            return api_response(None, reason, 403)

        return f(current_user_id, *args, **kwargs)

    return decorated


@admin_bp.route('/dashboard', methods=['GET'])
@token_required
@admin_required
def get_admin_dashboard(current_user_id):
    """Get admin dashboard overview."""
    try:
        db_session = get_db_session()

        # Calculate date ranges
        now = datetime.utcnow()
        thirty_days_ago = now - timedelta(days=30)
        seven_days_ago = now - timedelta(days=7)

        # User statistics
        total_users = db_session.query(User).count()
        active_users = db_session.query(User).filter_by(is_active=True).count()
        verified_users = db_session.query(User).filter_by(is_verified=True).count()

        new_users_30d = db_session.query(User).filter(
            User.created_at >= thirty_days_ago
        ).count()

        # Usage statistics
        total_usage_logs = db_session.query(UsageLog).count()
        successful_jobs = db_session.query(UsageLog).filter_by(success=True).count()

        usage_last_30d = db_session.query(UsageLog).filter(
            UsageLog.created_at >= thirty_days_ago
        ).count()

        total_shots = db_session.query(func.sum(UsageLog.shots_executed)).filter(
            UsageLog.success == True
        ).scalar() or 0

        # Billing statistics
        total_bills = db_session.query(Bill).count()
        paid_bills = db_session.query(Bill).filter_by(status=BillStatusEnum.PAID).count()

        total_revenue = db_session.query(func.sum(
            func.cast(Payment.amount, db_session.bind.dialect.NUMERIC)
        )).filter_by(status=PaymentStatusEnum.SUCCEEDED).scalar() or 0

        revenue_30d = db_session.query(func.sum(
            func.cast(Payment.amount, db_session.bind.dialect.NUMERIC)
        )).filter(
            and_(
                Payment.status == PaymentStatusEnum.SUCCEEDED,
                Payment.created_at >= thirty_days_ago
            )
        ).scalar() or 0

        # Subscription statistics
        active_subscriptions = db_session.query(Subscription).filter_by(
            status='active'
        ).count()

        # Plan distribution
        plan_distribution = db_session.query(
            User.current_plan,
            func.count(User.id)
        ).group_by(User.current_plan).all()

        plan_stats = {plan.value: count for plan, count in plan_distribution}

        # Backend usage statistics
        backend_usage = db_session.query(
            UsageLog.backend_used,
            func.count(UsageLog.id),
            func.sum(UsageLog.shots_executed)
        ).filter(
            and_(
                UsageLog.success == True,
                UsageLog.created_at >= thirty_days_ago
            )
        ).group_by(UsageLog.backend_used).all()

        backend_stats = {
            backend: {'jobs': jobs, 'shots': shots or 0}
            for backend, jobs, shots in backend_usage
        }

        # System health metrics
        recent_errors = db_session.query(UsageLog).filter(
            and_(
                UsageLog.success == False,
                UsageLog.created_at >= seven_days_ago
            )
        ).count()

        dashboard_data = {
            'overview': {
                'total_users': total_users,
                'active_users': active_users,
                'verified_users': verified_users,
                'new_users_30d': new_users_30d,
                'total_usage_jobs': total_usage_logs,
                'successful_jobs': successful_jobs,
                'usage_jobs_30d': usage_last_30d,
                'total_shots': int(total_shots),
                'total_bills': total_bills,
                'paid_bills': paid_bills,
                'total_revenue': float(total_revenue),
                'revenue_30d': float(revenue_30d),
                'active_subscriptions': active_subscriptions,
                'recent_errors': recent_errors
            },
            'plan_distribution': plan_stats,
            'backend_usage': backend_stats,
            'generated_at': now.isoformat()
        }

        return api_response(dashboard_data)

    except Exception as e:
        current_app.logger.error(f"Admin dashboard error: {str(e)}")
        return api_response(None, "Failed to retrieve dashboard data", 500)


@admin_bp.route('/users', methods=['GET'])
@token_required
@admin_required
def list_users(current_user_id):
    """List all users with pagination and filtering."""
    try:
        page, per_page = get_pagination_params()
        search = request.args.get('search', '').strip()
        plan = request.args.get('plan')
        status = request.args.get('status')

        db_session = get_db_session()
        query = db_session.query(User)

        # Apply filters
        if search:
            search_filter = or_(
                User.email.ilike(f'%{search}%'),
                User.username.ilike(f'%{search}%'),
                User.first_name.ilike(f'%{search}%'),
                User.last_name.ilike(f'%{search}%')
            )
            query = query.filter(search_filter)

        if plan:
            try:
                plan_enum = UserPlanEnum(plan)
                query = query.filter_by(current_plan=plan_enum)
            except ValueError:
                return api_response(None, f"Invalid plan: {plan}", 400)

        if status == 'active':
            query = query.filter_by(is_active=True)
        elif status == 'inactive':
            query = query.filter_by(is_active=False)
        elif status == 'verified':
            query = query.filter_by(is_verified=True)
        elif status == 'unverified':
            query = query.filter_by(is_verified=False)

        query = query.order_by(User.created_at.desc())
        result = paginate_query(query, page, per_page)

        # Add additional user stats to each user
        for user_dict in result['items']:
            user_id = user_dict['id']

            # Get usage stats
            usage_count = db_session.query(UsageLog).filter_by(
                user_id=user_id,
                success=True
            ).count()

            total_spent = db_session.query(func.sum(
                func.cast(Payment.amount, db_session.bind.dialect.NUMERIC)
            )).filter(
                and_(
                    Payment.user_id == user_id,
                    Payment.status == PaymentStatusEnum.SUCCEEDED
                )
            ).scalar() or 0

            user_dict['stats'] = {
                'total_jobs': usage_count,
                'total_spent': float(total_spent)
            }

        return api_response(result)

    except Exception as e:
        current_app.logger.error(f"Admin users listing error: {str(e)}")
        return api_response(None, "Failed to retrieve users", 500)


@admin_bp.route('/users/<user_id>', methods=['GET'])
@token_required
@admin_required
def get_user_details(current_user_id, user_id):
    """Get detailed information for a specific user."""
    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        user_stats = auth_service.get_user_stats(user_id)
        if not user_stats:
            return api_response(None, "User not found", 404)

        # Add admin-specific information
        user = db_session.query(User).filter_by(id=user_id).first()

        # Get recent usage
        recent_usage = db_session.query(UsageLog).filter_by(
            user_id=user_id
        ).order_by(UsageLog.created_at.desc()).limit(10).all()

        # Get subscription information
        subscriptions = db_session.query(Subscription).filter_by(
            user_id=user_id
        ).order_by(Subscription.created_at.desc()).all()

        # Get billing information
        bills = db_session.query(Bill).filter_by(
            user_id=user_id
        ).order_by(Bill.created_at.desc()).limit(5).all()

        admin_details = {
            'user_info': user_stats['user_info'],
            'account_status': user_stats['account_status'],
            'api_access': user_stats['api_access'],
            'recent_usage': [usage.to_dict() for usage in recent_usage],
            'subscriptions': [sub.to_dict() for sub in subscriptions],
            'recent_bills': [bill.to_dict() for bill in bills],
            'admin_notes': {
                'stripe_customer_id': user.stripe_customer_id,
                'last_login': user.last_login.isoformat() if user.last_login else None
            }
        }

        return api_response(admin_details)

    except Exception as e:
        current_app.logger.error(f"Admin user details error: {str(e)}")
        return api_response(None, "Failed to retrieve user details", 500)


@admin_bp.route('/users/<user_id>/deactivate', methods=['POST'])
@token_required
@admin_required
def deactivate_user(current_user_id, user_id):
    """Deactivate a user account."""
    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        success = auth_service.deactivate_user(user_id)

        if success:
            current_app.logger.info(f"Admin {current_user_id} deactivated user {user_id}")
            return api_response(None, "User deactivated successfully")
        else:
            return api_response(None, "User not found", 404)

    except Exception as e:
        current_app.logger.error(f"User deactivation error: {str(e)}")
        return api_response(None, "Failed to deactivate user", 500)


@admin_bp.route('/users/<user_id>/reactivate', methods=['POST'])
@token_required
@admin_required
def reactivate_user(current_user_id, user_id):
    """Reactivate a user account."""
    try:
        db_session = get_db_session()
        auth_service = AuthService(db_session)

        success = auth_service.reactivate_user(user_id)

        if success:
            current_app.logger.info(f"Admin {current_user_id} reactivated user {user_id}")
            return api_response(None, "User reactivated successfully")
        else:
            return api_response(None, "User not found", 404)

    except Exception as e:
        current_app.logger.error(f"User reactivation error: {str(e)}")
        return api_response(None, "Failed to reactivate user", 500)


@admin_bp.route('/billing/overview', methods=['GET'])
@token_required
@admin_required
def get_billing_overview(current_user_id):
    """Get system-wide billing overview."""
    try:
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        start_date, end_date = parse_date_range(start_date_str, end_date_str)

        db_session = get_db_session()

        # Revenue statistics
        total_revenue = db_session.query(func.sum(
            func.cast(Payment.amount, db_session.bind.dialect.NUMERIC)
        )).filter(
            and_(
                Payment.status == PaymentStatusEnum.SUCCEEDED,
                Payment.created_at >= start_date,
                Payment.created_at <= end_date
            )
        ).scalar() or 0

        # Bill statistics
        bill_stats = db_session.query(
            Bill.status,
            func.count(Bill.id),
            func.sum(func.cast(Bill.total_amount, db_session.bind.dialect.NUMERIC))
        ).filter(
            and_(
                Bill.created_at >= start_date,
                Bill.created_at <= end_date
            )
        ).group_by(Bill.status).all()

        bill_summary = {
            status.value: {'count': count, 'amount': float(amount or 0)}
            for status, count, amount in bill_stats
        }

        # Top customers by revenue
        top_customers = db_session.query(
            User.id,
            User.email,
            User.username,
            func.sum(func.cast(Payment.amount, db_session.bind.dialect.NUMERIC)).label('total_revenue')
        ).join(Payment).filter(
            and_(
                Payment.status == PaymentStatusEnum.SUCCEEDED,
                Payment.created_at >= start_date,
                Payment.created_at <= end_date
            )
        ).group_by(User.id, User.email, User.username).order_by(
            func.sum(func.cast(Payment.amount, db_session.bind.dialect.NUMERIC)).desc()
        ).limit(10).all()

        top_customers_data = [
            {
                'user_id': user_id,
                'email': email,
                'username': username,
                'total_revenue': float(revenue)
            }
            for user_id, email, username, revenue in top_customers
        ]

        billing_overview = {
            'period': {
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat()
            },
            'total_revenue': float(total_revenue),
            'bill_summary': bill_summary,
            'top_customers': top_customers_data
        }

        return api_response(billing_overview)

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Billing overview error: {str(e)}")
        return api_response(None, "Failed to retrieve billing overview", 500)


@admin_bp.route('/usage/analytics', methods=['GET'])
@token_required
@admin_required
def get_usage_analytics(current_user_id):
    """Get system-wide usage analytics."""
    try:
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        start_date, end_date = parse_date_range(start_date_str, end_date_str)

        db_session = get_db_session()
        pricing_config = get_pricing_config()
        usage_tracker = UsageTracker(db_session, pricing_config)

        # System-wide usage statistics
        backend_stats = usage_tracker.get_usage_by_backend(
            user_id=None,  # All users
            start_date=start_date,
            end_date=end_date
        )

        # Algorithm usage statistics
        algorithm_stats = db_session.query(
            UsageLog.algorithm_type,
            func.count(UsageLog.id),
            func.sum(UsageLog.shots_executed)
        ).filter(
            and_(
                UsageLog.success == True,
                UsageLog.created_at >= start_date,
                UsageLog.created_at <= end_date
            )
        ).group_by(UsageLog.algorithm_type).all()

        algorithm_summary = {
            algo.value: {'jobs': count, 'shots': shots or 0}
            for algo, count, shots in algorithm_stats
        }

        # Error analysis
        error_stats = db_session.query(
            func.count(UsageLog.id)
        ).filter(
            and_(
                UsageLog.success == False,
                UsageLog.created_at >= start_date,
                UsageLog.created_at <= end_date
            )
        ).scalar() or 0

        total_jobs = db_session.query(
            func.count(UsageLog.id)
        ).filter(
            and_(
                UsageLog.created_at >= start_date,
                UsageLog.created_at <= end_date
            )
        ).scalar() or 0

        success_rate = ((total_jobs - error_stats) / total_jobs * 100) if total_jobs > 0 else 100

        usage_analytics = {
            'period': {
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat()
            },
            'backend_statistics': backend_stats,
            'algorithm_statistics': algorithm_summary,
            'system_health': {
                'total_jobs': total_jobs,
                'successful_jobs': total_jobs - error_stats,
                'failed_jobs': error_stats,
                'success_rate': success_rate
            }
        }

        return api_response(usage_analytics)

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Usage analytics error: {str(e)}")
        return api_response(None, "Failed to retrieve usage analytics", 500)


@admin_bp.route('/reports/users', methods=['GET'])
@token_required
@admin_required
def export_users_report(current_user_id):
    """Export users report as CSV."""
    try:
        db_session = get_db_session()

        users = db_session.query(User).order_by(User.created_at.desc()).all()

        csv_data = []
        for user in users:
            # Get additional stats for each user
            usage_count = db_session.query(UsageLog).filter_by(
                user_id=user.id,
                success=True
            ).count()

            total_spent = db_session.query(func.sum(
                func.cast(Payment.amount, db_session.bind.dialect.NUMERIC)
            )).filter(
                and_(
                    Payment.user_id == user.id,
                    Payment.status == PaymentStatusEnum.SUCCEEDED
                )
            ).scalar() or 0

            csv_data.append({
                'user_id': user.id,
                'email': user.email,
                'username': user.username,
                'full_name': user.full_name,
                'organization': user.organization or '',
                'current_plan': user.current_plan.value,
                'is_active': user.is_active,
                'is_verified': user.is_verified,
                'is_admin': user.is_admin,
                'created_at': user.created_at.isoformat(),
                'last_login': user.last_login.isoformat() if user.last_login else '',
                'total_jobs': usage_count,
                'total_spent': float(total_spent)
            })

        from ..utils import generate_report_filename
        filename = generate_report_filename('users_report')

        return create_csv_response(csv_data, filename)

    except Exception as e:
        current_app.logger.error(f"Users report export error: {str(e)}")
        return api_response(None, "Failed to export users report", 500)


@admin_bp.route('/system/health', methods=['GET'])
@token_required
@admin_required
def get_system_health(current_user_id):
    """Get system health metrics."""
    try:
        db_session = get_db_session()

        # Calculate health metrics
        now = datetime.utcnow()
        last_hour = now - timedelta(hours=1)
        last_24h = now - timedelta(hours=24)

        # Recent activity
        recent_jobs = db_session.query(UsageLog).filter(
            UsageLog.created_at >= last_hour
        ).count()

        recent_errors = db_session.query(UsageLog).filter(
            and_(
                UsageLog.created_at >= last_hour,
                UsageLog.success == False
            )
        ).count()

        # Database metrics
        total_records = {
            'users': db_session.query(User).count(),
            'usage_logs': db_session.query(UsageLog).count(),
            'bills': db_session.query(Bill).count(),
            'payments': db_session.query(Payment).count()
        }

        # Error rate
        error_rate_24h = 0
        total_jobs_24h = db_session.query(UsageLog).filter(
            UsageLog.created_at >= last_24h
        ).count()

        if total_jobs_24h > 0:
            errors_24h = db_session.query(UsageLog).filter(
                and_(
                    UsageLog.created_at >= last_24h,
                    UsageLog.success == False
                )
            ).count()
            error_rate_24h = (errors_24h / total_jobs_24h) * 100

        health_metrics = {
            'timestamp': now.isoformat(),
            'status': 'healthy' if error_rate_24h < 5 else 'degraded' if error_rate_24h < 20 else 'unhealthy',
            'metrics': {
                'recent_activity': {
                    'jobs_last_hour': recent_jobs,
                    'errors_last_hour': recent_errors
                },
                'error_rates': {
                    'last_24h_percent': round(error_rate_24h, 2),
                    'total_jobs_24h': total_jobs_24h
                },
                'database': total_records
            }
        }

        return api_response(health_metrics)

    except Exception as e:
        current_app.logger.error(f"System health check error: {str(e)}")
        return api_response(None, "Failed to retrieve system health", 500)