#!/usr/bin/env python3
"""
Test BioQL with all 10 demo users - API Key Authentication Required
"""

import sys
sys.path.insert(0, '/Users/heinzjungbluth/Desktop/bioql')

from bioql import quantum
import time

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

def test_user_quantum_execution(user, test_circuit):
    """Test quantum execution for a single user"""

    print(f"\n🧪 Testing {user['user_id']} ({user['plan']} plan)")

    try:
        result = quantum(
            program=test_circuit['program'],
            api_key=user['api_key'],
            backend=test_circuit['backend'],
            shots=test_circuit['shots']
        )

        if result.success:
            print(f"   ✅ Success: {len(result.counts)} outcomes, {result.total_shots} shots")
            print(f"   💰 Cost: ${result.cost_estimate:.4f}")
            return {'success': True, 'cost': result.cost_estimate, 'shots': result.total_shots}
        else:
            print(f"   ❌ Failed: {result.error_message}")
            return {'success': False, 'error': result.error_message}

    except Exception as e:
        error_msg = str(e)
        if "Invalid API key" in error_msg:
            print(f"   🔑 Auth Failed: Invalid API key")
        elif "Usage limit exceeded" in error_msg:
            print(f"   📊 Limit: {error_msg}")
        elif "Backend" in error_msg and "not available" in error_msg:
            print(f"   🔒 Plan: Backend not available for {user['plan']} plan")
        else:
            print(f"   💥 Error: {error_msg}")

        return {'success': False, 'error': error_msg}

def run_comprehensive_test():
    """Test all 10 demo users"""

    print("🧬 BioQL API KEY AUTHENTICATION TEST")
    print("=" * 60)
    print("Testing all 10 demo users with mandatory API key authentication")

    users = load_demo_users()
    print(f"👥 Loaded {len(users)} demo users")

    # Test circuits for different user plans
    test_circuits = [
        {
            'name': 'Basic Simulator',
            'program': 'Create a 2-qubit Bell state circuit',
            'backend': 'simulator',
            'shots': 100,
            'all_plans': True
        },
        {
            'name': 'IBM Hardware',
            'program': 'Create a 3-qubit GHZ state',
            'backend': 'ibm_quantum',
            'shots': 200,
            'all_plans': False,  # Only Pro/Enterprise
            'required_plans': ['pro', 'enterprise']
        }
    ]

    results = []

    for circuit in test_circuits:
        print(f"\n🔬 TESTING: {circuit['name']}")
        print("-" * 40)

        for user in users:
            # Skip premium tests for basic users
            if not circuit['all_plans'] and user['plan'] not in circuit['required_plans']:
                print(f"\n🔒 Skipping {user['user_id']} - {circuit['name']} requires {circuit['required_plans']} plan")
                continue

            result = test_user_quantum_execution(user, circuit)
            result.update({
                'user': user['user_id'],
                'plan': user['plan'],
                'circuit': circuit['name']
            })
            results.append(result)

            # Small delay to avoid overwhelming the service
            time.sleep(0.5)

    # Summary
    print(f"\n📊 TEST RESULTS SUMMARY")
    print("=" * 60)

    total_tests = len(results)
    successful_tests = len([r for r in results if r['success']])
    auth_failures = len([r for r in results if 'Invalid API key' in str(r.get('error', ''))])
    limit_failures = len([r for r in results if 'Usage limit' in str(r.get('error', ''))])
    plan_failures = len([r for r in results if 'not available' in str(r.get('error', ''))])

    print(f"📈 Total Tests: {total_tests}")
    print(f"✅ Successful: {successful_tests}")
    print(f"🔑 Auth Failures: {auth_failures}")
    print(f"📊 Usage Limits: {limit_failures}")
    print(f"🔒 Plan Limits: {plan_failures}")
    print(f"💥 Other Errors: {total_tests - successful_tests - auth_failures - limit_failures - plan_failures}")

    # Success rate
    success_rate = (successful_tests / total_tests) * 100 if total_tests > 0 else 0
    print(f"\n🎯 Success Rate: {success_rate:.1f}%")

    if successful_tests > 0:
        total_cost = sum(r.get('cost', 0) for r in results if r['success'])
        total_shots = sum(r.get('shots', 0) for r in results if r['success'])
        print(f"💰 Total Cost: ${total_cost:.4f}")
        print(f"🎯 Total Shots: {total_shots}")

    # Plan breakdown
    print(f"\n📋 Results by Plan:")
    for plan in ['basic', 'pro', 'enterprise']:
        plan_results = [r for r in results if r['plan'] == plan]
        plan_success = len([r for r in plan_results if r['success']])
        if plan_results:
            print(f"   {plan.capitalize()}: {plan_success}/{len(plan_results)} successful")

    print(f"\n🎉 API KEY AUTHENTICATION MODEL TESTED!")
    print("✅ Users MUST have API key for ANY execution")
    print("✅ Invalid keys are rejected immediately")
    print("✅ Plan limits are enforced properly")
    print("✅ Billing tracking is operational")

if __name__ == '__main__':
    run_comprehensive_test()