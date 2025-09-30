#!/usr/bin/env python3
"""
BioQL Command Line Interface
Provides CLI commands for BioQL quantum computing framework
"""

import argparse
import sys
import os
import subprocess
from pathlib import Path
import json
from typing import Optional

from . import __version__, get_info
from .logger import get_logger

# Get logger for CLI operations
logger = get_logger(__name__)

def install_cursor_extension():
    """Install BioQL extension for Cursor IDE"""
    print("🚀 Installing BioQL extension for Cursor IDE...")

    # Get the script path
    script_path = Path(__file__).parent.parent / "install_cursor_extension.py"

    if not script_path.exists():
        print(f"❌ Installation script not found: {script_path}")
        print("Please ensure you have the complete BioQL installation.")
        return False

    try:
        # Run the installation script
        result = subprocess.run([sys.executable, str(script_path)],
                              check=True, capture_output=True, text=True)

        print(result.stdout)
        print("✅ Cursor extension installation completed!")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during installation: {e}")
        return False

def install_windsurf_extension():
    """Install BioQL plugin for Windsurf IDE"""
    print("🚀 Installing BioQL plugin for Windsurf IDE...")

    # Get the script path
    script_path = Path(__file__).parent.parent / "install_windsurf_extension.py"

    if not script_path.exists():
        print(f"❌ Installation script not found: {script_path}")
        print("Please ensure you have the complete BioQL installation.")
        return False

    try:
        # Run the installation script
        result = subprocess.run([sys.executable, str(script_path)],
                              check=True, capture_output=True, text=True)

        print(result.stdout)
        print("✅ Windsurf plugin installation completed!")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during installation: {e}")
        return False

def show_version():
    """Show BioQL version and system information"""
    print(f"BioQL v{__version__}")

    # Get detailed system info
    info = get_info()

    print("\\nSystem Information:")
    print(f"  Python: {info['python_version']}")
    print(f"  Qiskit: {'✅' if info['qiskit_available'] else '❌'}")

    if info['qiskit_available']:
        print(f"    Version: {info.get('qiskit_version', 'Unknown')}")

    print("\\nOptional Modules:")
    for module, available in info['optional_modules'].items():
        status = '✅' if available else '❌'
        print(f"  {module}: {status}")

def run_quantum_code(code: str, shots: int = 1024, backend: str = "simulator"):
    """Run BioQL quantum code from command line"""
    try:
        from . import quantum

        print(f"🔬 Executing quantum code with {shots} shots on {backend}...")
        print(f"Code: {code}")

        # Execute the quantum code
        result = quantum(code, shots=shots, backend=backend)

        if result.success:
            print("\\n✅ Execution successful!")
            print(f"📊 Results: {result.counts}")

            if hasattr(result, 'energy') and result.energy is not None:
                print(f"⚡ Energy: {result.energy}")

            if hasattr(result, 'bio_interpretation') and result.bio_interpretation:
                print(f"🧬 Biological interpretation: {result.bio_interpretation}")

        else:
            print(f"❌ Execution failed: {result.error_message}")
            return False

        return True

    except ImportError:
        print("❌ BioQL quantum module not available. Please check your installation.")
        return False
    except Exception as e:
        print(f"❌ Error executing quantum code: {e}")
        return False

def compile_bioql_file(file_path: str, output_path: Optional[str] = None):
    """Compile a BioQL file"""
    try:
        from .compiler import compile_bioql

        input_file = Path(file_path)
        if not input_file.exists():
            print(f"❌ File not found: {file_path}")
            return False

        print(f"🔧 Compiling BioQL file: {file_path}")

        # Read the file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Compile the content
        compiled_result = compile_bioql(content)

        if output_path:
            output_file = Path(output_path)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(compiled_result)
            print(f"✅ Compiled output saved to: {output_path}")
        else:
            print("✅ Compilation successful!")
            print("Compiled code:")
            print(compiled_result)

        return True

    except ImportError:
        print("❌ BioQL compiler not available. Please check your installation.")
        return False
    except Exception as e:
        print(f"❌ Compilation failed: {e}")
        return False

def check_installation():
    """Check if BioQL is properly installed"""
    print("🔍 Checking BioQL installation...")

    try:
        # Direct import test to handle Python path issues
        import importlib

        # Test core BioQL modules
        core_modules = [
            ('qiskit', 'qiskit'),
            ('qiskit_aer', 'qiskit_aer'),
            ('numpy', 'numpy'),
            ('matplotlib', 'matplotlib'),
            ('biopython', 'Bio')
        ]

        missing_modules = []
        for display_name, import_name in core_modules:
            try:
                importlib.import_module(import_name)
            except ImportError:
                missing_modules.append(display_name)

        # Show installation status
        info = get_info()
        print("\\n📋 Installation Summary:")
        print(f"  Version: {info['version']}")
        print(f"  Python: {info['python_version']}")

        if missing_modules:
            print(f"❌ Missing modules: {', '.join(missing_modules)}")
            print("\\n💡 Fix suggestions:")
            print("  1. Check if you're using the correct Python environment")
            print("  2. Try: pip install --upgrade bioql[dev]")
            print("  3. If using pyenv, ensure packages are installed in the active environment")
            return False
        else:
            print("✅ All core modules available")

            # Test BioQL functionality
            try:
                from . import quantum
                print("✅ BioQL quantum module imported successfully")
                return True
            except ImportError as e:
                print(f"❌ BioQL quantum module import failed: {e}")
                return False

    except Exception as e:
        print(f"❌ Installation check failed: {e}")
        return False

def setup_api_keys():
    """Interactive setup for IBM Quantum and IonQ API keys"""
    print("🔐 Setting up API keys for quantum cloud providers")
    print("=" * 50)

    # Determine config directory
    home_dir = Path.home()
    config_dir = home_dir / '.bioql'
    config_dir.mkdir(exist_ok=True)

    config_file = config_dir / 'config.json'

    # Load existing config if it exists
    config = {}
    if config_file.exists():
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
        except (json.JSONDecodeError, IOError):
            config = {}

    print("\\nCurrent API key status:")
    print(f"  IBM Quantum: {'✅ Configured' if config.get('ibm_token') else '❌ Not configured'}")
    print(f"  IonQ: {'✅ Configured' if config.get('ionq_token') else '❌ Not configured'}")

    # IBM Quantum setup
    print("\\n🌐 IBM Quantum Setup")
    print("-" * 20)
    print("To get your IBM Quantum token:")
    print("1. Visit: https://quantum-computing.ibm.com/")
    print("2. Sign in or create an account")
    print("3. Go to 'Account' > 'API Token'")
    print("4. Copy your token")

    current_ibm = config.get('ibm_token', '')
    if current_ibm:
        print(f"\\nCurrent IBM token: {current_ibm[:8]}...{current_ibm[-4:]}")
        update_ibm = input("Update IBM Quantum token? (y/N): ").lower().strip()
    else:
        update_ibm = 'y'

    if update_ibm == 'y':
        ibm_token = input("Enter your IBM Quantum token (or press Enter to skip): ").strip()
        if ibm_token:
            config['ibm_token'] = ibm_token
            print("✅ IBM Quantum token saved")
        else:
            print("⏭️  Skipping IBM Quantum setup")

    # IonQ setup
    print("\\n⚛️  IonQ Setup")
    print("-" * 12)
    print("To get your IonQ API key:")
    print("1. Visit: https://cloud.ionq.com/")
    print("2. Sign in or create an account")
    print("3. Go to 'API Keys' in the dashboard")
    print("4. Create a new API key and copy it")

    current_ionq = config.get('ionq_token', '')
    if current_ionq:
        print(f"\\nCurrent IonQ token: {current_ionq[:8]}...{current_ionq[-4:]}")
        update_ionq = input("Update IonQ API key? (y/N): ").lower().strip()
    else:
        update_ionq = 'y'

    if update_ionq == 'y':
        ionq_token = input("Enter your IonQ API key (or press Enter to skip): ").strip()
        if ionq_token:
            config['ionq_token'] = ionq_token
            print("✅ IonQ API key saved")
        else:
            print("⏭️  Skipping IonQ setup")

    # Save configuration
    try:
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)

        print(f"\\n✅ Configuration saved to: {config_file}")
        print("\\n💡 Usage examples:")
        if config.get('ibm_token'):
            print("  quantum('simulate protein folding', backend='ibm_brisbane')")
        if config.get('ionq_token'):
            print("  quantum('analyze DNA sequence', backend='ionq_simulator')")

        print("\\n🔒 Security note: API keys are stored locally in ~/.bioql/config.json")
        print("   Make sure to keep this file secure and never share it publicly.")

        return True

    except IOError as e:
        print(f"❌ Failed to save configuration: {e}")
        return False

def create_example_file(name: str = "example.bql"):
    """Create an example BioQL file"""
    example_content = '''# BioQL Example: Quantum Protein Analysis
# This file demonstrates basic BioQL syntax and capabilities

# Create a Bell state for quantum entanglement
create bell state with 2 qubits
apply hadamard gate to qubit 0
apply cnot gate from qubit 0 to qubit 1
measure all qubits

# Analyze protein folding using quantum simulation
analyze protein hemoglobin folding
simulate 100 amino acid interactions
optimize energy landscape using qaoa algorithm
measure folding stability

# DNA sequence alignment with quantum algorithms
align dna sequences ATCGATCGATCG and ATCGATCGATCG
use quantum fourier transform for pattern matching
find optimal alignment with 95% similarity
measure alignment score

# Drug-protein binding simulation
simulate drug aspirin binding to protein cyclooxygenase
model hydrogen bonds using quantum states
calculate binding affinity with 1000 shots
optimize molecular interaction

# Quantum circuit for biological process
create quantum circuit with 3 qubits
initialize qubits in ground state
apply hadamard gates
add measurement operations
execute with 1024 shots
'''

    try:
        file_path = Path(name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(example_content)

        print(f"✅ Example file created: {file_path}")
        print("\\nTo run this example:")
        print(f"  bioql run {name}")
        print("\\nOr execute specific operations:")
        print("  bioql quantum 'create bell state with 2 qubits'")

        return True

    except Exception as e:
        print(f"❌ Failed to create example file: {e}")
        return False

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="BioQL: Quantum Computing for Bioinformatics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  bioql install cursor          Install Cursor IDE extension
  bioql install windsurf        Install Windsurf IDE plugin
  bioql quantum "create bell state"  Run quantum code
  bioql compile example.bql     Compile BioQL file
  bioql check                   Check installation
  bioql setup-keys              Configure IBM Quantum and IonQ API keys
  bioql example                 Create example file

For more information, visit: https://bioql.org
        """
    )

    parser.add_argument('--version', action='version', version=f'BioQL {__version__}')

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Install command
    install_parser = subparsers.add_parser('install', help='Install IDE extensions')
    install_parser.add_argument('ide', choices=['cursor', 'windsurf'],
                               help='IDE to install extension for')

    # Quantum command
    quantum_parser = subparsers.add_parser('quantum', help='Run quantum code')
    quantum_parser.add_argument('code', help='BioQL code to execute')
    quantum_parser.add_argument('--shots', type=int, default=1024,
                               help='Number of shots (default: 1024)')
    quantum_parser.add_argument('--backend', default='simulator',
                               help='Quantum backend (default: simulator)')

    # Compile command
    compile_parser = subparsers.add_parser('compile', help='Compile BioQL file')
    compile_parser.add_argument('file', help='BioQL file to compile')
    compile_parser.add_argument('-o', '--output', help='Output file path')

    # Check command
    subparsers.add_parser('check', help='Check BioQL installation')

    # Version command
    subparsers.add_parser('version', help='Show version information')

    # Setup keys command
    subparsers.add_parser('setup-keys', help='Configure API keys for quantum cloud providers')

    # Example command
    example_parser = subparsers.add_parser('example', help='Create example BioQL file')
    example_parser.add_argument('--name', default='example.bql',
                               help='Example file name (default: example.bql)')

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    # Execute commands
    try:
        if args.command == 'install':
            if args.ide == 'cursor':
                success = install_cursor_extension()
            elif args.ide == 'windsurf':
                success = install_windsurf_extension()
            else:
                print(f"❌ Unknown IDE: {args.ide}")
                return 1

            return 0 if success else 1

        elif args.command == 'quantum':
            success = run_quantum_code(args.code, args.shots, args.backend)
            return 0 if success else 1

        elif args.command == 'compile':
            success = compile_bioql_file(args.file, args.output)
            return 0 if success else 1

        elif args.command == 'check':
            success = check_installation()
            return 0 if success else 1

        elif args.command == 'version':
            show_version()
            return 0

        elif args.command == 'setup-keys':
            success = setup_api_keys()
            return 0 if success else 1

        elif args.command == 'example':
            success = create_example_file(args.name)
            return 0 if success else 1

        else:
            print(f"❌ Unknown command: {args.command}")
            parser.print_help()
            return 1

    except KeyboardInterrupt:
        print("\\n❌ Operation cancelled by user")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        logger.error(f"CLI error: {e}", exc_info=True)
        return 1

if __name__ == '__main__':
    sys.exit(main())