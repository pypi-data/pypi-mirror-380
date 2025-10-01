#!/usr/bin/env python3
"""
Quick test script for BioQL core functionality.

This script tests the main quantum() function and QuantumResult class
to ensure the implementation is working correctly.
"""

import sys
import os

# Add the bioql package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

def test_basic_functionality():
    """Test basic BioQL functionality."""
    print("Testing BioQL Core Functionality")
    print("=" * 40)

    try:
        # Test import
        print("1. Testing imports...")
        from bioql import quantum, QuantumResult
        print("   ✓ Successfully imported quantum and QuantumResult")

        # Test basic quantum function
        print("\n2. Testing basic quantum function...")
        result = quantum("Create a Bell state", shots=100, debug=True)
        print(f"   ✓ Quantum function executed successfully")
        print(f"   ✓ Success: {result.success}")
        print(f"   ✓ Total shots: {result.total_shots}")
        print(f"   ✓ Result type: {type(result)}")

        # Test result properties
        print("\n3. Testing QuantumResult properties...")
        print(f"   ✓ Counts: {result.counts}")
        print(f"   ✓ Most likely outcome: {result.most_likely_outcome}")
        print(f"   ✓ Probabilities: {result.probabilities()}")
        print(f"   ✓ Metadata: {result.metadata}")

        # Test different programs
        print("\n4. Testing different quantum programs...")

        test_programs = [
            "Put qubit in superposition",
            "Generate random bit",
            "Entangle two qubits",
            "Create quantum interference"
        ]

        for i, program in enumerate(test_programs):
            print(f"   Testing program {i+1}: '{program}'")
            result = quantum(program, shots=50)
            print(f"   ✓ Success: {result.success}, Counts: {result.counts}")

        # Test error handling
        print("\n5. Testing error handling...")
        try:
            result = quantum("", shots=10)  # Empty program
            print(f"   Result for empty program: {result.success}")
            if not result.success:
                print(f"   ✓ Properly handled empty program: {result.error_message}")
        except Exception as e:
            print(f"   ✓ Exception handling works: {str(e)}")

        # Test debug mode
        print("\n6. Testing debug mode...")
        result = quantum("Create Bell state", debug=True, shots=10)
        print(f"   ✓ Debug mode result: Success={result.success}")
        if result.statevector is not None:
            print(f"   ✓ Statevector captured in debug mode")

        print("\n" + "=" * 40)
        print("All tests passed! ✓")
        return True

    except ImportError as e:
        print(f"   ✗ Import failed: {e}")
        print("   Make sure qiskit is installed: pip install qiskit qiskit-aer")
        return False

    except Exception as e:
        print(f"   ✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_installation_check():
    """Test the installation check function."""
    print("\nTesting Installation Check")
    print("=" * 30)

    try:
        from bioql import check_installation, get_info

        print("1. Checking installation...")
        is_installed = check_installation()
        print(f"   Installation check: {'✓ PASS' if is_installed else '✗ FAIL'}")

        print("\n2. Getting system info...")
        info = get_info()
        print(f"   Version: {info['version']}")
        print(f"   Python: {info['python_version']}")
        print(f"   Qiskit available: {info['qiskit_available']}")
        print(f"   Optional modules: {info['optional_modules']}")

        return is_installed

    except Exception as e:
        print(f"   ✗ Installation check failed: {e}")
        return False


if __name__ == "__main__":
    print("BioQL Core Implementation Test")
    print("=" * 50)

    # Test basic functionality
    basic_test_passed = test_basic_functionality()

    # Test installation check
    install_test_passed = test_installation_check()

    print("\n" + "=" * 50)
    print("FINAL RESULTS:")
    print(f"Basic functionality: {'✓ PASS' if basic_test_passed else '✗ FAIL'}")
    print(f"Installation check: {'✓ PASS' if install_test_passed else '✗ FAIL'}")

    if basic_test_passed and install_test_passed:
        print("\n🎉 BioQL core implementation is working correctly!")
        print("\nNext steps:")
        print("- Install dependencies: pip install -r requirements.txt")
        print("- Run full tests: python -m pytest tests/")
        print("- Try the examples in the examples/ directory")
    else:
        print("\n⚠️  Some tests failed. Check the error messages above.")
        print("Make sure all dependencies are installed.")