#!/usr/bin/env python3
"""
Test script for BioQL Admin CLI (Simple Version)
This script tests the CLI functionality without user interaction.
"""

import subprocess
import time
import os

def run_cli_command(command, timeout=10):
    """Run a CLI command and return output."""
    try:
        # Create process
        process = subprocess.Popen(
            ['python3', 'bioql_admin_simple.py', '--db', 'bioql_billing.db'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Send command and exit
        output, error = process.communicate(input=f"{command}\nexit\n", timeout=timeout)

        return output, error, process.returncode
    except subprocess.TimeoutExpired:
        process.kill()
        return "", "Command timed out", 1

def test_cli_commands():
    """Test various CLI commands."""
    print("🧪 Testing BioQL Admin CLI Commands (Simple Version)")
    print("="*50)

    commands_to_test = [
        ("status", "System status"),
        ("list_users --limit 3", "List users with limit"),
        ("usage_stats --days 7", "Usage statistics"),
        ("list_bills --limit 5", "List bills"),
        ("sql SELECT COUNT(*) FROM users", "SQL query"),
        ("help", "Help command"),
    ]

    for command, description in commands_to_test:
        print(f"\n🔍 Testing: {description}")
        print(f"Command: {command}")
        print("-" * 30)

        output, error, returncode = run_cli_command(command, timeout=15)

        if returncode == 0:
            print("✅ Command successful")
            # Show relevant output (skip CLI prompt lines)
            lines = output.split('\n')
            relevant_lines = []
            for line in lines:
                if (line.strip() and
                    not line.startswith('bioql-admin>') and
                    not line.startswith('(Cmd)') and
                    '👋 Goodbye!' not in line):
                    relevant_lines.append(line)

            # Show first 10 relevant lines
            for line in relevant_lines[:10]:
                print(f"   {line}")

            if len(relevant_lines) > 10:
                print(f"   ... ({len(relevant_lines) - 10} more lines)")
        else:
            print(f"❌ Command failed: {error}")

        time.sleep(1)  # Brief pause between commands

def main():
    """Main test function."""
    print("🧬 BioQL Admin CLI Test Suite (Simple Version)")
    print("="*60)

    # Check if database exists
    if not os.path.exists('bioql_billing.db'):
        print("❌ Database not found. Run setup_admin_cli.sh first.")
        return

    # Check if CLI exists
    if not os.path.exists('bioql_admin_simple.py'):
        print("❌ CLI script not found.")
        return

    print("✅ Prerequisites check passed")

    # Run tests
    test_cli_commands()

    print("\n" + "="*60)
    print("🎉 Test suite completed!")
    print("\n💡 To use the CLI interactively:")
    print("   ./bioql-admin-simple")
    print("   or")
    print("   python3 bioql_admin_simple.py --db bioql_billing.db")

if __name__ == "__main__":
    main()