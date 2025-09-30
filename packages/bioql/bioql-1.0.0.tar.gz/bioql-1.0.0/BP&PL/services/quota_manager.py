"""
Quota and rate limiting management service.
"""

from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, func

from ..models.quota import Quota, QuotaUsage, QuotaTypeEnum
from ..models.user import User, APIKey
from ..models.subscription import Subscription, SubscriptionStatusEnum


class QuotaManager:
    """
    Service for managing user quotas and rate limiting.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_quota(self, name: str, quota_type: QuotaTypeEnum,
                    limit_value: int, period_seconds: int,
                    user_id: str = None, plan_id: str = None,
                    api_key_id: str = None, is_hard_limit: bool = True) -> Quota:
        """
        Create a new quota.

        Args:
            name: Quota name
            quota_type: Type of quota
            limit_value: Limit amount
            period_seconds: Time period in seconds
            user_id: User-specific quota (optional)
            plan_id: Plan-level quota (optional)
            api_key_id: API key-specific quota (optional)
            is_hard_limit: Whether this is a hard limit

        Returns:
            Created Quota instance
        """
        quota = Quota(
            name=name,
            quota_type=quota_type,
            limit_value=limit_value,
            period_seconds=period_seconds,
            user_id=user_id,
            plan_id=plan_id,
            api_key_id=api_key_id,
            is_hard_limit=is_hard_limit
        )

        self.db_session.add(quota)
        self.db_session.commit()

        return quota

    def get_user_quotas(self, user_id: str, api_key_id: str = None) -> List[Quota]:
        """
        Get all applicable quotas for a user.

        Args:
            user_id: User ID
            api_key_id: Optional API key ID

        Returns:
            List of applicable quotas
        """
        quotas = []

        # User-specific quotas
        user_quotas = self.db_session.query(Quota).filter(
            and_(
                Quota.user_id == user_id,
                Quota.is_active == True
            )
        ).all()
        quotas.extend(user_quotas)

        # Plan-level quotas
        active_subscription = self.db_session.query(Subscription).filter(
            and_(
                Subscription.user_id == user_id,
                Subscription.status == SubscriptionStatusEnum.ACTIVE
            )
        ).first()

        if active_subscription:
            plan_quotas = self.db_session.query(Quota).filter(
                and_(
                    Quota.plan_id == active_subscription.plan_id,
                    Quota.is_active == True
                )
            ).all()
            quotas.extend(plan_quotas)

        # API key-specific quotas
        if api_key_id:
            api_key_quotas = self.db_session.query(Quota).filter(
                and_(
                    Quota.api_key_id == api_key_id,
                    Quota.is_active == True
                )
            ).all()
            quotas.extend(api_key_quotas)

        return quotas

    def check_quota(self, quota: Quota, requested_amount: int,
                   user_id: str, api_key_id: str = None) -> Dict[str, Any]:
        """
        Check if a quota allows the requested amount.

        Args:
            quota: Quota to check
            requested_amount: Amount being requested
            user_id: User ID
            api_key_id: Optional API key ID

        Returns:
            Dictionary with check results
        """
        # Get current usage within the quota period
        cutoff_time = datetime.utcnow() - timedelta(seconds=quota.period_seconds)

        usage_query = self.db_session.query(func.sum(QuotaUsage.amount)).filter(
            and_(
                QuotaUsage.quota_id == quota.id,
                QuotaUsage.user_id == user_id,
                QuotaUsage.created_at >= cutoff_time
            )
        )

        if api_key_id:
            usage_query = usage_query.filter(QuotaUsage.api_key_id == api_key_id)

        current_usage = usage_query.scalar() or 0

        # Check if request would exceed quota
        new_usage = current_usage + requested_amount
        allowed = new_usage <= quota.limit_value

        return {
            'quota_id': quota.id,
            'quota_name': quota.name,
            'quota_type': quota.quota_type.value,
            'limit': quota.limit_value,
            'current_usage': current_usage,
            'requested': requested_amount,
            'new_usage': new_usage,
            'remaining': max(0, quota.limit_value - current_usage),
            'allowed': allowed,
            'is_hard_limit': quota.is_hard_limit,
            'period_seconds': quota.period_seconds,
            'reset_time': (cutoff_time + timedelta(seconds=quota.period_seconds)).isoformat()
        }

    def check_user_quotas(self, user_id: str, shots: int = 0, api_calls: int = 1,
                         api_key_id: str = None) -> Dict[str, Any]:
        """
        Check all applicable quotas for a user's request.

        Args:
            user_id: User ID
            shots: Number of quantum shots requested
            api_calls: Number of API calls
            api_key_id: Optional API key ID

        Returns:
            Dictionary with quota check results
        """
        quotas = self.get_user_quotas(user_id, api_key_id)

        if not quotas:
            return {
                'allowed': True,
                'quotas': [],
                'violations': [],
                'warnings': []
            }

        violations = []
        warnings = []
        quota_results = []

        for quota in quotas:
            # Determine requested amount based on quota type
            if quota.quota_type in [QuotaTypeEnum.SHOTS_PER_HOUR,
                                  QuotaTypeEnum.SHOTS_PER_DAY,
                                  QuotaTypeEnum.SHOTS_PER_MONTH]:
                requested_amount = shots
            elif quota.quota_type in [QuotaTypeEnum.API_CALLS_PER_MINUTE,
                                    QuotaTypeEnum.API_CALLS_PER_HOUR,
                                    QuotaTypeEnum.API_CALLS_PER_DAY]:
                requested_amount = api_calls
            else:
                requested_amount = 1

            result = self.check_quota(quota, requested_amount, user_id, api_key_id)
            quota_results.append(result)

            if not result['allowed']:
                if quota.is_hard_limit:
                    violations.append({
                        'quota_name': quota.name,
                        'quota_type': quota.quota_type.value,
                        'limit': quota.limit_value,
                        'current_usage': result['current_usage'],
                        'requested': requested_amount
                    })
                else:
                    warnings.append({
                        'quota_name': quota.name,
                        'quota_type': quota.quota_type.value,
                        'limit': quota.limit_value,
                        'current_usage': result['current_usage'],
                        'requested': requested_amount
                    })

        # Check API key rate limits separately
        if api_key_id:
            api_key_result = self._check_api_key_rate_limits(api_key_id, api_calls)
            if not api_key_result['allowed']:
                violations.extend(api_key_result['violations'])

        allowed = len(violations) == 0

        return {
            'allowed': allowed,
            'quotas': quota_results,
            'violations': violations,
            'warnings': warnings,
            'reason': violations[0]['quota_name'] if violations else None
        }

    def _check_api_key_rate_limits(self, api_key_id: str, api_calls: int) -> Dict[str, Any]:
        """Check API key specific rate limits."""
        api_key = self.db_session.query(APIKey).filter_by(id=api_key_id).first()

        if not api_key:
            return {'allowed': False, 'violations': [{'reason': 'API key not found'}]}

        violations = []

        # Check per-minute limit
        minute_ago = datetime.utcnow() - timedelta(minutes=1)
        minute_usage = self.db_session.query(func.count(QuotaUsage.id)).filter(
            and_(
                QuotaUsage.api_key_id == api_key_id,
                QuotaUsage.created_at >= minute_ago,
                QuotaUsage.operation_type == 'api_call'
            )
        ).scalar() or 0

        if minute_usage + api_calls > api_key.rate_limit_per_minute:
            violations.append({
                'limit_type': 'per_minute',
                'limit': api_key.rate_limit_per_minute,
                'current_usage': minute_usage,
                'requested': api_calls
            })

        # Check per-hour limit
        hour_ago = datetime.utcnow() - timedelta(hours=1)
        hour_usage = self.db_session.query(func.count(QuotaUsage.id)).filter(
            and_(
                QuotaUsage.api_key_id == api_key_id,
                QuotaUsage.created_at >= hour_ago,
                QuotaUsage.operation_type == 'api_call'
            )
        ).scalar() or 0

        if hour_usage + api_calls > api_key.rate_limit_per_hour:
            violations.append({
                'limit_type': 'per_hour',
                'limit': api_key.rate_limit_per_hour,
                'current_usage': hour_usage,
                'requested': api_calls
            })

        # Check per-day limit
        day_ago = datetime.utcnow() - timedelta(days=1)
        day_usage = self.db_session.query(func.count(QuotaUsage.id)).filter(
            and_(
                QuotaUsage.api_key_id == api_key_id,
                QuotaUsage.created_at >= day_ago,
                QuotaUsage.operation_type == 'api_call'
            )
        ).scalar() or 0

        if day_usage + api_calls > api_key.rate_limit_per_day:
            violations.append({
                'limit_type': 'per_day',
                'limit': api_key.rate_limit_per_day,
                'current_usage': day_usage,
                'requested': api_calls
            })

        return {
            'allowed': len(violations) == 0,
            'violations': violations
        }

    def record_usage(self, user_id: str, shots: int = 0, api_calls: int = 1,
                    api_key_id: str = None, usage_log_id: str = None,
                    operation_type: str = 'quantum_execution') -> List[QuotaUsage]:
        """
        Record usage against applicable quotas.

        Args:
            user_id: User ID
            shots: Number of shots used
            api_calls: Number of API calls made
            api_key_id: Optional API key ID
            usage_log_id: Optional usage log ID for reference
            operation_type: Type of operation

        Returns:
            List of created QuotaUsage records
        """
        quotas = self.get_user_quotas(user_id, api_key_id)
        usage_records = []

        for quota in quotas:
            # Determine amount to record based on quota type
            if quota.quota_type in [QuotaTypeEnum.SHOTS_PER_HOUR,
                                  QuotaTypeEnum.SHOTS_PER_DAY,
                                  QuotaTypeEnum.SHOTS_PER_MONTH]:
                amount = shots
            elif quota.quota_type in [QuotaTypeEnum.API_CALLS_PER_MINUTE,
                                    QuotaTypeEnum.API_CALLS_PER_HOUR,
                                    QuotaTypeEnum.API_CALLS_PER_DAY]:
                amount = api_calls
            else:
                amount = 1

            if amount > 0:
                usage_record = QuotaUsage(
                    quota_id=quota.id,
                    user_id=user_id,
                    api_key_id=api_key_id,
                    usage_log_id=usage_log_id,
                    amount=amount,
                    operation_type=operation_type
                )

                self.db_session.add(usage_record)
                usage_records.append(usage_record)

        # Record API key usage separately
        if api_key_id and api_calls > 0:
            api_call_record = QuotaUsage(
                quota_id=None,  # Not tied to a specific quota
                user_id=user_id,
                api_key_id=api_key_id,
                usage_log_id=usage_log_id,
                amount=api_calls,
                operation_type='api_call'
            )

            self.db_session.add(api_call_record)
            usage_records.append(api_call_record)

        self.db_session.commit()
        return usage_records

    def get_quota_usage_summary(self, user_id: str, api_key_id: str = None,
                               start_date: datetime = None,
                               end_date: datetime = None) -> Dict[str, Any]:
        """
        Get quota usage summary for a user.

        Args:
            user_id: User ID
            api_key_id: Optional API key ID
            start_date: Start date for summary
            end_date: End date for summary

        Returns:
            Dictionary with usage summary
        """
        if not start_date:
            start_date = datetime.utcnow() - timedelta(days=30)
        if not end_date:
            end_date = datetime.utcnow()

        quotas = self.get_user_quotas(user_id, api_key_id)

        summary = {
            'period': {
                'start': start_date.isoformat(),
                'end': end_date.isoformat()
            },
            'quotas': [],
            'current_usage': {},
            'violations_count': 0
        }

        for quota in quotas:
            # Get usage for this quota in the period
            usage_query = self.db_session.query(func.sum(QuotaUsage.amount)).filter(
                and_(
                    QuotaUsage.quota_id == quota.id,
                    QuotaUsage.user_id == user_id,
                    QuotaUsage.created_at >= start_date,
                    QuotaUsage.created_at <= end_date
                )
            )

            if api_key_id:
                usage_query = usage_query.filter(QuotaUsage.api_key_id == api_key_id)

            period_usage = usage_query.scalar() or 0

            # Get current usage (within quota window)
            current_check = self.check_quota(quota, 0, user_id, api_key_id)

            quota_summary = {
                'quota_id': quota.id,
                'name': quota.name,
                'type': quota.quota_type.value,
                'limit': quota.limit_value,
                'period_seconds': quota.period_seconds,
                'period_usage': period_usage,
                'current_usage': current_check['current_usage'],
                'remaining': current_check['remaining'],
                'utilization_percent': (current_check['current_usage'] / quota.limit_value) * 100 if quota.limit_value > 0 else 0
            }

            summary['quotas'].append(quota_summary)

            # Track violations
            if current_check['current_usage'] >= quota.limit_value:
                summary['violations_count'] += 1

        return summary

    def setup_default_quotas_for_plan(self, plan_id: str, plan_type: str):
        """
        Set up default quotas for a subscription plan.

        Args:
            plan_id: Plan ID
            plan_type: Plan type (free, basic, pro, enterprise)
        """
        # Default quota configurations by plan type
        quota_configs = {
            'free': {
                'shots_per_day': {'limit': 1000, 'period': 86400},
                'api_calls_per_hour': {'limit': 100, 'period': 3600},
                'concurrent_jobs': {'limit': 1, 'period': 3600}
            },
            'basic': {
                'shots_per_day': {'limit': 10000, 'period': 86400},
                'shots_per_month': {'limit': 250000, 'period': 2592000},
                'api_calls_per_minute': {'limit': 60, 'period': 60},
                'api_calls_per_hour': {'limit': 1000, 'period': 3600},
                'concurrent_jobs': {'limit': 3, 'period': 3600}
            },
            'pro': {
                'shots_per_day': {'limit': 50000, 'period': 86400},
                'shots_per_month': {'limit': 1000000, 'period': 2592000},
                'api_calls_per_minute': {'limit': 120, 'period': 60},
                'api_calls_per_hour': {'limit': 5000, 'period': 3600},
                'concurrent_jobs': {'limit': 10, 'period': 3600}
            },
            'enterprise': {
                'shots_per_day': {'limit': 200000, 'period': 86400},
                'api_calls_per_minute': {'limit': 300, 'period': 60},
                'api_calls_per_hour': {'limit': 20000, 'period': 3600},
                'concurrent_jobs': {'limit': 50, 'period': 3600}
            }
        }

        config = quota_configs.get(plan_type.lower(), {})

        for quota_name, quota_data in config.items():
            # Convert quota name to enum
            quota_type_map = {
                'shots_per_hour': QuotaTypeEnum.SHOTS_PER_HOUR,
                'shots_per_day': QuotaTypeEnum.SHOTS_PER_DAY,
                'shots_per_month': QuotaTypeEnum.SHOTS_PER_MONTH,
                'api_calls_per_minute': QuotaTypeEnum.API_CALLS_PER_MINUTE,
                'api_calls_per_hour': QuotaTypeEnum.API_CALLS_PER_HOUR,
                'api_calls_per_day': QuotaTypeEnum.API_CALLS_PER_DAY,
                'concurrent_jobs': QuotaTypeEnum.CONCURRENT_JOBS
            }

            quota_type = quota_type_map.get(quota_name)
            if quota_type:
                self.create_quota(
                    name=f"{plan_type.title()} Plan - {quota_name.replace('_', ' ').title()}",
                    quota_type=quota_type,
                    limit_value=quota_data['limit'],
                    period_seconds=quota_data['period'],
                    plan_id=plan_id
                )

    def cleanup_old_usage_records(self, days_old: int = 90):
        """
        Clean up old quota usage records.

        Args:
            days_old: Number of days after which to delete records

        Returns:
            Number of records deleted
        """
        cutoff_date = datetime.utcnow() - timedelta(days=days_old)

        deleted_count = self.db_session.query(QuotaUsage).filter(
            QuotaUsage.created_at < cutoff_date
        ).delete()

        self.db_session.commit()
        return deleted_count