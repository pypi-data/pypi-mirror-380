"""
Comprehensive Test Suite for BioQL Quantum Module

Tests for the core quantum() function, QuantumResult class, QuantumSimulator,
and related quantum computing functionality.
"""

import pytest
import numpy as np
import time
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, List, Any

from bioql import quantum, QuantumResult, QuantumSimulator
from bioql.quantum_connector import (
    BioQLError, QuantumBackendError, ProgramParsingError,
    parse_bioql_program
)

try:
    from qiskit import QuantumCircuit
    QISKIT_AVAILABLE = True
except ImportError:
    QISKIT_AVAILABLE = False


class TestQuantumResult:
    """Test cases for the QuantumResult class."""

    def test_quantum_result_creation_success(self):
        """Test successful QuantumResult creation."""
        counts = {'00': 512, '11': 512}
        statevector = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
        metadata = {'shots': 1024, 'backend': 'aer_simulator'}

        result = QuantumResult(
            counts=counts,
            statevector=statevector,
            metadata=metadata,
            success=True
        )

        assert result.counts == counts
        assert np.array_equal(result.statevector, statevector)
        assert result.metadata == metadata
        assert result.success is True
        assert result.error_message is None

    def test_quantum_result_creation_failure(self):
        """Test QuantumResult creation for failed computation."""
        error_msg = "Circuit execution failed"
        result = QuantumResult(
            success=False,
            error_message=error_msg
        )

        assert result.success is False
        assert result.error_message == error_msg
        assert result.counts == {}

    def test_quantum_result_validation_error(self):
        """Test that QuantumResult validation catches invalid states."""
        with pytest.raises(ValueError, match="Failed results must include an error message"):
            QuantumResult(success=False, error_message=None)

    def test_total_shots_property(self, sample_quantum_result):
        """Test the total_shots property calculation."""
        assert sample_quantum_result.total_shots == 1024

        # Test with empty counts
        empty_result = QuantumResult()
        assert empty_result.total_shots == 0

    def test_most_likely_outcome_property(self, sample_quantum_result):
        """Test the most_likely_outcome property."""
        # Both outcomes have equal probability in the fixture
        outcome = sample_quantum_result.most_likely_outcome
        assert outcome in ['00', '11']

        # Test with empty counts
        empty_result = QuantumResult()
        assert empty_result.most_likely_outcome is None

        # Test with unequal probabilities
        unequal_result = QuantumResult(counts={'0': 800, '1': 200})
        assert unequal_result.most_likely_outcome == '0'

    def test_probabilities_method(self, sample_quantum_result):
        """Test the probabilities method."""
        probs = sample_quantum_result.probabilities()

        expected_probs = {'00': 0.5, '11': 0.5}
        assert probs == expected_probs

        # Test with empty counts
        empty_result = QuantumResult()
        assert empty_result.probabilities() == {}

    def test_quantum_result_with_additional_fields(self):
        """Test QuantumResult with optional fields."""
        result = QuantumResult(
            counts={'0': 500, '1': 500},
            job_id='test_job_123',
            backend_name='ibmq_qasm_simulator',
            execution_time=1.5,
            queue_time=30.0,
            cost_estimate=0.05
        )

        assert result.job_id == 'test_job_123'
        assert result.backend_name == 'ibmq_qasm_simulator'
        assert result.execution_time == 1.5
        assert result.queue_time == 30.0
        assert result.cost_estimate == 0.05


class TestQuantumSimulator:
    """Test cases for the QuantumSimulator class."""

    @pytest.mark.requires_qiskit
    def test_quantum_simulator_initialization(self):
        """Test QuantumSimulator initialization."""
        simulator = QuantumSimulator('aer_simulator')
        assert simulator.backend_name == 'aer_simulator'
        assert simulator.backend is not None

    def test_quantum_simulator_initialization_without_qiskit(self, mock_qiskit_unavailable):
        """Test QuantumSimulator initialization fails without Qiskit."""
        with pytest.raises(QuantumBackendError, match="Qiskit not available"):
            QuantumSimulator()

    @pytest.mark.requires_qiskit
    def test_execute_circuit_success(self, bell_state_circuit):
        """Test successful circuit execution."""
        simulator = QuantumSimulator()
        result = simulator.execute_circuit(bell_state_circuit, shots=100)

        assert result.success is True
        assert result.error_message is None
        assert isinstance(result.counts, dict)
        assert result.total_shots == 100
        assert result.metadata['backend'] == 'aer_simulator'
        assert result.metadata['shots'] == 100
        assert result.metadata['num_qubits'] == 2

    @pytest.mark.requires_qiskit
    def test_execute_circuit_with_statevector(self, superposition_circuit):
        """Test circuit execution with statevector calculation."""
        simulator = QuantumSimulator()
        result = simulator.execute_circuit(
            superposition_circuit,
            shots=1000,
            get_statevector=True
        )

        assert result.success is True
        assert result.statevector is not None
        assert isinstance(result.statevector, np.ndarray)

    @pytest.mark.requires_qiskit
    def test_execute_circuit_handles_backend_error(self, simple_circuit):
        """Test that circuit execution handles backend errors gracefully."""
        simulator = QuantumSimulator()

        # Mock the backend to raise an exception
        with patch.object(simulator.backend, 'run', side_effect=Exception("Backend error")):
            result = simulator.execute_circuit(simple_circuit)

            assert result.success is False
            assert "Circuit execution failed" in result.error_message
            assert "Backend error" in result.error_message


class TestParseBioQLProgram:
    """Test cases for the parse_bioql_program function."""

    @pytest.mark.requires_qiskit
    def test_parse_bell_state_program(self):
        """Test parsing Bell state programs."""
        programs = [
            "Create a Bell state",
            "Generate entangled Bell pair",
            "entangle two qubits"
        ]

        for program in programs:
            circuit = parse_bioql_program(program)
            assert isinstance(circuit, QuantumCircuit)
            assert circuit.num_qubits == 2
            assert circuit.num_clbits == 2

    @pytest.mark.requires_qiskit
    def test_parse_superposition_program(self):
        """Test parsing superposition programs."""
        programs = [
            "Put qubit in superposition",
            "Create superposition state",
            "Apply superposition to qubit"
        ]

        for program in programs:
            circuit = parse_bioql_program(program)
            assert isinstance(circuit, QuantumCircuit)
            assert circuit.num_qubits == 2  # Default circuit size

    @pytest.mark.requires_qiskit
    def test_parse_random_program(self):
        """Test parsing random bit generation programs."""
        programs = [
            "Generate random bit",
            "Create quantum random number",
            "Make random outcome"
        ]

        for program in programs:
            circuit = parse_bioql_program(program)
            assert isinstance(circuit, QuantumCircuit)

    @pytest.mark.requires_qiskit
    def test_parse_unknown_program(self):
        """Test parsing unknown/default programs."""
        circuit = parse_bioql_program("Unknown quantum operation")
        assert isinstance(circuit, QuantumCircuit)
        assert circuit.num_qubits == 2

    def test_parse_program_with_exception(self):
        """Test parse_bioql_program handles exceptions."""
        with patch('bioql.quantum_connector.QuantumCircuit', side_effect=Exception("Mock error")):
            with pytest.raises(ProgramParsingError, match="Failed to parse program"):
                parse_bioql_program("test program")


class TestQuantumFunction:
    """Test cases for the main quantum() function."""

    @pytest.mark.requires_qiskit
    def test_quantum_function_basic_usage(self):
        """Test basic usage of the quantum() function."""
        result = quantum("Create a Bell state", shots=100)

        assert isinstance(result, QuantumResult)
        assert result.success is True
        assert result.total_shots == 100
        assert result.metadata['original_program'] == "Create a Bell state"
        assert result.metadata['backend_requested'] == 'simulator'

    @pytest.mark.requires_qiskit
    def test_quantum_function_different_backends(self):
        """Test quantum() function with different backend specifications."""
        backends = ['simulator', 'sim', 'aer']

        for backend in backends:
            result = quantum("Create superposition", backend=backend, shots=50)
            assert result.success is True
            assert result.metadata['backend_requested'] == backend

    def test_quantum_function_unsupported_backend(self):
        """Test quantum() function with unsupported backend."""
        result = quantum("test", backend='unsupported_backend')

        assert result.success is False
        assert "Backend 'unsupported_backend' not supported" in result.error_message

    @pytest.mark.requires_qiskit
    def test_quantum_function_debug_mode(self):
        """Test quantum() function with debug mode enabled."""
        with patch('bioql.quantum_connector.logger') as mock_logger:
            result = quantum("Create Bell state", debug=True, shots=10)

            assert result.success is True
            assert result.statevector is not None  # Debug mode gets statevector
            mock_logger.debug.assert_called()

    def test_quantum_function_input_validation(self):
        """Test quantum() function input validation."""
        # Test empty program
        result = quantum("")
        assert result.success is False
        assert "non-empty string" in result.error_message

        # Test None program
        result = quantum(None)
        assert result.success is False

        # Test invalid shots
        result = quantum("test", shots=0)
        assert result.success is False
        assert "positive integer" in result.error_message

        result = quantum("test", shots=-10)
        assert result.success is False

    @pytest.mark.requires_qiskit
    def test_quantum_function_with_bio_interpretation_real(self):
        """Test that quantum() function includes real bio interpretation."""
        result = quantum("Create Bell state", shots=100)

        assert 'bio_interpretation' in result.__dict__
        assert result.bio_interpretation['status'] == 'success'
        assert 'biological_context' in result.bio_interpretation

    @pytest.mark.parametrize("program,expected_shots", [
        ("Create Bell state", 1024),
        ("Generate superposition", 2048),
        ("Random bit", 512)
    ])
    @pytest.mark.requires_qiskit
    def test_quantum_function_parameterized_shots(self, program, expected_shots):
        """Test quantum() function with parameterized shots."""
        result = quantum(program, shots=expected_shots)

        assert result.success is True
        assert result.total_shots == expected_shots

    @pytest.mark.requires_qiskit
    def test_quantum_function_handles_parsing_error(self):
        """Test quantum() function handles parsing errors gracefully."""
        with patch('bioql.quantum_connector.parse_bioql_program',
                  side_effect=ProgramParsingError("Parse error")):
            result = quantum("test program")

            assert result.success is False
            assert "Parse error" in result.error_message


class TestQuantumFunctionIntegration:
    """Integration tests for the quantum() function with different scenarios."""

    @pytest.mark.requires_qiskit
    @pytest.mark.integration
    def test_bell_state_generation(self):
        """Test Bell state generation and verify outcomes."""
        result = quantum("Create a Bell state", shots=1000)

        assert result.success is True

        # Bell state should primarily produce '00' and '11' outcomes
        bell_outcomes = result.counts.get('00', 0) + result.counts.get('11', 0)
        total_shots = result.total_shots
        bell_fidelity = bell_outcomes / total_shots

        # Bell state should have high fidelity (allowing for noise)
        assert bell_fidelity >= 0.85, f"Bell fidelity {bell_fidelity} too low"

    @pytest.mark.requires_qiskit
    @pytest.mark.integration
    def test_superposition_generation(self):
        """Test superposition state generation."""
        result = quantum("Put qubit in superposition", shots=2000)

        assert result.success is True

        # Superposition should produce roughly equal '0' and '1' outcomes
        if '0' in result.counts and '1' in result.counts:
            prob_0 = result.counts['0'] / result.total_shots
            prob_1 = result.counts['1'] / result.total_shots

            # Allow for statistical variation (�0.1)
            assert abs(prob_0 - 0.5) < 0.1, f"Superposition not balanced: {prob_0:.3f}"
            assert abs(prob_1 - 0.5) < 0.1, f"Superposition not balanced: {prob_1:.3f}"

    @pytest.mark.requires_qiskit
    @pytest.mark.integration
    def test_multiple_consecutive_calls(self):
        """Test multiple consecutive calls to quantum() function."""
        programs = [
            "Create Bell state",
            "Generate superposition",
            "Random bit"
        ]

        results = []
        for program in programs:
            result = quantum(program, shots=100)
            assert result.success is True
            results.append(result)

        # Verify all results are independent
        assert len(results) == 3
        for i, result in enumerate(results):
            assert result.metadata['original_program'] == programs[i]

    @pytest.mark.requires_qiskit
    @pytest.mark.slow
    def test_large_circuit_execution(self):
        """Test execution of larger quantum circuits."""
        result = quantum("Create Bell state", shots=10000)

        assert result.success is True
        assert result.total_shots == 10000

        # Check execution completes in reasonable time
        assert result.metadata.get('execution_time', 0) < 10.0  # seconds


class TestQuantumFunctionErrorConditions:
    """Test error conditions and edge cases for quantum functions."""

    def test_quantum_without_qiskit(self, mock_qiskit_unavailable):
        """Test quantum() function behavior when Qiskit is unavailable."""
        result = quantum("test program")
        assert result.success is False
        assert "Qiskit not available" in result.error_message

    @pytest.mark.requires_qiskit
    def test_quantum_with_circuit_execution_failure(self):
        """Test quantum() function when circuit execution fails."""
        with patch('bioql.quantum_connector.QuantumSimulator.execute_circuit') as mock_execute:
            mock_execute.return_value = QuantumResult(
                success=False,
                error_message="Mock execution failure"
            )

            result = quantum("test program")
            assert result.success is False
            assert "Mock execution failure" in result.error_message

    @pytest.mark.parametrize("invalid_input", [
        "",
        "   ",
        None,
        123,
        []
    ])
    def test_quantum_with_invalid_inputs(self, invalid_input):
        """Test quantum() function with various invalid inputs."""
        result = quantum(invalid_input)
        assert result.success is False
        assert result.error_message is not None

    @pytest.mark.requires_qiskit
    def test_quantum_with_backend_initialization_failure(self):
        """Test quantum() function when backend initialization fails."""
        with patch('bioql.quantum_connector.QuantumSimulator') as mock_simulator:
            mock_simulator.side_effect = QuantumBackendError("Backend init failed")

            result = quantum("test program", backend='simulator')
            assert result.success is False
            assert "Backend init failed" in result.error_message


class TestQuantumFunctionBiologyContext:
    """Test quantum() function with biology-specific programs."""

    @pytest.mark.requires_qiskit
    @pytest.mark.bio
    def test_protein_folding_program(self):
        """Test quantum() with protein folding programs."""
        programs = [
            "Simulate protein folding energy landscape",
            "Model protein structure optimization",
            "Analyze protein conformation states"
        ]

        for program in programs:
            result = quantum(program, shots=1000)
            assert result.success is True
            assert result.metadata['original_program'] == program

    @pytest.mark.requires_qiskit
    @pytest.mark.bio
    def test_drug_discovery_program(self):
        """Test quantum() with drug discovery programs."""
        programs = [
            "Model drug-target binding affinity",
            "Simulate molecular docking",
            "Optimize pharmaceutical compounds"
        ]

        for program in programs:
            result = quantum(program, shots=500)
            assert result.success is True

    @pytest.mark.requires_qiskit
    @pytest.mark.bio
    def test_dna_analysis_program(self):
        """Test quantum() with DNA analysis programs."""
        programs = [
            "Analyze DNA sequence patterns",
            "Model genetic variations",
            "Simulate DNA-protein interactions"
        ]

        for program in programs:
            result = quantum(program, shots=800)
            assert result.success is True


class TestQuantumFunctionPerformance:
    """Performance tests for quantum() function."""

    @pytest.mark.requires_qiskit
    @pytest.mark.slow
    def test_quantum_function_performance_small_circuit(self, performance_test_params):
        """Test performance with small quantum circuits."""
        params = performance_test_params['small_circuit']

        start_time = time.time()
        result = quantum("Create Bell state", shots=params['shots'])
        execution_time = time.time() - start_time

        assert result.success is True
        assert execution_time < 5.0  # Should complete within 5 seconds

    @pytest.mark.requires_qiskit
    @pytest.mark.slow
    def test_quantum_function_performance_medium_circuit(self, performance_test_params):
        """Test performance with medium quantum circuits."""
        params = performance_test_params['medium_circuit']

        start_time = time.time()
        result = quantum("Generate superposition", shots=params['shots'])
        execution_time = time.time() - start_time

        assert result.success is True
        assert execution_time < 10.0  # Should complete within 10 seconds

    @pytest.mark.requires_qiskit
    @pytest.mark.integration
    def test_quantum_function_memory_usage(self):
        """Test memory usage doesn't grow excessively with multiple calls."""
        import psutil
        import os

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss

        # Execute multiple quantum programs
        for i in range(10):
            result = quantum(f"Create Bell state iteration {i}", shots=100)
            assert result.success is True

        final_memory = process.memory_info().rss
        memory_growth = (final_memory - initial_memory) / 1024 / 1024  # MB

        # Memory growth should be reasonable (less than 100MB for 10 iterations)
        assert memory_growth < 100, f"Memory growth too high: {memory_growth:.1f}MB"


class TestQuantumResultDocstrings:
    """Test that docstring examples work correctly."""

    @pytest.mark.requires_qiskit
    def test_quantum_docstring_examples(self):
        """Test the examples from quantum() function docstring."""
        # Example 1: Bell state
        result = quantum("Create a Bell state and measure both qubits")
        assert result.success is True
        assert '00' in result.counts or '11' in result.counts

        # Example 2: Superposition
        result = quantum("Put qubit in superposition", shots=2048)
        assert result.success is True
        most_likely = result.most_likely_outcome
        assert most_likely is not None

        # Example 3: Random bit with debug
        result = quantum("Generate random bit", debug=True)
        assert result.success is True
        assert isinstance(result.bio_interpretation, dict)


# Helper test functions for complex scenarios
class TestComplexQuantumScenarios:
    """Test complex quantum computing scenarios."""

    @pytest.mark.requires_qiskit
    @pytest.mark.integration
    def test_quantum_teleportation_simulation(self):
        """Test simulation of quantum teleportation protocol."""
        # This is a simplified test of a complex quantum protocol
        result = quantum("Entangle qubits for teleportation protocol", shots=1024)
        assert result.success is True

    @pytest.mark.requires_qiskit
    @pytest.mark.integration
    def test_quantum_fourier_transform_simulation(self):
        """Test simulation of quantum Fourier transform."""
        result = quantum("Apply quantum Fourier transform", shots=2048)
        assert result.success is True

    @pytest.mark.requires_qiskit
    @pytest.mark.bio
    @pytest.mark.integration
    def test_variational_quantum_eigensolver_simulation(self):
        """Test VQE simulation for molecular chemistry."""
        result = quantum("Optimize molecular ground state energy", shots=1000)
        assert result.success is True
        assert result.bio_interpretation is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])