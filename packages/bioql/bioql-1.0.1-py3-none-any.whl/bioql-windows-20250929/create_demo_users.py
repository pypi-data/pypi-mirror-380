#!/usr/bin/env python3
"""
Create 10 demo users for comprehensive BioQL testing
"""
import sqlite3
import uuid
import hashlib
import secrets
from datetime import datetime

def create_demo_users():
    # Connect to database
    db_path = "bioql_billing.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Demo users data
    demo_users = [
        ("demo1@bioql.test", "Demo User One", "BioQL Testing Corp", "basic"),
        ("demo2@bioql.test", "Demo User Two", "BioQL Testing Corp", "pro"),
        ("demo3@bioql.test", "Demo User Three", "BioQL Testing Corp", "enterprise"),
        ("demo4@bioql.test", "Demo User Four", "BioQL Testing Corp", "basic"),
        ("demo5@bioql.test", "Demo User Five", "BioQL Testing Corp", "pro"),
        ("demo6@bioql.test", "Demo User Six", "BioQL Testing Corp", "enterprise"),
        ("demo7@bioql.test", "Demo User Seven", "BioQL Testing Corp", "basic"),
        ("demo8@bioql.test", "Demo User Eight", "BioQL Testing Corp", "pro"),
        ("demo9@bioql.test", "Demo User Nine", "BioQL Testing Corp", "enterprise"),
        ("demo10@bioql.test", "Demo User Ten", "BioQL Testing Corp", "basic")
    ]

    created_users = []

    for email, full_name, org, plan in demo_users:
        try:
            # Check if user already exists
            cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
            if cursor.fetchone():
                print(f"❌ User {email} already exists, skipping...")
                continue

            # Split name for database compatibility
            name_parts = full_name.split(' ', 2)
            first_name = name_parts[0]
            last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''

            # Generate IDs and credentials
            user_id = str(uuid.uuid4())
            api_key = f"bioql_{secrets.token_urlsafe(32)}"
            api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()
            api_key_id = str(uuid.uuid4())
            username = email.split('@')[0]
            password_hash = "demo_placeholder_hash"
            now = datetime.now().isoformat()

            # Insert user
            user_query = """
                INSERT INTO users (id, email, username, password_hash, first_name, last_name,
                                 organization, current_plan, is_active, is_verified, is_admin,
                                 created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1, 1, 0, ?, ?)
            """
            cursor.execute(user_query, (user_id, email, username, password_hash, first_name,
                                      last_name, org, plan, now, now))

            # Insert API key
            key_prefix = api_key[:12]
            api_key_query = """
                INSERT INTO api_keys (id, user_id, key_name, key_hash, key_prefix, is_active,
                                    total_requests, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, 1, 0, ?, ?)
            """
            cursor.execute(api_key_query, (api_key_id, user_id, "Default API Key", api_key_hash,
                                         key_prefix, now, now))

            created_users.append({
                'email': email,
                'name': full_name,
                'plan': plan,
                'user_id': user_id,
                'api_key': api_key
            })

            print(f"✅ Created user: {email} (Plan: {plan})")

        except Exception as e:
            print(f"❌ Error creating user {email}: {e}")

    # Commit all changes
    conn.commit()
    conn.close()

    return created_users

if __name__ == "__main__":
    print("🧬 Creating BioQL Demo Users")
    print("=" * 50)

    users = create_demo_users()

    print(f"\n🎉 Successfully created {len(users)} demo users:")
    print("=" * 80)

    for user in users:
        print(f"📧 Email: {user['email']}")
        print(f"👤 Name: {user['name']}")
        print(f"📋 Plan: {user['plan']}")
        print(f"🔑 API Key: {user['api_key']}")
        print(f"🆔 User ID: {user['user_id']}")
        print("-" * 80)

    # Save API keys to file for testing
    with open("demo_api_keys.txt", "w") as f:
        f.write("# BioQL Demo User API Keys\n")
        f.write("# Format: email,api_key,plan\n\n")
        for user in users:
            f.write(f"{user['email']},{user['api_key']},{user['plan']}\n")

    print(f"💾 API keys saved to demo_api_keys.txt")
    print(f"🚀 Ready for comprehensive testing!")