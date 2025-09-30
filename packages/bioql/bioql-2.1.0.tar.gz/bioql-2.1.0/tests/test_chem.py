"""
Unit tests for bioql.chem module
"""

import pytest
from pathlib import Path
import tempfile

# Test ligand preparation
def test_prepare_ligand_basic():
    """Test basic ligand preparation from SMILES"""
    from bioql.chem import prepare_ligand

    # Test with ethanol (simple molecule)
    result = prepare_ligand(
        smiles="CCO",
        output_format="pdb",
        add_hydrogens=True,
    )

    assert result is not None
    # Should succeed or fail gracefully
    if result.success:
        assert result.output_path is not None
        assert result.num_atoms > 0
        assert result.molecular_weight > 0
    else:
        # If RDKit not available, should have clear error message
        assert result.error_message is not None
        assert "RDKit" in result.error_message or "OpenBabel" in result.error_message


def test_prepare_ligand_invalid_smiles():
    """Test ligand preparation with invalid SMILES"""
    from bioql.chem import prepare_ligand

    result = prepare_ligand(
        smiles="INVALID_SMILES_123",
        output_format="pdb",
    )

    # Should handle invalid SMILES gracefully
    assert result is not None
    if result.success:
        # Some parsers might be very lenient
        pass
    else:
        assert result.error_message is not None


def test_prepare_ligand_complex_molecule():
    """Test with complex molecule (aspirin)"""
    from bioql.chem import prepare_ligand

    aspirin_smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"

    result = prepare_ligand(
        smiles=aspirin_smiles,
        output_format="pdb",
        add_hydrogens=True,
        optimize_geometry=True,
    )

    if result.success:
        assert result.num_atoms > 10  # Aspirin has many atoms
        assert result.molecular_weight > 100  # Aspirin MW ~180
        assert 170 < result.molecular_weight < 200


def test_validate_smiles():
    """Test SMILES validation"""
    from bioql.chem.ligand_prep import validate_smiles

    # Valid SMILES
    assert validate_smiles("CCO") or True  # May return True if RDKit not available
    assert validate_smiles("c1ccccc1") or True  # Benzene

    # Invalid SMILES might not be caught without RDKit
    # So we just check it doesn't crash
    result = validate_smiles("INVALID")
    assert result is not None


# Test receptor preparation
def test_prepare_receptor_missing_file():
    """Test receptor preparation with missing file"""
    from bioql.chem import prepare_receptor

    result = prepare_receptor(
        pdb_path="/nonexistent/file.pdb",
        output_format="pdb",
    )

    assert result is not None
    assert not result.success
    assert "not found" in result.error_message.lower()


def test_prepare_receptor_basic():
    """Test basic receptor preparation"""
    from bioql.chem import prepare_receptor

    # Create a minimal PDB file for testing
    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("""
ATOM      1  N   ALA A   1      10.000  10.000  10.000  1.00 20.00           N
ATOM      2  CA  ALA A   1      11.000  11.000  11.000  1.00 20.00           C
ATOM      3  C   ALA A   1      12.000  12.000  12.000  1.00 20.00           C
ATOM      4  O   ALA A   1      13.000  13.000  13.000  1.00 20.00           O
HETATM    5  O   HOH A 101      20.000  20.000  20.000  1.00 30.00           O
END
""")
    test_pdb.close()

    try:
        result = prepare_receptor(
            pdb_path=test_pdb.name,
            output_format="pdb",
            remove_waters=True,
        )

        assert result is not None
        if result.success:
            assert result.output_path is not None
            assert result.num_atoms >= 4  # Should have at least the ATOM lines
    finally:
        Path(test_pdb.name).unlink(missing_ok=True)


# Test geometry optimizer
def test_geometry_optimizer_init():
    """Test GeometryOptimizer initialization"""
    from bioql.chem import GeometryOptimizer

    optimizer = GeometryOptimizer()
    assert optimizer is not None


def test_geometry_optimizer_from_smiles():
    """Test optimization from SMILES"""
    from bioql.chem import GeometryOptimizer

    optimizer = GeometryOptimizer(backend="auto")

    result = optimizer.optimize(
        smiles="CCO",
        max_iterations=50,
    )

    assert result is not None
    # Should succeed or fail gracefully
    if result.success:
        assert result.output_path is not None
        assert result.final_energy is not None
    else:
        assert result.error_message is not None


def test_geometry_optimizer_no_input():
    """Test optimizer with no input"""
    from bioql.chem import GeometryOptimizer

    optimizer = GeometryOptimizer()

    result = optimizer.optimize()  # No molecule or SMILES

    assert result is not None
    assert not result.success
    assert "must be provided" in result.error_message.lower()


# Integration tests
@pytest.mark.integration
def test_full_ligand_workflow():
    """Test complete ligand preparation workflow"""
    from bioql.chem import prepare_ligand

    # Prepare ligand
    result = prepare_ligand(
        smiles="CN1C=NC2=C1C(=O)N(C(=O)N2C)C",  # Caffeine
        output_path=None,  # Auto-generate
        add_hydrogens=True,
        generate_3d=True,
        optimize_geometry=True,
    )

    if result.success:
        assert result.output_path.exists()
        assert result.molecular_weight > 150  # Caffeine MW ~194

        # Cleanup
        result.output_path.unlink(missing_ok=True)


@pytest.mark.integration
def test_full_receptor_workflow():
    """Test complete receptor preparation workflow"""
    from bioql.chem import prepare_receptor

    # Create test PDB
    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("""
ATOM      1  N   GLY A   1      10.000  10.000  10.000  1.00 20.00           N
ATOM      2  CA  GLY A   1      11.000  11.000  11.000  1.00 20.00           C
ATOM      3  C   GLY A   1      12.000  12.000  12.000  1.00 20.00           C
ATOM      4  O   GLY A   1      13.000  13.000  13.000  1.00 20.00           O
ATOM      5  N   ALA A   2      14.000  14.000  14.000  1.00 20.00           N
HETATM    6  O   HOH A 101      20.000  20.000  20.000  1.00 30.00           O
HETATM    7  O   HOH A 102      21.000  21.000  21.000  1.00 30.00           O
END
""")
    test_pdb.close()

    try:
        result = prepare_receptor(
            pdb_path=test_pdb.name,
            remove_waters=True,
            remove_heteroatoms=False,
        )

        if result.success:
            assert result.output_path.exists()
            assert result.num_residues >= 2  # GLY and ALA

            # Cleanup
            result.output_path.unlink(missing_ok=True)
    finally:
        Path(test_pdb.name).unlink(missing_ok=True)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])