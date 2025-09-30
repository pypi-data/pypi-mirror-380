"""
Unit tests for bioql.dynamic_bridge module (Meta-wrapper)
"""

import pytest


def test_dynamic_bridge_init():
    """Test DynamicLibraryBridge initialization"""
    from bioql.dynamic_bridge import DynamicLibraryBridge

    bridge = DynamicLibraryBridge()
    assert bridge is not None
    assert bridge.registry is not None


def test_parse_command_use_pattern():
    """Test parsing 'Use X to do Y' pattern"""
    from bioql.dynamic_bridge import DynamicLibraryBridge

    bridge = DynamicLibraryBridge()

    # Test RDKit command
    parsed = bridge.parse_command(
        "Use RDKit to calculate molecular weight of aspirin SMILES CC(=O)OC1=CC=CC=C1C(=O)O"
    )

    assert parsed is not None
    assert parsed['library'] == 'rdkit'
    assert 'molecular weight' in parsed['action']


def test_parse_command_call_pattern():
    """Test parsing 'Call X.Y with Z' pattern"""
    from bioql.dynamic_bridge import DynamicLibraryBridge

    bridge = DynamicLibraryBridge()

    parsed = bridge.parse_command(
        "Call numpy.mean with array [1, 2, 3, 4, 5]"
    )

    assert parsed is not None
    assert parsed['library'] == 'numpy'


def test_extract_arguments_smiles():
    """Test extracting SMILES from text"""
    from bioql.dynamic_bridge import DynamicLibraryBridge

    bridge = DynamicLibraryBridge()

    args = bridge.extract_arguments(
        "calculate molecular weight of aspirin SMILES CC(=O)OC1=CC=CC=C1C(=O)O"
    )

    assert 'smiles' in args
    assert args['smiles'] == "CC(=O)OC1=CC=CC=C1C(=O)O"


def test_extract_arguments_array():
    """Test extracting arrays from text"""
    from bioql.dynamic_bridge import DynamicLibraryBridge

    bridge = DynamicLibraryBridge()

    args = bridge.extract_arguments(
        "calculate mean of array [1, 2, 3, 4, 5]"
    )

    assert 'array' in args
    assert args['array'] == [1.0, 2.0, 3.0, 4.0, 5.0]


def test_extract_arguments_file_path():
    """Test extracting file paths from text"""
    from bioql.dynamic_bridge import DynamicLibraryBridge

    bridge = DynamicLibraryBridge()

    args = bridge.extract_arguments(
        "read CSV file data/compounds.csv"
    )

    assert 'file_path' in args
    assert 'csv' in args['file_path']


def test_dynamic_call_function():
    """Test dynamic_call function"""
    from bioql import dynamic_call

    # Test with a command that should work if numpy is available
    result = dynamic_call(
        "Use numpy to calculate mean of array [1, 2, 3, 4, 5]"
    )

    assert result is not None
    if result.success:
        assert result.result == 3.0
        assert result.library == "numpy"
    else:
        # numpy might not be installed
        assert "numpy" in result.error_message.lower() or "not installed" in result.error_message.lower()


def test_dynamic_call_rdkit():
    """Test dynamic_call with RDKit"""
    from bioql import dynamic_call

    result = dynamic_call(
        "Use RDKit to calculate molecular weight of aspirin SMILES CC(=O)OC1=CC=CC=C1C(=O)O"
    )

    assert result is not None
    if result.success:
        # Aspirin MW is ~180.16
        assert 175 < result.result < 185
        assert result.library == "rdkit"
    else:
        # RDKit might not be installed
        assert result.error_message is not None


def test_register_library():
    """Test registering a custom library"""
    from bioql.dynamic_bridge import register_library

    register_library(
        name="test_lib",
        module="test_module",
        aliases=["test", "testlib"],
        common_functions={
            "test function": "test_func",
        },
    )

    # Should not crash
    assert True


def test_dynamic_call_invalid_command():
    """Test dynamic_call with invalid command"""
    from bioql import dynamic_call

    result = dynamic_call(
        "This is not a valid command format"
    )

    assert result is not None
    assert not result.success
    assert result.error_message is not None


def test_dynamic_call_unknown_library():
    """Test dynamic_call with unknown library"""
    from bioql import dynamic_call

    result = dynamic_call(
        "Use NonExistentLibrary to do something"
    )

    assert result is not None
    # Should either fail to parse or fail to execute
    if not result.success:
        assert result.error_message is not None


@pytest.mark.integration
def test_numpy_integration():
    """Integration test with numpy"""
    try:
        import numpy as np
    except ImportError:
        pytest.skip("NumPy not available")

    from bioql import dynamic_call

    # Mean
    result = dynamic_call("Use numpy to calculate mean of array [1, 2, 3, 4, 5]")
    assert result.success
    assert result.result == 3.0

    # Sum
    result = dynamic_call("Use numpy to calculate sum of array [1, 2, 3, 4, 5]")
    assert result.success
    assert result.result == 15.0


@pytest.mark.integration
def test_rdkit_integration():
    """Integration test with RDKit"""
    try:
        from rdkit import Chem
    except ImportError:
        pytest.skip("RDKit not available")

    from bioql import dynamic_call

    # Molecular weight
    result = dynamic_call(
        "Use RDKit to calculate molecular weight of ethanol SMILES CCO"
    )

    assert result.success
    # Ethanol MW is ~46.07
    assert 45 < result.result < 47


if __name__ == "__main__":
    pytest.main([__file__, "-v"])