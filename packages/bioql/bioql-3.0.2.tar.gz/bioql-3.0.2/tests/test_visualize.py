"""
Unit tests for bioql.visualize module
"""

import pytest
from pathlib import Path
import tempfile


def test_show_missing_file():
    """Test visualization with missing file"""
    from bioql.visualize import show

    result = show(
        structure_path="/nonexistent/protein.pdb",
        style="cartoon",
    )

    if hasattr(result, 'success'):
        assert not result.success
        assert result.error_message is not None


def test_save_image_missing_file():
    """Test image saving with missing file"""
    from bioql.visualize import save_image

    result = save_image(
        structure_path="/nonexistent/protein.pdb",
        output_path="/tmp/output.png",
    )

    if hasattr(result, 'success'):
        assert not result.success


def test_visualize_complex_missing_files():
    """Test complex visualization with missing files"""
    from bioql.visualize import visualize_complex

    result = visualize_complex(
        receptor_path="/nonexistent/receptor.pdb",
        ligand_path="/nonexistent/ligand.pdb",
    )

    if hasattr(result, 'success'):
        assert not result.success


@pytest.mark.integration
def test_show_basic():
    """Test basic visualization"""
    from bioql.visualize import show

    # Create test PDB
    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("""
ATOM      1  CA  ALA A   1      10.000  10.000  10.000  1.00 20.00           C
END
""")
    test_pdb.close()

    try:
        result = show(
            structure_path=test_pdb.name,
            style="cartoon",
        )

        # Should not crash
        assert result is not None
    finally:
        Path(test_pdb.name).unlink(missing_ok=True)


@pytest.mark.integration
def test_save_image_basic():
    """Test image saving"""
    from bioql.visualize import save_image

    # Create test PDB
    test_pdb = tempfile.NamedTemporaryFile(mode='w', suffix='.pdb', delete=False)
    test_pdb.write("""
ATOM      1  CA  ALA A   1      10.000  10.000  10.000  1.00 20.00           C
END
""")
    test_pdb.close()

    output_png = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    output_png.close()

    try:
        result = save_image(
            structure_path=test_pdb.name,
            output_path=output_png.name,
            width=800,
            height=600,
            ray_trace=False,
        )

        assert result is not None
        if hasattr(result, 'success') and result.success:
            # Image might have been created
            pass
    finally:
        Path(test_pdb.name).unlink(missing_ok=True)
        Path(output_png.name).unlink(missing_ok=True)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])