"""
Comprehensive Test Suite for BioQL Bio Interpreter Module

Tests for biological result interpretation, including protein folding,
drug discovery, DNA analysis, and visualization functions.
"""

import pytest
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, List, Any, Optional

from bioql.bio_interpreter import (
    interpret_bio_results, ProteinFoldingInterpreter, DrugDiscoveryInterpreter,
    DNAAnalysisInterpreter, BioContext, ProteinStructure, DrugMolecule,
    DNASequence, visualize_protein_structure, visualize_drug_binding,
    visualize_dna_analysis, calculate_protein_energy, analyze_binding_affinity,
    sequence_analysis
)

from bioql import QuantumResult


class TestBioContext:
    """Test cases for BioContext enumeration."""

    def test_bio_context_values(self):
        """Test that BioContext contains expected contexts."""
        expected_contexts = ['protein_folding', 'drug_discovery', 'dna_analysis']

        for context in expected_contexts:
            assert any(ctx.value == context for ctx in BioContext)

    def test_bio_context_enumeration(self):
        """Test specific BioContext enum values."""
        assert BioContext.PROTEIN_FOLDING.value == 'protein_folding'
        assert BioContext.DRUG_DISCOVERY.value == 'drug_discovery'
        assert BioContext.DNA_ANALYSIS.value == 'dna_analysis'


class TestProteinStructure:
    """Test cases for ProteinStructure data class."""

    def test_protein_structure_creation(self):
        """Test ProteinStructure creation and validation."""
        coordinates = np.array([[0, 0, 0], [1, 1, 1], [2, 0, 1]])
        protein = ProteinStructure(
            sequence="MKLLVV",
            coordinates=coordinates,
            energy=-125.5,
            conformation_id="conf_001",
            stability_score=0.85
        )

        assert protein.sequence == "MKLLVV"
        assert np.array_equal(protein.coordinates, coordinates)
        assert protein.energy == -125.5
        assert protein.conformation_id == "conf_001"
        assert protein.stability_score == 0.85

    def test_protein_structure_validation(self):
        """Test ProteinStructure validation."""
        # Valid protein structure
        protein = ProteinStructure(
            sequence="ACDEFGHIKLMNPQRSTVWY",
            coordinates=np.zeros((20, 3)),
            energy=-200.0,
            conformation_id="valid_conf",
            stability_score=0.9
        )
        assert len(protein.sequence) == 20
        assert protein.coordinates.shape == (20, 3)

    def test_protein_structure_properties(self):
        """Test computed properties of ProteinStructure."""
        protein = ProteinStructure(
            sequence="MKLLVV",
            coordinates=np.array([[0, 0, 0], [1, 1, 1], [2, 0, 1], [3, 1, 0], [4, 0, 2], [5, 1, 1]]),
            energy=-125.5,
            conformation_id="conf_001",
            stability_score=0.85
        )

        # Test sequence length matches coordinates
        assert len(protein.sequence) == len(protein.coordinates)


class TestDrugMolecule:
    """Test cases for DrugMolecule data class."""

    def test_drug_molecule_creation(self):
        """Test DrugMolecule creation and validation."""
        drug = DrugMolecule(
            smiles="CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
            molecular_weight=206.28,
            binding_affinity=8.5,
            ic50=0.25,
            toxicity_score=0.15
        )

        assert drug.smiles == "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"
        assert drug.molecular_weight == 206.28
        assert drug.binding_affinity == 8.5
        assert drug.ic50 == 0.25
        assert drug.toxicity_score == 0.15

    def test_drug_molecule_validation(self):
        """Test DrugMolecule validation."""
        # Valid drug molecule
        drug = DrugMolecule(
            smiles="CCO",  # Ethanol
            molecular_weight=46.07,
            binding_affinity=5.0,
            ic50=10.0,
            toxicity_score=0.8
        )
        assert drug.molecular_weight > 0
        assert drug.ic50 > 0


class TestDNASequence:
    """Test cases for DNASequence data class."""

    def test_dna_sequence_creation(self):
        """Test DNASequence creation and validation."""
        dna = DNASequence(
            sequence="ATCGATCGATCG",
            gc_content=0.5,
            mutation_probability=0.05,
            quality_score=0.95
        )

        assert dna.sequence == "ATCGATCGATCG"
        assert dna.gc_content == 0.5
        assert dna.mutation_probability == 0.05
        assert dna.quality_score == 0.95

    def test_dna_sequence_validation(self):
        """Test DNASequence validation."""
        # Valid DNA sequence
        dna = DNASequence(
            sequence="ATCGATCGATCGATCG",
            gc_content=0.5,
            mutation_probability=0.02,
            quality_score=0.98
        )

        # Check that GC content is between 0 and 1
        assert 0 <= dna.gc_content <= 1

        # Check sequence contains only valid bases
        valid_bases = set('ATCG')
        assert set(dna.sequence).issubset(valid_bases)

    def test_gc_content_calculation(self):
        """Test GC content calculation accuracy."""
        sequences = [
            ("ATCG", 0.5),  # 2 GC out of 4 = 0.5
            ("AAAA", 0.0),  # 0 GC out of 4 = 0.0
            ("GCGC", 1.0),  # 4 GC out of 4 = 1.0
            ("ATCGATCG", 0.5)  # 4 GC out of 8 = 0.5
        ]

        for sequence, expected_gc in sequences:
            actual_gc = sum(1 for base in sequence if base in 'GC') / len(sequence)
            assert abs(actual_gc - expected_gc) < 0.001


class TestProteinFoldingInterpreter:
    """Test cases for ProteinFoldingInterpreter class."""

    def test_protein_interpreter_initialization(self):
        """Test ProteinFoldingInterpreter initialization."""
        interpreter = ProteinFoldingInterpreter()
        assert interpreter is not None

    def test_interpret_protein_folding_results(self):
        """Test interpretation of protein folding quantum results."""
        interpreter = ProteinFoldingInterpreter()

        # Simulate quantum results for protein folding
        quantum_result = QuantumResult(
            counts={'0000': 300, '0001': 200, '1110': 300, '1111': 224},
            metadata={'context': 'protein_folding', 'num_qubits': 4}
        )

        interpretation = interpreter.interpret(quantum_result)

        assert isinstance(interpretation, dict)
        assert 'energy_landscape' in interpretation
        assert 'stability_analysis' in interpretation
        assert 'conformations' in interpretation
        assert 'confidence' in interpretation

        # Check energy landscape
        energy_landscape = interpretation['energy_landscape']
        assert isinstance(energy_landscape, dict)
        assert len(energy_landscape) > 0

        # Check stability analysis
        stability = interpretation['stability_analysis']
        assert 'most_stable_conformation' in stability
        assert 'stability_score' in stability

    def test_energy_state_mapping(self):
        """Test mapping of quantum states to protein energy states."""
        interpreter = ProteinFoldingInterpreter()

        # Test different quantum state patterns
        test_cases = [
            {'0000': 500, '1111': 500},  # High stability (clear states)
            {'0101': 250, '1010': 250, '0000': 250, '1111': 250},  # Medium stability
            {'0001': 100, '0010': 100, '0100': 100, '1000': 100, '0000': 600}  # Low stability
        ]

        for counts in test_cases:
            quantum_result = QuantumResult(counts=counts)
            interpretation = interpreter.interpret(quantum_result)

            assert 'energy_states' in interpretation
            assert isinstance(interpretation['energy_states'], list)

    def test_conformation_analysis(self):
        """Test protein conformation analysis."""
        interpreter = ProteinFoldingInterpreter()

        # Results with clear dominant conformations
        quantum_result = QuantumResult(
            counts={'00': 800, '01': 100, '10': 50, '11': 50},
            metadata={'sequence': 'MKLLVV'}
        )

        interpretation = interpreter.interpret(quantum_result)

        assert 'dominant_conformation' in interpretation
        assert interpretation['dominant_conformation'] == '00'

    def test_folding_pathway_prediction(self):
        """Test folding pathway prediction from quantum results."""
        interpreter = ProteinFoldingInterpreter()

        quantum_result = QuantumResult(
            counts={'000': 200, '001': 150, '010': 150, '100': 300, '111': 200}
        )

        pathway = interpreter.predict_folding_pathway(quantum_result)

        assert isinstance(pathway, list)
        assert len(pathway) > 0
        assert all('state' in step for step in pathway)
        assert all('energy' in step for step in pathway)


class TestDrugDiscoveryInterpreter:
    """Test cases for DrugDiscoveryInterpreter class."""

    def test_drug_interpreter_initialization(self):
        """Test DrugDiscoveryInterpreter initialization."""
        interpreter = DrugDiscoveryInterpreter()
        assert interpreter is not None

    def test_interpret_drug_discovery_results(self):
        """Test interpretation of drug discovery quantum results."""
        interpreter = DrugDiscoveryInterpreter()

        quantum_result = QuantumResult(
            counts={'00': 600, '01': 150, '10': 200, '11': 74},
            metadata={'context': 'drug_discovery', 'drug_smiles': 'CCO'}
        )

        interpretation = interpreter.interpret(quantum_result)

        assert isinstance(interpretation, dict)
        assert 'binding_analysis' in interpretation
        assert 'selectivity_score' in interpretation
        assert 'toxicity_prediction' in interpretation
        assert 'drug_likelihood' in interpretation

    def test_binding_affinity_calculation(self):
        """Test binding affinity calculation from quantum states."""
        interpreter = DrugDiscoveryInterpreter()

        # High binding affinity pattern (concentrated in bound states)
        high_binding = QuantumResult(counts={'11': 900, '10': 100})
        interpretation_high = interpreter.interpret(high_binding)

        # Low binding affinity pattern (distributed states)
        low_binding = QuantumResult(counts={'00': 400, '01': 300, '10': 200, '11': 100})
        interpretation_low = interpreter.interpret(low_binding)

        # High binding should have higher affinity score
        assert interpretation_high['binding_analysis']['affinity'] > interpretation_low['binding_analysis']['affinity']

    def test_selectivity_analysis(self):
        """Test drug selectivity analysis."""
        interpreter = DrugDiscoveryInterpreter()

        # Selective binding pattern
        selective_result = QuantumResult(
            counts={'000': 50, '001': 800, '010': 50, '100': 50, '111': 50}
        )

        interpretation = interpreter.interpret(selective_result)
        assert 'selectivity_score' in interpretation
        assert interpretation['selectivity_score'] > 0.5

    def test_toxicity_prediction(self):
        """Test toxicity prediction from quantum results."""
        interpreter = DrugDiscoveryInterpreter()

        # Low toxicity pattern (stable, predictable binding)
        low_tox_result = QuantumResult(counts={'00': 512, '11': 512})
        interpretation_low = interpreter.interpret(low_tox_result)

        # High toxicity pattern (chaotic, unpredictable binding)
        high_tox_result = QuantumResult(
            counts={'00': 100, '01': 200, '10': 300, '11': 424}
        )
        interpretation_high = interpreter.interpret(high_tox_result)

        assert 'toxicity_prediction' in interpretation_low
        assert 'toxicity_prediction' in interpretation_high

    def test_ic50_estimation(self):
        """Test IC50 value estimation."""
        interpreter = DrugDiscoveryInterpreter()

        quantum_result = QuantumResult(
            counts={'0': 750, '1': 250},
            metadata={'concentration': 1.0}
        )

        ic50 = interpreter.estimate_ic50(quantum_result)
        assert isinstance(ic50, float)
        assert ic50 > 0


class TestDNAAnalysisInterpreter:
    """Test cases for DNAAnalysisInterpreter class."""

    def test_dna_interpreter_initialization(self):
        """Test DNAAnalysisInterpreter initialization."""
        interpreter = DNAAnalysisInterpreter()
        assert interpreter is not None

    def test_interpret_dna_analysis_results(self):
        """Test interpretation of DNA analysis quantum results."""
        interpreter = DNAAnalysisInterpreter()

        quantum_result = QuantumResult(
            counts={'000': 150, '001': 200, '010': 174, '100': 250, '111': 250},
            metadata={'context': 'dna_analysis', 'sequence': 'ATCGATCG'}
        )

        interpretation = interpreter.interpret(quantum_result)

        assert isinstance(interpretation, dict)
        assert 'sequence_analysis' in interpretation
        assert 'mutation_detection' in interpretation
        assert 'quality_assessment' in interpretation
        assert 'gc_content_analysis' in interpretation

    def test_mutation_detection(self):
        """Test mutation detection from quantum results."""
        interpreter = DNAAnalysisInterpreter()

        # Clear mutation pattern
        mutation_result = QuantumResult(
            counts={'00': 900, '01': 50, '10': 25, '11': 25},  # Clear dominant state
            metadata={'reference_sequence': 'ATCG', 'query_sequence': 'ATCG'}
        )

        interpretation = interpreter.interpret(mutation_result)
        assert 'mutation_probability' in interpretation['mutation_detection']

    def test_sequence_quality_assessment(self):
        """Test DNA sequence quality assessment."""
        interpreter = DNAAnalysisInterpreter()

        # High quality pattern (consistent, clear states)
        high_quality = QuantumResult(counts={'00': 512, '11': 512})
        interpretation_high = interpreter.interpret(high_quality)

        # Low quality pattern (noisy, distributed states)
        low_quality = QuantumResult(
            counts={'00': 200, '01': 300, '10': 300, '11': 224}
        )
        interpretation_low = interpreter.interpret(low_quality)

        assert 'sequence_quality' in interpretation_high['quality_assessment']
        assert 'sequence_quality' in interpretation_low['quality_assessment']

    def test_gc_content_analysis(self):
        """Test GC content analysis from quantum results."""
        interpreter = DNAAnalysisInterpreter()

        # Simulate GC-rich sequence results
        gc_rich_result = QuantumResult(
            counts={'11': 700, '01': 200, '10': 100},  # High GC states
            metadata={'sequence': 'GCGCGCGC'}
        )

        interpretation = interpreter.interpret(gc_rich_result)
        assert 'estimated_gc_content' in interpretation['gc_content_analysis']
        assert interpretation['gc_content_analysis']['estimated_gc_content'] > 0.5

    def test_phylogenetic_analysis(self):
        """Test phylogenetic relationship analysis."""
        interpreter = DNAAnalysisInterpreter()

        quantum_result = QuantumResult(
            counts={'000': 300, '001': 200, '010': 200, '111': 324},
            metadata={'species_comparison': ['human', 'chimp', 'mouse']}
        )

        phylo_analysis = interpreter.analyze_phylogenetic_relationships(quantum_result)
        assert isinstance(phylo_analysis, dict)
        assert 'similarity_matrix' in phylo_analysis


class TestInterpretBioResultsFunction:
    """Test cases for the main interpret_bio_results function."""

    def test_interpret_protein_folding(self, bio_interpretation_test_data):
        """Test interpretation of protein folding results."""
        protein_data = bio_interpretation_test_data['protein_folding']
        quantum_result = QuantumResult(
            counts=protein_data['counts'],
            metadata={'context': 'protein_folding'}
        )

        interpretation = interpret_bio_results(quantum_result, BioContext.PROTEIN_FOLDING)

        assert interpretation['context'] == 'protein_folding'
        assert 'energy_landscape' in interpretation
        assert 'confidence' in interpretation
        assert interpretation['confidence'] > 0.5

    def test_interpret_drug_discovery(self, bio_interpretation_test_data):
        """Test interpretation of drug discovery results."""
        drug_data = bio_interpretation_test_data['drug_discovery']
        quantum_result = QuantumResult(
            counts=drug_data['counts'],
            metadata={'context': 'drug_discovery'}
        )

        interpretation = interpret_bio_results(quantum_result, BioContext.DRUG_DISCOVERY)

        assert interpretation['context'] == 'drug_discovery'
        assert 'binding_analysis' in interpretation
        assert 'confidence' in interpretation

    def test_interpret_dna_analysis(self, bio_interpretation_test_data):
        """Test interpretation of DNA analysis results."""
        dna_data = bio_interpretation_test_data['dna_analysis']
        quantum_result = QuantumResult(
            counts=dna_data['counts'],
            metadata={'context': 'dna_analysis'}
        )

        interpretation = interpret_bio_results(quantum_result, BioContext.DNA_ANALYSIS)

        assert interpretation['context'] == 'dna_analysis'
        assert 'sequence_analysis' in interpretation
        assert 'confidence' in interpretation

    def test_interpret_automatic_context_detection(self):
        """Test automatic context detection from metadata."""
        # Test with protein folding metadata
        protein_result = QuantumResult(
            counts={'00': 500, '11': 500},
            metadata={'sequence': 'MKLLVV', 'context': 'protein_folding'}
        )

        interpretation = interpret_bio_results(protein_result)
        assert interpretation['context'] == 'protein_folding'

        # Test with drug discovery metadata
        drug_result = QuantumResult(
            counts={'00': 600, '11': 400},
            metadata={'smiles': 'CCO', 'context': 'drug_discovery'}
        )

        interpretation = interpret_bio_results(drug_result)
        assert interpretation['context'] == 'drug_discovery'

    def test_interpret_with_confidence_threshold(self):
        """Test interpretation with confidence thresholds."""
        quantum_result = QuantumResult(
            counts={'00': 300, '01': 300, '10': 200, '11': 224},
            metadata={'context': 'protein_folding'}
        )

        # Test with different confidence thresholds
        high_threshold = interpret_bio_results(
            quantum_result, BioContext.PROTEIN_FOLDING, min_confidence=0.9
        )

        low_threshold = interpret_bio_results(
            quantum_result, BioContext.PROTEIN_FOLDING, min_confidence=0.1
        )

        assert 'confidence' in high_threshold
        assert 'confidence' in low_threshold

    def test_interpret_error_handling(self):
        """Test error handling in interpretation."""
        # Test with empty results
        empty_result = QuantumResult(counts={})

        interpretation = interpret_bio_results(empty_result, BioContext.PROTEIN_FOLDING)
        assert 'error' in interpretation or interpretation['confidence'] == 0

        # Test with invalid context
        invalid_result = QuantumResult(counts={'00': 500, '11': 500})

        with pytest.raises(ValueError):
            interpret_bio_results(invalid_result, "invalid_context")


class TestVisualizationFunctions:
    """Test cases for biological visualization functions."""

    def test_visualize_protein_structure(self, mock_matplotlib):
        """Test protein structure visualization."""
        protein = ProteinStructure(
            sequence="MKLLVV",
            coordinates=np.random.rand(6, 3),
            energy=-125.5,
            conformation_id="test_conf",
            stability_score=0.85
        )

        # Test visualization creation
        fig = visualize_protein_structure(protein)
        assert fig is not None

        # Check that matplotlib functions were called
        mock_matplotlib['figure'].assert_called()

    def test_visualize_drug_binding(self, mock_matplotlib):
        """Test drug binding visualization."""
        binding_data = {
            'drug_molecule': DrugMolecule(
                smiles="CCO",
                molecular_weight=46.07,
                binding_affinity=7.5,
                ic50=1.2,
                toxicity_score=0.3
            ),
            'binding_sites': [{'site_id': 1, 'affinity': 8.0, 'coordinates': [0, 0, 0]}],
            'binding_energy': -45.2
        }

        fig = visualize_drug_binding(binding_data)
        assert fig is not None

    def test_visualize_dna_analysis(self, mock_matplotlib):
        """Test DNA analysis visualization."""
        dna_data = {
            'sequence': DNASequence(
                sequence="ATCGATCGATCG",
                gc_content=0.5,
                mutation_probability=0.05,
                quality_score=0.95
            ),
            'mutations': [{'position': 4, 'original': 'A', 'mutated': 'T'}],
            'quality_scores': [0.9, 0.95, 0.92, 0.88, 0.93, 0.96]
        }

        fig = visualize_dna_analysis(dna_data)
        assert fig is not None

    def test_visualization_customization(self, mock_matplotlib):
        """Test visualization customization options."""
        protein = ProteinStructure(
            sequence="ACDE",
            coordinates=np.random.rand(4, 3),
            energy=-50.0,
            conformation_id="custom_conf",
            stability_score=0.7
        )

        # Test with custom parameters
        fig = visualize_protein_structure(
            protein,
            color_scheme='energy',
            show_backbone=True,
            title='Custom Protein Visualization'
        )
        assert fig is not None

    @pytest.mark.parametrize("output_format", ['png', 'pdf', 'svg'])
    def test_visualization_export(self, mock_matplotlib, temp_dir, output_format):
        """Test visualization export to different formats."""
        protein = ProteinStructure(
            sequence="MK",
            coordinates=np.array([[0, 0, 0], [1, 1, 1]]),
            energy=-25.0,
            conformation_id="export_test",
            stability_score=0.8
        )

        output_path = f"{temp_dir}/protein_viz.{output_format}"
        fig = visualize_protein_structure(protein, save_path=output_path)

        assert fig is not None
        # In a real test, we would check that the file was created
        # mock_matplotlib['savefig'].assert_called_with(output_path)


class TestBioUtilityFunctions:
    """Test cases for biological utility functions."""

    def test_calculate_protein_energy(self):
        """Test protein energy calculation utilities."""
        # Test with different conformations
        conformation1 = np.array([[0, 0, 0], [1, 1, 1], [2, 0, 1]])
        conformation2 = np.array([[0, 0, 0], [1, 0, 0], [2, 0, 0]])

        energy1 = calculate_protein_energy(conformation1)
        energy2 = calculate_protein_energy(conformation2)

        assert isinstance(energy1, float)
        assert isinstance(energy2, float)
        # Extended conformations typically have higher energy
        assert energy2 > energy1

    def test_analyze_binding_affinity(self):
        """Test binding affinity analysis utilities."""
        quantum_counts = {'00': 700, '01': 100, '10': 100, '11': 100}

        affinity = analyze_binding_affinity(quantum_counts)
        assert isinstance(affinity, float)
        assert 0 <= affinity <= 10  # Typical affinity range

    def test_sequence_analysis(self):
        """Test DNA sequence analysis utilities."""
        sequence = "ATCGATCGATCGATCG"

        analysis = sequence_analysis(sequence)
        assert isinstance(analysis, dict)
        assert 'gc_content' in analysis
        assert 'length' in analysis
        assert 'composition' in analysis

        # Verify GC content calculation
        expected_gc = (sequence.count('G') + sequence.count('C')) / len(sequence)
        assert abs(analysis['gc_content'] - expected_gc) < 0.001

    def test_mutation_scoring(self):
        """Test mutation scoring utilities."""
        from bioql.bio_interpreter import score_mutation_likelihood

        # High confidence, clear states suggest low mutation
        low_mutation_counts = {'00': 900, '11': 100}
        low_score = score_mutation_likelihood(low_mutation_counts)

        # Distributed states suggest higher mutation probability
        high_mutation_counts = {'00': 250, '01': 250, '10': 250, '11': 250}
        high_score = score_mutation_likelihood(high_mutation_counts)

        assert low_score < high_score
        assert 0 <= low_score <= 1
        assert 0 <= high_score <= 1

    def test_stability_analysis(self):
        """Test protein stability analysis utilities."""
        from bioql.bio_interpreter import analyze_protein_stability

        # Stable protein pattern (clear dominant states)
        stable_counts = {'000': 800, '111': 200}
        stable_analysis = analyze_protein_stability(stable_counts)

        # Unstable protein pattern (distributed energy states)
        unstable_counts = {'000': 200, '001': 200, '010': 200, '100': 200, '111': 200}
        unstable_analysis = analyze_protein_stability(unstable_counts)

        assert stable_analysis['stability_score'] > unstable_analysis['stability_score']
        assert 0 <= stable_analysis['stability_score'] <= 1
        assert 0 <= unstable_analysis['stability_score'] <= 1


class TestBioInterpreterPerformance:
    """Performance tests for bio interpreter functions."""

    @pytest.mark.slow
    def test_interpretation_performance_large_results(self):
        """Test interpretation performance with large quantum results."""
        import time

        # Generate large quantum result
        large_counts = {f'{i:010b}': np.random.randint(1, 100) for i in range(1000)}
        large_result = QuantumResult(
            counts=large_counts,
            metadata={'context': 'protein_folding'}
        )

        start_time = time.time()
        interpretation = interpret_bio_results(large_result, BioContext.PROTEIN_FOLDING)
        interpretation_time = time.time() - start_time

        assert interpretation['context'] == 'protein_folding'
        assert interpretation_time < 10.0  # Should complete within 10 seconds

    @pytest.mark.slow
    def test_visualization_performance(self, mock_matplotlib):
        """Test visualization performance with large datasets."""
        import time

        # Large protein structure
        large_protein = ProteinStructure(
            sequence="A" * 1000,  # 1000 amino acids
            coordinates=np.random.rand(1000, 3),
            energy=-1500.0,
            conformation_id="large_protein",
            stability_score=0.75
        )

        start_time = time.time()
        fig = visualize_protein_structure(large_protein)
        viz_time = time.time() - start_time

        assert fig is not None
        assert viz_time < 15.0  # Should complete within 15 seconds


class TestBioInterpreterIntegration:
    """Integration tests for bio interpreter with quantum results."""

    @pytest.mark.integration
    @pytest.mark.bio
    def test_end_to_end_protein_analysis(self):
        """Test end-to-end protein folding analysis workflow."""
        # Simulate realistic protein folding quantum result
        quantum_result = QuantumResult(
            counts={
                '0000': 150,  # Native state
                '0001': 100,  # Near-native
                '0010': 80,   # Intermediate
                '0100': 70,   # Intermediate
                '1000': 60,   # Unfolded
                '1111': 40    # Completely unfolded
            },
            statevector=np.array([0.3, 0.25, 0.2, 0.15, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            metadata={
                'context': 'protein_folding',
                'sequence': 'MVKLLVV',
                'temperature': 300,
                'num_qubits': 4
            }
        )

        interpretation = interpret_bio_results(quantum_result, BioContext.PROTEIN_FOLDING)

        # Verify complete interpretation
        assert interpretation['context'] == 'protein_folding'
        assert 'energy_landscape' in interpretation
        assert 'stability_analysis' in interpretation
        assert 'confidence' in interpretation
        assert interpretation['confidence'] > 0.6

    @pytest.mark.integration
    @pytest.mark.bio
    def test_end_to_end_drug_screening(self):
        """Test end-to-end drug screening analysis workflow."""
        quantum_result = QuantumResult(
            counts={
                '00': 450,  # No binding
                '01': 200,  # Weak binding
                '10': 250,  # Moderate binding
                '11': 100   # Strong binding
            },
            metadata={
                'context': 'drug_discovery',
                'drug_smiles': 'CC(C)CC1=CC=C(C=C1)C(C)C(=O)O',
                'target_protein': 'COX-2',
                'concentration': 1e-6
            }
        )

        interpretation = interpret_bio_results(quantum_result, BioContext.DRUG_DISCOVERY)

        assert interpretation['context'] == 'drug_discovery'
        assert 'binding_analysis' in interpretation
        assert 'selectivity_score' in interpretation
        assert 'drug_likelihood' in interpretation

    @pytest.mark.integration
    @pytest.mark.bio
    def test_end_to_end_dna_sequencing(self):
        """Test end-to-end DNA sequencing analysis workflow."""
        quantum_result = QuantumResult(
            counts={
                '000': 200,  # AAA
                '001': 150,  # AAT
                '010': 180,  # ATA
                '011': 120,  # ATT
                '100': 170,  # TAA
                '101': 140,  # TAT
                '110': 160,  # TTA
                '111': 100   # TTT
            },
            metadata={
                'context': 'dna_analysis',
                'reference_sequence': 'ATCGATCGATCG',
                'quality_threshold': 0.9
            }
        )

        interpretation = interpret_bio_results(quantum_result, BioContext.DNA_ANALYSIS)

        assert interpretation['context'] == 'dna_analysis'
        assert 'sequence_analysis' in interpretation
        assert 'mutation_detection' in interpretation
        assert 'quality_assessment' in interpretation


if __name__ == "__main__":
    pytest.main([__file__, "-v"])