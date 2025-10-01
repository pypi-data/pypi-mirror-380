#!/usr/bin/env python3
"""
Test database column references after fixes
"""

import sqlite3

def test_database_queries():
    """Test all the corrected database queries"""

    conn = sqlite3.connect('bioql_billing.db')
    cursor = conn.cursor()

    try:
        # Test 1: Demo user usage statistics
        print('📊 Testing Demo User Usage Statistics...')
        cursor.execute('''
            SELECT u.email, COUNT(ul.id) as usage_count,
                   SUM(CAST(ul.total_cost as FLOAT)) as total_cost,
                   AVG(ul.shots_executed) as avg_shots
            FROM users u
            LEFT JOIN usage_logs ul ON u.id = ul.user_id
            WHERE u.email LIKE 'demo%@bioql.test'
            GROUP BY u.id, u.email
            ORDER BY u.email
        ''')

        print('Demo User Usage Statistics:')
        print('-' * 60)

        for row in cursor.fetchall():
            email, usage_count, total_cost, avg_shots = row
            cost_val = total_cost or 0.0
            shots_val = avg_shots or 0
            print(f'{email:20} | {usage_count:3} jobs | ${cost_val:8.4f} | {shots_val:6.0f} avg shots')

        print('✅ Demo user query - SUCCESS')

        # Test 2: Recent usage logs
        print('\n📊 Testing Recent Usage Logs...')
        cursor.execute('''
            SELECT ul.user_id, ul.shots_executed, ul.total_cost, ul.algorithm_type, ul.created_at
            FROM usage_logs ul
            ORDER BY ul.created_at DESC
            LIMIT 5
        ''')

        print('Recent Usage (last 5):')
        print('-' * 60)

        for row in cursor.fetchall():
            user_id, shots, cost, algorithm, timestamp = row
            cost_val = float(cost) if cost else 0.0
            print(f'{user_id[:8]}... | {shots} shots | ${cost_val:.4f} | {algorithm} | {timestamp[:19]}')

        print('✅ Usage logs query - SUCCESS')

        # Test 3: Backend statistics
        print('\n📊 Testing Backend Statistics...')
        cursor.execute('''
            SELECT backend_used, COUNT(*) as job_count,
                   SUM(CAST(total_cost as FLOAT)) as total_cost,
                   AVG(shots_executed) as avg_shots
            FROM usage_logs
            GROUP BY backend_used
            ORDER BY job_count DESC
        ''')

        print('Backend Statistics:')
        print('-' * 60)

        for row in cursor.fetchall():
            backend, job_count, total_cost, avg_shots = row
            cost_val = total_cost or 0.0
            shots_val = avg_shots or 0
            print(f'{backend:15} | {job_count:3} jobs | ${cost_val:8.4f} | {shots_val:6.0f} avg shots')

        print('✅ Backend statistics query - SUCCESS')

        print('\n🎉 ALL DATABASE COLUMN REFERENCES FIXED SUCCESSFULLY!')

    except Exception as e:
        print(f'❌ Database error: {e}')
        return False

    finally:
        conn.close()

    return True

if __name__ == '__main__':
    test_database_queries()