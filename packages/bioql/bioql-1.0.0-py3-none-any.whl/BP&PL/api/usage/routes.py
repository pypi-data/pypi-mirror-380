"""
Usage tracking API routes for quantum computing metrics.
"""

from flask import Blueprint, request, current_app
from datetime import datetime

from ...services.usage_tracker import UsageTracker
from ...models.usage import UsageLog, UsageSession
from ...config import get_pricing_config
from ..main import get_db_session
from ..utils import api_response, paginate_query, get_pagination_params, parse_date_range, create_csv_response
from ..auth.routes import token_required, api_key_required


usage_bp = Blueprint('usage', __name__)


@usage_bp.route('/summary', methods=['GET'])
@token_required
def get_usage_summary(current_user_id):
    """Get usage summary for the current user."""
    try:
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        start_date, end_date = parse_date_range(start_date_str, end_date_str)

        db_session = get_db_session()
        pricing_config = get_pricing_config()
        usage_tracker = UsageTracker(db_session, pricing_config)

        summary = usage_tracker.get_user_usage_summary(current_user_id, start_date, end_date)

        return api_response(summary)

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Usage summary error: {str(e)}")
        return api_response(None, "Failed to retrieve usage summary", 500)


@usage_bp.route('/logs', methods=['GET'])
@token_required
def list_usage_logs(current_user_id):
    """List usage logs for the current user."""
    try:
        page, per_page = get_pagination_params()
        backend = request.args.get('backend')
        success_only = request.args.get('success_only', 'false').lower() == 'true'

        db_session = get_db_session()
        query = db_session.query(UsageLog).filter_by(user_id=current_user_id)

        if backend:
            query = query.filter_by(backend_used=backend)

        if success_only:
            query = query.filter_by(success=True)

        query = query.order_by(UsageLog.created_at.desc())
        result = paginate_query(query, page, per_page)

        return api_response(result)

    except Exception as e:
        current_app.logger.error(f"Usage logs listing error: {str(e)}")
        return api_response(None, "Failed to retrieve usage logs", 500)


@usage_bp.route('/logs/<log_id>', methods=['GET'])
@token_required
def get_usage_log_details(current_user_id, log_id):
    """Get detailed information for a specific usage log."""
    try:
        db_session = get_db_session()
        usage_log = db_session.query(UsageLog).filter_by(
            id=log_id,
            user_id=current_user_id
        ).first()

        if not usage_log:
            return api_response(None, "Usage log not found", 404)

        log_data = usage_log.to_dict()

        # Include quantum job details if available
        if usage_log.quantum_job:
            log_data['quantum_job'] = usage_log.quantum_job.to_dict()

        # Include session details if available
        if usage_log.session:
            log_data['session'] = {
                'id': usage_log.session.id,
                'session_name': usage_log.session.session_name,
                'started_at': usage_log.session.started_at.isoformat(),
                'ended_at': usage_log.session.ended_at.isoformat() if usage_log.session.ended_at else None
            }

        return api_response(log_data)

    except Exception as e:
        current_app.logger.error(f"Usage log details error: {str(e)}")
        return api_response(None, "Failed to retrieve usage log details", 500)


@usage_bp.route('/logs/export', methods=['GET'])
@token_required
def export_usage_logs(current_user_id):
    """Export usage logs as CSV."""
    try:
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        start_date, end_date = parse_date_range(start_date_str, end_date_str)

        db_session = get_db_session()
        query = db_session.query(UsageLog).filter_by(user_id=current_user_id)
        query = query.filter(UsageLog.created_at >= start_date)
        query = query.filter(UsageLog.created_at <= end_date)
        query = query.order_by(UsageLog.created_at.desc())

        usage_logs = query.all()

        if not usage_logs:
            return api_response(None, "No usage data found for the specified period", 404)

        # Prepare data for CSV export
        csv_data = []
        for log in usage_logs:
            csv_data.append({
                'timestamp': log.created_at.isoformat(),
                'backend_used': log.backend_used,
                'backend_type': log.backend_type.value,
                'shots_executed': log.shots_executed,
                'circuit_qubits': log.circuit_qubits,
                'circuit_depth': log.circuit_depth,
                'algorithm_type': log.algorithm_type.value,
                'biological_context': log.biological_context,
                'execution_time': log.execution_time,
                'total_cost': log.total_cost,
                'success': log.success,
                'error_message': log.error_message or ''
            })

        from ..utils import generate_report_filename
        filename = generate_report_filename(
            'usage_logs',
            current_user_id,
            start_date_str,
            end_date_str
        )

        return create_csv_response(csv_data, filename)

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Usage logs export error: {str(e)}")
        return api_response(None, "Failed to export usage logs", 500)


@usage_bp.route('/sessions', methods=['GET'])
@token_required
def list_usage_sessions(current_user_id):
    """List usage sessions for the current user."""
    try:
        page, per_page = get_pagination_params()
        active_only = request.args.get('active_only', 'false').lower() == 'true'

        db_session = get_db_session()
        query = db_session.query(UsageSession).filter_by(user_id=current_user_id)

        if active_only:
            query = query.filter(UsageSession.ended_at.is_(None))

        query = query.order_by(UsageSession.started_at.desc())
        result = paginate_query(query, page, per_page)

        return api_response(result)

    except Exception as e:
        current_app.logger.error(f"Usage sessions listing error: {str(e)}")
        return api_response(None, "Failed to retrieve usage sessions", 500)


@usage_bp.route('/sessions', methods=['POST'])
@token_required
def create_usage_session(current_user_id):
    """Create a new usage session."""
    try:
        data = request.get_json() or {}

        db_session = get_db_session()
        pricing_config = get_pricing_config()
        usage_tracker = UsageTracker(db_session, pricing_config)

        session = usage_tracker.start_session(
            user_id=current_user_id,
            session_name=data.get('session_name'),
            client_ip=request.remote_addr,
            user_agent=request.headers.get('User-Agent')
        )

        return api_response({
            'session_id': session.id,
            'session_name': session.session_name,
            'started_at': session.started_at.isoformat()
        })

    except Exception as e:
        current_app.logger.error(f"Session creation error: {str(e)}")
        return api_response(None, "Failed to create session", 500)


@usage_bp.route('/sessions/<session_id>/end', methods=['POST'])
@token_required
def end_usage_session(current_user_id, session_id):
    """End a usage session."""
    try:
        db_session = get_db_session()
        session = db_session.query(UsageSession).filter_by(
            id=session_id,
            user_id=current_user_id
        ).first()

        if not session:
            return api_response(None, "Session not found", 404)

        if not session.is_active:
            return api_response(None, "Session is already ended", 400)

        session.end_session()
        db_session.commit()

        return api_response({
            'session_id': session.id,
            'ended_at': session.ended_at.isoformat(),
            'duration_seconds': session.duration_seconds,
            'total_jobs': session.total_jobs,
            'total_shots': session.total_shots,
            'total_cost': session.total_cost
        })

    except Exception as e:
        current_app.logger.error(f"Session end error: {str(e)}")
        return api_response(None, "Failed to end session", 500)


@usage_bp.route('/sessions/<session_id>', methods=['GET'])
@token_required
def get_session_details(current_user_id, session_id):
    """Get detailed information for a specific usage session."""
    try:
        db_session = get_db_session()
        session = db_session.query(UsageSession).filter_by(
            id=session_id,
            user_id=current_user_id
        ).first()

        if not session:
            return api_response(None, "Session not found", 404)

        session_data = session.to_dict()
        session_data['duration_seconds'] = session.duration_seconds
        session_data['is_active'] = session.is_active

        # Include usage logs for this session
        usage_logs = [log.to_dict() for log in session.usage_logs]
        session_data['usage_logs'] = usage_logs

        return api_response(session_data)

    except Exception as e:
        current_app.logger.error(f"Session details error: {str(e)}")
        return api_response(None, "Failed to retrieve session details", 500)


@usage_bp.route('/backend-stats', methods=['GET'])
@token_required
def get_backend_statistics(current_user_id):
    """Get usage statistics grouped by backend."""
    try:
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        start_date, end_date = parse_date_range(start_date_str, end_date_str)

        db_session = get_db_session()
        pricing_config = get_pricing_config()
        usage_tracker = UsageTracker(db_session, pricing_config)

        backend_stats = usage_tracker.get_usage_by_backend(
            user_id=current_user_id,
            start_date=start_date,
            end_date=end_date
        )

        return api_response({
            'backend_statistics': backend_stats,
            'period': {
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat()
            }
        })

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Backend statistics error: {str(e)}")
        return api_response(None, "Failed to retrieve backend statistics", 500)


@usage_bp.route('/quantum', methods=['POST'])
@api_key_required
def execute_quantum_with_billing(current_user_id, api_key_id):
    """
    Execute quantum program with integrated billing tracking.
    This endpoint provides the billing-enabled quantum() function via API.
    """
    try:
        from ...services.usage_tracker import BillingQuantumConnector

        data = request.get_json()

        if not data or 'program' not in data:
            return api_response(None, "Program text is required", 400)

        db_session = get_db_session()
        pricing_config = get_pricing_config()

        # Create billing-enabled quantum connector
        connector = BillingQuantumConnector(db_session, pricing_config)

        # Execute quantum program with billing
        result = connector.quantum_with_billing(
            program=data['program'],
            backend=data.get('backend', 'simulator'),
            shots=data.get('shots', 1024),
            debug=data.get('debug', False),
            token=data.get('token'),
            instance=data.get('instance'),
            timeout=data.get('timeout', 3600),
            auto_select=data.get('auto_select', False),
            # Billing parameters
            user_id=current_user_id,
            api_key=None,  # Already authenticated
            client_ip=request.remote_addr,
            user_agent=request.headers.get('User-Agent')
        )

        # Convert result to API response format
        result_data = {
            'success': result.success,
            'counts': result.counts,
            'total_shots': result.total_shots,
            'most_likely_outcome': result.most_likely_outcome,
            'probabilities': result.probabilities(),
            'execution_time': result.execution_time,
            'backend_name': result.backend_name,
            'job_id': result.job_id,
            'cost_estimate': result.cost_estimate,
            'metadata': result.metadata
        }

        if not result.success:
            result_data['error_message'] = result.error_message

        if result.bio_interpretation:
            result_data['bio_interpretation'] = result.bio_interpretation

        return api_response(result_data)

    except Exception as e:
        current_app.logger.error(f"Quantum execution error: {str(e)}")
        return api_response(None, f"Quantum execution failed: {str(e)}", 500)


@usage_bp.route('/quotas', methods=['GET'])
@token_required
def get_quota_status(current_user_id):
    """Get quota status and usage for the current user."""
    try:
        db_session = get_db_session()

        from ...services.quota_manager import QuotaManager
        quota_manager = QuotaManager(db_session)

        quota_summary = quota_manager.get_quota_usage_summary(current_user_id)

        return api_response(quota_summary)

    except Exception as e:
        current_app.logger.error(f"Quota status error: {str(e)}")
        return api_response(None, "Failed to retrieve quota status", 500)


@usage_bp.route('/analytics', methods=['GET'])
@token_required
def get_usage_analytics(current_user_id):
    """Get detailed usage analytics for the current user."""
    try:
        start_date_str = request.args.get('start_date')
        end_date_str = request.args.get('end_date')
        start_date, end_date = parse_date_range(start_date_str, end_date_str)

        db_session = get_db_session()

        # Get basic usage summary
        pricing_config = get_pricing_config()
        usage_tracker = UsageTracker(db_session, pricing_config)
        usage_summary = usage_tracker.get_user_usage_summary(current_user_id, start_date, end_date)

        # Get backend statistics
        backend_stats = usage_tracker.get_usage_by_backend(current_user_id, start_date, end_date)

        # Get quota information
        from ...services.quota_manager import QuotaManager
        quota_manager = QuotaManager(db_session)
        quota_summary = quota_manager.get_quota_usage_summary(current_user_id)

        analytics_data = {
            'period': {
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat()
            },
            'usage_summary': usage_summary,
            'backend_statistics': backend_stats,
            'quota_status': quota_summary,
            'trends': {
                # Could add trend analysis here
                'daily_usage': [],
                'cost_trends': [],
                'backend_preferences': []
            }
        }

        return api_response(analytics_data)

    except ValueError as e:
        return api_response(None, str(e), 400)
    except Exception as e:
        current_app.logger.error(f"Usage analytics error: {str(e)}")
        return api_response(None, "Failed to retrieve usage analytics", 500)