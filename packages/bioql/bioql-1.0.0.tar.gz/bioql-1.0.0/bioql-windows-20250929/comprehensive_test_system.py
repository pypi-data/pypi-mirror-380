#!/usr/bin/env python3
"""
Comprehensive BioQL Testing System
Tests all demo users across multiple quantum backends with real billing tracking
"""

import sys
import os
import time
import json
import sqlite3
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Add bioql to path
sys.path.insert(0, '/Users/heinzjungbluth/Desktop/bioql')

def load_demo_users():
    """Load demo users from file"""
    users = []
    with open('demo_api_keys.txt', 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            email, api_key, plan = line.strip().split(',')
            users.append({
                'email': email,
                'api_key': api_key,
                'plan': plan,
                'user_id': email.split('@')[0]
            })
    return users

# Test circuits of different complexities
TEST_CIRCUITS = {
    'basic_2q': {
        'program': 'Create a simple 2-qubit Bell state circuit with Hadamard and CNOT gates',
        'shots': 100,
        'complexity': 'basic',
        'expected_qubits': 2
    },
    'intermediate_4q': {
        'program': 'Create a 4-qubit quantum Fourier transform circuit',
        'shots': 200,
        'complexity': 'intermediate',
        'expected_qubits': 4
    },
    'complex_8q': {
        'program': 'Create an 8-qubit variational quantum eigensolver (VQE) circuit for molecular simulation',
        'shots': 400,
        'complexity': 'complex',
        'expected_qubits': 8
    },
    'bio_specific': {
        'program': 'Create a quantum circuit to simulate protein folding using 6 qubits with entanglement for molecular interactions',
        'shots': 300,
        'complexity': 'bio_complex',
        'expected_qubits': 6
    }
}

# Backend configurations
BACKEND_CONFIGS = {
    'simulator': {
        'name': 'simulator',
        'type': 'local',
        'expected_cost_per_shot': 0.001,
        'max_qubits': 32
    },
    'ionq_simulator': {
        'name': 'ionq_simulator',  # Correct IonQ simulator backend name
        'type': 'ionq',
        'expected_cost_per_shot': 0.01,
        'max_qubits': 29
    }
}

def test_single_user_circuit(user, circuit_name, circuit_config, backend_config):
    """Test a single circuit for a single user on a specific backend"""

    print(f"🧪 Testing {user['user_id']} | {circuit_name} | {backend_config['name']}")

    try:
        # Import BioQL (this should trigger billing integration)
        from bioql import quantum

        # Set up the test parameters
        program = circuit_config['program']
        backend = backend_config['name']
        shots = circuit_config['shots']
        api_key = user['api_key']

        start_time = time.time()

        # Make the quantum call with billing
        result = quantum(
            program=program,
            backend=backend,
            shots=shots,
            api_key=api_key,
            debug=True
        )

        execution_time = time.time() - start_time

        # Analyze result
        test_result = {
            'user_id': user['user_id'],
            'user_email': user['email'],
            'user_plan': user['plan'],
            'circuit_name': circuit_name,
            'circuit_complexity': circuit_config['complexity'],
            'backend': backend_config['name'],
            'backend_type': backend_config['type'],
            'shots_requested': shots,
            'success': result.success if hasattr(result, 'success') else True,
            'execution_time': execution_time,
            'timestamp': datetime.now().isoformat(),
            'error_message': result.error_message if hasattr(result, 'error_message') else None,
            'cost_estimate': result.cost_estimate if hasattr(result, 'cost_estimate') else None,
            'billing_metadata': result.billing_metadata if hasattr(result, 'billing_metadata') else {}
        }

        if result.success if hasattr(result, 'success') else True:
            test_result.update({
                'shots_executed': result.total_shots if hasattr(result, 'total_shots') else sum(result.counts.values()) if hasattr(result, 'counts') else 0,
                'unique_outcomes': len(result.counts) if hasattr(result, 'counts') else 0,
                'most_likely_outcome': result.most_likely_outcome if hasattr(result, 'most_likely_outcome') else None
            })

            print(f"   ✅ Success | {test_result['shots_executed']} shots | {execution_time:.2f}s")
            if test_result['cost_estimate']:
                print(f"   💰 Cost: ${test_result['cost_estimate']:.4f}")
        else:
            print(f"   ❌ Failed | {test_result['error_message']}")

        return test_result

    except Exception as e:
        print(f"   💥 Exception | {str(e)}")
        return {
            'user_id': user['user_id'],
            'user_email': user['email'],
            'circuit_name': circuit_name,
            'backend': backend_config['name'],
            'success': False,
            'execution_time': time.time() - start_time,
            'error_message': str(e),
            'timestamp': datetime.now().isoformat()
        }

def run_comprehensive_tests():
    """Run comprehensive tests across all users and backends"""

    print("🧬 BioQL COMPREHENSIVE TESTING SYSTEM")
    print("=" * 60)

    # Load users
    users = load_demo_users()
    print(f"👥 Loaded {len(users)} demo users")

    # Create test plan
    test_cases = []

    # For each user, test different circuits on different backends
    for user in users:
        # Basic tests on local simulator
        test_cases.append((user, 'basic_2q', TEST_CIRCUITS['basic_2q'], BACKEND_CONFIGS['simulator']))
        test_cases.append((user, 'intermediate_4q', TEST_CIRCUITS['intermediate_4q'], BACKEND_CONFIGS['simulator']))

        # Complex tests based on user plan
        if user['plan'] in ['pro', 'enterprise']:
            test_cases.append((user, 'complex_8q', TEST_CIRCUITS['complex_8q'], BACKEND_CONFIGS['simulator']))
            test_cases.append((user, 'bio_specific', TEST_CIRCUITS['bio_specific'], BACKEND_CONFIGS['simulator']))

        # IonQ simulator test (one per user)
        if user['plan'] == 'enterprise':
            test_cases.append((user, 'basic_2q', TEST_CIRCUITS['basic_2q'], BACKEND_CONFIGS['ionq_simulator']))

    print(f"🎯 Total test cases: {len(test_cases)}")
    print(f"⏱️  Starting comprehensive testing...")
    print()

    # Execute tests with thread pool for parallel execution
    results = []
    max_workers = 3  # Conservative to avoid overwhelming providers

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_test = {
            executor.submit(test_single_user_circuit, user, circuit_name, circuit_config, backend_config):
            (user['user_id'], circuit_name, backend_config['name'])
            for user, circuit_name, circuit_config, backend_config in test_cases
        }

        # Collect results as they complete
        for future in as_completed(future_to_test):
            test_id = future_to_test[future]
            try:
                result = future.result(timeout=60)  # 60 second timeout per test
                results.append(result)
            except Exception as e:
                print(f"💥 Test {test_id} failed with exception: {e}")
                results.append({
                    'user_id': test_id[0],
                    'circuit_name': test_id[1],
                    'backend': test_id[2],
                    'success': False,
                    'error_message': f"Test execution failed: {e}",
                    'timestamp': datetime.now().isoformat()
                })

    return results

def analyze_test_results(results):
    """Analyze and display test results"""

    print("\n" + "=" * 60)
    print("📊 TEST RESULTS ANALYSIS")
    print("=" * 60)

    # Basic stats
    total_tests = len(results)
    successful_tests = len([r for r in results if r.get('success', False)])
    failed_tests = total_tests - successful_tests

    print(f"📈 Total Tests: {total_tests}")
    print(f"✅ Successful: {successful_tests} ({successful_tests/total_tests*100:.1f}%)")
    print(f"❌ Failed: {failed_tests} ({failed_tests/total_tests*100:.1f}%)")

    # Backend performance
    backend_stats = {}
    for result in results:
        backend = result.get('backend', 'unknown')
        if backend not in backend_stats:
            backend_stats[backend] = {'total': 0, 'success': 0}
        backend_stats[backend]['total'] += 1
        if result.get('success', False):
            backend_stats[backend]['success'] += 1

    print(f"\n🖥️  Backend Performance:")
    for backend, stats in backend_stats.items():
        success_rate = stats['success'] / stats['total'] * 100 if stats['total'] > 0 else 0
        print(f"   {backend}: {stats['success']}/{stats['total']} ({success_rate:.1f}%)")

    # User plan performance
    plan_stats = {}
    for result in results:
        plan = result.get('user_plan', 'unknown')
        if plan not in plan_stats:
            plan_stats[plan] = {'total': 0, 'success': 0}
        plan_stats[plan]['total'] += 1
        if result.get('success', False):
            plan_stats[plan]['success'] += 1

    print(f"\n📋 Plan Performance:")
    for plan, stats in plan_stats.items():
        success_rate = stats['success'] / stats['total'] * 100 if stats['total'] > 0 else 0
        print(f"   {plan}: {stats['success']}/{stats['total']} ({success_rate:.1f}%)")

    # Cost analysis
    total_cost = 0
    cost_by_backend = {}
    for result in results:
        cost = result.get('cost_estimate', 0) or 0
        backend = result.get('backend', 'unknown')
        total_cost += cost
        if backend not in cost_by_backend:
            cost_by_backend[backend] = 0
        cost_by_backend[backend] += cost

    print(f"\n💰 Cost Analysis:")
    print(f"   Total Estimated Cost: ${total_cost:.4f}")
    for backend, cost in cost_by_backend.items():
        print(f"   {backend}: ${cost:.4f}")

    # Save results to file
    with open('test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n💾 Detailed results saved to test_results.json")

def check_billing_database():
    """Check the billing database for usage logs"""

    print("\n" + "=" * 60)
    print("🗃️  BILLING DATABASE ANALYSIS")
    print("=" * 60)

    try:
        conn = sqlite3.connect('bioql_billing.db')
        cursor = conn.cursor()

        # Check usage logs
        cursor.execute("SELECT COUNT(*) FROM usage_logs")
        usage_count = cursor.fetchone()[0]
        print(f"📈 Total usage logs: {usage_count}")

        # Check recent logs
        cursor.execute("""
            SELECT user_id, shots_executed, total_cost, algorithm_type, created_at
            FROM usage_logs
            ORDER BY created_at DESC
            LIMIT 10
        """)
        recent_logs = cursor.fetchall()

        if recent_logs:
            print(f"\n🕒 Recent Usage (last 10):")
            for log in recent_logs:
                user_id, shots, cost, algorithm, timestamp = log
                cost_val = float(cost) if cost else 0.0
                print(f"   {user_id[:8]}... | {shots} shots | ${cost_val:.4f} | {algorithm} | {timestamp[:19]}")

        conn.close()

    except Exception as e:
        print(f"❌ Error accessing billing database: {e}")

def main():
    """Main execution function"""

    start_time = time.time()

    # Run comprehensive tests
    results = run_comprehensive_tests()

    # Analyze results
    analyze_test_results(results)

    # Check billing database
    check_billing_database()

    total_time = time.time() - start_time

    print(f"\n" + "=" * 60)
    print(f"🏁 TESTING COMPLETED")
    print(f"⏱️  Total execution time: {total_time:.2f} seconds")
    print(f"🎯 System validation: {'✅ PASSED' if len(results) > 0 else '❌ FAILED'}")
    print("=" * 60)

if __name__ == "__main__":
    main()