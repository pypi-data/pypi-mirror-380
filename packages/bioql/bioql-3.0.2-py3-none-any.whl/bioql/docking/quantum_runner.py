"""
Quantum Computing Backend Runner for Molecular Docking

Uses BioQL's quantum computing capabilities for docking calculations.
"""

from pathlib import Path
from typing import Optional, Union, Dict, Any, List
from dataclasses import dataclass

from ..logger import get_logger

logger = get_logger(__name__)


@dataclass
class QuantumDockingResult:
    """Result from quantum docking."""

    success: bool
    score: Optional[float]
    energy: Optional[float]
    poses: List[str]
    output_path: Optional[Path]
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class QuantumRunner:
    """
    Quantum computing runner for molecular docking.

    Uses BioQL's quantum backend to calculate binding energies
    and optimal ligand conformations.
    """

    def __init__(self, api_key: Optional[str] = None, backend: str = "simulator"):
        """
        Initialize quantum runner.

        Args:
            api_key: BioQL API key (optional)
            backend: Quantum backend (simulator, ibm_brisbane, ionq, etc.)
        """
        self.api_key = api_key
        self.backend = backend
        logger.info(f"Initialized QuantumRunner with backend: {backend}")

    def check_available(self) -> bool:
        """Check if quantum backend is available."""
        try:
            from .. import quantum
            return True
        except ImportError:
            return False

    def dock(
        self,
        receptor_pdb: Union[str, Path],
        ligand_smiles: str,
        shots: int = 1024,
        output_dir: Optional[Union[str, Path]] = None,
    ) -> QuantumDockingResult:
        """
        Run quantum docking.

        Args:
            receptor_pdb: Path to receptor PDB file
            ligand_smiles: Ligand SMILES string
            shots: Number of quantum shots
            output_dir: Output directory

        Returns:
            QuantumDockingResult object

        Example:
            >>> runner = QuantumRunner(api_key="your_key")
            >>> result = runner.dock(
            ...     receptor_pdb="protein.pdb",
            ...     ligand_smiles="CCO",
            ...     shots=1024,
            ... )
        """
        logger.info("Starting quantum docking")

        try:
            from .. import quantum

            # Construct natural language command for quantum docking
            command = f"Dock ligand with SMILES {ligand_smiles} to receptor protein, calculate binding energy using quantum simulation"

            logger.debug(f"Quantum command: {command}")

            # Execute quantum docking
            if self.api_key:
                result = quantum(
                    command,
                    api_key=self.api_key,
                    backend=self.backend,
                    shots=shots,
                )
            else:
                # Try without API key (local simulator)
                logger.warning("No API key provided, using local simulator")
                result = quantum(
                    command,
                    backend="simulator",
                    shots=shots,
                )

            if not result.success:
                return QuantumDockingResult(
                    success=False,
                    score=None,
                    energy=None,
                    poses=[],
                    output_path=None,
                    error_message=result.error_message,
                )

            # Extract binding energy from quantum result
            energy = result.energy if hasattr(result, 'energy') else None

            # Convert energy to score (kcal/mol equivalent)
            # This is a simplified conversion
            score = energy * 627.509 if energy else None  # Hartree to kcal/mol

            logger.info(f"Quantum docking complete. Energy: {energy}, Score: {score}")

            return QuantumDockingResult(
                success=True,
                score=score,
                energy=energy,
                poses=[],  # Quantum docking doesn't generate explicit poses yet
                output_path=None,
                metadata={
                    "quantum_backend": self.backend,
                    "shots": shots,
                    "quantum_counts": result.counts if hasattr(result, 'counts') else None,
                },
            )

        except ImportError:
            error_msg = "BioQL quantum module not available"
            logger.error(error_msg)
            return QuantumDockingResult(
                success=False,
                score=None,
                energy=None,
                poses=[],
                output_path=None,
                error_message=error_msg,
            )

        except Exception as e:
            logger.error(f"Quantum docking error: {e}")
            return QuantumDockingResult(
                success=False,
                score=None,
                energy=None,
                poses=[],
                output_path=None,
                error_message=str(e),
            )

    def calculate_binding_energy(
        self,
        receptor_pdb: Union[str, Path],
        ligand_smiles: str,
        shots: int = 1024,
    ) -> Optional[float]:
        """
        Calculate binding energy using quantum computing.

        Args:
            receptor_pdb: Path to receptor PDB
            ligand_smiles: Ligand SMILES
            shots: Number of quantum shots

        Returns:
            Binding energy in Hartrees or None if failed
        """
        result = self.dock(receptor_pdb, ligand_smiles, shots=shots)

        if result.success:
            return result.energy

        return None