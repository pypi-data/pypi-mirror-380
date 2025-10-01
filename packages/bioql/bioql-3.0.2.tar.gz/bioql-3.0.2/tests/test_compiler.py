"""
Comprehensive Test Suite for BioQL Compiler Module

Tests for the English to QASM translation engine, including natural language
processing, biotechnology context parsing, and quantum circuit generation.
"""

import pytest
import re
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, List, Any, Optional

try:
    from qiskit import QuantumCircuit
    QISKIT_AVAILABLE = True
except ImportError:
    QISKIT_AVAILABLE = False

# Import BioQL compiler modules
from bioql.compiler import (
    compile_bioql, NaturalLanguageProcessor, QuantumGateExtractor,
    BiotechContextAnalyzer, QASMGenerator, CompilerError,
    QuantumGateType, BiotechContext
)


class TestQuantumGateType:
    """Test cases for QuantumGateType enumeration."""

    def test_quantum_gate_type_values(self):
        """Test that QuantumGateType contains expected gate types."""
        expected_gates = [
            'h', 'x', 'y', 'z', 'cnot', 'cz', 'ccx',
            'rx', 'ry', 'rz', 'p', 'swap', 'measure'
        ]

        for gate in expected_gates:
            assert any(gate_type.value == gate for gate_type in QuantumGateType)

    def test_quantum_gate_type_enumeration(self):
        """Test specific QuantumGateType enum values."""
        assert QuantumGateType.HADAMARD.value == 'h'
        assert QuantumGateType.PAULI_X.value == 'x'
        assert QuantumGateType.CNOT.value == 'cnot'
        assert QuantumGateType.TOFFOLI.value == 'ccx'
        assert QuantumGateType.MEASURE.value == 'measure'


class TestBiotechContext:
    """Test cases for BiotechContext enumeration."""

    def test_biotech_context_values(self):
        """Test that BiotechContext contains expected contexts."""
        expected_contexts = [
            'protein_folding', 'drug_discovery', 'dna_analysis',
            'molecular_simulation', 'general'
        ]

        for context in expected_contexts:
            assert any(ctx.value == context for ctx in BiotechContext)

    def test_biotech_context_enumeration(self):
        """Test specific BiotechContext enum values."""
        assert BiotechContext.PROTEIN_FOLDING.value == 'protein_folding'
        assert BiotechContext.DRUG_DISCOVERY.value == 'drug_discovery'
        assert BiotechContext.DNA_ANALYSIS.value == 'dna_analysis'
        assert BiotechContext.GENERAL.value == 'general'


class TestNaturalLanguageProcessor:
    """Test cases for the NaturalLanguageProcessor class."""

    def test_nlp_initialization(self):
        """Test NaturalLanguageProcessor initialization."""
        nlp = NaturalLanguageProcessor()
        assert nlp is not None
        assert hasattr(nlp, 'process_text')

    def test_process_basic_quantum_terms(self):
        """Test processing of basic quantum computing terms."""
        nlp = NaturalLanguageProcessor()

        test_cases = [
            ("Create a Bell state", ["bell", "state", "create"]),
            ("Apply Hadamard gate", ["hadamard", "gate", "apply"]),
            ("Entangle two qubits", ["entangle", "qubits"]),
            ("Measure all qubits", ["measure", "qubits"]),
            ("Generate superposition", ["superposition", "generate"])
        ]

        for text, expected_tokens in test_cases:
            result = nlp.process_text(text)
            assert isinstance(result, dict)
            assert 'tokens' in result

            # Check that expected tokens are found (case-insensitive)
            found_tokens = [token.lower() for token in result['tokens']]
            for expected_token in expected_tokens:
                assert any(expected_token in token for token in found_tokens)

    def test_process_biotechnology_terms(self):
        """Test processing of biotechnology-specific terms."""
        nlp = NaturalLanguageProcessor()

        biotech_programs = [
            "Simulate protein folding energy landscape",
            "Model drug-target binding affinity",
            "Analyze DNA methylation patterns",
            "Optimize pharmaceutical molecular structure"
        ]

        for program in biotech_programs:
            result = nlp.process_text(program)
            assert isinstance(result, dict)
            assert 'tokens' in result
            assert 'biotech_keywords' in result

    def test_process_empty_input(self):
        """Test processing of empty or invalid input."""
        nlp = NaturalLanguageProcessor()

        with pytest.raises(CompilerError):
            nlp.process_text("")

        with pytest.raises(CompilerError):
            nlp.process_text("   ")

        with pytest.raises(CompilerError):
            nlp.process_text(None)

    def test_extract_quantum_operations(self):
        """Test extraction of quantum operations from text."""
        nlp = NaturalLanguageProcessor()

        operations_text = [
            "Apply Hadamard to qubit 0",
            "CNOT between qubits 0 and 1",
            "Measure qubit 2",
            "Rotate qubit around X axis",
            "Create superposition on all qubits"
        ]

        for text in operations_text:
            result = nlp.process_text(text)
            assert 'quantum_operations' in result
            assert isinstance(result['quantum_operations'], list)

    def test_extract_qubit_references(self):
        """Test extraction of qubit references from text."""
        nlp = NaturalLanguageProcessor()

        qubit_texts = [
            "Apply gate to qubit 0",
            "Entangle qubits 1 and 2",
            "Measure all 4 qubits",
            "Use 8 qubits for simulation"
        ]

        for text in qubit_texts:
            result = nlp.process_text(text)
            assert 'qubit_references' in result
            assert isinstance(result['qubit_references'], list)


class TestQuantumGateExtractor:
    """Test cases for the QuantumGateExtractor class."""

    def test_gate_extractor_initialization(self):
        """Test QuantumGateExtractor initialization."""
        extractor = QuantumGateExtractor()
        assert extractor is not None

    def test_extract_basic_gates(self):
        """Test extraction of basic quantum gates."""
        extractor = QuantumGateExtractor()

        test_cases = [
            ("Apply Hadamard gate", [QuantumGateType.HADAMARD]),
            ("Use Pauli-X gate", [QuantumGateType.PAULI_X]),
            ("CNOT gate between qubits", [QuantumGateType.CNOT]),
            ("Measure all qubits", [QuantumGateType.MEASURE]),
            ("Create Bell state", [QuantumGateType.HADAMARD, QuantumGateType.CNOT])
        ]

        for text, expected_gates in test_cases:
            gates = extractor.extract_gates(text)
            assert isinstance(gates, list)

            # Check that all expected gates are found
            gate_values = [gate.value for gate in gates]
            for expected_gate in expected_gates:
                assert expected_gate.value in gate_values

    def test_extract_parameterized_gates(self):
        """Test extraction of parameterized gates."""
        extractor = QuantumGateExtractor()

        parameterized_texts = [
            "Rotate qubit by 45 degrees around X axis",
            "Apply RY rotation with angle pi/4",
            "Phase shift by pi/2",
            "RZ gate with parameter 0.5"
        ]

        for text in parameterized_texts:
            gates = extractor.extract_gates(text)
            assert len(gates) > 0

            # Should contain rotation or phase gates
            gate_values = [gate.value for gate in gates]
            rotation_gates = ['rx', 'ry', 'rz', 'p']
            assert any(gate in gate_values for gate in rotation_gates)

    def test_extract_multi_qubit_gates(self):
        """Test extraction of multi-qubit gates."""
        extractor = QuantumGateExtractor()

        multi_qubit_texts = [
            "CNOT between qubits 0 and 1",
            "Controlled-Z gate",
            "Toffoli gate with two controls",
            "SWAP gate between qubits"
        ]

        for text in multi_qubit_texts:
            gates = extractor.extract_gates(text)
            assert len(gates) > 0

            # Should contain multi-qubit gates
            gate_values = [gate.value for gate in gates]
            multi_gates = ['cnot', 'cz', 'ccx', 'swap']
            assert any(gate in gate_values for gate in multi_gates)

    def test_extract_complex_sequences(self):
        """Test extraction from complex gate sequences."""
        extractor = QuantumGateExtractor()

        complex_text = (
            "Apply Hadamard to qubit 0, then CNOT between 0 and 1, "
            "followed by measurement of both qubits"
        )

        gates = extractor.extract_gates(complex_text)
        gate_values = [gate.value for gate in gates]

        expected_gates = ['h', 'cnot', 'measure']
        for expected in expected_gates:
            assert expected in gate_values

    def test_extract_gates_with_parameters(self):
        """Test extraction of gates with specific parameters."""
        extractor = QuantumGateExtractor()

        result = extractor.extract_gates_with_parameters(
            "Apply RX rotation of pi/4 to qubit 0 and RY of pi/2 to qubit 1"
        )

        assert isinstance(result, list)
        assert len(result) > 0

        # Each item should have gate type and parameters
        for gate_info in result:
            assert 'gate' in gate_info
            assert 'parameters' in gate_info
            assert 'qubits' in gate_info


class TestBiotechContextAnalyzer:
    """Test cases for the BiotechContextAnalyzer class."""

    def test_context_analyzer_initialization(self):
        """Test BiotechContextAnalyzer initialization."""
        analyzer = BiotechContextAnalyzer()
        assert analyzer is not None

    def test_analyze_protein_folding_context(self):
        """Test analysis of protein folding contexts."""
        analyzer = BiotechContextAnalyzer()

        protein_texts = [
            "Simulate protein folding energy landscape",
            "Model protein structure optimization",
            "Analyze amino acid interactions",
            "Predict protein conformation states"
        ]

        for text in protein_texts:
            context = analyzer.analyze_context(text)
            assert context == BiotechContext.PROTEIN_FOLDING

    def test_analyze_drug_discovery_context(self):
        """Test analysis of drug discovery contexts."""
        analyzer = BiotechContextAnalyzer()

        drug_texts = [
            "Model drug-target binding affinity",
            "Optimize pharmaceutical compounds",
            "Simulate molecular docking",
            "Analyze drug metabolism pathways"
        ]

        for text in drug_texts:
            context = analyzer.analyze_context(text)
            assert context == BiotechContext.DRUG_DISCOVERY

    def test_analyze_dna_analysis_context(self):
        """Test analysis of DNA analysis contexts."""
        analyzer = BiotechContextAnalyzer()

        dna_texts = [
            "Analyze DNA sequence patterns",
            "Model genetic variations",
            "Study DNA methylation",
            "Sequence alignment analysis"
        ]

        for text in dna_texts:
            context = analyzer.analyze_context(text)
            assert context == BiotechContext.DNA_ANALYSIS

    def test_analyze_general_context(self):
        """Test analysis of general quantum contexts."""
        analyzer = BiotechContextAnalyzer()

        general_texts = [
            "Create Bell state",
            "Apply Hadamard gate",
            "Generate superposition",
            "Quantum Fourier transform"
        ]

        for text in general_texts:
            context = analyzer.analyze_context(text)
            assert context == BiotechContext.GENERAL

    def test_context_confidence_scoring(self):
        """Test context confidence scoring."""
        analyzer = BiotechContextAnalyzer()

        result = analyzer.analyze_with_confidence(
            "Simulate protein folding with quantum annealing"
        )

        assert 'context' in result
        assert 'confidence' in result
        assert 'keywords_found' in result
        assert isinstance(result['confidence'], float)
        assert 0.0 <= result['confidence'] <= 1.0

    def test_mixed_context_resolution(self):
        """Test resolution of mixed biotechnology contexts."""
        analyzer = BiotechContextAnalyzer()

        mixed_text = "Analyze protein-drug interactions for binding affinity"
        result = analyzer.analyze_with_confidence(mixed_text)

        # Should detect the primary context with reasonable confidence
        assert result['context'] in [BiotechContext.PROTEIN_FOLDING, BiotechContext.DRUG_DISCOVERY]
        assert result['confidence'] > 0.3


class TestQASMGenerator:
    """Test cases for the QASMGenerator class."""

    def test_qasm_generator_initialization(self):
        """Test QASMGenerator initialization."""
        generator = QASMGenerator()
        assert generator is not None

    def test_generate_basic_qasm(self):
        """Test generation of basic QASM code."""
        generator = QASMGenerator()

        # Test simple Bell state
        gates = [
            {'gate': QuantumGateType.HADAMARD, 'qubits': [0], 'parameters': []},
            {'gate': QuantumGateType.CNOT, 'qubits': [0, 1], 'parameters': []},
            {'gate': QuantumGateType.MEASURE, 'qubits': [0, 1], 'parameters': []}
        ]

        qasm_code = generator.generate_qasm(gates, num_qubits=2)

        assert isinstance(qasm_code, str)
        assert "OPENQASM 3.0" in qasm_code
        assert "include \"stdgates.inc\"" in qasm_code
        assert "qubit[2] q" in qasm_code
        assert "bit[2] c" in qasm_code
        assert "h q[0]" in qasm_code
        assert "cx q[0], q[1]" in qasm_code

    def test_generate_parameterized_qasm(self):
        """Test generation of QASM with parameterized gates."""
        generator = QASMGenerator()

        gates = [
            {'gate': QuantumGateType.ROTATION_X, 'qubits': [0], 'parameters': ['pi/4']},
            {'gate': QuantumGateType.ROTATION_Y, 'qubits': [1], 'parameters': ['pi/2']},
            {'gate': QuantumGateType.MEASURE, 'qubits': [0, 1], 'parameters': []}
        ]

        qasm_code = generator.generate_qasm(gates, num_qubits=2)

        assert "rx(pi/4) q[0]" in qasm_code
        assert "ry(pi/2) q[1]" in qasm_code

    def test_generate_multi_qubit_qasm(self):
        """Test generation of QASM with multi-qubit gates."""
        generator = QASMGenerator()

        gates = [
            {'gate': QuantumGateType.HADAMARD, 'qubits': [0], 'parameters': []},
            {'gate': QuantumGateType.CNOT, 'qubits': [0, 1], 'parameters': []},
            {'gate': QuantumGateType.TOFFOLI, 'qubits': [0, 1, 2], 'parameters': []},
            {'gate': QuantumGateType.MEASURE, 'qubits': [0, 1, 2], 'parameters': []}
        ]

        qasm_code = generator.generate_qasm(gates, num_qubits=3)

        assert "cx q[0], q[1]" in qasm_code
        assert "ccx q[0], q[1], q[2]" in qasm_code

    def test_qasm_validation(self):
        """Test QASM code validation."""
        generator = QASMGenerator()

        valid_gates = [
            {'gate': QuantumGateType.HADAMARD, 'qubits': [0], 'parameters': []},
            {'gate': QuantumGateType.MEASURE, 'qubits': [0], 'parameters': []}
        ]

        qasm_code = generator.generate_qasm(valid_gates, num_qubits=1)
        is_valid = generator.validate_qasm(qasm_code)
        assert is_valid

    def test_qasm_optimization(self):
        """Test QASM code optimization."""
        generator = QASMGenerator()

        # Gates that can be optimized
        redundant_gates = [
            {'gate': QuantumGateType.HADAMARD, 'qubits': [0], 'parameters': []},
            {'gate': QuantumGateType.HADAMARD, 'qubits': [0], 'parameters': []},  # Redundant
            {'gate': QuantumGateType.MEASURE, 'qubits': [0], 'parameters': []}
        ]

        qasm_code = generator.generate_qasm(redundant_gates, num_qubits=1, optimize=True)

        # Should have fewer Hadamard gates due to optimization
        h_count = qasm_code.count("h q[0]")
        assert h_count == 0  # Two Hadamards cancel out


class TestCompileBioQLFunction:
    """Test cases for the main compile_bioql function."""

    def test_compile_basic_programs(self, sample_natural_language_programs):
        """Test compilation of basic BioQL programs."""
        for program in sample_natural_language_programs:
            result = compile_bioql(program)

            assert isinstance(result, dict)
            assert 'qasm_code' in result
            assert 'success' in result
            assert result['success'] is True
            assert isinstance(result['qasm_code'], str)
            assert "OPENQASM 3.0" in result['qasm_code']

    def test_compile_biotechnology_programs(self, biotechnology_programs):
        """Test compilation of biotechnology-specific programs."""
        for program in biotechnology_programs:
            result = compile_bioql(program)

            assert result['success'] is True
            assert 'context' in result
            assert result['context'] in ['protein_folding', 'drug_discovery', 'dna_analysis']

    def test_compile_with_options(self):
        """Test compilation with various options."""
        program = "Create Bell state"

        # Test with optimization
        result = compile_bioql(program, optimize=True)
        assert result['success'] is True
        assert 'optimization_applied' in result

        # Test with debug mode
        result = compile_bioql(program, debug=True)
        assert result['success'] is True
        assert 'debug_info' in result

        # Test with custom backend
        result = compile_bioql(program, target_backend='ibm_quantum')
        assert result['success'] is True

    def test_compile_to_circuit(self):
        """Test compilation to Qiskit circuit object."""
        if not QISKIT_AVAILABLE:
            pytest.skip("Qiskit not available")

        program = "Create Bell state"
        result = compile_bioql(program, output_format='circuit')

        assert result['success'] is True
        assert 'circuit' in result
        assert isinstance(result['circuit'], QuantumCircuit)

    def test_compile_error_handling(self, invalid_programs):
        """Test compilation error handling."""
        for invalid_program in invalid_programs:
            result = compile_bioql(invalid_program)

            if invalid_program is None or invalid_program == "":
                assert result['success'] is False
                assert 'error' in result

    def test_compile_complex_programs(self):
        """Test compilation of complex multi-step programs."""
        complex_programs = [
            "Create Bell state, apply rotation, then measure",
            "Initialize superposition on 4 qubits, entangle pairs, measure all",
            "Simulate protein folding: create superposition, apply molecular interactions, measure energy states"
        ]

        for program in complex_programs:
            result = compile_bioql(program)
            assert result['success'] is True
            assert len(result['qasm_code']) > 100  # Complex programs should generate substantial QASM

    @pytest.mark.parametrize("program,expected_gates", [
        ("Create Bell state", ['h', 'cx']),
        ("Apply Hadamard then measure", ['h', 'measure']),
        ("CNOT between qubits 0 and 1", ['cx']),
        ("Generate superposition", ['h'])
    ])
    def test_compile_parameterized_gate_detection(self, program, expected_gates):
        """Test parameterized gate detection in compilation."""
        result = compile_bioql(program)

        assert result['success'] is True
        qasm_code = result['qasm_code']

        for gate in expected_gates:
            if gate == 'cx':
                assert 'cx ' in qasm_code or 'cnot ' in qasm_code
            elif gate == 'measure':
                assert 'measure ' in qasm_code or 'c[' in qasm_code
            else:
                assert f'{gate} ' in qasm_code

    def test_compile_with_qubit_specification(self):
        """Test compilation with explicit qubit specifications."""
        programs_with_qubits = [
            "Apply Hadamard to qubit 0",
            "CNOT between qubits 2 and 3",
            "Measure qubits 0, 1, and 2",
            "Create 8-qubit entangled state"
        ]

        for program in programs_with_qubits:
            result = compile_bioql(program)
            assert result['success'] is True
            assert 'num_qubits' in result
            assert result['num_qubits'] > 0

    def test_compile_performance(self):
        """Test compilation performance for various program sizes."""
        import time

        programs = [
            "Create Bell state",  # Simple
            "Generate 4-qubit GHZ state with measurements",  # Medium
            "Simulate protein folding energy landscape with 8 qubits and complex interactions"  # Complex
        ]

        for program in programs:
            start_time = time.time()
            result = compile_bioql(program)
            compilation_time = time.time() - start_time

            assert result['success'] is True
            assert compilation_time < 5.0  # Should compile within 5 seconds


class TestCompilerIntegration:
    """Integration tests for the compiler module."""

    @pytest.mark.integration
    def test_end_to_end_bell_state_compilation(self):
        """Test end-to-end compilation of Bell state program."""
        program = "Create a Bell state by applying Hadamard to qubit 0 and CNOT to qubits 0 and 1"
        result = compile_bioql(program)

        assert result['success'] is True
        assert 'qasm_code' in result
        assert 'context' in result
        assert 'metadata' in result

        qasm_code = result['qasm_code']
        assert "h q[0]" in qasm_code
        assert "cx q[0], q[1]" in qasm_code

    @pytest.mark.integration
    def test_end_to_end_protein_simulation(self):
        """Test end-to-end compilation of protein folding simulation."""
        program = "Simulate protein folding energy landscape with 4 qubits representing amino acid interactions"
        result = compile_bioql(program)

        assert result['success'] is True
        assert result['context'] == 'protein_folding'
        assert result['num_qubits'] >= 4

    @pytest.mark.integration
    def test_compilation_with_visualization(self):
        """Test compilation with circuit visualization."""
        if not QISKIT_AVAILABLE:
            pytest.skip("Qiskit not available")

        program = "Create Bell state"
        result = compile_bioql(program, include_visualization=True)

        assert result['success'] is True
        assert 'visualization' in result

    @pytest.mark.integration
    def test_multi_format_output(self):
        """Test compilation with multiple output formats."""
        program = "Create superposition"

        # Test QASM output
        qasm_result = compile_bioql(program, output_format='qasm')
        assert qasm_result['success'] is True
        assert 'qasm_code' in qasm_result

        # Test circuit output (if Qiskit available)
        if QISKIT_AVAILABLE:
            circuit_result = compile_bioql(program, output_format='circuit')
            assert circuit_result['success'] is True
            assert 'circuit' in circuit_result


class TestCompilerErrorConditions:
    """Test error conditions and edge cases for the compiler."""

    def test_empty_program_compilation(self):
        """Test compilation of empty programs."""
        empty_programs = ["", "   ", "\n\t  ", None]

        for program in empty_programs:
            result = compile_bioql(program)
            assert result['success'] is False
            assert 'error' in result

    def test_unsupported_operations(self):
        """Test compilation of unsupported quantum operations."""
        unsupported_programs = [
            "Apply quantum magic gate",
            "Use time travel operator",
            "Execute impossible quantum operation"
        ]

        for program in unsupported_programs:
            result = compile_bioql(program)
            # Should either succeed with best-effort or fail gracefully
            assert 'success' in result
            if not result['success']:
                assert 'error' in result

    def test_malformed_syntax_handling(self):
        """Test handling of malformed syntax in programs."""
        malformed_programs = [
            "Apply gate to qubit -1",  # Invalid qubit index
            "CNOT with only one qubit",  # Insufficient qubits
            "Measure qubit 100 in 2-qubit system"  # Qubit out of range
        ]

        for program in malformed_programs:
            result = compile_bioql(program)
            # Should handle gracefully
            assert 'success' in result

    def test_compilation_with_invalid_options(self):
        """Test compilation with invalid options."""
        program = "Create Bell state"

        # Invalid output format
        result = compile_bioql(program, output_format='invalid_format')
        assert result['success'] is False

        # Invalid backend
        result = compile_bioql(program, target_backend='nonexistent_backend')
        # Should either succeed with fallback or fail gracefully
        assert 'success' in result

    def test_resource_exhaustion_handling(self):
        """Test handling of resource exhaustion scenarios."""
        # Very large circuit request
        large_program = "Create entangled state with 1000 qubits"
        result = compile_bioql(large_program)

        # Should either succeed or fail gracefully
        assert 'success' in result
        if not result['success']:
            assert 'error' in result
            assert 'resource' in result['error'].lower() or 'limit' in result['error'].lower()


class TestCompilerUtilities:
    """Test utility functions and helper methods in the compiler."""

    def test_gate_mapping_utilities(self):
        """Test gate mapping and conversion utilities."""
        from bioql.compiler import gate_name_to_enum, gate_enum_to_qasm

        # Test gate name conversion
        assert gate_name_to_enum('hadamard') == QuantumGateType.HADAMARD
        assert gate_name_to_enum('cnot') == QuantumGateType.CNOT

        # Test QASM conversion
        assert gate_enum_to_qasm(QuantumGateType.HADAMARD) == 'h'
        assert gate_enum_to_qasm(QuantumGateType.PAULI_X) == 'x'

    def test_parameter_parsing(self):
        """Test parameter parsing utilities."""
        from bioql.compiler import parse_angle_parameter

        angle_tests = [
            ("pi/4", "pi/4"),
            ("45 degrees", "pi/4"),
            ("90 deg", "pi/2"),
            ("0.5", "0.5")
        ]

        for input_param, expected in angle_tests:
            result = parse_angle_parameter(input_param)
            assert result == expected

    def test_qubit_index_extraction(self):
        """Test qubit index extraction utilities."""
        from bioql.compiler import extract_qubit_indices

        text_tests = [
            ("qubit 0", [0]),
            ("qubits 1 and 2", [1, 2]),
            ("all 4 qubits", list(range(4))),
            ("qubits 0, 2, and 3", [0, 2, 3])
        ]

        for text, expected in text_tests:
            result = extract_qubit_indices(text)
            assert result == expected

    def test_circuit_depth_estimation(self):
        """Test circuit depth estimation utilities."""
        from bioql.compiler import estimate_circuit_depth

        gate_sequences = [
            [QuantumGateType.HADAMARD, QuantumGateType.CNOT],  # Depth 2
            [QuantumGateType.HADAMARD, QuantumGateType.HADAMARD],  # Depth 2 (parallel)
            [QuantumGateType.CNOT, QuantumGateType.CNOT, QuantumGateType.CNOT]  # Depth 3
        ]

        for gates in gate_sequences:
            depth = estimate_circuit_depth(gates, num_qubits=2)
            assert isinstance(depth, int)
            assert depth > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])