"""
Usage tracking models for quantum computing operations.
"""

from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text, JSON, Enum
from sqlalchemy.orm import relationship
import enum

from .base import BaseModel


class BackendTypeEnum(enum.Enum):
    """Enum for quantum backend types."""
    SIMULATOR = "simulator"
    REAL_HARDWARE = "real_hardware"


class AlgorithmTypeEnum(enum.Enum):
    """Enum for algorithm types with different pricing."""
    BASIC = "basic"
    VQE = "vqe"
    GROVER = "grover"
    SHOR = "shor"
    QAOA = "qaoa"
    CUSTOM = "custom"


class JobStatusEnum(enum.Enum):
    """Enum for quantum job status."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class UsageSession(BaseModel):
    """Session model to group related quantum operations."""

    __tablename__ = 'usage_sessions'

    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    session_name = Column(String(255))
    description = Column(Text)

    # Session metadata
    client_ip = Column(String(45))
    user_agent = Column(String(500))
    api_key_id = Column(String(36), ForeignKey('api_keys.id'))

    # Session totals
    total_shots = Column(Integer, default=0)
    total_cost = Column(String(20), default='0.00')  # Store as string
    total_jobs = Column(Integer, default=0)

    # Session timing
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    ended_at = Column(DateTime)

    # Relationships
    user = relationship("User", foreign_keys=[user_id])
    api_key = relationship("APIKey", foreign_keys=[api_key_id])
    usage_logs = relationship("UsageLog", back_populates="session", cascade="all, delete-orphan")

    @property
    def duration_seconds(self):
        """Calculate session duration in seconds."""
        if self.ended_at:
            return (self.ended_at - self.started_at).total_seconds()
        return (datetime.utcnow() - self.started_at).total_seconds()

    @property
    def is_active(self):
        """Check if session is still active."""
        return self.ended_at is None

    def end_session(self):
        """Mark session as ended."""
        if self.is_active:
            self.ended_at = datetime.utcnow()


class QuantumJob(BaseModel):
    """Individual quantum job details."""

    __tablename__ = 'quantum_jobs'

    # Job identification
    job_id = Column(String(100), unique=True, nullable=False, index=True)
    usage_log_id = Column(String(36), ForeignKey('usage_logs.id'), nullable=False)

    # Backend information
    backend_name = Column(String(100), nullable=False)
    backend_type = Column(Enum(BackendTypeEnum), nullable=False)
    backend_version = Column(String(50))

    # Job status and timing
    status = Column(Enum(JobStatusEnum), default=JobStatusEnum.PENDING, nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)

    # Queue information
    queue_position = Column(Integer)
    estimated_queue_time = Column(Integer)  # seconds
    actual_queue_time = Column(Integer)  # seconds

    # Execution details
    execution_time = Column(Float)  # seconds
    optimization_level = Column(Integer)
    transpiled_depth = Column(Integer)
    transpiled_gates = Column(Integer)

    # Results and errors
    error_message = Column(Text)
    result_counts = Column(JSON)
    fidelity_estimate = Column(Float)

    # Relationships
    usage_log = relationship("UsageLog", back_populates="quantum_job")

    @property
    def total_time_seconds(self):
        """Calculate total time from submission to completion."""
        if self.completed_at:
            return (self.completed_at - self.submitted_at).total_seconds()
        return None

    @property
    def is_completed(self):
        """Check if job is completed (successfully or failed)."""
        return self.status in [JobStatusEnum.COMPLETED, JobStatusEnum.FAILED]

    def update_status(self, status, **kwargs):
        """Update job status with timestamp."""
        self.status = status
        now = datetime.utcnow()

        if status == JobStatusEnum.RUNNING and not self.started_at:
            self.started_at = now
        elif status in [JobStatusEnum.COMPLETED, JobStatusEnum.FAILED] and not self.completed_at:
            self.completed_at = now

        # Update additional fields
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


class UsageLog(BaseModel):
    """Detailed usage log for each quantum() call."""

    __tablename__ = 'usage_logs'

    # User and session information
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    session_id = Column(String(36), ForeignKey('usage_sessions.id'))
    api_key_id = Column(String(36), ForeignKey('api_keys.id'))

    # Program and circuit information
    program_text = Column(Text)
    program_hash = Column(String(64), index=True)  # For deduplication
    circuit_qubits = Column(Integer, nullable=False)
    circuit_depth = Column(Integer, nullable=False)
    circuit_gates = Column(Integer)

    # Algorithm classification
    algorithm_type = Column(Enum(AlgorithmTypeEnum), default=AlgorithmTypeEnum.BASIC)
    biological_context = Column(String(100))  # protein_folding, drug_discovery, etc.

    # Execution parameters
    backend_requested = Column(String(100), nullable=False)
    backend_used = Column(String(100), nullable=False)
    backend_type = Column(Enum(BackendTypeEnum), nullable=False)
    shots_requested = Column(Integer, nullable=False)
    shots_executed = Column(Integer)

    # Execution results
    success = Column(Boolean, nullable=False)
    execution_time = Column(Float)  # seconds
    error_message = Column(Text)

    # Pricing calculation
    base_cost_per_shot = Column(String(20))  # Store as string
    complexity_multiplier = Column(Float, default=1.0)
    algorithm_multiplier = Column(Float, default=1.0)
    total_cost = Column(String(20))  # Store as string

    # Billing status
    billed = Column(Boolean, default=False)
    bill_id = Column(String(36), ForeignKey('bills.id'))

    # Metadata
    client_metadata = Column(JSON)

    # Relationships
    user = relationship("User", back_populates="usage_logs")
    session = relationship("UsageSession", back_populates="usage_logs")
    api_key = relationship("APIKey", foreign_keys=[api_key_id])
    bill = relationship("Bill", foreign_keys=[bill_id])
    quantum_job = relationship("QuantumJob", back_populates="usage_log", uselist=False, cascade="all, delete-orphan")

    def calculate_cost(self, pricing_config):
        """Calculate the cost for this usage log entry."""
        # Base cost per shot
        if self.backend_type == BackendTypeEnum.SIMULATOR:
            base_cost = float(pricing_config.get('simulator_cost_per_shot', '0.001'))
        else:
            base_cost = float(pricing_config.get('hardware_cost_per_shot', '0.01'))

        # Complexity multiplier based on qubits
        if self.circuit_qubits <= 4:
            complexity_mult = 1.0
        elif self.circuit_qubits <= 8:
            complexity_mult = 2.0
        else:
            complexity_mult = 5.0

        # Algorithm multiplier
        algo_mult = pricing_config.get('algorithm_multipliers', {}).get(
            self.algorithm_type.value, 1.0
        )

        # Calculate total cost
        shots = self.shots_executed or self.shots_requested
        total = base_cost * shots * complexity_mult * algo_mult

        # Store calculated values
        self.base_cost_per_shot = f"{base_cost:.6f}"
        self.complexity_multiplier = complexity_mult
        self.algorithm_multiplier = algo_mult
        self.total_cost = f"{total:.6f}"

        return total

    @property
    def cost_float(self):
        """Get total cost as float."""
        try:
            return float(self.total_cost) if self.total_cost else 0.0
        except (ValueError, TypeError):
            return 0.0

    def classify_algorithm(self, program_text):
        """Classify the algorithm type based on program text."""
        program_lower = program_text.lower()

        if any(keyword in program_lower for keyword in ['vqe', 'variational quantum eigensolver']):
            self.algorithm_type = AlgorithmTypeEnum.VQE
        elif any(keyword in program_lower for keyword in ['grover', 'search', 'amplitude amplification']):
            self.algorithm_type = AlgorithmTypeEnum.GROVER
        elif any(keyword in program_lower for keyword in ['shor', 'factoring', 'period finding']):
            self.algorithm_type = AlgorithmTypeEnum.SHOR
        elif any(keyword in program_lower for keyword in ['qaoa', 'quantum approximate optimization']):
            self.algorithm_type = AlgorithmTypeEnum.QAOA
        else:
            self.algorithm_type = AlgorithmTypeEnum.BASIC

    def classify_biological_context(self, program_text):
        """Classify the biological context."""
        program_lower = program_text.lower()

        if any(keyword in program_lower for keyword in ['protein', 'folding', 'structure']):
            self.biological_context = 'protein_folding'
        elif any(keyword in program_lower for keyword in ['drug', 'molecule', 'binding', 'docking']):
            self.biological_context = 'drug_discovery'
        elif any(keyword in program_lower for keyword in ['dna', 'sequence', 'gene', 'genetic']):
            self.biological_context = 'dna_analysis'
        elif any(keyword in program_lower for keyword in ['enzyme', 'catalyst', 'reaction']):
            self.biological_context = 'enzyme_analysis'
        else:
            self.biological_context = 'general'