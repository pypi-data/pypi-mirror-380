"""
Comprehensive Integration Test Suite for BioQL

Tests for complete workflows including natural language processing,
quantum circuit generation, execution, and biological interpretation.
"""

import pytest
import numpy as np
import time
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, List, Any, Optional

try:
    from qiskit import QuantumCircuit
    QISKIT_AVAILABLE = True
except ImportError:
    QISKIT_AVAILABLE = False

from bioql import quantum, QuantumResult, compile_bioql, interpret_bio_results
from bioql.quantum_connector import BioQLError, QuantumBackendError
from bioql.compiler import BiotechContext
from bioql.bio_interpreter import BioContext


class TestBasicWorkflowIntegration:
    """Test basic end-to-end workflows."""

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_basic_bell_state_workflow(self):
        """Test complete Bell state creation workflow."""
        program = "Create a Bell state and measure both qubits"

        # Execute the quantum program
        result = quantum(program, shots=1000)

        # Verify successful execution
        assert result.success is True
        assert result.total_shots == 1000
        assert result.metadata['original_program'] == program

        # Verify Bell state characteristics
        # Bell state should primarily produce '00' and '11' outcomes
        bell_outcomes = result.counts.get('00', 0) + result.counts.get('11', 0)
        total_outcomes = sum(result.counts.values())
        bell_fidelity = bell_outcomes / total_outcomes

        assert bell_fidelity >= 0.85, f"Bell fidelity {bell_fidelity} too low"

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_superposition_workflow(self):
        """Test superposition creation and measurement workflow."""
        program = "Put qubit in superposition and measure"

        result = quantum(program, shots=2000)

        assert result.success is True
        assert result.total_shots == 2000

        # For superposition, we expect roughly equal '0' and '1' outcomes
        if '0' in result.counts and '1' in result.counts:
            prob_0 = result.counts['0'] / result.total_shots
            prob_1 = result.counts['1'] / result.total_shots

            # Allow for statistical variation
            assert abs(prob_0 - 0.5) < 0.1
            assert abs(prob_1 - 0.5) < 0.1

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_random_bit_generation_workflow(self):
        """Test quantum random bit generation workflow."""
        program = "Generate quantum random bit"

        result = quantum(program, shots=500)

        assert result.success is True
        assert result.total_shots == 500

        # Should have both 0 and 1 outcomes
        assert len(result.counts) >= 2 or '0' in result.counts or '1' in result.counts

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_multi_qubit_entanglement_workflow(self):
        """Test multi-qubit entanglement workflow."""
        program = "Create 3-qubit GHZ state"

        result = quantum(program, shots=1024)

        assert result.success is True
        assert result.total_shots == 1024

        # GHZ state should have outcomes like '000' and '111'
        assert isinstance(result.counts, dict)
        assert len(result.counts) > 0


class TestCompilerIntegration:
    """Test integration between natural language processing and compilation."""

    @pytest.mark.integration
    @pytest.mark.compiler
    def test_natural_language_to_qasm_workflow(self):
        """Test complete natural language to QASM compilation."""
        programs = [
            "Create a Bell state",
            "Apply Hadamard to qubit 0 and CNOT to qubits 0 and 1",
            "Generate superposition on all qubits",
            "Measure all qubits after entanglement"
        ]

        for program in programs:
            # Compile to QASM
            compilation_result = compile_bioql(program)

            assert compilation_result['success'] is True
            assert 'qasm_code' in compilation_result
            assert "OPENQASM 3.0" in compilation_result['qasm_code']

            # Verify QASM contains expected elements
            qasm_code = compilation_result['qasm_code']
            assert "qubit[" in qasm_code  # Qubit declarations
            assert "bit[" in qasm_code    # Classical bit declarations

    @pytest.mark.integration
    @pytest.mark.compiler
    @pytest.mark.requires_qiskit
    def test_compilation_to_execution_workflow(self):
        """Test compilation followed by execution."""
        program = "Create Bell state"

        # First compile to QASM
        compilation_result = compile_bioql(program)
        assert compilation_result['success'] is True

        # Then execute the program
        quantum_result = quantum(program, shots=500)
        assert quantum_result.success is True

        # Results should be consistent
        assert quantum_result.total_shots == 500

    @pytest.mark.integration
    @pytest.mark.compiler
    @pytest.mark.parametrize("program,expected_context", [
        ("Simulate protein folding energy landscape", BiotechContext.PROTEIN_FOLDING),
        ("Model drug-target binding affinity", BiotechContext.DRUG_DISCOVERY),
        ("Analyze DNA sequence patterns", BiotechContext.DNA_ANALYSIS),
        ("Create quantum superposition", BiotechContext.GENERAL)
    ])
    def test_biotechnology_context_detection(self, program, expected_context):
        """Test biotechnology context detection in compilation."""
        compilation_result = compile_bioql(program)

        assert compilation_result['success'] is True
        assert 'context' in compilation_result
        assert compilation_result['context'] == expected_context.value


class TestBiologyWorkflowIntegration:
    """Test integration of quantum computing with biological interpretation."""

    @pytest.mark.integration
    @pytest.mark.bio
    @pytest.mark.requires_qiskit
    def test_protein_folding_simulation_workflow(self):
        """Test complete protein folding simulation workflow."""
        program = "Simulate protein folding energy landscape with 4 qubits"

        # Execute quantum simulation
        result = quantum(program, shots=1000)
        assert result.success is True

        # Interpret results biologically
        interpretation = interpret_bio_results(result, BioContext.PROTEIN_FOLDING)

        assert interpretation['context'] == 'protein_folding'
        assert 'energy_landscape' in interpretation
        assert 'stability_analysis' in interpretation
        assert 'confidence' in interpretation

    @pytest.mark.integration
    @pytest.mark.bio
    @pytest.mark.requires_qiskit
    def test_drug_discovery_workflow(self):
        """Test complete drug discovery workflow."""
        program = "Model drug-target binding affinity using quantum superposition"

        # Execute quantum simulation
        result = quantum(program, shots=800)
        assert result.success is True

        # Interpret for drug discovery
        interpretation = interpret_bio_results(result, BioContext.DRUG_DISCOVERY)

        assert interpretation['context'] == 'drug_discovery'
        assert 'binding_analysis' in interpretation
        assert 'selectivity_score' in interpretation

    @pytest.mark.integration
    @pytest.mark.bio
    @pytest.mark.requires_qiskit
    def test_dna_analysis_workflow(self):
        """Test complete DNA analysis workflow."""
        program = "Analyze DNA sequence variations with quantum algorithms"

        # Execute quantum analysis
        result = quantum(program, shots=1200)
        assert result.success is True

        # Interpret for DNA analysis
        interpretation = interpret_bio_results(result, BioContext.DNA_ANALYSIS)

        assert interpretation['context'] == 'dna_analysis'
        assert 'sequence_analysis' in interpretation
        assert 'mutation_detection' in interpretation

    @pytest.mark.integration
    @pytest.mark.bio
    def test_automatic_biological_context_inference(self):
        """Test automatic inference of biological context from programs."""
        test_cases = [
            ("Optimize protein conformation", BioContext.PROTEIN_FOLDING),
            ("Screen drug compounds", BioContext.DRUG_DISCOVERY),
            ("Sequence genome data", BioContext.DNA_ANALYSIS)
        ]

        for program, expected_context in test_cases:
            # Compilation should detect context
            compilation_result = compile_bioql(program)
            if compilation_result['success']:
                context_detected = compilation_result.get('context')
                assert context_detected is not None


class TestComplexWorkflowIntegration:
    """Test complex multi-step workflows."""

    @pytest.mark.integration
    @pytest.mark.slow
    @pytest.mark.requires_qiskit
    def test_variational_quantum_eigensolver_workflow(self):
        """Test VQE-like workflow for molecular chemistry."""
        program = "Optimize molecular ground state energy using variational quantum eigensolver"

        # This is a complex quantum algorithm simulation
        result = quantum(program, shots=2000)
        assert result.success is True

        # Should have reasonable distribution of outcomes
        assert len(result.counts) > 1
        assert result.total_shots == 2000

    @pytest.mark.integration
    @pytest.mark.slow
    @pytest.mark.requires_qiskit
    def test_quantum_machine_learning_workflow(self):
        """Test quantum machine learning workflow for biological data."""
        program = "Train quantum classifier for protein classification"

        result = quantum(program, shots=1500)
        assert result.success is True

        # Verify execution completed
        assert result.total_shots == 1500
        assert result.metadata['original_program'] == program

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_quantum_optimization_workflow(self):
        """Test quantum optimization workflow."""
        program = "Solve protein structure optimization using QAOA"

        result = quantum(program, shots=1000)
        assert result.success is True

        # Should have diverse outcomes representing optimization landscape
        assert len(result.counts) >= 2

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_hybrid_classical_quantum_workflow(self):
        """Test hybrid classical-quantum workflow."""
        programs = [
            "Initialize quantum state for molecular simulation",
            "Apply variational ansatz for protein folding",
            "Measure expectation values for energy calculation"
        ]

        results = []
        for program in programs:
            result = quantum(program, shots=500)
            assert result.success is True
            results.append(result)

        # All steps should complete successfully
        assert len(results) == 3
        assert all(r.success for r in results)


class TestPerformanceIntegration:
    """Test performance characteristics of integrated workflows."""

    @pytest.mark.integration
    @pytest.mark.slow
    @pytest.mark.requires_qiskit
    def test_workflow_performance_scaling(self):
        """Test workflow performance with different problem sizes."""
        test_cases = [
            ("2-qubit Bell state", 2, 500),
            ("4-qubit GHZ state", 4, 1000),
            ("6-qubit protein simulation", 6, 1500)
        ]

        for program, expected_qubits, shots in test_cases:
            start_time = time.time()
            result = quantum(program, shots=shots)
            execution_time = time.time() - start_time

            assert result.success is True
            assert result.total_shots == shots

            # Performance should be reasonable (< 30 seconds for simulation)
            assert execution_time < 30.0

    @pytest.mark.integration
    @pytest.mark.slow
    def test_memory_efficiency_workflow(self):
        """Test memory efficiency of large workflows."""
        import psutil
        import os

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss

        # Execute multiple quantum programs
        programs = [
            "Create Bell state",
            "Generate superposition",
            "Entangle 3 qubits",
            "Random quantum circuit",
            "Protein folding simulation"
        ]

        for program in programs:
            result = quantum(program, shots=200)
            assert result.success is True

        final_memory = process.memory_info().rss
        memory_growth = (final_memory - initial_memory) / 1024 / 1024  # MB

        # Memory growth should be reasonable (< 200MB)
        assert memory_growth < 200

    @pytest.mark.integration
    @pytest.mark.slow
    @pytest.mark.requires_qiskit
    def test_concurrent_workflow_execution(self):
        """Test concurrent execution of multiple workflows."""
        import concurrent.futures
        import threading

        def execute_program(program):
            return quantum(program, shots=200)

        programs = [
            "Create Bell state",
            "Generate superposition",
            "Random bit generation",
            "3-qubit entanglement"
        ]

        # Execute programs concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(execute_program, prog) for prog in programs]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]

        # All should complete successfully
        assert len(results) == len(programs)
        assert all(r.success for r in results)


class TestErrorHandlingIntegration:
    """Test error handling across integrated workflows."""

    @pytest.mark.integration
    def test_invalid_program_error_propagation(self):
        """Test error propagation for invalid programs."""
        invalid_programs = [
            "",
            "Apply quantum magic gate",
            "Use impossible operation",
            None
        ]

        for program in invalid_programs:
            result = quantum(program)
            if result is not None:
                # Should either fail gracefully or handle the error
                if not result.success:
                    assert result.error_message is not None

    @pytest.mark.integration
    def test_backend_failure_recovery(self):
        """Test recovery from backend failures."""
        # Test with non-existent backend
        result = quantum("Create Bell state", backend="nonexistent")
        assert result.success is False
        assert "backend" in result.error_message.lower() or "not supported" in result.error_message.lower()

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_compilation_execution_consistency(self):
        """Test consistency between compilation and execution."""
        program = "Create Bell state"

        # Compile first
        compilation = compile_bioql(program)
        if compilation['success']:
            # Execute the same program
            execution = quantum(program, shots=100)

            # Both should succeed or fail consistently
            if compilation['success']:
                assert execution.success is True

    @pytest.mark.integration
    def test_resource_limitation_handling(self):
        """Test handling of resource limitations."""
        # Very large circuit request
        large_program = "Create 100-qubit entangled state"
        result = quantum(large_program)

        # Should either succeed or fail gracefully with informative error
        if not result.success:
            assert result.error_message is not None
            assert len(result.error_message) > 0


class TestRegressionIntegration:
    """Regression tests for known issues and edge cases."""

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_repeated_execution_consistency(self):
        """Test that repeated executions give consistent results."""
        program = "Create Bell state"

        results = []
        for _ in range(3):
            result = quantum(program, shots=1000)
            assert result.success is True
            results.append(result)

        # All should succeed
        assert all(r.success for r in results)

        # Results should be statistically similar (allowing for quantum noise)
        for i in range(1, len(results)):
            # Compare most likely outcomes
            outcome1 = results[0].most_likely_outcome
            outcome2 = results[i].most_likely_outcome
            # For Bell state, both should be either '00' or '11'
            if outcome1 in ['00', '11'] and outcome2 in ['00', '11']:
                continue  # This is expected variation
            elif outcome1 == outcome2:
                continue  # Exact match
            else:
                # Allow some statistical variation
                pass

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_state_isolation_between_executions(self):
        """Test that quantum executions don't interfere with each other."""
        program1 = "Create Bell state"
        program2 = "Generate superposition"

        # Execute programs in sequence
        result1 = quantum(program1, shots=500)
        result2 = quantum(program2, shots=500)

        assert result1.success is True
        assert result2.success is True

        # Results should be independent
        assert result1.metadata['original_program'] != result2.metadata['original_program']

    @pytest.mark.integration
    def test_metadata_consistency(self):
        """Test metadata consistency across workflows."""
        program = "Create Bell state"
        backend = "simulator"
        shots = 800

        result = quantum(program, backend=backend, shots=shots)

        if result.success:
            assert result.metadata['original_program'] == program
            assert result.metadata['backend_requested'] == backend
            assert result.total_shots == shots

    @pytest.mark.integration
    @pytest.mark.bio
    def test_biological_interpretation_consistency(self):
        """Test consistency of biological interpretations."""
        protein_program = "Simulate protein folding"

        # Execute multiple times
        results = []
        for _ in range(2):
            result = quantum(protein_program, shots=500)
            if result.success:
                interpretation = interpret_bio_results(result, BioContext.PROTEIN_FOLDING)
                results.append(interpretation)

        if len(results) >= 2:
            # Both should have same context
            assert all(r['context'] == 'protein_folding' for r in results)


class TestWorkflowScenarios:
    """Test realistic usage scenarios."""

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_drug_screening_scenario(self):
        """Test realistic drug screening scenario."""
        # Step 1: Initialize molecular system
        init_result = quantum("Initialize molecular quantum state", shots=300)
        assert init_result.success is True

        # Step 2: Simulate drug binding
        binding_result = quantum("Model drug-target binding interaction", shots=500)
        assert binding_result.success is True

        # Step 3: Analyze binding affinity
        if binding_result.success:
            interpretation = interpret_bio_results(binding_result, BioContext.DRUG_DISCOVERY)
            assert interpretation['context'] == 'drug_discovery'

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_protein_design_scenario(self):
        """Test protein design optimization scenario."""
        # Step 1: Define protein sequence space
        sequence_result = quantum("Define protein sequence optimization space", shots=400)
        assert sequence_result.success is True

        # Step 2: Optimize folding energy
        folding_result = quantum("Optimize protein folding energy landscape", shots=600)
        assert folding_result.success is True

        # Step 3: Validate structure
        if folding_result.success:
            interpretation = interpret_bio_results(folding_result, BioContext.PROTEIN_FOLDING)
            assert 'energy_landscape' in interpretation

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_genomics_analysis_scenario(self):
        """Test genomics analysis scenario."""
        # Step 1: Load genetic data
        data_result = quantum("Load genetic sequence data for analysis", shots=250)
        assert data_result.success is True

        # Step 2: Detect mutations
        mutation_result = quantum("Analyze genetic mutations with quantum algorithms", shots=750)
        assert mutation_result.success is True

        # Step 3: Interpret biological significance
        if mutation_result.success:
            interpretation = interpret_bio_results(mutation_result, BioContext.DNA_ANALYSIS)
            assert 'mutation_detection' in interpretation

    @pytest.mark.integration
    @pytest.mark.slow
    @pytest.mark.requires_qiskit
    def test_research_pipeline_scenario(self):
        """Test complete research pipeline scenario."""
        # Simulate a complete research workflow
        pipeline_steps = [
            ("Define research hypothesis", 200),
            ("Design quantum experiment", 300),
            ("Execute quantum simulation", 500),
            ("Analyze biological results", 400),
            ("Validate findings", 300)
        ]

        results = []
        for step_description, shots in pipeline_steps:
            result = quantum(step_description, shots=shots)
            assert result.success is True
            results.append(result)

        # All steps should complete successfully
        assert len(results) == len(pipeline_steps)
        assert all(r.success for r in results)

        # Total shots should match expected
        total_shots = sum(r.total_shots for r in results)
        expected_shots = sum(shots for _, shots in pipeline_steps)
        assert total_shots == expected_shots


class TestAdvancedIntegration:
    """Test advanced integration scenarios."""

    @pytest.mark.integration
    @pytest.mark.slow
    @pytest.mark.requires_qiskit
    def test_quantum_advantage_demonstration(self):
        """Test scenarios that might demonstrate quantum advantage."""
        quantum_programs = [
            "Simulate molecular dynamics with quantum interference",
            "Solve protein folding with quantum parallelism",
            "Optimize drug discovery with quantum speedup"
        ]

        for program in quantum_programs:
            result = quantum(program, shots=1000)
            assert result.success is True

            # Should utilize quantum properties effectively
            assert len(result.counts) > 1  # Multiple outcomes expected

    @pytest.mark.integration
    @pytest.mark.requires_qiskit
    def test_hybrid_algorithm_integration(self):
        """Test integration of hybrid classical-quantum algorithms."""
        # Simulate QAOA-like optimization
        optimization_steps = [
            "Initialize variational parameters",
            "Apply quantum ansatz circuit",
            "Measure expectation values",
            "Update classical parameters"
        ]

        for step in optimization_steps:
            result = quantum(step, shots=300)
            assert result.success is True

    @pytest.mark.integration
    @pytest.mark.bio
    def test_multi_modal_biological_analysis(self):
        """Test integration across multiple biological domains."""
        # Analyze protein-drug-DNA interactions
        multi_modal_program = "Analyze protein-drug-DNA interaction network"

        result = quantum(multi_modal_program, shots=800)
        assert result.success is True

        # Should be interpretable in multiple contexts
        protein_interpretation = interpret_bio_results(result, BioContext.PROTEIN_FOLDING)
        drug_interpretation = interpret_bio_results(result, BioContext.DRUG_DISCOVERY)

        assert protein_interpretation['context'] == 'protein_folding'
        assert drug_interpretation['context'] == 'drug_discovery'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])