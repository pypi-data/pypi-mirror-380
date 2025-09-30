#!/usr/bin/env python3
"""
BioQL Quantum Connector Module

This module provides the core quantum computing functionality for BioQL,
including the quantum() function and QuantumResult class.
"""

from typing import Dict, List, Optional, Union, Any, Tuple, Callable
import numpy as np
from dataclasses import dataclass, field
import warnings
import logging
import time
import hashlib
import json
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
from datetime import datetime, timedelta

try:
    from qiskit import QuantumCircuit, transpile
    from qiskit_aer import AerSimulator
    from qiskit.quantum_info import Statevector
    from qiskit.result import Result
    # Try new primitives API first, fallback to old
    try:
        from qiskit.primitives import StatevectorSampler as Sampler
    except ImportError:
        try:
            from qiskit.primitives import BackendSamplerV2 as Sampler
        except ImportError:
            # For older versions
            Sampler = None
    QISKIT_AVAILABLE = True
except ImportError:
    QISKIT_AVAILABLE = False
    # Create dummy classes when qiskit is not available
    class QuantumCircuit:
        pass
    warnings.warn(
        "Qiskit not available. Install with: pip install qiskit qiskit-aer",
        ImportWarning
    )

try:
    from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler as RuntimeSampler
    from qiskit_ibm_runtime.exceptions import IBMRuntimeError, IBMAccountError
    IBM_QUANTUM_AVAILABLE = True
except ImportError:
    IBM_QUANTUM_AVAILABLE = False
    warnings.warn(
        "IBM Quantum libraries not available. Install with: pip install qiskit-ibm-runtime",
        ImportWarning
    )

try:
    from qiskit_ionq import IonQProvider
    IONQ_AVAILABLE = True
except ImportError:
    IONQ_AVAILABLE = False
    warnings.warn(
        "IonQ libraries not available. Install with: pip install qiskit-ionq",
        ImportWarning
    )

# Configure logging
logger = logging.getLogger(__name__)

# Billing integration imports (optional)
try:
    from .billing_integration import (
        BillingIntegration,
        create_billing_quantum_function,
        get_billing_status,
        BILLING_ENABLED
    )
    BILLING_INTEGRATION_AVAILABLE = True
except ImportError:
    BILLING_INTEGRATION_AVAILABLE = False
    BILLING_ENABLED = False
    logger.debug("Billing integration not available")


class BioQLError(Exception):
    """Base exception for BioQL-related errors."""
    pass


class QuantumBackendError(BioQLError):
    """Exception raised for quantum backend-related errors."""
    pass


class ProgramParsingError(BioQLError):
    """Exception raised for program parsing errors."""
    pass


class IBMQuantumError(BioQLError):
    """Exception raised for IBM Quantum-related errors."""
    pass


class JobTimeoutError(IBMQuantumError):
    """Exception raised when a quantum job times out."""
    pass


class AuthenticationError(IBMQuantumError):
    """Exception raised for authentication errors."""
    pass


class BackendNotAvailableError(IBMQuantumError):
    """Exception raised when a requested backend is not available."""
    pass


class CircuitTooLargeError(IBMQuantumError):
    """Exception raised when circuit exceeds backend capabilities."""
    pass


# Circuit caching utility
class CircuitCache:
    """Simple in-memory cache for quantum circuits and results."""

    def __init__(self, max_size: int = 100):
        self._cache: Dict[str, Tuple[QuantumResult, datetime]] = {}
        self._max_size = max_size

    def _hash_circuit(self, circuit: QuantumCircuit, shots: int, backend: str) -> str:
        """Generate a hash for circuit identification."""
        circuit_str = str(circuit)
        data = f"{circuit_str}_{shots}_{backend}"
        return hashlib.md5(data.encode()).hexdigest()

    def get(self, circuit: QuantumCircuit, shots: int, backend: str,
            max_age_hours: int = 24) -> Optional['QuantumResult']:
        """Get cached result if available and not expired."""
        cache_key = self._hash_circuit(circuit, shots, backend)

        if cache_key in self._cache:
            result, timestamp = self._cache[cache_key]
            age = datetime.now() - timestamp

            if age < timedelta(hours=max_age_hours):
                logger.info(f"Cache hit for circuit {cache_key[:8]}...")
                return result
            else:
                # Remove expired entry
                del self._cache[cache_key]

        return None

    def put(self, circuit: QuantumCircuit, shots: int, backend: str,
            result: 'QuantumResult') -> None:
        """Store result in cache."""
        if len(self._cache) >= self._max_size:
            # Remove oldest entry
            oldest_key = min(self._cache.keys(),
                           key=lambda k: self._cache[k][1])
            del self._cache[oldest_key]

        cache_key = self._hash_circuit(circuit, shots, backend)
        self._cache[cache_key] = (result, datetime.now())
        logger.info(f"Cached result for circuit {cache_key[:8]}...")


# Global circuit cache instance
_circuit_cache = CircuitCache()


# Retry decorator for IBM Quantum operations
def retry_on_failure(max_retries: int = 3, delay: float = 1.0,
                    backoff: float = 2.0):
    """Decorator to retry operations with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except (IBMRuntimeError,
                       ConnectionError, TimeoutError) as e:
                    last_exception = e

                    if attempt < max_retries:
                        logger.warning(
                            f"Attempt {attempt + 1} failed: {str(e)}. "
                            f"Retrying in {current_delay:.1f}s..."
                        )
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(
                            f"All {max_retries + 1} attempts failed. "
                            f"Last error: {str(e)}"
                        )

            raise IBMQuantumError(
                f"Operation failed after {max_retries + 1} attempts: "
                f"{str(last_exception)}"
            )

        return wrapper
    return decorator


@dataclass
class QuantumResult:
    """
    Result object containing the output of a quantum computation.

    Attributes:
        counts: Dictionary mapping measurement outcomes to their frequencies
        statevector: Complex amplitudes of the quantum state (if available)
        bio_interpretation: Biological interpretation of the quantum results
        metadata: Additional metadata about the computation
        success: Whether the computation completed successfully
        error_message: Error message if computation failed
        job_id: Job ID from quantum backend (if available)
        backend_name: Name of the backend used
        execution_time: Total execution time in seconds
        queue_time: Time spent in queue (if available)
        cost_estimate: Estimated cost of the computation
        billing_metadata: Billing and usage tracking information (if enabled)
    """
    counts: Dict[str, int] = field(default_factory=dict)
    statevector: Optional[np.ndarray] = None
    bio_interpretation: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    success: bool = True
    error_message: Optional[str] = None
    job_id: Optional[str] = None
    backend_name: Optional[str] = None
    execution_time: Optional[float] = None
    queue_time: Optional[float] = None
    cost_estimate: Optional[float] = None
    # Billing integration fields
    billing_metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """Validate the result after initialization."""
        if not self.success and not self.error_message:
            raise ValueError("Failed results must include an error message")

    @property
    def total_shots(self) -> int:
        """Total number of shots executed."""
        return sum(self.counts.values()) if self.counts else 0

    @property
    def most_likely_outcome(self) -> Optional[str]:
        """The measurement outcome with the highest probability."""
        if not self.counts:
            return None
        return max(self.counts.keys(), key=lambda k: self.counts[k])

    def probabilities(self) -> Dict[str, float]:
        """Convert counts to probabilities."""
        if not self.counts:
            return {}
        total = self.total_shots
        return {outcome: count / total for outcome, count in self.counts.items()}


class QuantumSimulator:
    """
    Quantum simulator backend using Qiskit.

    This class provides a simple interface to quantum simulation
    functionality for BioQL programs.
    """

    def __init__(self, backend_name: str = 'aer_simulator'):
        """
        Initialize the quantum simulator.

        Args:
            backend_name: Name of the Qiskit backend to use
        """
        if not QISKIT_AVAILABLE:
            raise QuantumBackendError(
                "Qiskit not available. Please install qiskit and qiskit-aer"
            )

        self.backend_name = backend_name
        self.backend = AerSimulator()
        logger.info(f"Initialized quantum simulator with backend: {backend_name}")

    def execute_circuit(
        self,
        circuit: QuantumCircuit,
        shots: int = 1024,
        get_statevector: bool = False
    ) -> QuantumResult:
        """
        Execute a quantum circuit on the simulator.

        Args:
            circuit: The quantum circuit to execute
            shots: Number of measurement shots
            get_statevector: Whether to compute the final statevector

        Returns:
            QuantumResult containing the computation results
        """
        try:
            # Transpile circuit for the backend
            transpiled_circuit = transpile(circuit, self.backend)

            # Execute the circuit
            job = self.backend.run(transpiled_circuit, shots=shots)
            result = job.result()

            # Extract counts
            counts = result.get_counts()

            # Get statevector if requested
            statevector = None
            if get_statevector:
                try:
                    # For statevector, we need to run without measurements
                    statevector_circuit = circuit.copy()
                    # Remove measurements for statevector calculation
                    for instruction in statevector_circuit.data[:]:
                        if instruction.operation.name == 'measure':
                            statevector_circuit.data.remove(instruction)

                    # Use statevector simulator
                    sv_backend = AerSimulator(method='statevector')
                    sv_job = sv_backend.run(statevector_circuit, shots=1)
                    sv_result = sv_job.result()
                    statevector = sv_result.get_statevector().data
                except Exception as e:
                    logger.warning(f"Could not compute statevector: {str(e)}")
                    statevector = None

            # Create metadata
            metadata = {
                'backend': self.backend_name,
                'shots': shots,
                'circuit_depth': circuit.depth(),
                'num_qubits': circuit.num_qubits,
                'num_clbits': circuit.num_clbits,
                'execution_time': getattr(job.result(), 'time_taken', None)
            }

            return QuantumResult(
                counts=counts,
                statevector=statevector,
                bio_interpretation={},  # Will be filled by bio interpreter
                metadata=metadata,
                success=True
            )

        except Exception as e:
            logger.error(f"Circuit execution failed: {str(e)}")
            return QuantumResult(
                success=False,
                error_message=f"Circuit execution failed: {str(e)}"
            )


class IBMQuantumBackend:
    """
    IBM Quantum backend for executing circuits on real quantum hardware.

    This class provides comprehensive integration with IBM Quantum services,
    including authentication, job management, queue monitoring, and error handling.
    """

    # Known IBM backends with their capabilities
    KNOWN_BACKENDS = {
        'ibm_eagle': {'qubits': 127, 'basis_gates': ['id', 'rz', 'sx', 'x', 'cx'], 'coupling_map': True},
        'ibm_condor': {'qubits': 1121, 'basis_gates': ['id', 'rz', 'sx', 'x', 'cx'], 'coupling_map': True},
        'ibm_sherbrooke': {'qubits': 127, 'basis_gates': ['id', 'rz', 'sx', 'x', 'cx'], 'coupling_map': True},
        'ibm_brisbane': {'qubits': 127, 'basis_gates': ['id', 'rz', 'sx', 'x', 'cx'], 'coupling_map': True},
        'ibm_kyoto': {'qubits': 127, 'basis_gates': ['id', 'rz', 'sx', 'x', 'cx'], 'coupling_map': True},
        'ibm_osaka': {'qubits': 127, 'basis_gates': ['id', 'rz', 'sx', 'x', 'cx'], 'coupling_map': True},
        'simulator_statevector': {'qubits': 32, 'basis_gates': None, 'coupling_map': False},
        'simulator_mps': {'qubits': 100, 'basis_gates': None, 'coupling_map': False},
    }

    # Cost estimates per shot (in USD, approximate)
    COST_PER_SHOT = {
        'ibm_eagle': 0.00125,
        'ibm_condor': 0.00250,
        'ibm_sherbrooke': 0.00125,
        'ibm_brisbane': 0.00125,
        'ibm_kyoto': 0.00125,
        'ibm_osaka': 0.00125,
        'simulator_statevector': 0.0,
        'simulator_mps': 0.0,
    }

    def __init__(self, backend_name: str, token: Optional[str] = None,
                 instance: Optional[str] = None, channel: str = 'ibm_quantum_platform'):
        """
        Initialize IBM Quantum backend.

        Args:
            backend_name: Name of the IBM backend to use
            token: IBM Quantum API token (if not provided, looks for env var)
            instance: IBM Quantum instance (hub/group/project)
            channel: IBM Quantum channel ('ibm_quantum_platform' or 'ibm_cloud')
        """
        if not IBM_QUANTUM_AVAILABLE:
            raise IBMQuantumError(
                "IBM Quantum libraries not available. Install with: "
                "pip install qiskit-ibm-runtime qiskit-ibm-provider"
            )

        self.backend_name = backend_name
        self.channel = channel
        self.instance = instance
        self._service = None
        self._provider = None
        self._backend = None
        self._session = None

        # Get token from environment if not provided
        if token is None:
            token = os.getenv('IBM_QUANTUM_TOKEN')
            if token is None:
                raise AuthenticationError(
                    "IBM Quantum token not found. Provide token parameter or "
                    "set IBM_QUANTUM_TOKEN environment variable."
                )

        self.token = token
        self._initialize_connection()

    @retry_on_failure(max_retries=3)
    def _initialize_connection(self) -> None:
        """Initialize connection to IBM Quantum services."""
        try:
            # Initialize runtime service
            if self.instance:
                self._service = QiskitRuntimeService(
                    channel=self.channel,
                    token=self.token,
                    instance=self.instance
                )
            else:
                self._service = QiskitRuntimeService(
                    channel=self.channel,
                    token=self.token
                )

            # Get the backend
            self._backend = self._service.backend(self.backend_name)

            # Provider functionality is now handled by QiskitRuntimeService
            self._provider = self._service

            logger.info(f"Successfully connected to IBM backend: {self.backend_name}")
            self._log_backend_info()

        except (IBMRuntimeError, IBMAccountError) as e:
            raise AuthenticationError(f"Failed to authenticate with IBM Quantum: {str(e)}")
        except Exception as e:
            if "not found" in str(e).lower():
                available_backends = self.list_available_backends()
                raise BackendNotAvailableError(
                    f"Backend '{self.backend_name}' not found. "
                    f"Available backends: {available_backends}"
                )
            raise IBMQuantumError(f"Failed to initialize IBM Quantum connection: {str(e)}")

    def _log_backend_info(self) -> None:
        """Log information about the selected backend."""
        try:
            config = self._backend.configuration()
            status = self._backend.status()

            logger.info(f"Backend: {config.backend_name}")
            logger.info(f"Qubits: {config.n_qubits}")
            logger.info(f"Operational: {status.operational}")
            logger.info(f"Pending jobs: {status.pending_jobs}")

            if hasattr(status, 'queue_length'):
                logger.info(f"Queue length: {status.queue_length}")

        except Exception as e:
            logger.warning(f"Could not retrieve backend info: {str(e)}")

    def list_available_backends(self) -> List[str]:
        """List all available backends for the current account."""
        try:
            if self._service is None:
                return list(self.KNOWN_BACKENDS.keys())

            backends = self._service.backends()
            return [backend.name for backend in backends]

        except Exception as e:
            logger.warning(f"Could not list backends: {str(e)}")
            return list(self.KNOWN_BACKENDS.keys())

    def get_backend_info(self) -> Dict[str, Any]:
        """Get detailed information about the current backend."""
        try:
            config = self._backend.configuration()
            status = self._backend.status()

            info = {
                'name': config.backend_name,
                'version': getattr(config, 'backend_version', 'unknown'),
                'qubits': config.n_qubits,
                'basis_gates': config.basis_gates,
                'coupling_map': config.coupling_map.get_edges() if hasattr(config, 'coupling_map') and config.coupling_map else None,
                'operational': status.operational,
                'pending_jobs': status.pending_jobs,
                'description': getattr(config, 'description', '')
            }

            if hasattr(status, 'queue_length'):
                info['queue_length'] = status.queue_length

            return info

        except Exception as e:
            logger.error(f"Failed to get backend info: {str(e)}")
            return {'name': self.backend_name, 'error': str(e)}

    def validate_circuit(self, circuit: QuantumCircuit) -> Tuple[bool, str]:
        """Validate if circuit can run on this backend."""
        try:
            config = self._backend.configuration()

            # Check qubit count
            if circuit.num_qubits > config.n_qubits:
                return False, f"Circuit requires {circuit.num_qubits} qubits but backend only has {config.n_qubits}"

            # Check circuit depth (basic check)
            if circuit.depth() > 1000:  # Arbitrary limit
                return False, f"Circuit depth ({circuit.depth()}) may be too large for reliable execution"

            return True, "Circuit validation passed"

        except Exception as e:
            return False, f"Validation failed: {str(e)}"

    def estimate_cost(self, shots: int) -> float:
        """Estimate the cost of running the circuit."""
        base_cost = self.COST_PER_SHOT.get(self.backend_name, 0.001)
        return base_cost * shots

    def estimate_queue_time(self) -> Tuple[Optional[int], str]:
        """Estimate queue waiting time in minutes."""
        try:
            status = self._backend.status()

            if not status.operational:
                return None, "Backend is not operational"

            pending_jobs = status.pending_jobs

            # Rough estimate: assume each job takes 2-5 minutes on average
            if pending_jobs == 0:
                return 0, "No queue"
            elif pending_jobs < 5:
                return pending_jobs * 3, "Short queue"
            elif pending_jobs < 20:
                return pending_jobs * 4, "Medium queue"
            else:
                return pending_jobs * 5, "Long queue"

        except Exception as e:
            logger.warning(f"Could not estimate queue time: {str(e)}")
            return None, "Queue time unknown"

    @retry_on_failure(max_retries=2)
    def execute_circuit(self, circuit: QuantumCircuit, shots: int = 1024,
                       timeout: int = 3600, max_circuits: int = 1) -> QuantumResult:
        """
        Execute a quantum circuit on IBM hardware.

        Args:
            circuit: The quantum circuit to execute
            shots: Number of measurement shots
            timeout: Maximum time to wait for job completion (seconds)
            max_circuits: Maximum number of circuits to run in batch

        Returns:
            QuantumResult containing the computation results
        """
        start_time = time.time()

        try:
            # Check cache first
            cached_result = _circuit_cache.get(circuit, shots, self.backend_name)
            if cached_result is not None:
                logger.info("Returning cached result")
                return cached_result

            # Validate circuit
            valid, message = self.validate_circuit(circuit)
            if not valid:
                raise CircuitTooLargeError(message)

            # Log cost and queue estimates
            cost = self.estimate_cost(shots)
            queue_time, queue_status = self.estimate_queue_time()

            logger.info(f"Estimated cost: ${cost:.4f}")
            logger.info(f"Queue status: {queue_status}")
            if queue_time is not None:
                logger.info(f"Estimated queue time: {queue_time} minutes")

            # Transpile circuit for the backend
            logger.info("Transpiling circuit for backend...")
            transpiled_circuit = transpile(circuit, self._backend, optimization_level=3)

            # For Open plan, use Sampler primitive without session
            logger.info(f"Submitting job to {self.backend_name} with {shots} shots...")

            # Use SamplerV2 for Open plan (no session support)
            from qiskit_ibm_runtime import SamplerV2
            sampler = SamplerV2(mode=self._backend)

            # Create PUB (Primitive Unified Block) for SamplerV2
            pub = (transpiled_circuit, None, shots)
            job = sampler.run([pub])

            logger.info(f"Job submitted with ID: {job.job_id()}")
            logger.info("Waiting for job completion...")

            # Wait for job completion with status updates
            result = self._wait_for_job(job, timeout)

            # Calculate timing
            execution_time = time.time() - start_time

            # Extract counts from SamplerV2 result
            # In SamplerV2, result has data attribute with BitArray
            pub_result = result[0]
            bit_array = pub_result.data.meas
            counts = bit_array.get_counts()
            int_counts = counts

            # Create metadata
            backend_info = self.get_backend_info()
            metadata = {
                'backend': self.backend_name,
                'backend_info': backend_info,
                'shots': shots,
                'circuit_depth': circuit.depth(),
                'num_qubits': circuit.num_qubits,
                'num_clbits': circuit.num_clbits,
                'transpiled_depth': transpiled_circuit.depth(),
                'job_id': job.job_id(),
                'execution_time': execution_time,
                'cost_estimate': cost,
                'queue_estimate': queue_time
            }

            quantum_result = QuantumResult(
                counts=int_counts,
                statevector=None,  # Not available from real hardware
                bio_interpretation={},
                metadata=metadata,
                success=True,
                job_id=job.job_id(),
                backend_name=self.backend_name,
                execution_time=execution_time,
                cost_estimate=cost
            )

            # Cache the result
            _circuit_cache.put(circuit, shots, self.backend_name, quantum_result)

            logger.info(f"Job completed successfully in {execution_time:.1f}s")
            return quantum_result

        except (IBMRuntimeError) as e:
            error_msg = f"IBM Quantum execution failed: {str(e)}"
            logger.error(error_msg)
            return QuantumResult(
                success=False,
                error_message=error_msg,
                metadata={'backend': self.backend_name, 'execution_time': time.time() - start_time}
            )
        except Exception as e:
            error_msg = f"Circuit execution failed: {str(e)}"
            logger.error(error_msg)
            return QuantumResult(
                success=False,
                error_message=error_msg,
                metadata={'backend': self.backend_name, 'execution_time': time.time() - start_time}
            )

    def _wait_for_job(self, job, timeout: int):
        """Wait for job completion with periodic status updates."""
        start_time = time.time()
        last_status = None

        while True:
            try:
                # Check if job is done
                status = job.status()

                if status != last_status:
                    logger.info(f"Job status: {status}")
                    last_status = status

                if job.done():
                    return job.result()

                # Check timeout
                elapsed = time.time() - start_time
                if elapsed > timeout:
                    raise JobTimeoutError(
                        f"Job {job.job_id()} timed out after {timeout}s"
                    )

                # Wait before next status check
                time.sleep(min(30, max(5, timeout // 100)))  # Adaptive polling

            except JobTimeoutError:
                raise
            except Exception as e:
                logger.warning(f"Error checking job status: {str(e)}")
                time.sleep(10)

    def close(self) -> None:
        """Close the IBM Quantum connection."""
        if self._session:
            self._session.close()
        logger.info("IBM Quantum connection closed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class IonQBackend:
    """
    IonQ quantum backend interface using qiskit-ionq provider.

    Supports IonQ quantum computers and simulators through the IonQ Cloud API.
    """

    # Known IonQ backends with their capabilities
    KNOWN_BACKENDS = {
        'ionq_simulator': {'qubits': 29, 'basis_gates': ['rx', 'ry', 'rz', 'cnot'], 'coupling_map': False, 'type': 'simulator'},
        'ionq_qpu': {'qubits': 36, 'basis_gates': ['rx', 'ry', 'rz', 'cnot'], 'coupling_map': False, 'type': 'hardware'},
    }

    # Cost estimates per shot (in USD, approximate)
    COST_PER_SHOT = {
        'ionq_simulator': 0.0,  # Simulator es gratis
        'ionq_qpu': 0.0030,     # Aproximadamente $0.003 por shot en hardware real
    }

    def __init__(self, backend_name: str, token: Optional[str] = None):
        """
        Initialize IonQ backend.

        Args:
            backend_name: Name of the IonQ backend ('ionq_simulator' or 'ionq_qpu')
            token: IonQ API token
        """
        if not IONQ_AVAILABLE:
            raise QuantumBackendError(
                "IonQ libraries not available. Please install qiskit-ionq"
            )

        self.backend_name = backend_name
        self._provider = None
        self._backend = None
        self._token = token

        # Load token from config if not provided
        if not self._token:
            self._token = self._load_token_from_config()

        if not self._token:
            raise AuthenticationError(
                "IonQ token not provided. Use bioql setup-keys to configure or pass token parameter."
            )

        self._initialize_provider()

    def _load_token_from_config(self) -> Optional[str]:
        """Load IonQ token from configuration file."""
        try:
            import json
            from pathlib import Path

            config_file = Path.home() / '.bioql' / 'config.json'
            if config_file.exists():
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    return config.get('ionq_token')
        except Exception as e:
            logger.warning(f"Could not load IonQ token from config: {e}")
        return None

    def _initialize_provider(self):
        """Initialize the IonQ provider."""
        try:
            self._provider = IonQProvider(self._token)
            self._backend = self._provider.get_backend(self.backend_name)
            logger.info(f"Initialized IonQ backend: {self.backend_name}")
        except Exception as e:
            raise QuantumBackendError(f"Failed to initialize IonQ backend: {str(e)}")

    def execute_circuit(self, circuit: QuantumCircuit, shots: int = 1024) -> QuantumResult:
        """
        Execute a quantum circuit on IonQ backend.

        Args:
            circuit: Quantum circuit to execute
            shots: Number of measurement shots

        Returns:
            QuantumResult object with execution results
        """
        if not self._backend:
            raise QuantumBackendError("IonQ backend not initialized")

        start_time = time.time()

        try:
            logger.info(f"Submitting job to {self.backend_name} with {shots} shots...")

            # Transpile circuit for IonQ backend (IonQ recommends optimization_level=1)
            transpiled_circuit = transpile(circuit, self._backend, optimization_level=1)

            # Submit job
            job = self._backend.run(transpiled_circuit, shots=shots)

            # Wait for completion
            logger.info(f"Job submitted. Job ID: {job.job_id()}")
            result = job.result()

            execution_time = time.time() - start_time

            # Get counts
            counts = result.get_counts()

            # Calculate cost estimate
            cost = self.COST_PER_SHOT.get(self.backend_name, 0.01) * shots

            # Create metadata
            metadata = {
                'backend': self.backend_name,
                'shots': shots,
                'circuit_depth': circuit.depth(),
                'num_qubits': circuit.num_qubits,
                'num_clbits': circuit.num_clbits,
                'execution_time': execution_time,
                'cost_estimate': cost,
                'job_id': job.job_id(),
                'provider': 'ionq'
            }

            logger.info(f"Job completed in {execution_time:.2f}s")

            return QuantumResult(
                counts=counts,
                success=True,
                metadata=metadata,
                cost_estimate=cost,
                job_id=job.job_id(),
                backend_name=self.backend_name,
                execution_time=execution_time
            )

        except Exception as e:
            execution_time = time.time() - start_time
            error_msg = f"IonQ execution failed: {str(e)}"
            logger.error(error_msg)

            return QuantumResult(
                counts={},
                success=False,
                error_message=error_msg,
                execution_time=execution_time,
                backend_name=self.backend_name
            )

    def get_backend_info(self) -> Dict[str, Any]:
        """Get information about the IonQ backend."""
        backend_info = self.KNOWN_BACKENDS.get(self.backend_name, {})
        return {
            'name': self.backend_name,
            'provider': 'ionq',
            'qubits': backend_info.get('qubits', 32),
            'basis_gates': backend_info.get('basis_gates', ['rx', 'ry', 'rz', 'cnot']),
            'coupling_map': backend_info.get('coupling_map', False),
            'cost_per_shot': self.COST_PER_SHOT.get(self.backend_name, 0.01),
            'operational': True  # Assume operational
        }

    def list_available_backends(self) -> List[str]:
        """List available IonQ backends."""
        if self._provider:
            try:
                backends = self._provider.backends()
                return [backend.name() for backend in backends]
            except Exception as e:
                logger.warning(f"Could not query IonQ backends: {str(e)}")
                return list(self.KNOWN_BACKENDS.keys())
        else:
            return list(self.KNOWN_BACKENDS.keys())


def select_best_backend(required_qubits: int, prefer_simulator: bool = False,
                       available_backends: Optional[List[str]] = None,
                       service: Optional[Any] = None) -> str:
    """
    Select the best IBM Quantum backend based on requirements.

    Args:
        required_qubits: Minimum number of qubits needed
        prefer_simulator: Whether to prefer simulator backends
        available_backends: List of available backend names (if known)
        service: QiskitRuntimeService instance to query real backends

    Returns:
        Name of the recommended backend

    Raises:
        BackendNotAvailableError: If no suitable backend is found
    """
    # Get available backends
    if available_backends is None and service is not None:
        try:
            backends = service.backends()
            available_backends = [backend.name for backend in backends if backend.operational]
        except Exception as e:
            logger.warning(f"Could not query available backends: {str(e)}")
            available_backends = list(IBMQuantumBackend.KNOWN_BACKENDS.keys())
    elif available_backends is None:
        available_backends = list(IBMQuantumBackend.KNOWN_BACKENDS.keys())

    # Filter by qubit requirements
    suitable_backends = []
    for backend_name in available_backends:
        backend_info = IBMQuantumBackend.KNOWN_BACKENDS.get(backend_name, {})
        backend_qubits = backend_info.get('qubits', 0)

        if backend_qubits >= required_qubits:
            suitable_backends.append((backend_name, backend_info))

    if not suitable_backends:
        raise BackendNotAvailableError(
            f"No backend found with at least {required_qubits} qubits. "
            f"Available backends: {available_backends}"
        )

    # Sort by preference
    def backend_priority(backend_tuple):
        name, info = backend_tuple
        qubits = info.get('qubits', 0)
        is_simulator = 'simulator' in name.lower()

        if prefer_simulator:
            # Prefer simulators, then by qubit count (ascending)
            return (0 if is_simulator else 1, qubits)
        else:
            # Prefer real hardware, then by qubit count (ascending to minimize cost)
            return (1 if is_simulator else 0, qubits)

    suitable_backends.sort(key=backend_priority)
    selected_backend = suitable_backends[0][0]

    logger.info(f"Selected backend: {selected_backend} for {required_qubits} qubits")
    return selected_backend


def get_backend_recommendations(circuit: QuantumCircuit,
                               service: Optional[Any] = None) -> Dict[str, Any]:
    """
    Get backend recommendations for a specific circuit.

    Args:
        circuit: The quantum circuit to analyze
        service: QiskitRuntimeService instance to query real backends

    Returns:
        Dictionary with backend recommendations and analysis
    """
    required_qubits = circuit.num_qubits
    circuit_depth = circuit.depth()

    # Get available backends
    available_backends = []
    if service is not None:
        try:
            backends = service.backends()
            for backend in backends:
                if backend.operational:
                    available_backends.append({
                        'name': backend.name,
                        'qubits': backend.configuration().n_qubits,
                        'pending_jobs': backend.status().pending_jobs,
                        'operational': backend.status().operational
                    })
        except Exception as e:
            logger.warning(f"Could not query backends: {str(e)}")

    # Analyze circuit requirements
    recommendations = {
        'circuit_analysis': {
            'qubits_required': required_qubits,
            'circuit_depth': circuit_depth,
            'complexity': 'low' if circuit_depth < 50 else 'medium' if circuit_depth < 200 else 'high'
        },
        'recommended_backends': {},
        'cost_estimates': {},
        'warnings': []
    }

    # Add recommendations for different categories
    try:
        # Best simulator
        sim_backend = select_best_backend(required_qubits, prefer_simulator=True)
        recommendations['recommended_backends']['best_simulator'] = sim_backend
        recommendations['cost_estimates'][sim_backend] = 0.0

        # Best real hardware
        hw_backend = select_best_backend(required_qubits, prefer_simulator=False)
        recommendations['recommended_backends']['best_hardware'] = hw_backend
        cost = IBMQuantumBackend.COST_PER_SHOT.get(hw_backend, 0.001) * 1024  # Default 1024 shots
        recommendations['cost_estimates'][hw_backend] = cost

        # Add warnings
        if circuit_depth > 100:
            recommendations['warnings'].append(
                f"Circuit depth ({circuit_depth}) is high. Consider circuit optimization."
            )

        if required_qubits > 50:
            recommendations['warnings'].append(
                f"Large circuit ({required_qubits} qubits) will be expensive on real hardware."
            )

    except BackendNotAvailableError as e:
        recommendations['warnings'].append(str(e))

    return recommendations


def parse_bioql_program(program: str) -> QuantumCircuit:
    """
    Parse a BioQL natural language program into a quantum circuit.

    Uses the real BioQL compiler to convert natural language descriptions
    into optimized quantum circuits for biological applications.

    Args:
        program: Natural language description of the quantum program

    Returns:
        Quantum circuit representing the program

    Raises:
        ProgramParsingError: If the program cannot be parsed
    """
    # Real BioQL compiler implementation
    logger.info("Parsing natural language using BioQL compiler")

    try:
        # Use the real BioQL compiler to parse natural language
        from .compiler import BioQLCompiler

        compiler = BioQLCompiler()
        circuit = compiler.parse_to_circuit(program)

        if circuit is None:
            raise ProgramParsingError("Compiler returned None - this should never happen with real BioQL compiler")

        logger.info(f"Parsed program into circuit with {circuit.num_qubits} qubits, {len(circuit.data)} operations")
        return circuit

    except Exception as e:
        logger.error(f"BioQL compiler failed: {e}")
        raise ProgramParsingError(f"Real BioQL compiler failed to parse program: {str(e)}")


def _load_ibm_token_from_config() -> Optional[str]:
    """Load IBM Quantum token from configuration file."""
    try:
        import json
        from pathlib import Path

        config_file = Path.home() / '.bioql' / 'config.json'
        if config_file.exists():
            with open(config_file, 'r') as f:
                config = json.load(f)
                return config.get('ibm_token')
    except Exception as e:
        logger.warning(f"Could not load IBM token from config: {e}")
    return None


def quantum(
    program: str,
    api_key: str,  # NOW REQUIRED - MOVED TO FRONT
    backend: str = 'simulator',
    shots: int = 1024,
    debug: bool = False,
    token: Optional[str] = None,
    instance: Optional[str] = None,
    timeout: int = 3600,
    auto_select: bool = False
) -> QuantumResult:
    """
    Execute a BioQL quantum program.

    This is the main entry point for BioQL quantum computations. It accepts
    natural language descriptions of quantum programs and executes them on
    the specified backend, including real IBM Quantum hardware.

    Args:
        program: Natural language description of the quantum program
        backend: Quantum backend to use. Options include:
                - 'simulator', 'sim', 'aer': Local simulator
                - 'ibm_eagle', 'ibm_condor', etc.: Specific IBM hardware
                - 'auto': Automatically select best backend
        shots: Number of measurement shots to perform
        debug: Whether to enable debug mode with additional logging
        token: IBM Quantum API token (or set IBM_QUANTUM_TOKEN env var)
        instance: IBM Quantum instance (hub/group/project format)
        timeout: Maximum time to wait for job completion (seconds)
        auto_select: Whether to automatically select the best backend for the circuit

    Returns:
        QuantumResult object containing the computation results

    Raises:
        QuantumBackendError: If the backend is not available
        ProgramParsingError: If the program cannot be parsed
        AuthenticationError: If IBM Quantum authentication fails
        JobTimeoutError: If the job times out

    Examples:
        >>> # Run on local simulator (API key required)
        >>> result = quantum("Create a Bell state and measure both qubits",
        ...                  api_key="bioql_your_api_key_here")
        >>> print(result.counts)
        {'00': 512, '11': 512}

        >>> # Run on IBM Eagle hardware
        >>> result = quantum("Put qubit in superposition",
        ...                  backend='ibm_eagle',
        ...                  token='your_token_here')
        >>> print(result.cost_estimate)
        1.28

        >>> # Automatically select best backend
        >>> result = quantum("Generate 3-qubit GHZ state",
        ...                  backend='auto',
        ...                  auto_select=True)
        >>> print(result.backend_name)
        'ibm_sherbrooke'

        >>> # Get cost and queue estimates
        >>> result = quantum("Random circuit",
        ...                  backend='ibm_brisbane',
        ...                  shots=2048,
        ...                  debug=True)
        >>> print(f"Cost: ${result.cost_estimate:.4f}")
        >>> print(f"Queue time: {result.metadata.get('queue_estimate')} min")
    """
    # Configure logging for debug mode
    if debug:
        logging.basicConfig(level=logging.DEBUG)
        logger.setLevel(logging.DEBUG)
        logger.debug(f"Debug mode enabled for program: {program}")

    try:
        # Validate inputs
        if not isinstance(program, str) or not program.strip():
            raise ProgramParsingError("Program must be a non-empty string")

        if shots <= 0:
            raise ValueError("Shots must be a positive integer")

        # MANDATORY API KEY AUTHENTICATION
        # Import cloud authentication module
        from .cloud_auth import authenticate_api_key, check_usage_limits, record_usage

        # Step 1: Authenticate API key (REQUIRED)
        try:
            user_info = authenticate_api_key(api_key)
            logger.debug(f"Authentication successful for user: {user_info.get('email')}")
        except Exception as auth_error:
            raise AuthenticationError(
                f"BioQL API key authentication failed: {auth_error}\n\n"
                f"🔑 Get your API key at: https://bioql.com/signup\n"
                f"📧 Already have an account? Login at: https://bioql.com/login\n"
                f"💡 Need help? Contact: support@bioql.com"
            )

        # Step 2: Check usage limits (REQUIRED)
        try:
            limits_check = check_usage_limits(api_key, shots, backend)
            if not limits_check.get('allowed', False):
                raise ValueError(
                    f"Usage limit exceeded: {limits_check.get('reason')}\n\n"
                    f"💰 Upgrade your plan at: https://bioql.com/pricing\n"
                    f"📊 Check usage at: https://bioql.com/dashboard"
                )

            estimated_cost = limits_check.get('cost', 0.0)
            logger.debug(f"Usage check passed. Estimated cost: ${estimated_cost:.4f}")

        except Exception as limit_error:
            raise ValueError(f"Usage validation failed: {limit_error}")

        # Extract user info for billing
        user_id = user_info.get('user_id')
        api_key_id = user_info.get('api_key_id')

        # Authentication successful - extract user info for tracking
        user_email = user_info.get('email', 'unknown')
        user_plan = user_info.get('plan', 'free')
        logger.info(f"✅ Authenticated user: {user_email} ({user_plan})")

        # Load token from config if not provided
        if not token and backend.startswith('ibm_'):
            token = _load_ibm_token_from_config()

        # Parse the natural language program
        logger.info(f"Parsing BioQL program: {program[:50]}...")
        circuit = parse_bioql_program(program)

        # Determine the actual backend to use
        actual_backend = backend.lower()

        # Handle auto-selection
        if actual_backend == 'auto' or auto_select:
            if IBM_QUANTUM_AVAILABLE and token:
                try:
                    # Try to connect to IBM Quantum for backend selection
                    temp_service = QiskitRuntimeService(token=token, instance=instance) if instance else QiskitRuntimeService(token=token)
                    actual_backend = select_best_backend(
                        circuit.num_qubits,
                        prefer_simulator=False,
                        service=temp_service
                    )
                    logger.info(f"Auto-selected backend: {actual_backend}")
                except Exception as e:
                    logger.warning(f"Auto-selection failed, falling back to simulator: {str(e)}")
                    actual_backend = 'simulator'
            else:
                actual_backend = 'simulator'

        # Show circuit recommendations in debug mode
        if debug:
            try:
                if IBM_QUANTUM_AVAILABLE and token:
                    temp_service = QiskitRuntimeService(token=token, instance=instance) if instance else QiskitRuntimeService(token=token)
                    recommendations = get_backend_recommendations(circuit, temp_service)
                    logger.debug(f"Backend recommendations: {recommendations}")
            except Exception as e:
                logger.debug(f"Could not get recommendations: {str(e)}")

        # Initialize quantum backend
        quantum_backend = None
        if actual_backend in ['simulator', 'sim', 'aer']:
            quantum_backend = QuantumSimulator('aer_simulator')
            logger.info(f"Using local simulator")
        elif actual_backend.startswith('ionq_'):
            # IonQ backend
            if not IONQ_AVAILABLE:
                raise QuantumBackendError(
                    "IonQ not available. Install with: pip install qiskit-ionq"
                )

            logger.info(f"Initializing IonQ backend: {actual_backend}")
            quantum_backend = IonQBackend(
                backend_name=actual_backend,
                token=token
            )

            # Log cost estimate
            cost = IonQBackend.COST_PER_SHOT.get(actual_backend, 0.01) * shots
            logger.info(f"Estimated cost: ${cost:.3f}")

        elif actual_backend.startswith('ibm_') or actual_backend.startswith('simulator_'):
            # IBM Quantum backend
            if not IBM_QUANTUM_AVAILABLE:
                raise QuantumBackendError(
                    "IBM Quantum not available. Install with: pip install qiskit-ibm-runtime qiskit-ibm-provider"
                )

            logger.info(f"Initializing IBM backend: {actual_backend}")
            quantum_backend = IBMQuantumBackend(
                backend_name=actual_backend,
                token=token,
                instance=instance
            )

            # Log cost and queue estimates
            cost = quantum_backend.estimate_cost(shots)
            queue_time, queue_status = quantum_backend.estimate_queue_time()
            logger.info(f"Estimated cost: ${cost:.4f}")
            logger.info(f"Queue status: {queue_status}")
            if queue_time is not None:
                logger.info(f"Estimated queue time: {queue_time} minutes")

        else:
            raise QuantumBackendError(f"Unknown backend '{actual_backend}'. Supported: simulator, ionq_simulator, ionq_qpu, ibm_eagle, ibm_condor, etc.")

        # Execute the circuit
        logger.info(f"Executing circuit on {actual_backend} with {shots} shots")

        if isinstance(quantum_backend, QuantumSimulator):
            result = quantum_backend.execute_circuit(
                circuit,
                shots=shots,
                get_statevector=debug
            )
        elif isinstance(quantum_backend, IonQBackend):
            result = quantum_backend.execute_circuit(
                circuit,
                shots=shots
            )
        else:  # IBM backend
            result = quantum_backend.execute_circuit(
                circuit,
                shots=shots,
                timeout=timeout
            )

        # Add program information to metadata
        result.metadata['original_program'] = program
        result.metadata['backend_requested'] = backend
        result.metadata['backend_used'] = actual_backend

        # Real biological interpretation using bio_interpreter module
        try:
            from .bio_interpreter import interpret_bio_results

            # Detect biological context from program text
            context = "general"
            if "protein" in program.lower() or "folding" in program.lower():
                context = "protein_folding"
            elif "drug" in program.lower() or "binding" in program.lower():
                context = "drug_discovery"
            elif "dna" in program.lower() or "sequence" in program.lower():
                context = "dna_analysis"

            result.bio_interpretation = interpret_bio_results(result.counts, context)

        except ImportError:
            logger.warning("Bio interpreter module not available")
            result.bio_interpretation = {
                'status': 'error',
                'message': 'Bio interpreter module not available'
            }
        except Exception as e:
            logger.error(f"Bio interpretation failed: {e}")
            result.bio_interpretation = {
                'status': 'error',
                'message': f'Bio interpretation failed: {str(e)}'
            }

        if debug:
            logger.debug(f"Execution completed successfully")
            logger.debug(f"Results: {result.counts}")
            logger.debug(f"Metadata: {result.metadata}")

        # Log usage for billing if enabled
        # MANDATORY: Record usage for billing (always enabled)
        try:
            execution_time = result.metadata.get('execution_time', 0) if result.metadata else 0
            actual_shots = getattr(result, 'total_shots', shots)

            # Record usage with cloud service
            record_usage(
                api_key=api_key,
                shots_executed=actual_shots,
                backend=actual_backend,
                cost=estimated_cost,
                success=getattr(result, 'success', True)
            )

            # Add cost info to result
            if hasattr(result, 'metadata'):
                result.metadata['cost_estimate'] = estimated_cost
                result.metadata['billing_status'] = 'recorded'
            else:
                result.metadata = {
                    'cost_estimate': estimated_cost,
                    'billing_status': 'recorded'
                }

            result.cost_estimate = estimated_cost
            logger.info(f"💰 Usage recorded: {actual_shots} shots, ${estimated_cost:.4f}")

        except Exception as e:
            logger.warning(f"⚠️  Usage recording failed: {e}")
            # Don't fail the execution, but warn user
            if hasattr(result, 'metadata'):
                result.metadata['billing_status'] = 'failed'

        # Clean up IBM backend connection
        if isinstance(quantum_backend, IBMQuantumBackend):
            quantum_backend.close()

        return result

    except Exception as e:
        logger.error(f"Quantum execution failed: {str(e)}")

        # Record failed usage (only if we got past authentication)
        if 'api_key' in locals() and api_key:
            try:
                record_usage(
                    api_key=api_key,
                    shots_executed=0,  # No shots executed on failure
                    backend=backend,
                    cost=0.0,  # No cost for failed executions
                    success=False
                )
                logger.info(f"🚫 Failed execution recorded for billing")
            except Exception as billing_error:
                logger.warning(f"⚠️  Failed to record failed usage: {billing_error}")

        return QuantumResult(
            success=False,
            error_message=str(e),
            metadata={
                'original_program': program,
                'backend_requested': backend,
                'backend_used': actual_backend if 'actual_backend' in locals() else backend
            }
        )


def list_available_backends(token: Optional[str] = None,
                           instance: Optional[str] = None) -> Dict[str, Any]:
    """
    List all available quantum backends and their status.

    Args:
        token: IBM Quantum API token
        instance: IBM Quantum instance

    Returns:
        Dictionary with backend information
    """
    backends_info = {
        'simulators': {},
        'ibm_hardware': {},
        'ionq_hardware': {},
        'status': 'success',
        'error': None
    }

    # Add simulator backends
    backends_info['simulators']['aer_simulator'] = {
        'qubits': 'unlimited',
        'cost_per_shot': 0.0,
        'queue_length': 0,
        'operational': True,
        'description': 'Local Qiskit Aer simulator'
    }

    # Add known IonQ backends
    for backend_name, info in IonQBackend.KNOWN_BACKENDS.items():
        if 'simulator' in backend_name:
            backends_info['simulators'][backend_name] = {
                'qubits': info['qubits'],
                'cost_per_shot': IonQBackend.COST_PER_SHOT.get(backend_name, 0.0),
                'queue_length': 0,
                'operational': True,
                'description': 'IonQ cloud simulator'
            }
        else:
            backends_info['ionq_hardware'][backend_name] = {
                'qubits': info['qubits'],
                'cost_per_shot': IonQBackend.COST_PER_SHOT.get(backend_name, 0.01),
                'queue_length': 'N/A',
                'operational': 'N/A',
                'description': 'IonQ quantum computer'
            }

    # Add known IBM backends
    for backend_name, info in IBMQuantumBackend.KNOWN_BACKENDS.items():
        if 'simulator' in backend_name:
            backends_info['simulators'][backend_name] = {
                'qubits': info['qubits'],
                'cost_per_shot': IBMQuantumBackend.COST_PER_SHOT.get(backend_name, 0.0),
                'queue_length': 'N/A',
                'operational': 'N/A',
                'description': 'IBM Quantum simulator'
            }
        else:
            backends_info['ibm_hardware'][backend_name] = {
                'qubits': info['qubits'],
                'cost_per_shot': IBMQuantumBackend.COST_PER_SHOT.get(backend_name, 0.001),
                'queue_length': 'Unknown',
                'operational': 'Unknown',
                'description': 'IBM Quantum hardware'
            }

    # Try to get real-time status if token is provided
    if token and IBM_QUANTUM_AVAILABLE:
        try:
            service = QiskitRuntimeService(
                token=token,
                instance=instance
            ) if instance else QiskitRuntimeService(token=token)

            live_backends = service.backends()
            for backend in live_backends:
                config = backend.configuration()
                status = backend.status()

                backend_info = {
                    'qubits': config.n_qubits,
                    'cost_per_shot': IBMQuantumBackend.COST_PER_SHOT.get(backend.name, 0.001),
                    'queue_length': status.pending_jobs,
                    'operational': status.operational,
                    'description': getattr(config, 'description', 'IBM Quantum hardware')
                }

                if 'simulator' in backend.name:
                    backends_info['simulators'][backend.name] = backend_info
                else:
                    backends_info['ibm_hardware'][backend.name] = backend_info

        except Exception as e:
            backends_info['error'] = f"Could not get live backend status: {str(e)}"
            backends_info['status'] = 'partial'

    return backends_info


def estimate_job_cost(circuit: QuantumCircuit, backend: str, shots: int = 1024) -> Dict[str, Any]:
    """
    Estimate the cost and time for running a circuit.

    Args:
        circuit: The quantum circuit to analyze
        backend: Target backend name
        shots: Number of shots

    Returns:
        Dictionary with cost and time estimates
    """
    cost_info = {
        'backend': backend,
        'shots': shots,
        'cost_usd': 0.0,
        'time_estimate_minutes': 0,
        'warnings': [],
        'recommendations': []
    }

    # Calculate cost
    if backend in IBMQuantumBackend.COST_PER_SHOT:
        cost_info['cost_usd'] = IBMQuantumBackend.COST_PER_SHOT[backend] * shots
    elif backend.startswith('ibm_'):
        cost_info['cost_usd'] = 0.001 * shots  # Default estimate
    else:
        cost_info['cost_usd'] = 0.0  # Simulators are free

    # Estimate time
    if 'simulator' in backend.lower():
        cost_info['time_estimate_minutes'] = max(1, circuit.depth() // 100)  # Very rough estimate
    else:
        # For real hardware, factor in queue time
        cost_info['time_estimate_minutes'] = 5 + (circuit.depth() // 50)  # Basic estimate

    # Add warnings and recommendations
    if circuit.num_qubits > 50:
        cost_info['warnings'].append(f"Large circuit ({circuit.num_qubits} qubits) will be expensive")

    if circuit.depth() > 200:
        cost_info['warnings'].append(f"Deep circuit ({circuit.depth()} depth) may have low fidelity on hardware")
        cost_info['recommendations'].append("Consider circuit optimization or use simulator for testing")

    if cost_info['cost_usd'] > 10.0:
        cost_info['warnings'].append(f"High cost estimate: ${cost_info['cost_usd']:.2f}")
        cost_info['recommendations'].append("Consider reducing shots or using a simulator")

    return cost_info


def main():
    """Command-line interface for the quantum connector."""
    import argparse

    parser = argparse.ArgumentParser(
        description='BioQL Quantum Connector with IBM Quantum Integration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run on local simulator
  bioql-quantum "Create Bell state" --backend simulator

  # Run on IBM Eagle hardware
  bioql-quantum "Create Bell state" --backend ibm_eagle --token YOUR_TOKEN

  # Auto-select best backend
  bioql-quantum "3-qubit GHZ state" --backend auto --token YOUR_TOKEN

  # List available backends
  bioql-quantum --list-backends --token YOUR_TOKEN

  # Estimate cost
  bioql-quantum "Random circuit" --estimate-cost --backend ibm_brisbane
        """
    )

    # Main arguments
    parser.add_argument('program', nargs='?', help='BioQL program to execute')
    parser.add_argument('--backend', default='simulator',
                       help='Quantum backend (simulator, ibm_eagle, auto, etc.)')
    parser.add_argument('--shots', type=int, default=1024, help='Number of shots')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    # IBM Quantum arguments
    parser.add_argument('--token', help='IBM Quantum API token')
    parser.add_argument('--instance', help='IBM Quantum instance (hub/group/project)')
    parser.add_argument('--timeout', type=int, default=3600,
                       help='Job timeout in seconds')
    parser.add_argument('--auto-select', action='store_true',
                       help='Automatically select best backend')

    # Utility arguments
    parser.add_argument('--list-backends', action='store_true',
                       help='List available backends and exit')
    parser.add_argument('--estimate-cost', action='store_true',
                       help='Estimate cost without running')

    args = parser.parse_args()

    # Handle utility commands
    if args.list_backends:
        backends = list_available_backends(args.token, args.instance)
        print("\n=== Available Quantum Backends ===")

        print("\n--- Simulators ---")
        for name, info in backends['simulators'].items():
            status = "✓" if info['operational'] else "✗"
            print(f"{status} {name:20} | {info['qubits']:>6} qubits | ${info['cost_per_shot']:.4f}/shot")

        print("\n--- IBM Hardware ---")
        for name, info in backends['ibm_hardware'].items():
            status = "✓" if info['operational'] else "?"
            queue = f"{info['queue_length']} jobs" if isinstance(info['queue_length'], int) else info['queue_length']
            print(f"{status} {name:20} | {info['qubits']:>6} qubits | ${info['cost_per_shot']:.4f}/shot | Queue: {queue}")

        if backends['error']:
            print(f"\nNote: {backends['error']}")

        return

    # Require program for other operations
    if not args.program:
        parser.error("Program is required unless using --list-backends")

    if args.estimate_cost:
        # Parse program and estimate cost
        circuit = parse_bioql_program(args.program)
        estimate = estimate_job_cost(circuit, args.backend, args.shots)

        print(f"\n=== Cost Estimate ===")
        print(f"Backend: {estimate['backend']}")
        print(f"Circuit: {circuit.num_qubits} qubits, {circuit.depth()} depth")
        print(f"Shots: {estimate['shots']}")
        print(f"Estimated cost: ${estimate['cost_usd']:.4f}")
        print(f"Estimated time: {estimate['time_estimate_minutes']} minutes")

        if estimate['warnings']:
            print("\nWarnings:")
            for warning in estimate['warnings']:
                print(f"  ⚠ {warning}")

        if estimate['recommendations']:
            print("\nRecommendations:")
            for rec in estimate['recommendations']:
                print(f"  💡 {rec}")

        return

    # Execute the quantum program
    result = quantum(
        args.program,
        backend=args.backend,
        shots=args.shots,
        debug=args.debug,
        token=args.token,
        instance=args.instance,
        timeout=args.timeout,
        auto_select=args.auto_select
    )

    # Display results
    print(f"\n=== Quantum Execution Results ===")
    if result.success:
        print(f"✓ Execution successful!")
        print(f"Backend: {result.metadata.get('backend_used', args.backend)}")

        if result.job_id:
            print(f"Job ID: {result.job_id}")

        if result.execution_time:
            print(f"Execution time: {result.execution_time:.1f}s")

        if result.cost_estimate:
            print(f"Cost: ${result.cost_estimate:.4f}")

        print(f"\nResults:")
        print(f"Total shots: {result.total_shots}")
        print(f"Most likely outcome: {result.most_likely_outcome}")

        print(f"\nCounts:")
        for outcome, count in sorted(result.counts.items()):
            probability = count / result.total_shots
            print(f"  {outcome}: {count:4d} ({probability:.3f})")

        if args.debug and result.metadata:
            print(f"\nMetadata: {result.metadata}")

    else:
        print(f"✗ Execution failed: {result.error_message}")

        if result.metadata.get('backend_used'):
            print(f"Backend: {result.metadata['backend_used']}")

        return 1

    return 0


# Billing-aware quantum function factory
def get_quantum_function(billing_enabled: bool = None) -> Callable:
    """
    Get quantum function with optional billing integration.

    This factory function returns either the original quantum() function
    or a billing-enabled version depending on configuration.

    Args:
        billing_enabled: Override billing configuration (optional)

    Returns:
        Quantum function (with or without billing)

    Examples:
        >>> # Get standard quantum function
        >>> quantum_func = get_quantum_function(billing_enabled=False)
        >>> result = quantum_func("Create Bell state")
        >>>
        >>> # Get billing-enabled quantum function
        >>> quantum_with_billing = get_quantum_function(billing_enabled=True)
        >>> result = quantum_with_billing("Create Bell state", api_key="your_key")
        >>> print(result.billing_metadata)
    """
    # Determine if billing should be enabled
    use_billing = billing_enabled
    if use_billing is None:
        use_billing = BILLING_ENABLED and BILLING_INTEGRATION_AVAILABLE

    if use_billing and BILLING_INTEGRATION_AVAILABLE:
        logger.info("Creating billing-enabled quantum function")
        return create_billing_quantum_function()
    else:
        logger.info("Using standard quantum function (billing disabled)")
        return quantum


# Convenience function that automatically detects billing availability
def quantum_auto(*args, **kwargs):
    """
    Quantum function that automatically uses billing if available.

    This function automatically detects if billing integration is available
    and uses it if configured. Falls back to standard quantum() if not.

    Usage is identical to quantum() but with optional billing parameters:
    - api_key: BioQL API key for user authentication
    - user_id: Direct user ID (for internal use)
    - session_id: Session ID for grouping operations
    """
    if BILLING_ENABLED and BILLING_INTEGRATION_AVAILABLE:
        # Extract billing parameters
        billing_params = {}
        for param in ['api_key', 'user_id', 'session_id', 'client_ip', 'user_agent']:
            if param in kwargs:
                billing_params[param] = kwargs.pop(param)

        # Use billing-enabled function
        billing_quantum = create_billing_quantum_function()
        return billing_quantum(*args, **kwargs, **billing_params)
    else:
        # Remove billing parameters and use standard function
        for param in ['api_key', 'user_id', 'session_id', 'client_ip', 'user_agent']:
            kwargs.pop(param, None)

        result = quantum(*args, **kwargs)

        # Add empty billing metadata for consistency
        if hasattr(result, 'billing_metadata'):
            result.billing_metadata = {
                'billing_enabled': False,
                'reason': 'Billing integration not available or disabled'
            }

        return result


# Module-level utilities
def enable_billing() -> Dict[str, Any]:
    """
    Enable billing integration for this module.

    Returns:
        Dictionary with enablement status
    """
    global BILLING_ENABLED

    if not BILLING_INTEGRATION_AVAILABLE:
        return {
            'success': False,
            'error': 'Billing integration not available. Check billing_integration module.'
        }

    BILLING_ENABLED = True
    return {
        'success': True,
        'message': 'Billing integration enabled for quantum_connector module'
    }


def disable_billing() -> Dict[str, Any]:
    """
    Disable billing integration for this module.

    Returns:
        Dictionary with disablement status
    """
    global BILLING_ENABLED
    BILLING_ENABLED = False
    return {
        'success': True,
        'message': 'Billing integration disabled for quantum_connector module'
    }


def get_integration_status() -> Dict[str, Any]:
    """
    Get status of billing integration.

    Returns:
        Dictionary with integration status information
    """
    status = {
        'billing_integration_available': BILLING_INTEGRATION_AVAILABLE,
        'billing_enabled': BILLING_ENABLED,
        'quantum_connector_version': '2.0.0-billing'
    }

    if BILLING_INTEGRATION_AVAILABLE:
        status['billing_system_status'] = get_billing_status()

    return status


if __name__ == '__main__':
    main()