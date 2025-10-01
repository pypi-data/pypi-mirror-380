#!/usr/bin/env python3
"""
Test single user with API key authentication
"""

import sys
sys.path.insert(0, '/Users/heinzjungbluth/Desktop/bioql')

from bioql import quantum

def test_single_user():
    print("🧪 Testing Single User with API Key")
    print("=" * 40)

    # Use demo1 API key (correct one from file)
    api_key = "bioql_sQ3MalPqjQvgZ_TtNdkLySeDD6u4eStvEvkUbFK4Ayw"

    try:
        result = quantum(
            program="Create a 2-qubit Bell state circuit",
            api_key=api_key,
            backend="simulator",
            shots=100,
            debug=True
        )

        print(f"✅ Success: {result.success}")
        print(f"📊 Results: {result.counts}")
        if hasattr(result, 'cost_estimate'):
            print(f"💰 Cost: ${result.cost_estimate:.4f}")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_single_user()