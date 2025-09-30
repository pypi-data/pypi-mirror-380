"""
Usage tracking service that intercepts quantum() calls and logs billing data.
"""

import hashlib
import inspect
import time
from datetime import datetime
from typing import Dict, Any, Optional, List
from functools import wraps
from sqlalchemy.orm import Session

from ..models.usage import UsageLog, UsageSession, QuantumJob, BackendTypeEnum, AlgorithmTypeEnum, JobStatusEnum
from ..models.user import User, APIKey
from ..models.quota import QuotaUsage
from .quota_manager import QuotaManager
from .billing_engine import BillingEngine


class UsageTracker:
    """
    Service for tracking quantum computing usage and logging billing data.
    """

    def __init__(self, db_session: Session, pricing_config: Dict[str, Any]):
        self.db_session = db_session
        self.pricing_config = pricing_config
        self.quota_manager = QuotaManager(db_session)
        self.billing_engine = BillingEngine(db_session, pricing_config)
        self.current_sessions: Dict[str, UsageSession] = {}

    def start_session(self, user_id: str, session_name: str = None,
                     api_key_id: str = None, client_ip: str = None,
                     user_agent: str = None) -> UsageSession:
        """Start a new usage session for a user."""
        session = UsageSession(
            user_id=user_id,
            session_name=session_name or f"Session {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}",
            api_key_id=api_key_id,
            client_ip=client_ip,
            user_agent=user_agent
        )

        self.db_session.add(session)
        self.db_session.commit()

        self.current_sessions[user_id] = session
        return session

    def end_session(self, user_id: str) -> Optional[UsageSession]:
        """End the current session for a user."""
        session = self.current_sessions.get(user_id)
        if session:
            session.end_session()
            self.db_session.commit()
            del self.current_sessions[user_id]
        return session

    def get_or_create_session(self, user_id: str, **kwargs) -> UsageSession:
        """Get current session or create a new one."""
        if user_id not in self.current_sessions:
            return self.start_session(user_id, **kwargs)
        return self.current_sessions[user_id]

    def log_quantum_execution(self, user_id: str, program_text: str,
                            circuit_qubits: int, circuit_depth: int,
                            circuit_gates: int, backend_requested: str,
                            backend_used: str, shots_requested: int,
                            result: Any, api_key_id: str = None,
                            session_id: str = None, client_metadata: Dict = None) -> UsageLog:
        """
        Log a quantum execution for billing purposes.

        Args:
            user_id: User ID executing the quantum program
            program_text: Original BioQL program text
            circuit_qubits: Number of qubits in the circuit
            circuit_depth: Circuit depth
            circuit_gates: Number of gates in circuit
            backend_requested: Backend originally requested
            backend_used: Actual backend used
            shots_requested: Number of shots requested
            result: QuantumResult object
            api_key_id: API key used (if any)
            session_id: Session ID (if any)
            client_metadata: Additional client metadata

        Returns:
            UsageLog instance
        """
        # Generate program hash for deduplication
        program_hash = hashlib.sha256(program_text.encode()).hexdigest()

        # Determine backend type
        backend_type = BackendTypeEnum.SIMULATOR
        if 'ibm_' in backend_used or 'ionq_qpu' in backend_used:
            backend_type = BackendTypeEnum.REAL_HARDWARE

        # Get or create session
        if session_id:
            session = self.db_session.query(UsageSession).filter_by(id=session_id).first()
        else:
            session = self.get_or_create_session(user_id, api_key_id=api_key_id)

        # Create usage log
        usage_log = UsageLog(
            user_id=user_id,
            session_id=session.id if session else None,
            api_key_id=api_key_id,
            program_text=program_text,
            program_hash=program_hash,
            circuit_qubits=circuit_qubits,
            circuit_depth=circuit_depth,
            circuit_gates=circuit_gates,
            backend_requested=backend_requested,
            backend_used=backend_used,
            backend_type=backend_type,
            shots_requested=shots_requested,
            shots_executed=result.total_shots if result.success else 0,
            success=result.success,
            execution_time=result.execution_time,
            error_message=result.error_message,
            client_metadata=client_metadata or {}
        )

        # Classify algorithm and biological context
        usage_log.classify_algorithm(program_text)
        usage_log.classify_biological_context(program_text)

        # Calculate cost
        cost = usage_log.calculate_cost(self.pricing_config)

        # Check quota limits before saving
        quota_check = self.quota_manager.check_user_quotas(
            user_id,
            shots=usage_log.shots_executed,
            api_key_id=api_key_id
        )

        if not quota_check['allowed']:
            usage_log.success = False
            usage_log.error_message = f"Quota exceeded: {quota_check['reason']}"

        # Save to database
        self.db_session.add(usage_log)
        self.db_session.commit()

        # Create quantum job record if applicable
        if result.job_id:
            quantum_job = QuantumJob(
                job_id=result.job_id,
                usage_log_id=usage_log.id,
                backend_name=backend_used,
                backend_type=backend_type,
                status=JobStatusEnum.COMPLETED if result.success else JobStatusEnum.FAILED,
                submitted_at=datetime.utcnow(),
                completed_at=datetime.utcnow(),
                execution_time=result.execution_time,
                result_counts=result.counts if result.success else None,
                error_message=result.error_message
            )
            self.db_session.add(quantum_job)

        # Update session totals
        if session:
            session.total_shots += usage_log.shots_executed
            session.total_cost = str(float(session.total_cost) + cost)
            session.total_jobs += 1

        # Record quota usage
        if usage_log.success:
            self.quota_manager.record_usage(
                user_id=user_id,
                shots=usage_log.shots_executed,
                api_calls=1,
                api_key_id=api_key_id,
                usage_log_id=usage_log.id
            )

        self.db_session.commit()
        return usage_log

    def get_user_usage_summary(self, user_id: str, start_date: datetime = None,
                              end_date: datetime = None) -> Dict[str, Any]:
        """Get usage summary for a user."""
        query = self.db_session.query(UsageLog).filter_by(user_id=user_id)

        if start_date:
            query = query.filter(UsageLog.created_at >= start_date)
        if end_date:
            query = query.filter(UsageLog.created_at <= end_date)

        usage_logs = query.all()

        total_shots = sum(log.shots_executed for log in usage_logs if log.success)
        total_cost = sum(log.cost_float for log in usage_logs if log.success)
        total_jobs = len(usage_logs)
        successful_jobs = len([log for log in usage_logs if log.success])

        # Backend usage
        backend_usage = {}
        algorithm_usage = {}

        for log in usage_logs:
            if log.success:
                backend_usage[log.backend_used] = backend_usage.get(log.backend_used, 0) + log.shots_executed
                algorithm_usage[log.algorithm_type.value] = algorithm_usage.get(log.algorithm_type.value, 0) + 1

        return {
            'total_shots': total_shots,
            'total_cost': total_cost,
            'total_jobs': total_jobs,
            'successful_jobs': successful_jobs,
            'success_rate': successful_jobs / total_jobs if total_jobs > 0 else 0,
            'backend_usage': backend_usage,
            'algorithm_usage': algorithm_usage,
            'average_cost_per_job': total_cost / successful_jobs if successful_jobs > 0 else 0,
            'period_start': start_date,
            'period_end': end_date
        }

    def get_usage_by_backend(self, user_id: str = None, start_date: datetime = None,
                           end_date: datetime = None) -> Dict[str, Dict[str, Any]]:
        """Get usage statistics grouped by backend."""
        query = self.db_session.query(UsageLog)

        if user_id:
            query = query.filter_by(user_id=user_id)
        if start_date:
            query = query.filter(UsageLog.created_at >= start_date)
        if end_date:
            query = query.filter(UsageLog.created_at <= end_date)

        usage_logs = query.filter_by(success=True).all()

        backend_stats = {}
        for log in usage_logs:
            backend = log.backend_used
            if backend not in backend_stats:
                backend_stats[backend] = {
                    'total_shots': 0,
                    'total_cost': 0,
                    'job_count': 0,
                    'total_execution_time': 0,
                    'average_circuit_qubits': 0,
                    'backend_type': log.backend_type.value
                }

            stats = backend_stats[backend]
            stats['total_shots'] += log.shots_executed
            stats['total_cost'] += log.cost_float
            stats['job_count'] += 1
            stats['total_execution_time'] += log.execution_time or 0
            stats['average_circuit_qubits'] = (
                (stats['average_circuit_qubits'] * (stats['job_count'] - 1) + log.circuit_qubits)
                / stats['job_count']
            )

        # Calculate derived metrics
        for backend, stats in backend_stats.items():
            if stats['job_count'] > 0:
                stats['average_cost_per_job'] = stats['total_cost'] / stats['job_count']
                stats['average_shots_per_job'] = stats['total_shots'] / stats['job_count']
                stats['average_execution_time'] = stats['total_execution_time'] / stats['job_count']
                stats['cost_per_shot'] = stats['total_cost'] / stats['total_shots'] if stats['total_shots'] > 0 else 0

        return backend_stats

    def cleanup_old_sessions(self, days_old: int = 7):
        """Clean up old inactive sessions."""
        cutoff_date = datetime.utcnow() - timedelta(days=days_old)

        old_sessions = self.db_session.query(UsageSession).filter(
            UsageSession.ended_at.is_(None),
            UsageSession.created_at < cutoff_date
        ).all()

        for session in old_sessions:
            session.end_session()

        self.db_session.commit()
        return len(old_sessions)


class BillingQuantumConnector:
    """
    Enhanced quantum connector that integrates with the billing system.
    This replaces or wraps the original quantum() function.
    """

    def __init__(self, db_session: Session, pricing_config: Dict[str, Any]):
        self.usage_tracker = UsageTracker(db_session, pricing_config)
        self.db_session = db_session

    def quantum_with_billing(self, program: str, backend: str = 'simulator',
                           shots: int = 1024, debug: bool = False,
                           token: str = None, instance: str = None,
                           timeout: int = 3600, auto_select: bool = False,
                           # Billing-specific parameters
                           user_id: str = None, api_key: str = None,
                           session_id: str = None, client_ip: str = None,
                           user_agent: str = None) -> Any:
        """
        Execute quantum program with integrated billing and usage tracking.

        This function wraps the original quantum() function and adds billing
        functionality including usage logging, quota checking, and cost calculation.
        """
        # Import the original quantum function
        from ...bioql.quantum_connector import quantum, parse_bioql_program

        # Authenticate user if API key provided
        user_id_to_use = user_id
        api_key_id = None

        if api_key and not user_id:
            api_key_obj = self.db_session.query(APIKey).filter_by(key_hash=api_key).first()
            if api_key_obj and api_key_obj.is_valid():
                user_id_to_use = api_key_obj.user_id
                api_key_id = api_key_obj.id
                api_key_obj.record_usage()
            else:
                raise ValueError("Invalid or expired API key")

        if not user_id_to_use:
            raise ValueError("User ID or valid API key required for billing")

        # Parse circuit to get metadata before execution
        try:
            circuit = parse_bioql_program(program)
            circuit_qubits = circuit.num_qubits
            circuit_depth = circuit.depth()
            circuit_gates = len(circuit.data)
        except Exception as e:
            circuit_qubits = 0
            circuit_depth = 0
            circuit_gates = 0

        # Check user quotas before execution
        quota_check = self.usage_tracker.quota_manager.check_user_quotas(
            user_id_to_use,
            shots=shots,
            api_key_id=api_key_id
        )

        if not quota_check['allowed']:
            # Return failed result due to quota
            from ...bioql.quantum_connector import QuantumResult
            return QuantumResult(
                success=False,
                error_message=f"Quota exceeded: {quota_check['reason']}",
                metadata={
                    'quota_exceeded': True,
                    'quota_limits': quota_check['limits'],
                    'current_usage': quota_check['current_usage']
                }
            )

        # Start timing
        start_time = time.time()

        # Execute the original quantum function
        try:
            result = quantum(
                program=program,
                backend=backend,
                shots=shots,
                debug=debug,
                token=token,
                instance=instance,
                timeout=timeout,
                auto_select=auto_select
            )

            # Calculate execution time if not provided
            if not result.execution_time:
                result.execution_time = time.time() - start_time

        except Exception as e:
            # Create failed result
            from ...bioql.quantum_connector import QuantumResult
            result = QuantumResult(
                success=False,
                error_message=str(e),
                execution_time=time.time() - start_time
            )

        # Log usage for billing
        client_metadata = {
            'client_ip': client_ip,
            'user_agent': user_agent,
            'execution_timestamp': datetime.utcnow().isoformat(),
            'api_key_used': api_key_id is not None
        }

        usage_log = self.usage_tracker.log_quantum_execution(
            user_id=user_id_to_use,
            program_text=program,
            circuit_qubits=circuit_qubits,
            circuit_depth=circuit_depth,
            circuit_gates=circuit_gates,
            backend_requested=backend,
            backend_used=result.backend_name or backend,
            shots_requested=shots,
            result=result,
            api_key_id=api_key_id,
            session_id=session_id,
            client_metadata=client_metadata
        )

        # Add billing information to result metadata
        result.metadata.update({
            'billing': {
                'usage_log_id': usage_log.id,
                'total_cost': usage_log.total_cost,
                'base_cost_per_shot': usage_log.base_cost_per_shot,
                'complexity_multiplier': usage_log.complexity_multiplier,
                'algorithm_multiplier': usage_log.algorithm_multiplier,
                'algorithm_type': usage_log.algorithm_type.value,
                'biological_context': usage_log.biological_context,
                'billed': usage_log.billed
            }
        })

        return result


def create_billing_quantum_function(db_session: Session, pricing_config: Dict[str, Any]):
    """
    Factory function to create a billing-enabled quantum function.

    This can be used to replace the original quantum() function in applications
    that need billing integration.
    """
    connector = BillingQuantumConnector(db_session, pricing_config)
    return connector.quantum_with_billing


def quantum_billing_decorator(db_session: Session, pricing_config: Dict[str, Any]):
    """
    Decorator to add billing functionality to the quantum() function.

    Usage:
        @quantum_billing_decorator(db_session, pricing_config)
        def my_quantum_function(...):
            return quantum(...)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Extract billing parameters
            user_id = kwargs.pop('user_id', None)
            api_key = kwargs.pop('api_key', None)
            session_id = kwargs.pop('session_id', None)
            client_ip = kwargs.pop('client_ip', None)
            user_agent = kwargs.pop('user_agent', None)

            # Create billing connector
            connector = BillingQuantumConnector(db_session, pricing_config)

            # Execute with billing
            return connector.quantum_with_billing(
                *args, **kwargs,
                user_id=user_id,
                api_key=api_key,
                session_id=session_id,
                client_ip=client_ip,
                user_agent=user_agent
            )
        return wrapper
    return decorator