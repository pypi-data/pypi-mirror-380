#!/usr/bin/env python3
"""
BioQL Biological Results Interpreter

Translates quantum computing results into biologically meaningful insights
for protein folding, drug discovery, and DNA analysis applications.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import numpy as np
import logging

logger = logging.getLogger(__name__)


@dataclass
class BiologicalInterpretation:
    """Container for biological interpretation of quantum results"""
    interpretation_type: str
    confidence: float
    biological_meaning: str
    recommendations: List[str]
    raw_data: Dict[str, Any]


def interpret_bio_results(
    quantum_results: Dict[str, int],
    context: str,
    additional_params: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Interpret quantum computing results in biological context.

    Args:
        quantum_results: Dictionary of quantum measurement results
        context: Biological context (protein_folding, drug_discovery, dna_analysis)
        additional_params: Additional parameters for interpretation

    Returns:
        Dictionary containing biological interpretation
    """

    if not quantum_results:
        return {
            "status": "error",
            "message": "No quantum results to interpret"
        }

    # Normalize the results to probabilities
    total_counts = sum(quantum_results.values())
    probabilities = {state: count/total_counts for state, count in quantum_results.items()}

    # Interpret based on context
    if context.lower() in ["protein_folding", "protein", "folding"]:
        return interpret_protein_folding(probabilities, quantum_results, additional_params)
    elif context.lower() in ["drug_discovery", "drug", "molecular_docking"]:
        return interpret_drug_discovery(probabilities, quantum_results, additional_params)
    elif context.lower() in ["dna_analysis", "dna", "genomics", "sequence"]:
        return interpret_dna_analysis(probabilities, quantum_results, additional_params)
    else:
        return interpret_general_quantum(probabilities, quantum_results)


def interpret_protein_folding(
    probabilities: Dict[str, float],
    raw_results: Dict[str, int],
    params: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Interpret quantum results for protein folding simulations.
    """

    # Find the most probable conformations
    sorted_states = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
    dominant_states = sorted_states[:3]  # Top 3 conformations

    # Calculate folding energy (simplified)
    energy_landscape = calculate_energy_landscape(probabilities)

    # Determine stability
    stability = calculate_stability(probabilities)

    interpretation = {
        "status": "success",
        "biological_context": "protein_folding",
        "dominant_conformations": [
            {
                "state": state,
                "probability": prob,
                "structure": decode_protein_state(state)
            }
            for state, prob in dominant_states
        ],
        "energy_landscape": {
            "minimum_energy": energy_landscape["min"],
            "average_energy": energy_landscape["avg"],
            "energy_variance": energy_landscape["variance"]
        },
        "stability_score": stability,
        "folding_prediction": {
            "native_state": dominant_states[0][0] if dominant_states else "unknown",
            "confidence": dominant_states[0][1] if dominant_states else 0,
            "alternative_folds": len([s for s, p in sorted_states if p > 0.1])
        },
        "biological_insights": generate_protein_insights(stability, dominant_states),
        "recommendations": generate_protein_recommendations(stability, energy_landscape)
    }

    return interpretation


def interpret_drug_discovery(
    probabilities: Dict[str, float],
    raw_results: Dict[str, int],
    params: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Interpret quantum results for drug discovery and molecular docking.
    """

    # Analyze binding affinity
    binding_states = identify_binding_states(probabilities)
    binding_affinity = calculate_binding_affinity(binding_states)

    # Identify molecular interactions
    interactions = identify_molecular_interactions(probabilities)

    interpretation = {
        "status": "success",
        "biological_context": "drug_discovery",
        "binding_affinity": {
            "score": binding_affinity,
            "classification": classify_binding_strength(binding_affinity),
            "confidence": calculate_confidence(probabilities)
        },
        "molecular_interactions": {
            "hydrogen_bonds": interactions.get("h_bonds", 0),
            "hydrophobic_interactions": interactions.get("hydrophobic", 0),
            "electrostatic_interactions": interactions.get("electrostatic", 0)
        },
        "binding_sites": [
            {
                "state": state,
                "probability": prob,
                "interaction_type": classify_interaction(state)
            }
            for state, prob in binding_states[:5]
        ],
        "drug_efficacy_prediction": {
            "predicted_efficacy": "high" if binding_affinity > 0.7 else "moderate" if binding_affinity > 0.4 else "low",
            "selectivity_score": calculate_selectivity(probabilities),
            "off_target_risk": assess_off_target_risk(probabilities)
        },
        "biological_insights": generate_drug_insights(binding_affinity, interactions),
        "recommendations": generate_drug_recommendations(binding_affinity, interactions)
    }

    return interpretation


def interpret_dna_analysis(
    probabilities: Dict[str, float],
    raw_results: Dict[str, int],
    params: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Interpret quantum results for DNA sequence analysis and pattern matching.
    """

    # Identify matched patterns (Grover's algorithm results)
    matched_patterns = identify_dna_patterns(probabilities)

    # Calculate pattern similarity scores
    similarity_scores = calculate_pattern_similarity(matched_patterns)

    interpretation = {
        "status": "success",
        "biological_context": "dna_analysis",
        "matched_sequences": [
            {
                "pattern": decode_dna_state(state),
                "probability": prob,
                "significance": assess_pattern_significance(prob)
            }
            for state, prob in matched_patterns[:5]
        ],
        "pattern_analysis": {
            "total_matches": len([p for p in probabilities.values() if p > 0.1]),
            "highest_match_score": max(probabilities.values()) if probabilities else 0,
            "pattern_diversity": calculate_diversity(probabilities)
        },
        "genomic_insights": {
            "potential_mutations": identify_mutations(matched_patterns),
            "conserved_regions": identify_conserved_regions(matched_patterns),
            "variant_calls": make_variant_calls(matched_patterns)
        },
        "sequence_alignment": {
            "alignment_score": similarity_scores.get("alignment", 0),
            "gap_penalties": similarity_scores.get("gaps", 0),
            "mismatch_rate": similarity_scores.get("mismatches", 0)
        },
        "biological_insights": generate_dna_insights(matched_patterns, similarity_scores),
        "recommendations": generate_dna_recommendations(matched_patterns)
    }

    return interpretation


def interpret_general_quantum(
    probabilities: Dict[str, float],
    raw_results: Dict[str, int]
) -> Dict[str, Any]:
    """
    General interpretation for quantum results without specific biological context.
    """

    sorted_states = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)

    return {
        "status": "success",
        "biological_context": "general",
        "quantum_states": [
            {"state": state, "probability": prob}
            for state, prob in sorted_states[:10]
        ],
        "statistics": {
            "entropy": calculate_entropy(probabilities),
            "most_probable_state": sorted_states[0] if sorted_states else None,
            "total_states": len(probabilities),
            "effective_states": len([p for p in probabilities.values() if p > 0.01])
        },
        "message": "Quantum computation completed. Consider specifying biological context for detailed interpretation."
    }


# Helper functions

def calculate_energy_landscape(probabilities: Dict[str, float]) -> Dict[str, float]:
    """Calculate simplified energy landscape from probability distribution."""
    if not probabilities:
        return {"min": 0, "avg": 0, "variance": 0}

    # Convert probabilities to energies (Boltzmann-like)
    energies = [-np.log(p + 1e-10) for p in probabilities.values()]

    return {
        "min": min(energies),
        "avg": np.mean(energies),
        "variance": np.var(energies)
    }


def calculate_stability(probabilities: Dict[str, float]) -> float:
    """Calculate protein stability score from state distribution."""
    if not probabilities:
        return 0.0

    # High probability in few states indicates stability
    sorted_probs = sorted(probabilities.values(), reverse=True)
    if len(sorted_probs) == 0:
        return 0.0

    # Stability based on dominance of top states
    top_state_dominance = sorted_probs[0] if sorted_probs else 0
    entropy = calculate_entropy(probabilities)

    # Normalize to 0-1 scale
    stability_score = top_state_dominance * (1 - entropy / np.log(len(probabilities) + 1))

    return min(max(stability_score, 0.0), 1.0)


def calculate_binding_affinity(binding_states: List[tuple]) -> float:
    """Calculate binding affinity score from quantum states."""
    if not binding_states:
        return 0.0

    # Sum probabilities of binding-favorable states
    total_binding_prob = sum(prob for _, prob in binding_states)

    # Apply sigmoid transformation for realistic scoring
    affinity = 1 / (1 + np.exp(-10 * (total_binding_prob - 0.5)))

    return affinity


def calculate_entropy(probabilities: Dict[str, float]) -> float:
    """Calculate Shannon entropy of probability distribution."""
    entropy = 0.0
    for p in probabilities.values():
        if p > 0:
            entropy -= p * np.log2(p)
    return entropy


def decode_protein_state(state: str) -> str:
    """Decode quantum state to protein structure representation."""
    # Simplified mapping of quantum states to structural features
    structures = ["alpha-helix", "beta-sheet", "random-coil", "turn", "loop"]

    # Use state bits to determine structure
    state_int = int(state.replace(" ", ""), 2) if state.replace(" ", "").isdigit() else 0
    return structures[state_int % len(structures)]


def decode_dna_state(state: str) -> str:
    """Decode quantum state to DNA sequence."""
    # Map 2-bit patterns to nucleotides
    nucleotide_map = {"00": "A", "01": "T", "10": "G", "11": "C"}

    sequence = ""
    clean_state = state.replace(" ", "")

    for i in range(0, len(clean_state), 2):
        if i + 1 < len(clean_state):
            bits = clean_state[i:i+2]
            sequence += nucleotide_map.get(bits, "N")

    return sequence


def identify_binding_states(probabilities: Dict[str, float]) -> List[tuple]:
    """Identify states representing favorable binding configurations."""
    # States with high probability likely represent stable binding
    threshold = np.mean(list(probabilities.values())) if probabilities else 0
    binding_states = [(state, prob) for state, prob in probabilities.items()
                     if prob > threshold]
    return sorted(binding_states, key=lambda x: x[1], reverse=True)


def identify_molecular_interactions(probabilities: Dict[str, float]) -> Dict[str, int]:
    """Identify types of molecular interactions from quantum states."""
    interactions = {
        "h_bonds": 0,
        "hydrophobic": 0,
        "electrostatic": 0
    }

    for state, prob in probabilities.items():
        if prob > 0.1:  # Significant states only
            state_bits = state.replace(" ", "")

            # Simplified classification based on state patterns
            if "11" in state_bits:
                interactions["h_bonds"] += 1
            if "00" in state_bits:
                interactions["hydrophobic"] += 1
            if "10" in state_bits or "01" in state_bits:
                interactions["electrostatic"] += 1

    return interactions


def identify_dna_patterns(probabilities: Dict[str, float]) -> List[tuple]:
    """Identify DNA sequence patterns from quantum states."""
    # Grover's algorithm amplifies target patterns
    mean_prob = np.mean(list(probabilities.values())) if probabilities else 0
    std_prob = np.std(list(probabilities.values())) if len(probabilities) > 1 else 0

    # Patterns with probability > mean + std are likely matches
    threshold = mean_prob + std_prob
    patterns = [(state, prob) for state, prob in probabilities.items()
               if prob > threshold]

    return sorted(patterns, key=lambda x: x[1], reverse=True)


def calculate_pattern_similarity(patterns: List[tuple]) -> Dict[str, float]:
    """Calculate similarity metrics for DNA patterns."""
    if not patterns:
        return {"alignment": 0, "gaps": 0, "mismatches": 0}

    # Simplified scoring
    top_pattern_prob = patterns[0][1] if patterns else 0

    return {
        "alignment": top_pattern_prob,
        "gaps": 1 - top_pattern_prob,
        "mismatches": len(patterns) / 10 if patterns else 0
    }


def classify_binding_strength(affinity: float) -> str:
    """Classify binding affinity into categories."""
    if affinity > 0.8:
        return "strong"
    elif affinity > 0.5:
        return "moderate"
    elif affinity > 0.2:
        return "weak"
    else:
        return "negligible"


def classify_interaction(state: str) -> str:
    """Classify the type of molecular interaction from quantum state."""
    state_bits = state.replace(" ", "")

    # Simplified classification
    if state_bits.count("1") > state_bits.count("0"):
        return "polar"
    else:
        return "hydrophobic"


def calculate_confidence(probabilities: Dict[str, float]) -> float:
    """Calculate confidence score for predictions."""
    if not probabilities:
        return 0.0

    # High confidence when few states dominate
    sorted_probs = sorted(probabilities.values(), reverse=True)
    if len(sorted_probs) == 0:
        return 0.0

    top_prob = sorted_probs[0]
    entropy = calculate_entropy(probabilities)
    max_entropy = np.log2(len(probabilities)) if len(probabilities) > 1 else 1

    confidence = top_prob * (1 - entropy / max_entropy) if max_entropy > 0 else top_prob

    return min(max(confidence, 0.0), 1.0)


def calculate_selectivity(probabilities: Dict[str, float]) -> float:
    """Calculate drug selectivity score."""
    if not probabilities:
        return 0.0

    # High selectivity when binding is specific (low entropy)
    entropy = calculate_entropy(probabilities)
    max_entropy = np.log2(len(probabilities)) if len(probabilities) > 1 else 1

    selectivity = 1 - (entropy / max_entropy) if max_entropy > 0 else 1

    return min(max(selectivity, 0.0), 1.0)


def assess_off_target_risk(probabilities: Dict[str, float]) -> str:
    """Assess risk of off-target drug effects."""
    # Count states with significant probability
    significant_states = len([p for p in probabilities.values() if p > 0.1])

    if significant_states <= 2:
        return "low"
    elif significant_states <= 5:
        return "moderate"
    else:
        return "high"


def assess_pattern_significance(probability: float) -> str:
    """Assess biological significance of DNA pattern match."""
    if probability > 0.5:
        return "highly_significant"
    elif probability > 0.2:
        return "significant"
    elif probability > 0.05:
        return "moderately_significant"
    else:
        return "low_significance"


def identify_mutations(patterns: List[tuple]) -> List[str]:
    """Identify potential mutations from DNA patterns."""
    mutations = []

    for state, prob in patterns[:3]:  # Top 3 patterns
        if prob > 0.2:
            sequence = decode_dna_state(state)
            if "N" not in sequence:  # Valid sequence
                mutations.append(f"Potential variant: {sequence}")

    return mutations


def identify_conserved_regions(patterns: List[tuple]) -> List[str]:
    """Identify conserved DNA regions."""
    conserved = []

    # High probability patterns likely represent conserved regions
    for state, prob in patterns:
        if prob > 0.3:
            sequence = decode_dna_state(state)
            conserved.append(sequence)

    return conserved


def make_variant_calls(patterns: List[tuple]) -> List[Dict[str, Any]]:
    """Make variant calls from DNA pattern analysis."""
    variants = []

    for i, (state, prob) in enumerate(patterns[:5]):
        if prob > 0.15:
            variants.append({
                "position": i,
                "sequence": decode_dna_state(state),
                "confidence": prob,
                "type": "SNP" if len(state) <= 4 else "indel"
            })

    return variants


def calculate_diversity(probabilities: Dict[str, float]) -> float:
    """Calculate diversity index for patterns."""
    if not probabilities:
        return 0.0

    # Simpson's diversity index
    diversity = 1 - sum(p**2 for p in probabilities.values())

    return diversity


def generate_protein_insights(stability: float, dominant_states: List[tuple]) -> List[str]:
    """Generate biological insights for protein folding."""
    insights = []

    if stability > 0.7:
        insights.append("Protein shows high structural stability")
    elif stability > 0.4:
        insights.append("Protein exhibits moderate stability with some flexibility")
    else:
        insights.append("Protein appears to be highly dynamic or unfolded")

    if len(dominant_states) == 1:
        insights.append("Single dominant conformation suggests native fold")
    elif len(dominant_states) > 3:
        insights.append("Multiple conformations indicate structural heterogeneity")

    return insights


def generate_protein_recommendations(stability: float, energy: Dict[str, float]) -> List[str]:
    """Generate recommendations for protein folding analysis."""
    recommendations = []

    if stability < 0.5:
        recommendations.append("Consider molecular dynamics refinement")
        recommendations.append("Investigate stabilizing mutations")

    if energy["variance"] > 5:
        recommendations.append("High energy variance suggests multiple folding pathways")

    recommendations.append("Validate results with experimental structures if available")

    return recommendations


def generate_drug_insights(affinity: float, interactions: Dict[str, int]) -> List[str]:
    """Generate biological insights for drug discovery."""
    insights = []

    if affinity > 0.7:
        insights.append("Strong binding affinity indicates potential drug candidate")

    if interactions["h_bonds"] > 3:
        insights.append("Multiple hydrogen bonds suggest specific binding")

    if interactions["hydrophobic"] > interactions["electrostatic"]:
        insights.append("Binding dominated by hydrophobic interactions")

    return insights


def generate_drug_recommendations(affinity: float, interactions: Dict[str, int]) -> List[str]:
    """Generate recommendations for drug discovery."""
    recommendations = []

    if affinity > 0.6:
        recommendations.append("Proceed with lead optimization")
        recommendations.append("Consider ADMET profiling")
    else:
        recommendations.append("Explore structural modifications to improve binding")

    if interactions["h_bonds"] < 2:
        recommendations.append("Add hydrogen bond donors/acceptors for specificity")

    return recommendations


def generate_dna_insights(patterns: List[tuple], similarity: Dict[str, float]) -> List[str]:
    """Generate biological insights for DNA analysis."""
    insights = []

    if patterns and patterns[0][1] > 0.5:
        insights.append("Strong pattern match found in sequence")

    if similarity["alignment"] > 0.8:
        insights.append("High sequence similarity detected")

    if len(patterns) > 10:
        insights.append("Multiple sequence variants identified")

    return insights


def generate_dna_recommendations(patterns: List[tuple]) -> List[str]:
    """Generate recommendations for DNA analysis."""
    recommendations = []

    if patterns:
        recommendations.append("Validate findings with additional sequencing")

        if len(patterns) > 5:
            recommendations.append("Consider population-level analysis for variants")

    recommendations.append("Cross-reference with genomic databases")

    return recommendations


# Public API
__all__ = [
    'interpret_bio_results',
    'BiologicalInterpretation',
    'interpret_protein_folding',
    'interpret_drug_discovery',
    'interpret_dna_analysis'
]