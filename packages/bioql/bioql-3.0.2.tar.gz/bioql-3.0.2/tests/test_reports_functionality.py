#!/usr/bin/env python3
"""
Direct test of the fixed report functionality
"""

import sys
import os
sys.path.insert(0, '/Users/heinzjungbluth/Desktop/bioql')

from bioql_admin_interactive import BioQLInteractiveCLI

def test_reports():
    """Test all report functions directly"""

    print("🧪 TESTING FIXED REPORT FUNCTIONALITY")
    print("=" * 50)

    cli = BioQLInteractiveCLI()
    cli.db_path = '/Users/heinzjungbluth/Desktop/bioql/bioql_billing.db'

    try:
        # Test 1: Usage Statistics
        print("\n📊 Testing Usage Statistics...")
        cli._usage_stats_interactive()

        # Test 2: User Analytics
        print("\n👥 Testing User Analytics...")
        cli._user_analytics_interactive()

        # Test 3: Revenue Reports
        print("\n💰 Testing Revenue Reports...")
        cli._revenue_reports_interactive()

        # Test 4: System Health
        print("\n🔧 Testing System Health...")
        cli._system_health_interactive()

        print("\n🎉 ALL REPORTS TESTED SUCCESSFULLY!")
        return True

    except Exception as e:
        print(f"❌ Error testing reports: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

if __name__ == '__main__':
    test_reports()