#!/usr/bin/env python3
"""
Test quantum provider credentials and available backends
"""

def test_qiskit_installation():
    print("🔧 Testing Qiskit installation...")
    try:
        import qiskit
        from qiskit_aer import AerSimulator
        print(f"✅ Qiskit version: {qiskit.__version__}")
        print(f"✅ Qiskit Aer available")
        return True
    except ImportError as e:
        print(f"❌ Qiskit not available: {e}")
        return False

def test_ibm_quantum():
    print("\n🔧 Testing IBM Quantum credentials...")
    try:
        from qiskit_ibm_runtime import QiskitRuntimeService

        # Try to get service (will use saved credentials or environment)
        try:
            service = QiskitRuntimeService()
            backends = service.backends()
            print(f"✅ IBM Quantum connection successful")
            print(f"📊 Available backends: {len(list(backends))}")

            # Show available backends
            for backend in list(backends)[:5]:  # Show first 5
                print(f"   🖥️  {backend.name} ({backend.num_qubits} qubits)")

            return True
        except Exception as e:
            print(f"❌ IBM Quantum connection failed: {e}")
            print("💡 Try: qiskit-ibm-runtime save-account --token YOUR_TOKEN")
            return False

    except ImportError as e:
        print(f"❌ IBM Quantum libraries not available: {e}")
        print("💡 Install with: pip install qiskit-ibm-runtime")
        return False

def test_ionq():
    print("\n🔧 Testing IonQ credentials...")
    try:
        from qiskit_ionq import IonQProvider

        # Try to create provider (will use saved credentials or environment)
        try:
            provider = IonQProvider()
            backends = provider.backends()
            print(f"✅ IonQ connection successful")
            print(f"📊 Available backends: {len(backends)}")

            # Show available backends
            for backend in backends[:5]:  # Show first 5
                print(f"   🖥️  {backend.name()}")

            return True
        except Exception as e:
            print(f"❌ IonQ connection failed: {e}")
            print("💡 Set environment: IONQ_API_KEY=your_key")
            return False

    except ImportError as e:
        print(f"❌ IonQ libraries not available: {e}")
        print("💡 Install with: pip install qiskit-ionq")
        return False

def test_bioql_import():
    print("\n🔧 Testing BioQL framework...")
    import sys
    import os

    # Add current directory to path to import bioql
    sys.path.insert(0, '/Users/heinzjungbluth/Desktop/bioql')

    try:
        from bioql.quantum_connector import quantum, QuantumResult
        print("✅ BioQL framework import successful")
        print("✅ quantum() function available")
        return True
    except ImportError as e:
        print(f"❌ BioQL import failed: {e}")
        return False

if __name__ == "__main__":
    print("🧬 BioQL Provider Credentials Test")
    print("=" * 50)

    results = {
        'qiskit': test_qiskit_installation(),
        'ibm': test_ibm_quantum(),
        'ionq': test_ionq(),
        'bioql': test_bioql_import()
    }

    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)

    for provider, status in results.items():
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {provider.upper()}: {'Ready' if status else 'Not Available'}")

    ready_count = sum(results.values())
    print(f"\n🎯 {ready_count}/4 providers ready for testing")

    if ready_count >= 2:
        print("🚀 Sufficient providers available for comprehensive testing!")
    else:
        print("⚠️  Need more providers configured for full testing")