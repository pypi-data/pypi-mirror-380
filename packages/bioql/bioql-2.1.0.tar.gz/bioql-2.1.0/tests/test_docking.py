"""
Unit tests for bioql.docking module
"""

import pytest
from pathlib import Path
import tempfile

# Test docking pipeline
def test_dock_missing_receptor():
    """Test docking with missing receptor file"""
    from bioql.docking import dock

    result = dock(
        receptor="/nonexistent/protein.pdb",
        ligand_smiles="CCO",
        backend="auto",
    )

    assert result is not None
    assert not result.success
    assert "not found" in result.error_message.lower()


def test_dock_no_ligand():
    """Test docking with no ligand specified"""
    from bioql.docking import dock

    # Create minimal PDB
    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("ATOM      1  CA  ALA A   1      10.000  10.000  10.000  1.00 20.00           C\nEND\n")
    test_pdb.close()

    try:
        result = dock(
            receptor=test_pdb.name,
            ligand_smiles=None,
            ligand_file=None,
            backend="auto",
        )

        assert result is not None
        assert not result.success
        assert "must be provided" in result.error_message.lower()
    finally:
        Path(test_pdb.name).unlink(missing_ok=True)


def test_dock_unknown_backend():
    """Test docking with unknown backend"""
    from bioql.docking import dock

    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("ATOM      1  CA  ALA A   1      10.000  10.000  10.000  1.00 20.00           C\nEND\n")
    test_pdb.close()

    try:
        result = dock(
            receptor=test_pdb.name,
            ligand_smiles="CCO",
            backend="unknown_backend",
        )

        assert result is not None
        assert not result.success
        assert "unknown" in result.error_message.lower()
    finally:
        Path(test_pdb.name).unlink(missing_ok=True)


# Test Vina runner
def test_vina_runner_init():
    """Test VinaRunner initialization"""
    from bioql.docking.vina_runner import VinaRunner

    runner = VinaRunner()
    assert runner is not None


def test_vina_runner_check_available():
    """Test Vina availability check"""
    from bioql.docking.vina_runner import VinaRunner

    runner = VinaRunner()
    is_available = runner.check_available()

    # Should return bool without crashing
    assert isinstance(is_available, bool)


def test_vina_runner_missing_files():
    """Test Vina runner with missing input files"""
    from bioql.docking.vina_runner import VinaRunner

    runner = VinaRunner()

    result = runner.dock(
        receptor_pdbqt="/nonexistent/receptor.pdbqt",
        ligand_pdbqt="/nonexistent/ligand.pdbqt",
        center=(0, 0, 0),
        box_size=(20, 20, 20),
    )

    assert result is not None
    assert not result.success
    assert result.error_message is not None


# Test Quantum runner
def test_quantum_runner_init():
    """Test QuantumRunner initialization"""
    from bioql.docking.quantum_runner import QuantumRunner

    runner = QuantumRunner()
    assert runner is not None
    assert runner.backend == "simulator"


def test_quantum_runner_check_available():
    """Test quantum backend availability check"""
    from bioql.docking.quantum_runner import QuantumRunner

    runner = QuantumRunner()
    is_available = runner.check_available()

    # Should return bool
    assert isinstance(is_available, bool)


def test_quantum_runner_without_api_key():
    """Test quantum runner without API key"""
    from bioql.docking.quantum_runner import QuantumRunner

    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("ATOM      1  CA  ALA A   1      10.000  10.000  10.000  1.00 20.00           C\nEND\n")
    test_pdb.close()

    try:
        runner = QuantumRunner(api_key=None)

        result = runner.dock(
            receptor_pdb=test_pdb.name,
            ligand_smiles="CCO",
            shots=100,
        )

        # Should handle missing API key gracefully
        assert result is not None
    finally:
        Path(test_pdb.name).unlink(missing_ok=True)


# Test backend selection
def test_select_backend():
    """Test automatic backend selection"""
    from bioql.docking.pipeline import _select_backend

    backend = _select_backend()

    assert backend in ["vina", "quantum"]


def test_calculate_binding_site_center():
    """Test binding site center calculation"""
    from bioql.docking.pipeline import _calculate_binding_site_center

    # Create test PDB
    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("""
ATOM      1  CA  ALA A   1      10.000  10.000  10.000  1.00 20.00           C
ATOM      2  CA  GLY A   2      20.000  20.000  20.000  1.00 20.00           C
END
""")
    test_pdb.close()

    try:
        center = _calculate_binding_site_center(Path(test_pdb.name))

        assert center is not None
        assert len(center) == 3
        assert all(isinstance(x, (int, float)) for x in center)

        # Center should be around (15, 15, 15) - midpoint of two atoms
        assert 0 < center[0] < 30
        assert 0 < center[1] < 30
        assert 0 < center[2] < 30
    finally:
        Path(test_pdb.name).unlink(missing_ok=True)


# Integration tests
@pytest.mark.integration
def test_full_docking_workflow_quantum():
    """Test complete quantum docking workflow"""
    from bioql.docking import dock
    import os

    # Create test PDB
    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("""
ATOM      1  N   GLY A   1      10.000  10.000  10.000  1.00 20.00           N
ATOM      2  CA  GLY A   1      11.000  11.000  11.000  1.00 20.00           C
ATOM      3  C   GLY A   1      12.000  12.000  12.000  1.00 20.00           C
END
""")
    test_pdb.close()

    try:
        result = dock(
            receptor=test_pdb.name,
            ligand_smiles="CCO",
            backend="quantum",
            api_key=os.getenv("BIOQL_API_KEY"),  # May be None
            shots=100,
        )

        # Should complete without crashing
        assert result is not None
        assert result.job_id is not None
        assert result.backend == "quantum"

    finally:
        Path(test_pdb.name).unlink(missing_ok=True)


@pytest.mark.slow
@pytest.mark.integration
def test_full_docking_workflow_vina():
    """Test complete Vina docking workflow (if Vina available)"""
    from bioql.docking import dock
    from bioql.docking.vina_runner import VinaRunner

    # Check if Vina is available
    runner = VinaRunner()
    if not runner.check_available():
        pytest.skip("AutoDock Vina not available")

    # Create test PDB
    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("""
ATOM      1  N   GLY A   1      10.000  10.000  10.000  1.00 20.00           N
ATOM      2  CA  GLY A   1      11.000  11.000  11.000  1.00 20.00           C
END
""")
    test_pdb.close()

    try:
        result = dock(
            receptor=test_pdb.name,
            ligand_smiles="CCO",
            backend="vina",
            center=(10.0, 10.0, 10.0),
            box_size=(15, 15, 15),
        )

        assert result is not None
        assert result.backend == "vina"

    finally:
        Path(test_pdb.name).unlink(missing_ok=True)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])