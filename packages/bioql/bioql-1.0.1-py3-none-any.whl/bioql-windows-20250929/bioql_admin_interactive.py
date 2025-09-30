#!/usr/bin/env python3
"""
BioQL Admin CLI - Interactive Guided Version

Interactive CLI with guided workflows for managing BioQL billing system.
Features step-by-step wizards and intuitive menu navigation.
"""

import os
import sys
import sqlite3
import json
from datetime import datetime, timedelta
import cmd
import shlex

class InteractiveTable:
    """Enhanced table formatter with better visual appeal."""

    def __init__(self, headers):
        self.headers = headers
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def format(self):
        if not self.rows:
            return "📝 No data to display"

        # Calculate column widths
        all_rows = [self.headers] + self.rows
        col_widths = []

        for col in range(len(self.headers)):
            max_width = max(len(str(row[col])) for row in all_rows)
            col_widths.append(max(max_width + 2, 8))  # Minimum width of 8

        # Format table with better borders
        result = []

        # Top border
        top_border = "┌" + "┬".join("─" * (w + 1) for w in col_widths) + "┐"
        result.append(top_border)

        # Header
        header_line = "│ " + " │ ".join(
            str(self.headers[i]).ljust(col_widths[i] - 1) for i in range(len(self.headers))
        ) + " │"
        result.append(header_line)

        # Header separator
        header_sep = "├" + "┼".join("─" * (w + 1) for w in col_widths) + "┤"
        result.append(header_sep)

        # Rows
        for row in self.rows:
            row_line = "│ " + " │ ".join(
                str(row[i]).ljust(col_widths[i] - 1) for i in range(len(row))
            ) + " │"
            result.append(row_line)

        # Bottom border
        bottom_border = "└" + "┴".join("─" * (w + 1) for w in col_widths) + "┘"
        result.append(bottom_border)

        return "\n".join(result)

    def display(self):
        """Display the formatted table"""
        print(self.format())

class BioQLInteractiveCLI(cmd.Cmd):
    """Interactive CLI with guided workflows for BioQL administration."""

    intro = """
🧬 BioQL Administration Console - Interactive Mode
=================================================
¡Bienvenido al sistema interactivo de administración de BioQL!

Este CLI te guiará paso a paso para gestionar usuarios, facturación,
API keys y más. Selecciona opciones del menú o usa comandos directos.

💡 Tips rápidos:
   • Escribe 'menu' para ver opciones principales
   • Escribe 'wizard' para asistentes guiados
   • Escribe 'help' para ver todos los comandos
   • Escribe 'quick' para acciones rápidas
"""

    prompt = "🧬 bioql> "

    def __init__(self, database_path: str = None):
        super().__init__()
        self.database_path = database_path or "bioql_billing.db"

        # Check if database exists
        if not os.path.exists(self.database_path):
            print(f"❌ Database not found: {self.database_path}")
            print("Run setup_billing_database.py first to create the database.")
            sys.exit(1)

        print(f"✅ Connected to database: {self.database_path}")
        self._show_startup_info()
        print("\n💡 Type 'menu' to see main options or 'help' for all commands")

    def _execute_query(self, query: str, params=None, fetch=True):
        """Execute a SQL query and return results."""
        try:
            conn = sqlite3.connect(self.database_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if fetch:
                results = cursor.fetchall()
                conn.close()
                return results
            else:
                conn.commit()
                conn.close()
                return cursor.rowcount
        except sqlite3.Error as e:
            print(f"❌ Database error: {e}")
            return None

    def _show_startup_info(self):
        """Display startup information."""
        try:
            # Get database stats
            user_count = self._execute_query("SELECT COUNT(*) as count FROM users")[0]['count']
            active_subs = self._execute_query("SELECT COUNT(*) as count FROM subscriptions WHERE status = 'active'")[0]['count']
            total_usage = self._execute_query("SELECT COUNT(*) as count FROM usage_logs")[0]['count']
            pending_bills = self._execute_query("SELECT COUNT(*) as count FROM bills WHERE status = 'pending'")[0]['count']

            print("\n" + "="*70)
            print("                       📊 SYSTEM STATUS")
            print("="*70)
            print(f"  Database: {self.database_path}")
            print(f"  👥 Users: {user_count} | 🔄 Active Subscriptions: {active_subs}")
            print(f"  📈 Usage Logs: {total_usage} | 💰 Pending Bills: {pending_bills}")
            print("="*70)

        except Exception as e:
            print(f"⚠️  Could not load system stats: {e}")

    def _pause(self, message="Press Enter to continue..."):
        """Pause and wait for user input."""
        input(f"\n{message}")

    def _get_user_input(self, prompt, required=True, validation_func=None):
        """Get user input with validation."""
        while True:
            value = input(f"{prompt}: ").strip()

            if not value and required:
                print("❌ This field is required. Please enter a value.")
                continue

            if validation_func and value:
                if not validation_func(value):
                    continue

            return value

    def _validate_email(self, email):
        """Validate email format."""
        if '@' not in email or '.' not in email.split('@')[1]:
            print("❌ Please enter a valid email address (example@domain.com)")
            return False
        return True

    def _validate_plan(self, plan):
        """Validate plan type."""
        valid_plans = ['free', 'basic', 'pro', 'enterprise']
        if plan.lower() not in valid_plans:
            print(f"❌ Plan must be one of: {', '.join(valid_plans)}")
            return False
        return True

    # === MAIN MENU SYSTEM ===

    def do_menu(self, args):
        """Show main menu with all available options."""
        while True:
            print("\n" + "="*70)
            print("                    🧬 BIOQL MAIN MENU")
            print("="*70)
            print("  1. 👥 User Management")
            print("  2. 🔑 API Key Management")
            print("  3. 💰 Billing & Invoices")
            print("  4. 📊 Reports & Analytics")
            print("  5. 🔧 System Tools")
            print("  6. 🎯 Quick Actions")
            print("  7. 📚 Help & Documentation")
            print("  0. 🚪 Exit")
            print("="*70)

            choice = input("\nSelect an option (0-7): ").strip()

            if choice == '1':
                self._user_management_menu()
            elif choice == '2':
                self._api_key_menu()
            elif choice == '3':
                self._billing_menu()
            elif choice == '4':
                self._reports_menu()
            elif choice == '5':
                self._system_tools_menu()
            elif choice == '6':
                self._quick_actions_menu()
            elif choice == '7':
                self._help_menu()
            elif choice == '0':
                return
            else:
                print("❌ Invalid option. Please select 0-7.")

    def _user_management_menu(self):
        """User management submenu."""
        while True:
            print("\n" + "="*70)
            print("                   👥 USER MANAGEMENT")
            print("="*70)
            print("  1. 📋 List all users")
            print("  2. ➕ Create new user (Guided)")
            print("  3. 🔍 Search user details")
            print("  4. ❌ Deactivate user")
            print("  5. 🎯 Quick user lookup")
            print("  0. ⬅️  Back to main menu")
            print("="*70)

            choice = input("\nSelect an option (0-5): ").strip()

            if choice == '1':
                self._list_users_interactive()
            elif choice == '2':
                self._create_user_wizard()
            elif choice == '3':
                self._user_details_interactive()
            elif choice == '4':
                self._deactivate_user_interactive()
            elif choice == '5':
                self._quick_user_lookup()
            elif choice == '0':
                return
            else:
                print("❌ Invalid option. Please select 0-5.")

    def _api_key_menu(self):
        """API key management submenu."""
        while True:
            print("\n" + "="*70)
            print("                   🔑 API KEY MANAGEMENT")
            print("="*70)
            print("  1. 📋 List user's API keys")
            print("  2. ➕ Create new API key (Guided)")
            print("  3. 🔍 Find API key details")
            print("  0. ⬅️  Back to main menu")
            print("="*70)

            choice = input("\nSelect an option (0-3): ").strip()

            if choice == '1':
                self._list_api_keys_interactive()
            elif choice == '2':
                self._create_api_key_wizard()
            elif choice == '3':
                self._api_key_details_interactive()
            elif choice == '0':
                return
            else:
                print("❌ Invalid option. Please select 0-3.")

    def _billing_menu(self):
        """Billing management submenu."""
        while True:
            print("\n" + "="*70)
            print("                   💰 BILLING & INVOICES")
            print("="*70)
            print("  1. 📋 List all bills")
            print("  2. 🔍 Bills by user")
            print("  3. ⚠️  Pending bills")
            print("  4. 📊 Billing summary")
            print("  0. ⬅️  Back to main menu")
            print("="*70)

            choice = input("\nSelect an option (0-4): ").strip()

            if choice == '1':
                self._list_bills_interactive()
            elif choice == '2':
                self._bills_by_user_interactive()
            elif choice == '3':
                self._pending_bills_interactive()
            elif choice == '4':
                self._billing_summary_interactive()
            elif choice == '0':
                return
            else:
                print("❌ Invalid option. Please select 0-4.")

    def _reports_menu(self):
        """Reports and analytics submenu."""
        while True:
            print("\n" + "="*70)
            print("                   📊 REPORTS & ANALYTICS")
            print("="*70)
            print("  1. 📈 Usage statistics")
            print("  2. 👥 User analytics")
            print("  3. 💰 Revenue reports")
            print("  4. 🔧 System health")
            print("  0. ⬅️  Back to main menu")
            print("="*70)

            choice = input("\nSelect an option (0-4): ").strip()

            if choice == '1':
                self._usage_stats_interactive()
            elif choice == '2':
                self._user_analytics_interactive()
            elif choice == '3':
                self._revenue_reports_interactive()
            elif choice == '4':
                self._system_health_interactive()
            elif choice == '0':
                return
            else:
                print("❌ Invalid option. Please select 0-4.")

    def _system_tools_menu(self):
        """System tools submenu."""
        while True:
            print("\n" + "="*70)
            print("                     🔧 SYSTEM TOOLS")
            print("="*70)
            print("  1. 💾 Create database backup")
            print("  2. 🗃️  Execute SQL query")
            print("  3. 📊 System status")
            print("  4. 🧹 Maintenance tools")
            print("  0. ⬅️  Back to main menu")
            print("="*70)

            choice = input("\nSelect an option (0-4): ").strip()

            if choice == '1':
                self._backup_interactive()
            elif choice == '2':
                self._sql_query_interactive()
            elif choice == '3':
                self._show_startup_info()
                self._pause()
            elif choice == '4':
                self._maintenance_tools_interactive()
            elif choice == '0':
                return
            else:
                print("❌ Invalid option. Please select 0-4.")

    def _quick_actions_menu(self):
        """Quick actions for common tasks."""
        while True:
            print("\n" + "="*70)
            print("                     🎯 QUICK ACTIONS")
            print("="*70)
            print("  1. ⚡ Create user + API key (Express)")
            print("  2. 🔍 Find user by email")
            print("  3. 💰 Check user billing")
            print("  4. 📊 Today's stats")
            print("  0. ⬅️  Back to main menu")
            print("="*70)

            choice = input("\nSelect an option (0-4): ").strip()

            if choice == '1':
                self._express_user_creation()
            elif choice == '2':
                self._quick_user_search()
            elif choice == '3':
                self._quick_billing_check()
            elif choice == '4':
                self._todays_stats()
            elif choice == '0':
                return
            else:
                print("❌ Invalid option. Please select 0-4.")

    def _help_menu(self):
        """Help and documentation menu."""
        print("\n" + "="*70)
        print("                   📚 HELP & DOCUMENTATION")
        print("="*70)
        print("Available commands:")
        print("  • menu        - Show main menu")
        print("  • wizard      - Launch creation wizards")
        print("  • quick       - Quick actions menu")
        print("  • status      - System status")
        print("  • help        - Command help")
        print("  • exit/quit   - Exit the system")
        print("\nDirect commands:")
        print("  • list_users  - List all users")
        print("  • create_user - Create user wizard")
        print("  • user_details - Show user details")
        print("  • usage_stats - Usage statistics")
        print("  • list_bills  - List bills")
        print("  • backup      - Create backup")
        print("="*70)
        self._pause()

    # === INTERACTIVE IMPLEMENTATIONS ===

    def _list_users_interactive(self):
        """Interactive user listing with filters."""
        print("\n📋 USER LISTING OPTIONS")
        print("="*50)

        # Get filter options
        print("Filter options (press Enter to skip):")
        plan_filter = input("  Plan (free/basic/pro/enterprise): ").strip()
        limit_str = input("  Limit results (default: all): ").strip()

        # Build query
        query = "SELECT id, email, (first_name || ' ' || last_name) as name, organization, current_plan, is_active, created_at FROM users"
        params = []

        if plan_filter:
            query += " WHERE current_plan = ?"
            params.append(plan_filter)

        query += " ORDER BY created_at DESC"

        if limit_str and limit_str.isdigit():
            query += f" LIMIT {limit_str}"

        users = self._execute_query(query, params if params else None)

        if not users:
            print("\n❌ No users found with the specified criteria.")
            self._pause()
            return

        # Display results
        print(f"\n📋 Found {len(users)} users:")
        table = InteractiveTable(["ID", "Email", "Name", "Organization", "Plan", "Status"])

        for user in users:
            status = "🟢 Active" if user['is_active'] else "🔴 Inactive"
            table.add_row([
                user['id'][:8] + "...",
                user['email'],
                user['name'] or "-",
                user['organization'] or "-",
                user['current_plan'],
                status
            ])

        print(table.format())
        self._pause()

    def _create_user_wizard(self):
        """Guided user creation wizard."""
        print("\n" + "="*70)
        print("                   ➕ CREATE NEW USER WIZARD")
        print("="*70)
        print("Este asistente te guiará para crear un nuevo usuario paso a paso.\n")

        # Step 1: Email
        print("📧 STEP 1: Email Address")
        email = self._get_user_input(
            "Enter user email",
            required=True,
            validation_func=self._validate_email
        )

        # Check if user exists
        existing = self._execute_query("SELECT id FROM users WHERE email = ?", (email,))
        if existing:
            print(f"\n❌ User with email {email} already exists!")
            self._pause()
            return

        # Step 2: Name
        print(f"\n👤 STEP 2: User Name")
        name = self._get_user_input("Enter full name", required=True)

        # Step 3: Organization
        print(f"\n🏢 STEP 3: Organization")
        organization = self._get_user_input("Enter organization name", required=True)

        # Step 4: Plan
        print(f"\n📋 STEP 4: Subscription Plan")
        print("Available plans:")
        print("  • free - Free tier (limited usage)")
        print("  • basic - Basic plan ($99/month)")
        print("  • pro - Professional plan ($499/month)")
        print("  • enterprise - Enterprise plan ($2999/month)")

        plan = self._get_user_input(
            "Select plan",
            required=False,
            validation_func=self._validate_plan
        ) or 'free'

        # Step 5: Confirmation
        print(f"\n✅ STEP 5: Confirmation")
        print("="*50)
        print(f"Email: {email}")
        print(f"Name: {name}")
        print(f"Organization: {organization}")
        print(f"Plan: {plan}")
        print("="*50)

        confirm = input("\nCreate this user? (y/N): ").strip().lower()
        if confirm != 'y':
            print("❌ User creation cancelled.")
            self._pause()
            return

        # Create user
        try:
            import uuid
            import secrets
            import hashlib

            user_id = str(uuid.uuid4())
            api_key = f"bioql_{secrets.token_urlsafe(32)}"
            api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()
            api_key_id = str(uuid.uuid4())

            # Insert user (splitting name into first_name and last_name)
            name_parts = name.split(' ', 1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''

            user_query = """
                INSERT INTO users (id, email, username, password_hash, first_name, last_name, organization,
                                 current_plan, is_active, is_verified, is_admin, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1, 0, 0, ?, ?)
            """
            from datetime import datetime
            now = datetime.now().isoformat()
            # Use email as username and create a placeholder password hash
            username = email.split('@')[0]
            password_hash = "placeholder_hash"  # In a real system, this would be properly hashed

            self._execute_query(user_query, (user_id, email, username, password_hash, first_name,
                                           last_name, organization, plan, now, now), fetch=False)

            # Insert API key
            api_key_query = """
                INSERT INTO api_keys (id, user_id, key_name, key_hash, key_prefix, is_active,
                                    total_requests, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, 1, 0, ?, ?)
            """
            key_prefix = api_key[:12]  # First 12 characters as prefix
            self._execute_query(api_key_query, (api_key_id, user_id, "Default API Key", api_key_hash,
                                              key_prefix, now, now), fetch=False)

            # Success display
            print("\n" + "="*70)
            print("                  🎉 USER CREATED SUCCESSFULLY!")
            print("="*70)
            print(f"📧 Email: {email}")
            print(f"👤 Name: {name}")
            print(f"🏢 Organization: {organization}")
            print(f"📋 Plan: {plan}")
            print(f"🆔 User ID: {user_id}")
            print(f"🔑 API Key: {api_key}")
            print("\n⚠️  IMPORTANT: Save the API key - it won't be shown again!")
            print("="*70)

            # Ask if user wants to create another API key
            another_key = input("\nCreate additional API key for this user? (y/N): ").strip().lower()
            if another_key == 'y':
                key_name = self._get_user_input("API key name", required=True)
                self._create_api_key_for_user(user_id, email, key_name)

        except Exception as e:
            print(f"\n❌ Error creating user: {e}")

        self._pause()

    def _user_details_interactive(self):
        """Interactive user details lookup."""
        print("\n🔍 USER DETAILS LOOKUP")
        print("="*50)

        identifier = self._get_user_input("Enter email or user ID", required=True)

        # Find user
        if '@' in identifier:
            user_query = "SELECT * FROM users WHERE email = ?"
            user_params = (identifier,)
        else:
            user_query = "SELECT * FROM users WHERE id LIKE ?"
            user_params = (f"{identifier}%",)

        users = self._execute_query(user_query, user_params)

        if not users:
            print(f"\n❌ User not found: {identifier}")
            self._pause()
            return

        user = users[0]

        # Get additional data
        api_keys = self._execute_query("SELECT * FROM api_keys WHERE user_id = ?", (user['id'],))

        usage_stats = self._execute_query("""
            SELECT
                COUNT(*) as total_jobs,
                SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) as successful_jobs,
                SUM(CASE WHEN success = 1 THEN shots_executed ELSE 0 END) as total_shots,
                SUM(CASE WHEN success = 1 THEN CAST(total_cost as REAL) ELSE 0 END) as total_cost
            FROM usage_logs WHERE user_id = ?
        """, (user['id'],))

        stats = usage_stats[0] if usage_stats else {
            'total_jobs': 0, 'successful_jobs': 0, 'total_shots': 0, 'total_cost': 0
        }

        bills = self._execute_query("SELECT COUNT(*) as count FROM bills WHERE user_id = ?", (user['id'],))
        bill_count = bills[0]['count'] if bills else 0

        # Display comprehensive details
        print("\n" + "="*70)
        print("                    👤 USER DETAILS")
        print("="*70)
        print(f"🆔 User ID: {user['id']}")
        print(f"📧 Email: {user['email']}")
        print(f"👤 Name: {user['name'] or 'Not set'}")
        print(f"🏢 Organization: {user['organization'] or 'Not set'}")
        print(f"📋 Plan: {user['current_plan'].upper()}")
        print(f"🔄 Status: {'🟢 Active' if user['is_active'] else '🔴 Inactive'}")
        print(f"📅 Created: {user['created_at']}")
        print("\n📊 USAGE SUMMARY")
        print("-" * 20)
        print(f"🔑 API Keys: {len(api_keys)} active")
        print(f"⚡ Total Jobs: {stats['total_jobs']} ({stats['successful_jobs']} successful)")
        print(f"🎯 Total Shots: {stats['total_shots'] or 0:,}")
        print(f"💰 Total Spent: ${float(stats['total_cost'] or 0):.2f}")
        print(f"🧾 Bills: {bill_count}")
        print("="*70)

        # Show API keys if exist
        if api_keys:
            print("\n🔑 API KEYS:")
            api_table = InteractiveTable(["Key Prefix", "Name", "Created", "Usage"])
            for key in api_keys:
                prefix = f"bioql_{key['id'][:8]}..."
                created_date = datetime.fromisoformat(key['created_at']).strftime('%Y-%m-%d')
                api_table.add_row([prefix, key['key_name'], created_date, str(key['total_requests'])])
            print(api_table.format())

        # Action menu
        print("\n🎯 ACTIONS:")
        print("  1. Create new API key")
        print("  2. View usage details")
        print("  3. View billing details")
        print("  0. Return to menu")

        action = input("\nSelect action (0-3): ").strip()

        if action == '1':
            key_name = self._get_user_input("API key name", required=True)
            self._create_api_key_for_user(user['id'], user['email'], key_name)
        elif action == '2':
            self._show_user_usage_details(user['id'], user['email'])
        elif action == '3':
            self._show_user_billing_details(user['id'], user['email'])

        self._pause()

    def _create_api_key_for_user(self, user_id, user_email, key_name):
        """Helper to create API key for existing user."""
        try:
            import uuid
            import secrets
            import hashlib

            api_key = f"bioql_{secrets.token_urlsafe(32)}"
            api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()
            api_key_id = str(uuid.uuid4())

            # Insert API key
            api_key_query = """
                INSERT INTO api_keys (id, user_id, key_name, key_hash, key_prefix, is_active, total_requests, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, 1, 0, ?, ?)
            """
            now = datetime.utcnow().isoformat()
            key_prefix = api_key[:12]  # First 12 characters as prefix
            self._execute_query(api_key_query, (api_key_id, user_id, key_name, api_key_hash, key_prefix, now, now), fetch=False)

            print("\n" + "="*70)
            print("                  🔑 API KEY CREATED!")
            print("="*70)
            print(f"👤 User: {user_email}")
            print(f"🏷️  Name: {key_name}")
            print(f"🔑 API Key: {api_key}")
            print("\n⚠️  SAVE THIS KEY - IT WON'T BE SHOWN AGAIN!")
            print("="*70)

        except Exception as e:
            print(f"\n❌ Error creating API key: {e}")

    def _show_user_usage_details(self, user_id, user_email):
        """Show detailed usage information for a user."""
        print(f"\n📊 USAGE DETAILS FOR {user_email}")
        print("="*60)

        # Get usage by backend
        backend_usage = self._execute_query("""
            SELECT
                backend_used,
                algorithm_type,
                COUNT(*) as jobs,
                SUM(shots_executed) as total_shots,
                SUM(CAST(total_cost as REAL)) as total_cost
            FROM usage_logs
            WHERE user_id = ? AND success = 1
            GROUP BY backend_used, algorithm_type
            ORDER BY total_cost DESC
        """, (user_id,))

        if backend_usage:
            table = InteractiveTable(["Backend", "Algorithm", "Jobs", "Shots", "Cost"])
            for usage in backend_usage:
                table.add_row([
                    usage['backend_used'] or 'Unknown',
                    usage['algorithm_type'] or 'Unknown',
                    str(usage['jobs']),
                    f"{usage['total_shots']:,}",
                    f"${usage['total_cost']:.2f}"
                ])
            print(table.format())
        else:
            print("📝 No usage data found.")

    def _show_user_billing_details(self, user_id, user_email):
        """Show billing details for a user."""
        print(f"\n💰 BILLING DETAILS FOR {user_email}")
        print("="*60)

        bills = self._execute_query("""
            SELECT bill_number, period_start, period_end, total_amount, status, due_at
            FROM bills
            WHERE user_id = ?
            ORDER BY created_at DESC
        """, (user_id,))

        if bills:
            table = InteractiveTable(["Bill #", "Period", "Amount", "Status", "Due"])
            for bill in bills:
                period = datetime.fromisoformat(bill['period_start']).strftime('%Y-%m')
                due_date = datetime.fromisoformat(bill['due_at']).strftime('%Y-%m-%d') if bill['due_at'] else "-"
                table.add_row([
                    bill['bill_number'],
                    period,
                    f"${float(bill['total_amount']):.2f}",
                    bill['status'],
                    due_date
                ])
            print(table.format())
        else:
            print("📝 No bills found.")

    # === QUICK ACTIONS ===

    def _express_user_creation(self):
        """Express user creation - minimal steps."""
        print("\n⚡ EXPRESS USER CREATION")
        print("="*50)

        email = self._get_user_input("Email", required=True, validation_func=self._validate_email)
        name = self._get_user_input("Name", required=True)
        organization = self._get_user_input("Organization", required=True)

        try:
            import uuid
            import secrets
            import hashlib

            user_id = str(uuid.uuid4())
            api_key = f"bioql_{secrets.token_urlsafe(32)}"
            api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()
            api_key_id = str(uuid.uuid4())

            now = datetime.utcnow().isoformat()

            # Insert user
            user_query = """
                INSERT INTO users (id, email, name, organization, current_plan, is_active, created_at, updated_at)
                VALUES (?, ?, ?, ?, 'free', 1, ?, ?)
            """
            self._execute_query(user_query, (user_id, email, name, organization, now, now), fetch=False)

            # Insert API key
            api_key_query = """
                INSERT INTO api_keys (id, user_id, key_name, key_hash, key_prefix, is_active, total_requests, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, 1, 0, ?, ?)
            """
            self._execute_query(api_key_query, (api_key_id, user_id, "Default API Key", api_key_hash, now, now), fetch=False)

            print(f"\n✅ User created: {email}")
            print(f"🔑 API Key: {api_key}")
            print("⚠️  Save the API key!")

        except Exception as e:
            print(f"❌ Error: {e}")

        self._pause()

    def _quick_user_search(self):
        """Quick user search by email."""
        email = self._get_user_input("Enter email to search")
        if email:
            self.do_user_details(email)

    def _todays_stats(self):
        """Show today's statistics."""
        today = datetime.now().strftime('%Y-%m-%d')

        print(f"\n📊 TODAY'S STATISTICS ({today})")
        print("="*50)

        # Users created today
        users_today = self._execute_query(
            "SELECT COUNT(*) as count FROM users WHERE DATE(created_at) = DATE('now')"
        )[0]['count']

        # Usage today
        usage_today = self._execute_query(
            "SELECT COUNT(*) as count FROM usage_logs WHERE DATE(created_at) = DATE('now')"
        )[0]['count']

        print(f"👥 New users: {users_today}")
        print(f"⚡ Quantum jobs: {usage_today}")

        self._pause()

    # === LEGACY COMMAND COMPATIBILITY ===

    def do_wizard(self, args):
        """Launch creation wizards."""
        print("\n🧙‍♂️ BIOQL WIZARDS")
        print("="*30)
        print("  1. Create User")
        print("  2. Create API Key")
        print("  3. System Setup")
        print("  0. Cancel")

        choice = input("\nSelect wizard (0-3): ").strip()

        if choice == '1':
            self._create_user_wizard()
        elif choice == '2':
            self._create_api_key_wizard()
        elif choice == '3':
            print("🔧 System setup wizard not implemented yet.")
            self._pause()

    def do_quick(self, args):
        """Quick actions menu."""
        self._quick_actions_menu()

    def do_status(self, args):
        """Show system status."""
        self._show_startup_info()

    def do_user_details(self, args):
        """Show user details."""
        if args.strip():
            # Direct command with argument
            identifier = args.strip()
            # Implementation similar to _user_details_interactive but with direct arg
            print(f"Looking up user: {identifier}")
            # ... (implement lookup logic)
        else:
            self._user_details_interactive()

    def do_list_users(self, args):
        """List users command."""
        self._list_users_interactive()

    def do_backup(self, args):
        """Create database backup."""
        self._backup_interactive()

    def _backup_interactive(self):
        """Interactive backup creation."""
        print("\n💾 DATABASE BACKUP")
        print("="*30)

        filename = input("Backup filename (or Enter for auto): ").strip()
        if not filename:
            filename = f"bioql_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"

        try:
            import shutil
            shutil.copy2(self.database_path, filename)
            print(f"✅ Backup created: {filename}")
        except Exception as e:
            print(f"❌ Backup failed: {e}")

        self._pause()

    def do_help(self, args):
        """Enhanced help system."""
        if args.strip():
            # Help for specific command
            super().do_help(args)
        else:
            self._help_menu()

    def do_exit(self, args):
        """Exit the system."""
        print("\n👋 ¡Gracias por usar BioQL Admin!")
        print("💡 Tip: Recuerda hacer backups regulares de tu base de datos.")
        return True

    def do_quit(self, args):
        """Exit the system."""
        return self.do_exit(args)

    def default(self, line):
        """Handle unknown commands with suggestions."""
        print(f"❌ Unknown command: '{line}'")
        print("\n💡 Quick suggestions:")
        print("  • Type 'menu' to see all options")
        print("  • Type 'help' for command list")
        print("  • Type 'wizard' for guided setup")
        print("  • Type 'quick' for quick actions")

    # === PLACEHOLDER IMPLEMENTATIONS FOR MENU ITEMS ===

    def _create_api_key_wizard(self):
        """API key creation wizard."""
        print("\n🔑 API KEY CREATION WIZARD")
        print("="*50)

        email = self._get_user_input("User email", required=True)

        # Find user
        user = self._execute_query("SELECT * FROM users WHERE email = ?", (email,))
        if not user:
            print(f"❌ User not found: {email}")
            self._pause()
            return

        user = user[0]
        key_name = self._get_user_input("API key name", required=True)

        self._create_api_key_for_user(user['id'], user['email'], key_name)
        self._pause()

    def _list_api_keys_interactive(self):
        """Interactive API key listing."""
        email = self._get_user_input("User email", required=True)
        self.do_list_api_keys(email)

    def _api_key_details_interactive(self):
        """API key details lookup."""
        print("\n🔍 API KEY DETAILS")
        print("="*40)

        # Option to search by user email or key prefix
        print("Search options:")
        print("1. By user email")
        print("2. By API key prefix")
        print("0. Back to menu")

        choice = input("\nSelect option (0-2): ").strip()

        if choice == '0':
            return

        elif choice == '1':
            email = input("Enter user email: ").strip()
            if not email:
                print("❌ Email is required")
                self._pause()
                return

            try:
                # Get API keys for user
                api_keys_query = """
                    SELECT ak.*, u.email, (u.first_name || ' ' || u.last_name) as name
                    FROM api_keys ak
                    JOIN users u ON ak.user_id = u.id
                    WHERE u.email = ?
                    ORDER BY ak.created_at DESC
                """
                api_keys = self._execute_query(api_keys_query, (email,))

                if not api_keys:
                    print(f"📭 No API keys found for {email}")
                    self._pause()
                    return

                print(f"\n🔑 API KEYS FOR {email}")
                print("="*40)

                table = InteractiveTable(['Key Prefix', 'Name', 'Status', 'Usage', 'Created'])
                for key in api_keys:
                    key_prefix = f"bioql_{key['key_hash'][:8]}..."
                    status = "✅ Active" if key['is_active'] else "❌ Inactive"
                    table.add_row([
                        key_prefix,
                        key['name'],
                        status,
                        str(key['total_requests']),
                        key['created_at'][:10]
                    ])

                table.display()

            except Exception as e:
                print(f"❌ Error retrieving API keys: {e}")

        elif choice == '2':
            key_prefix = input("Enter API key prefix (first 8+ chars after 'bioql_'): ").strip()
            if not key_prefix:
                print("❌ Key prefix is required")
                self._pause()
                return

            try:
                # Search by key hash prefix
                key_search_query = """
                    SELECT ak.*, u.email, (u.first_name || ' ' || u.last_name) as name
                    FROM api_keys ak
                    JOIN users u ON ak.user_id = u.id
                    WHERE ak.key_hash LIKE ?
                    ORDER BY ak.created_at DESC
                    LIMIT 10
                """
                api_keys = self._execute_query(key_search_query, (f"{key_prefix}%",))

                if not api_keys:
                    print(f"📭 No API keys found matching prefix: {key_prefix}")
                    self._pause()
                    return

                print(f"\n🔍 API KEYS MATCHING: {key_prefix}")
                print("="*40)

                for i, key in enumerate(api_keys, 1):
                    key_prefix_display = f"bioql_{key['key_hash'][:8]}..."
                    status = "✅ Active" if key['is_active'] else "❌ Inactive"

                    print(f"\n{i}. {key_prefix_display}")
                    print(f"   User: {key['name']} ({key['email']})")
                    print(f"   Name: {key['key_name']}")
                    print(f"   Status: {status}")
                    print(f"   Usage: {key['total_requests']} calls")
                    print(f"   Created: {key['created_at'][:19]}")
                    print(f"   Updated: {key['updated_at'][:19]}")

            except Exception as e:
                print(f"❌ Error searching API keys: {e}")

        else:
            print("❌ Invalid selection")

        self._pause()

    def _list_bills_interactive(self):
        """Interactive bill listing."""
        print("\n💰 BILL LISTING")
        print("="*40)

        # Get filter options
        print("Filter options:")
        print("1. All bills")
        print("2. Filter by user")
        print("3. Filter by status")
        print("4. Filter by user AND status")
        print("0. Back to billing menu")

        choice = input("\nSelect option (0-4): ").strip()

        if choice == '0':
            return

        user_filter = None
        status_filter = None

        if choice in ['2', '4']:
            user_filter = input("Enter user email: ").strip()
            if not user_filter:
                print("❌ Email required")
                self._pause()
                return

        if choice in ['3', '4']:
            print("\nAvailable statuses:")
            print("• pending")
            print("• paid")
            print("• failed")
            print("• cancelled")
            status_filter = input("Enter status: ").strip()
            if not status_filter:
                print("❌ Status required")
                self._pause()
                return

        limit = input("\nLimit results (default: 20): ").strip()
        limit = int(limit) if limit.isdigit() else 20

        try:
            # Build query
            query = """
                SELECT b.*, u.email
                FROM bills b
                JOIN users u ON b.user_id = u.id
                WHERE 1=1
            """
            params = []

            if user_filter:
                query += " AND u.email = ?"
                params.append(user_filter)

            if status_filter:
                query += " AND b.status = ?"
                params.append(status_filter)

            query += " ORDER BY b.created_at DESC LIMIT ?"
            params.append(limit)

            bills = self._execute_query(query, params)

            if not bills:
                print("\n📭 No bills found matching criteria")
                self._pause()
                return

            # Display results
            print(f"\n📋 Found {len(bills)} bills:")
            print()

            table = InteractiveTable(['ID', 'User', 'Amount', 'Status', 'Created'])

            for bill in bills:
                table.add_row([
                    bill['id'][:8] + '...',
                    bill['email'],
                    f"${bill['total_amount']:.2f}",
                    bill['status'].upper(),
                    bill['created_at'][:10]
                ])

            table.display()

        except Exception as e:
            print(f"❌ Error listing bills: {e}")

        self._pause()

    def _bills_by_user_interactive(self):
        """Bills by user lookup."""
        print("\n👤 BILLS BY USER")
        print("="*40)

        email = input("Enter user email: ").strip()
        if not email:
            print("❌ Email is required")
            self._pause()
            return

        try:
            # First check if user exists
            user_query = "SELECT id, (first_name || ' ' || last_name) as name, email FROM users WHERE email = ?"
            users = self._execute_query(user_query, (email,))

            if not users:
                print(f"❌ User not found: {email}")
                self._pause()
                return

            user = users[0]
            print(f"\n👤 User: {user['name']} ({user['email']})")

            # Get bills for this user
            bills_query = """
                SELECT b.*, u.email
                FROM bills b
                JOIN users u ON b.user_id = u.id
                WHERE u.email = ?
                ORDER BY b.created_at DESC
            """
            bills = self._execute_query(bills_query, (email,))

            if not bills:
                print("📭 No bills found for this user")
                self._pause()
                return

            print(f"\n📋 Found {len(bills)} bills:")
            print()

            table = InteractiveTable(['ID', 'Amount', 'Status', 'Period', 'Created'])

            total_amount = 0
            for bill in bills:
                total_amount += bill['total_amount']
                table.add_row([
                    bill['id'][:8] + '...',
                    f"${bill['total_amount']:.2f}",
                    bill['status'].upper(),
                    f"{bill['billing_period_start'][:10]} to {bill['billing_period_end'][:10]}",
                    bill['created_at'][:10]
                ])

            table.display()

            print(f"\n💰 Total amount: ${total_amount:.2f}")

        except Exception as e:
            print(f"❌ Error retrieving user bills: {e}")

        self._pause()

    def _pending_bills_interactive(self):
        """Pending bills view."""
        print("\n⚠️ PENDING BILLS")
        print("="*40)

        try:
            # Get all pending bills
            query = """
                SELECT b.*, u.email, (u.first_name || ' ' || u.last_name) as name
                FROM bills b
                JOIN users u ON b.user_id = u.id
                WHERE b.status = 'pending'
                ORDER BY b.created_at ASC
            """
            bills = self._execute_query(query)

            if not bills:
                print("🎉 No pending bills found - all bills are up to date!")
                self._pause()
                return

            print(f"\n📋 Found {len(bills)} pending bills:")
            print()

            table = InteractiveTable(['ID', 'User', 'Name', 'Amount', 'Due Date', 'Days Overdue'])

            total_pending = 0
            from datetime import datetime, timedelta

            for bill in bills:
                total_pending += bill['total_amount']

                # Calculate days overdue
                due_date = datetime.fromisoformat(bill['billing_period_end'])
                days_overdue = (datetime.now() - due_date).days

                table.add_row([
                    bill['id'][:8] + '...',
                    bill['email'],
                    bill['name'],
                    f"${bill['total_amount']:.2f}",
                    bill['billing_period_end'][:10],
                    str(max(0, days_overdue))
                ])

            table.display()

            print(f"\n💰 Total pending amount: ${total_pending:.2f}")

            # Show action options
            print("\nActions:")
            print("1. View bill details")
            print("2. Send reminder email (placeholder)")
            print("0. Return to menu")

            action = input("\nSelect action (0-2): ").strip()

            if action == '1':
                bill_id = input("Enter bill ID (first 8 chars): ").strip()
                # Find matching bill
                for bill in bills:
                    if bill['id'].startswith(bill_id):
                        self._show_bill_details(bill)
                        break
                else:
                    print("❌ Bill not found")

            elif action == '2':
                print("📧 Email reminder feature not implemented yet")

        except Exception as e:
            print(f"❌ Error retrieving pending bills: {e}")

        self._pause()

    def _show_bill_details(self, bill):
        """Show detailed bill information."""
        print(f"\n🧾 BILL DETAILS")
        print("="*50)
        print(f"ID: {bill['id']}")
        print(f"User: {bill.get('name', 'N/A')} ({bill.get('email', 'N/A')})")
        print(f"Status: {bill['status'].upper()}")
        print(f"Amount: ${bill['total_amount']:.2f}")
        print(f"Period: {bill['billing_period_start'][:10]} to {bill['billing_period_end'][:10]}")
        print(f"Created: {bill['created_at'][:19]}")
        print(f"Updated: {bill['updated_at'][:19]}")
        print("="*50)

    def _billing_summary_interactive(self):
        """Billing summary."""
        print("\n📊 BILLING SUMMARY")
        print("="*40)

        try:
            # Get billing statistics
            stats_query = """
                SELECT
                    status,
                    COUNT(*) as count,
                    SUM(total_amount) as total_amount
                FROM bills
                GROUP BY status
            """
            stats = self._execute_query(stats_query)

            if not stats:
                print("📭 No billing data found")
                self._pause()
                return

            print("\n💰 Bills by Status:")
            print()

            table = InteractiveTable(['Status', 'Count', 'Total Amount'])

            grand_total = 0
            for stat in stats:
                grand_total += stat['total_amount']
                table.add_row([
                    stat['status'].upper(),
                    str(stat['count']),
                    f"${stat['total_amount']:.2f}"
                ])

            table.display()

            print(f"\n💎 Grand Total: ${grand_total:.2f}")

            # Get recent billing activity
            recent_query = """
                SELECT b.*, u.email
                FROM bills b
                JOIN users u ON b.user_id = u.id
                ORDER BY b.created_at DESC
                LIMIT 5
            """
            recent_bills = self._execute_query(recent_query)

            if recent_bills:
                print("\n🕒 Recent Billing Activity:")
                print()

                recent_table = InteractiveTable(['User', 'Amount', 'Status', 'Date'])

                for bill in recent_bills:
                    recent_table.add_row([
                        bill['email'],
                        f"${bill['total_amount']:.2f}",
                        bill['status'].upper(),
                        bill['created_at'][:10]
                    ])

                recent_table.display()

            # Get monthly summary for current year
            monthly_query = """
                SELECT
                    strftime('%Y-%m', created_at) as month,
                    COUNT(*) as count,
                    SUM(total_amount) as total
                FROM bills
                WHERE strftime('%Y', created_at) = strftime('%Y', 'now')
                GROUP BY strftime('%Y-%m', created_at)
                ORDER BY month DESC
                LIMIT 6
            """
            monthly_stats = self._execute_query(monthly_query)

            if monthly_stats:
                print("\n📅 Monthly Summary (Last 6 months):")
                print()

                monthly_table = InteractiveTable(['Month', 'Bills', 'Revenue'])

                for month_stat in monthly_stats:
                    monthly_table.add_row([
                        month_stat['month'],
                        str(month_stat['count']),
                        f"${month_stat['total']:.2f}"
                    ])

                monthly_table.display()

        except Exception as e:
            print(f"❌ Error generating billing summary: {e}")

        self._pause()

    def _usage_stats_interactive(self):
        """Interactive usage statistics."""
        print("\n📈 USAGE STATISTICS")
        print("="*40)

        # Get options
        print("Filter options:")
        print("1. All users (last 30 days)")
        print("2. Specific user")
        print("3. Custom date range")
        print("0. Back to reports menu")

        choice = input("\nSelect option (0-3): ").strip()

        if choice == '0':
            return

        user_filter = None
        days = 30

        if choice == '2':
            user_filter = input("Enter user email: ").strip()
            if not user_filter:
                print("❌ Email required")
                self._pause()
                return

        if choice == '3':
            days_input = input("Enter number of days (default: 30): ").strip()
            days = int(days_input) if days_input.isdigit() else 30

        try:
            from datetime import datetime, timedelta

            # Calculate date range
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)

            # Build base query
            where_clause = "WHERE ul.created_at >= ?"
            params = [start_date.isoformat()]

            if user_filter:
                # Get user ID first
                user_query = "SELECT id FROM users WHERE email = ?"
                user_result = self._execute_query(user_query, (user_filter,))
                if not user_result:
                    print(f"❌ User not found: {user_filter}")
                    self._pause()
                    return
                where_clause += " AND ul.user_id = ?"
                params.append(user_result[0]['id'])

            # Get usage statistics
            usage_query = f"""
                SELECT
                    COUNT(*) as total_jobs,
                    SUM(ul.shots_executed) as total_shots,
                    SUM(ul.total_cost) as total_cost,
                    AVG(ul.total_cost) as avg_cost_per_job,
                    MIN(ul.created_at) as first_job,
                    MAX(ul.created_at) as last_job
                FROM usage_logs ul
                {where_clause}
            """
            usage_stats = self._execute_query(usage_query, params)

            if not usage_stats or not usage_stats[0]['total_jobs']:
                print(f"\n📭 No usage data found for the last {days} days")
                self._pause()
                return

            stats = usage_stats[0]

            print(f"\n📊 Usage Statistics (Last {days} days)")
            if user_filter:
                print(f"👤 User: {user_filter}")
            print()

            # Display summary stats
            summary_table = InteractiveTable(['Metric', 'Value'])
            summary_table.add_row(['Total Jobs', f"{stats['total_jobs']:,}"])
            summary_table.add_row(['Total Shots', f"{stats['total_shots']:,}"])
            summary_table.add_row(['Total Cost', f"${stats['total_cost']:.2f}"])
            summary_table.add_row(['Avg Cost per Job', f"${stats['avg_cost_per_job']:.2f}"])
            summary_table.add_row(['First Job', stats['first_job'][:19]])
            summary_table.add_row(['Last Job', stats['last_job'][:19]])
            summary_table.display()

            # Get top users (if not filtering by user)
            if not user_filter:
                top_users_query = f"""
                    SELECT
                        u.email,
                        (u.first_name || ' ' || u.last_name) as name,
                        COUNT(*) as job_count,
                        SUM(ul.shots_executed) as total_shots,
                        SUM(ul.total_cost) as total_cost
                    FROM usage_logs ul
                    JOIN users u ON ul.user_id = u.id
                    {where_clause.replace('ul.user_id = ?', '1=1')}
                    GROUP BY u.id, u.email, u.first_name, u.last_name
                    ORDER BY total_cost DESC
                    LIMIT 10
                """
                top_users = self._execute_query(top_users_query, params[:-1] if user_filter else params)

                if top_users:
                    print(f"\n🏆 Top Users by Cost:")
                    print()

                    users_table = InteractiveTable(['User', 'Jobs', 'Shots', 'Cost'])
                    for user in top_users:
                        users_table.add_row([
                            user['email'],
                            str(user['job_count']),
                            f"{user['total_shots']:,}",
                            f"${user['total_cost']:.2f}"
                        ])

                    users_table.display()

            # Get daily usage trend
            daily_query = f"""
                SELECT
                    DATE(ul.created_at) as usage_date,
                    COUNT(*) as jobs,
                    SUM(ul.shots_executed) as shots,
                    SUM(ul.total_cost) as cost
                FROM usage_logs ul
                {where_clause}
                GROUP BY DATE(ul.created_at)
                ORDER BY usage_date DESC
                LIMIT 7
            """
            daily_usage = self._execute_query(daily_query, params)

            if daily_usage:
                print(f"\n📅 Daily Usage Trend (Last 7 days):")
                print()

                daily_table = InteractiveTable(['Date', 'Jobs', 'Shots', 'Cost'])
                for day in daily_usage:
                    daily_table.add_row([
                        day['usage_date'],
                        str(day['jobs']),
                        f"{day['shots']:,}",
                        f"${day['cost']:.2f}"
                    ])

                daily_table.display()

        except Exception as e:
            print(f"❌ Error retrieving usage statistics: {e}")

        self._pause()

    def _user_analytics_interactive(self):
        """User analytics."""
        print("\n👥 USER ANALYTICS")
        print("="*40)

        try:
            # Get user distribution by plan
            plan_query = """
                SELECT
                    UPPER(current_plan) as current_plan,
                    COUNT(*) as user_count,
                    SUM(CASE WHEN is_active = 1 THEN 1 ELSE 0 END) as active_users
                FROM users
                GROUP BY UPPER(current_plan)
                ORDER BY user_count DESC
            """
            plan_stats = self._execute_query(plan_query)

            if plan_stats:
                print("\n📊 Users by Plan:")
                print()

                plan_table = InteractiveTable(['Plan', 'Total Users', 'Active Users', 'Inactive'])
                total_users = 0
                total_active = 0

                for plan in plan_stats:
                    total_users += plan['user_count']
                    total_active += plan['active_users']
                    inactive = plan['user_count'] - plan['active_users']

                    plan_table.add_row([
                        plan['current_plan'].upper(),
                        str(plan['user_count']),
                        str(plan['active_users']),
                        str(inactive)
                    ])

                plan_table.display()
                print(f"\n📈 Total: {total_users} users ({total_active} active, {total_users - total_active} inactive)")
            else:
                print("\n📊 Users by Plan:")
                print("No user data found.")

            # Get user activity summary
            activity_query = """
                SELECT
                    u.email,
                    (u.first_name || ' ' || u.last_name) as name,
                    u.current_plan,
                    u.created_at,
                    COUNT(ul.id) as job_count,
                    COALESCE(SUM(ul.total_cost), 0) as total_spent,
                    MAX(ul.created_at) as last_activity
                FROM users u
                LEFT JOIN usage_logs ul ON u.id = ul.user_id
                WHERE u.is_active = 1
                GROUP BY u.id, u.email, u.first_name, u.last_name, u.current_plan, u.created_at
                ORDER BY total_spent DESC
                LIMIT 15
            """
            user_activity = self._execute_query(activity_query)

            if user_activity:
                print("\n🚀 Top Active Users:")
                print()

                activity_table = InteractiveTable(['User', 'Plan', 'Jobs', 'Spent', 'Last Activity'])

                for user in user_activity:
                    last_activity = user['last_activity'][:10] if user['last_activity'] else 'Never'
                    activity_table.add_row([
                        user['email'],
                        user['current_plan'].upper(),
                        str(user['job_count']),
                        f"${user['total_spent']:.2f}",
                        last_activity
                    ])

                activity_table.display()
            else:
                print("\n🚀 Top Active Users:")
                print("No active user data found.")

            # Get new user registrations (last 90 days to capture demo data)
            new_users_query = """
                SELECT
                    DATE(created_at) as reg_date,
                    COUNT(*) as new_users
                FROM users
                WHERE created_at >= datetime('now', '-90 days')
                GROUP BY DATE(created_at)
                ORDER BY reg_date DESC
                LIMIT 15
            """
            new_users = self._execute_query(new_users_query)

            if new_users:
                print("\n📅 New Registrations (Last 90 days):")
                print()

                reg_table = InteractiveTable(['Date', 'New Users'])
                total_new = 0

                for day in new_users:
                    total_new += day['new_users']
                    reg_table.add_row([
                        day['reg_date'],
                        str(day['new_users'])
                    ])

                reg_table.display()
                print(f"\n🎯 Total new users in last 90 days: {total_new}")
            else:
                print("\n📅 New Registrations (Last 90 days):")
                print("No new registrations found in the last 90 days.")

        except Exception as e:
            print(f"❌ Error generating user analytics: {e}")

        self._pause()

    def _revenue_reports_interactive(self):
        """Revenue reports."""
        print("\n💰 REVENUE REPORTS")
        print("="*40)

        # Get reporting options
        print("Report options:")
        print("1. Monthly revenue summary")
        print("2. Revenue by user plan")
        print("3. Payment status breakdown")
        print("4. Revenue trend analysis")
        print("0. Back to reports menu")

        choice = input("\nSelect option (0-4): ").strip()

        if choice == '0':
            return

        try:
            if choice == '1':
                # Monthly revenue summary
                monthly_query = """
                    SELECT
                        strftime('%Y-%m', created_at) as month,
                        COUNT(*) as bill_count,
                        SUM(CAST(total_cost AS FLOAT)) as total_revenue,
                        SUM(CASE WHEN success = 1 THEN CAST(total_cost AS FLOAT) ELSE 0 END) as paid_revenue,
                        SUM(CASE WHEN success = 0 THEN CAST(total_cost AS FLOAT) ELSE 0 END) as pending_revenue
                    FROM usage_logs
                    WHERE created_at >= datetime('now', '-12 months')
                    GROUP BY strftime('%Y-%m', created_at)
                    ORDER BY month DESC
                """
                monthly_data = self._execute_query(monthly_query)

                if monthly_data:
                    print("\n📅 Monthly Revenue Summary (Last 12 months):")
                    print()

                    monthly_table = InteractiveTable(['Month', 'Bills', 'Total Revenue', 'Paid', 'Pending'])
                    total_revenue = 0
                    total_paid = 0

                    for month in monthly_data:
                        total_revenue += month['total_revenue']
                        total_paid += month['paid_revenue']

                        monthly_table.add_row([
                            month['month'],
                            str(month['bill_count']),
                            f"${month['total_revenue']:.2f}",
                            f"${month['paid_revenue']:.2f}",
                            f"${month['pending_revenue']:.2f}"
                        ])

                    monthly_table.display()
                    print(f"\n💎 Total revenue (12 months): ${total_revenue:.2f}")
                    print(f"💰 Total paid: ${total_paid:.2f}")
                    print(f"⏳ Collection rate: {(total_paid/total_revenue*100):.1f}%" if total_revenue > 0 else "⏳ Collection rate: N/A")
                else:
                    print("\n📅 Monthly Revenue Summary (Last 12 months):")
                    print("No usage data found in the last 12 months.")

            elif choice == '2':
                # Revenue by user plan
                plan_revenue_query = """
                    SELECT
                        UPPER(u.current_plan) as current_plan,
                        COUNT(DISTINCT u.id) as user_count,
                        COUNT(ul.id) as bill_count,
                        SUM(CAST(ul.total_cost AS FLOAT)) as total_revenue,
                        AVG(CAST(ul.total_cost AS FLOAT)) as avg_bill_amount
                    FROM users u
                    LEFT JOIN usage_logs ul ON u.id = ul.user_id
                    GROUP BY UPPER(u.current_plan)
                    ORDER BY total_revenue DESC
                """
                plan_revenue = self._execute_query(plan_revenue_query)

                if plan_revenue:
                    print("\n📊 Revenue by User Plan:")
                    print()

                    plan_table = InteractiveTable(['Plan', 'Users', 'Bills', 'Total Revenue', 'Avg Bill'])

                    for plan in plan_revenue:
                        revenue = plan['total_revenue'] or 0
                        avg_bill = plan['avg_bill_amount'] or 0

                        plan_table.add_row([
                            plan['current_plan'],
                            str(plan['user_count']),
                            str(plan['bill_count'] or 0),
                            f"${revenue:.2f}",
                            f"${avg_bill:.2f}"
                        ])

                    plan_table.display()
                else:
                    print("\n📊 Revenue by User Plan:")
                    print("No usage data found for revenue analysis by user plan.")

            elif choice == '3':
                # Payment status breakdown
                status_query = """
                    SELECT
                        CASE WHEN success = 1 THEN 'paid' ELSE 'pending' END as status,
                        COUNT(*) as bill_count,
                        SUM(CAST(total_cost AS FLOAT)) as total_amount,
                        AVG(CAST(total_cost AS FLOAT)) as avg_amount,
                        MIN(created_at) as earliest,
                        MAX(created_at) as latest
                    FROM usage_logs
                    GROUP BY success
                    ORDER BY total_amount DESC
                """
                status_data = self._execute_query(status_query)

                if status_data:
                    print("\n📈 Payment Status Breakdown:")
                    print()

                    status_table = InteractiveTable(['Status', 'Count', 'Total Amount', 'Avg Amount', 'Date Range'])

                    for status in status_data:
                        date_range = f"{status['earliest'][:10]} to {status['latest'][:10]}"
                        status_table.add_row([
                            status['status'].upper(),
                            str(status['bill_count']),
                            f"${status['total_amount']:.2f}",
                            f"${status['avg_amount']:.2f}",
                            date_range
                        ])

                    status_table.display()
                else:
                    print("\n📈 Payment Status Breakdown:")
                    print("No usage data found for payment status analysis.")

            elif choice == '4':
                # Revenue trend analysis
                trend_query = """
                    SELECT
                        DATE(created_at) as bill_date,
                        COUNT(*) as daily_bills,
                        SUM(CAST(total_cost AS FLOAT)) as daily_revenue
                    FROM usage_logs
                    WHERE created_at >= datetime('now', '-30 days')
                    GROUP BY DATE(created_at)
                    ORDER BY bill_date DESC
                    LIMIT 15
                """
                trend_data = self._execute_query(trend_query)

                if trend_data:
                    print("\n📈 Daily Revenue Trend (Last 15 days):")
                    print()

                    trend_table = InteractiveTable(['Date', 'Bills', 'Revenue'])
                    total_revenue = 0

                    for day in trend_data:
                        total_revenue += day['daily_revenue']
                        trend_table.add_row([
                            day['bill_date'],
                            str(day['daily_bills']),
                            f"${day['daily_revenue']:.2f}"
                        ])

                    trend_table.display()
                    avg_daily = total_revenue / len(trend_data) if trend_data else 0
                    print(f"\n📊 Average daily revenue: ${avg_daily:.2f}")
                else:
                    print("\n📈 Daily Revenue Trend (Last 15 days):")
                    print("No usage data found in the last 30 days for trend analysis.")

        except Exception as e:
            print(f"❌ Error generating revenue reports: {e}")

        self._pause()

    def _system_health_interactive(self):
        """System health check."""
        print("\n🔧 SYSTEM HEALTH CHECK")
        print("="*40)

        try:
            health_data = []

            # Check database connectivity
            try:
                test_query = "SELECT COUNT(*) as count FROM users"
                result = self._execute_query(test_query)
                health_data.append(("Database Connection", "✅ Connected", f"{result[0]['count']} users"))
            except Exception as e:
                health_data.append(("Database Connection", "❌ Failed", str(e)))

            # Check tables existence
            tables = ['users', 'api_keys', 'usage_logs', 'bills', 'subscriptions']
            missing_tables = []

            for table in tables:
                try:
                    self._execute_query(f"SELECT COUNT(*) FROM {table}")
                except:
                    missing_tables.append(table)

            if missing_tables:
                health_data.append(("Database Schema", "⚠️ Issues", f"Missing: {', '.join(missing_tables)}"))
            else:
                health_data.append(("Database Schema", "✅ Complete", "All tables present"))

            # Check user statistics
            try:
                user_stats = self._execute_query("""
                    SELECT
                        COUNT(*) as total_users,
                        SUM(CASE WHEN is_active = 1 THEN 1 ELSE 0 END) as active_users,
                        COUNT(DISTINCT current_plan) as plan_types
                    FROM users
                """)
                stats = user_stats[0]
                health_data.append(("User Base", "📊 Info", f"{stats['active_users']}/{stats['total_users']} active, {stats['plan_types']} plans"))
            except Exception as e:
                health_data.append(("User Base", "❌ Error", str(e)))

            # Check API key usage
            try:
                api_stats = self._execute_query("""
                    SELECT
                        COUNT(*) as total_keys,
                        SUM(CASE WHEN is_active = 1 THEN 1 ELSE 0 END) as active_keys,
                        SUM(total_requests) as total_usage
                    FROM api_keys
                """)
                api_info = api_stats[0]
                health_data.append(("API Keys", "🔑 Info", f"{api_info['active_keys']}/{api_info['total_keys']} active, {api_info['total_usage']} total uses"))
            except Exception as e:
                health_data.append(("API Keys", "❌ Error", str(e)))

            # Check recent activity
            try:
                recent_activity = self._execute_query("""
                    SELECT COUNT(*) as recent_jobs
                    FROM usage_logs
                    WHERE created_at >= datetime('now', '-24 hours')
                """)
                recent_count = recent_activity[0]['recent_jobs']
                status = "✅ Active" if recent_count > 0 else "⚠️ Quiet"
                health_data.append(("Recent Activity", status, f"{recent_count} jobs in last 24h"))
            except Exception as e:
                health_data.append(("Recent Activity", "❌ Error", str(e)))

            # Check quantum job performance from usage logs
            try:
                performance_stats = self._execute_query("""
                    SELECT
                        COUNT(*) as total_jobs,
                        SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) as successful_jobs,
                        COUNT(CASE WHEN created_at >= datetime('now', '-7 days') THEN 1 END) as weekly_jobs,
                        AVG(execution_time) as avg_execution_time
                    FROM usage_logs
                """)
                perf = performance_stats[0]
                if perf['total_jobs'] > 0:
                    success_rate = (perf['successful_jobs'] / perf['total_jobs'] * 100)
                    if success_rate >= 95:
                        status = "✅ Excellent"
                    elif success_rate >= 80:
                        status = "⚠️ Good"
                    else:
                        status = "❌ Poor"
                    avg_time = perf['avg_execution_time'] or 0
                    health_data.append(("Job Performance", status, f"{success_rate:.1f}% success, {avg_time:.2f}s avg time"))
                else:
                    health_data.append(("Job Performance", "⚠️ No Data", "No jobs executed yet"))
            except Exception as e:
                health_data.append(("Job Performance", "❌ Error", str(e)))

            # Check billing health
            try:
                billing_stats = self._execute_query("""
                    SELECT
                        COUNT(*) as total_bills,
                        COALESCE(SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END), 0) as pending_bills,
                        COALESCE(SUM(CASE WHEN status = 'pending' THEN CAST(total_amount AS REAL) ELSE 0 END), 0.0) as pending_amount
                    FROM bills
                """)
                billing = billing_stats[0]
                if billing['pending_bills'] and billing['pending_bills'] > 0:
                    status = "⚠️ Pending"
                    detail = f"{billing['pending_bills']} bills, ${billing['pending_amount']:.2f}"
                else:
                    status = "✅ Current"
                    detail = "No pending bills"
                health_data.append(("Billing Status", status, detail))
            except Exception as e:
                health_data.append(("Billing Status", "❌ Error", str(e)))

            # Display health report
            print("\n🏥 System Health Report:")
            print()

            health_table = InteractiveTable(['Component', 'Status', 'Details'])
            for component, status, details in health_data:
                health_table.add_row([component, status, details])

            health_table.display()

            # Overall health assessment
            error_count = sum(1 for _, status, _ in health_data if "❌" in status)
            warning_count = sum(1 for _, status, _ in health_data if "⚠️" in status)

            print(f"\n🎯 Overall Status:")
            if error_count == 0 and warning_count == 0:
                print("✅ System is healthy")
            elif error_count == 0:
                print(f"⚠️ System operational with {warning_count} warnings")
            else:
                print(f"❌ System has {error_count} errors and {warning_count} warnings")

        except Exception as e:
            print(f"❌ Error performing health check: {e}")

        self._pause()

    def _sql_query_interactive(self):
        """Interactive SQL query."""
        print("\n🗃️ INTERACTIVE SQL QUERY")
        print("="*40)
        print("⚠️ Only SELECT queries are allowed for security")
        print()

        while True:
            print("Options:")
            print("1. Execute custom SQL query")
            print("2. Predefined queries")
            print("0. Back to system tools")

            choice = input("\nSelect option (0-2): ").strip()

            if choice == '0':
                break

            elif choice == '1':
                # Custom SQL query
                print("\n📝 Enter your SQL query (SELECT only):")
                print("Example: SELECT COUNT(*) FROM users WHERE is_active = 1")

                query = input("\nSQL> ").strip()

                if not query:
                    print("❌ Query cannot be empty")
                    continue

                # Security check - only allow SELECT queries
                if not query.upper().strip().startswith('SELECT'):
                    print("❌ Only SELECT queries are allowed")
                    continue

                try:
                    results = self._execute_query(query)

                    if not results:
                        print("📭 Query returned no results")
                    else:
                        print(f"\n📊 Query Results ({len(results)} rows):")
                        print()

                        # Get column names from first row
                        if results:
                            columns = list(results[0].keys())
                            table = InteractiveTable(columns)

                            # Limit to first 50 rows to avoid overwhelming output
                            display_results = results[:50]

                            for row in display_results:
                                table.add_row([str(row[col]) for col in columns])

                            table.display()

                            if len(results) > 50:
                                print(f"\n⚠️ Showing first 50 of {len(results)} results")

                except Exception as e:
                    print(f"❌ Query error: {e}")

            elif choice == '2':
                # Predefined queries
                self._show_predefined_queries()

            self._pause()

    def _show_predefined_queries(self):
        """Show predefined SQL queries."""
        print("\n📋 PREDEFINED QUERIES")
        print("="*30)

        queries = [
            ("User counts by plan", "SELECT current_plan, COUNT(*) as count FROM users GROUP BY current_plan"),
            ("Active API keys", "SELECT COUNT(*) as active_keys FROM api_keys WHERE is_active = 1"),
            ("Recent usage (24h)", "SELECT COUNT(*) as recent_jobs FROM usage_logs WHERE created_at >= datetime('now', '-24 hours')"),
            ("Billing summary", "SELECT status, COUNT(*) as count, SUM(total_amount) as total FROM bills GROUP BY status"),
            ("Top users by usage", "SELECT u.email, COUNT(ul.id) as jobs FROM users u LEFT JOIN usage_logs ul ON u.id = ul.user_id GROUP BY u.id ORDER BY jobs DESC LIMIT 10"),
            ("Monthly registrations", "SELECT strftime('%Y-%m', created_at) as month, COUNT(*) as new_users FROM users GROUP BY month ORDER BY month DESC LIMIT 6"),
        ]

        for i, (name, query) in enumerate(queries, 1):
            print(f"{i}. {name}")

        print("0. Back")

        choice = input("\nSelect query (0-{}): ".format(len(queries))).strip()

        if choice == '0':
            return

        try:
            query_idx = int(choice) - 1
            if 0 <= query_idx < len(queries):
                name, query = queries[query_idx]
                print(f"\n🔍 Executing: {name}")
                print(f"SQL: {query}")
                print()

                results = self._execute_query(query)

                if not results:
                    print("📭 Query returned no results")
                else:
                    print(f"📊 Results ({len(results)} rows):")
                    print()

                    columns = list(results[0].keys())
                    table = InteractiveTable(columns)

                    for row in results:
                        table.add_row([str(row[col]) for col in columns])

                    table.display()
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Invalid selection")

    def _maintenance_tools_interactive(self):
        """Maintenance tools."""
        print("\n🧹 MAINTENANCE TOOLS")
        print("="*40)

        print("Available maintenance tools:")
        print("1. Create database backup")
        print("2. Cleanup old logs (>90 days)")
        print("3. Verify database integrity")
        print("4. Update user statistics")
        print("0. Back to system tools")

        choice = input("\nSelect tool (0-4): ").strip()

        if choice == '0':
            return

        elif choice == '1':
            self._create_backup_interactive()

        elif choice == '2':
            self._cleanup_old_logs()

        elif choice == '3':
            self._verify_db_integrity()

        elif choice == '4':
            self._update_user_stats()

        else:
            print("❌ Invalid selection")
            self._pause()

    def _create_backup_interactive(self):
        """Create database backup."""
        print("\n💾 CREATING DATABASE BACKUP")
        print("="*40)

        from datetime import datetime
        import shutil
        import os

        try:
            # Generate backup filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = input(f"\nBackup name (default: bioql_backup_{timestamp}.db): ").strip()
            if not backup_name:
                backup_name = f"bioql_backup_{timestamp}.db"

            if not backup_name.endswith('.db'):
                backup_name += '.db'

            # Create backup
            source_db = self.db_path
            backup_path = backup_name

            print(f"\n🔄 Creating backup...")
            print(f"Source: {source_db}")
            print(f"Backup: {backup_path}")

            shutil.copy2(source_db, backup_path)

            # Verify backup
            if os.path.exists(backup_path):
                backup_size = os.path.getsize(backup_path)
                original_size = os.path.getsize(source_db)

                print(f"\n✅ Backup created successfully!")
                print(f"📊 Original size: {original_size:,} bytes")
                print(f"📊 Backup size: {backup_size:,} bytes")
                print(f"📁 Backup location: {os.path.abspath(backup_path)}")

                if backup_size == original_size:
                    print("✅ Backup verification: PASSED")
                else:
                    print("⚠️ Backup verification: Size mismatch")
            else:
                print("❌ Backup creation failed")

        except Exception as e:
            print(f"❌ Error creating backup: {e}")

        self._pause()

    def _cleanup_old_logs(self):
        """Cleanup old usage logs."""
        print("\n🧹 CLEANUP OLD LOGS")
        print("="*40)

        try:
            # Check how many old logs exist
            old_logs_query = """
                SELECT COUNT(*) as old_count
                FROM usage_logs
                WHERE created_at < datetime('now', '-90 days')
            """
            old_count = self._execute_query(old_logs_query)[0]['old_count']

            if old_count == 0:
                print("✅ No old logs to cleanup (older than 90 days)")
                self._pause()
                return

            print(f"📋 Found {old_count} logs older than 90 days")
            confirm = input(f"\nDelete these {old_count} old logs? (y/N): ").strip().lower()

            if confirm == 'y':
                # Delete old logs
                delete_query = "DELETE FROM usage_logs WHERE created_at < datetime('now', '-90 days')"
                self._execute_query(delete_query, fetch=False)

                print(f"✅ Deleted {old_count} old logs")
                print("🧹 Database cleanup completed")
            else:
                print("🚫 Cleanup cancelled")

        except Exception as e:
            print(f"❌ Error during cleanup: {e}")

        self._pause()

    def _verify_db_integrity(self):
        """Verify database integrity."""
        print("\n🔍 DATABASE INTEGRITY CHECK")
        print("="*40)

        try:
            # Run SQLite integrity check
            integrity_result = self._execute_query("PRAGMA integrity_check")

            if integrity_result and integrity_result[0].get('integrity_check') == 'ok':
                print("✅ Database integrity: PASSED")
            else:
                print("❌ Database integrity: FAILED")
                if integrity_result:
                    print(f"Error: {integrity_result[0]}")

            # Check for orphaned records
            orphan_checks = [
                ("API keys without users", "SELECT COUNT(*) as count FROM api_keys WHERE user_id NOT IN (SELECT id FROM users)"),
                ("Usage logs without users", "SELECT COUNT(*) as count FROM usage_logs WHERE user_id NOT IN (SELECT id FROM users)"),
                ("Bills without users", "SELECT COUNT(*) as count FROM bills WHERE user_id NOT IN (SELECT id FROM users)"),
            ]

            print("\n🔍 Checking for orphaned records:")
            for check_name, query in orphan_checks:
                try:
                    result = self._execute_query(query)
                    count = result[0]['count']
                    if count > 0:
                        print(f"⚠️ {check_name}: {count} orphaned records")
                    else:
                        print(f"✅ {check_name}: No orphaned records")
                except Exception as e:
                    print(f"❌ {check_name}: Error checking - {e}")

        except Exception as e:
            print(f"❌ Error during integrity check: {e}")

        self._pause()

    def _update_user_stats(self):
        """Update user statistics."""
        print("\n📈 UPDATE USER STATISTICS")
        print("="*40)

        try:
            # This would typically update computed fields in the user table
            # For now, just show what would be updated
            stats_query = """
                SELECT
                    u.id,
                    u.email,
                    COUNT(ul.id) as job_count,
                    COALESCE(SUM(ul.total_cost), 0) as total_spent
                FROM users u
                LEFT JOIN usage_logs ul ON u.id = ul.user_id
                GROUP BY u.id, u.email
                ORDER BY total_spent DESC
                LIMIT 10
            """
            user_stats = self._execute_query(stats_query)

            print("📈 Current user statistics (top 10 by spending):")
            print()

            table = InteractiveTable(['Email', 'Jobs', 'Total Spent'])
            for user in user_stats:
                table.add_row([
                    user['email'],
                    str(user['job_count']),
                    f"${user['total_spent']:.2f}"
                ])

            table.display()

            print("\n✅ User statistics refreshed")
            print("📊 Note: In a production system, this would update computed fields")

        except Exception as e:
            print(f"❌ Error updating user statistics: {e}")

        self._pause()

    def _quick_billing_check(self):
        """Quick billing check."""
        print("\n💰 QUICK BILLING CHECK")
        print("="*40)

        try:
            # Get billing overview
            overview_query = """
                SELECT
                    status,
                    COUNT(*) as count,
                    SUM(total_amount) as total_amount
                FROM bills
                GROUP BY status
            """
            overview = self._execute_query(overview_query)

            if not overview:
                print("📭 No billing data found")
                self._pause()
                return

            print("📊 Billing Overview:")
            print()

            table = InteractiveTable(['Status', 'Count', 'Total Amount'])
            grand_total = 0

            for item in overview:
                grand_total += item['total_amount']
                table.add_row([
                    item['status'].upper(),
                    str(item['count']),
                    f"${item['total_amount']:.2f}"
                ])

            table.display()
            print(f"\n💰 Grand Total: ${grand_total:.2f}")

            # Check for overdue bills
            overdue_query = """
                SELECT COUNT(*) as overdue_count, SUM(total_amount) as overdue_amount
                FROM bills
                WHERE status = 'pending' AND billing_period_end < datetime('now')
            """
            overdue = self._execute_query(overdue_query)[0]

            if overdue['overdue_count'] > 0:
                print(f"\n⚠️ Overdue bills: {overdue['overdue_count']} (${overdue['overdue_amount']:.2f})")
            else:
                print("\n✅ No overdue bills")

            # Recent billing activity
            recent_query = """
                SELECT COUNT(*) as recent_bills
                FROM bills
                WHERE created_at >= datetime('now', '-7 days')
            """
            recent = self._execute_query(recent_query)[0]
            print(f"🕒 Recent activity: {recent['recent_bills']} bills in last 7 days")

        except Exception as e:
            print(f"❌ Error checking billing: {e}")

        self._pause()

    def _deactivate_user_interactive(self):
        """Interactive user deactivation."""
        print("\n❌ USER DEACTIVATION")
        print("="*40)
        print("⚠️ This will deactivate the user and all their API keys")
        print()

        email = input("Enter user email to deactivate: ").strip()
        if not email:
            print("❌ Email is required")
            self._pause()
            return

        try:
            # Find user
            user_query = "SELECT * FROM users WHERE email = ?"
            users = self._execute_query(user_query, (email,))

            if not users:
                print(f"❌ User not found: {email}")
                self._pause()
                return

            user = users[0]

            if user['is_active'] == 0:
                print(f"⚠️ User {email} is already inactive")
                self._pause()
                return

            # Show user details
            print(f"\n👤 User Details:")
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Organization: {user['organization']}")
            print(f"Plan: {user['current_plan']}")
            print(f"Created: {user['created_at'][:10]}")

            # Get user's API keys
            api_keys = self._execute_query("SELECT COUNT(*) as count FROM api_keys WHERE user_id = ? AND is_active = 1", (user['id'],))
            active_keys = api_keys[0]['count']

            print(f"Active API keys: {active_keys}")

            # Confirm deactivation
            print(f"\n⚠️ This will:")
            print(f"- Deactivate user account")
            print(f"- Deactivate {active_keys} API keys")
            print(f"- Prevent future usage")
            print(f"- Preserve billing and usage history")

            confirm = input(f"\nDeactivate user {email}? (type 'DEACTIVATE' to confirm): ").strip()

            if confirm == 'DEACTIVATE':
                # Deactivate user
                from datetime import datetime
                now = datetime.utcnow().isoformat()

                # Update user
                user_update = "UPDATE users SET is_active = 0, updated_at = ? WHERE id = ?"
                self._execute_query(user_update, (now, user['id']), fetch=False)

                # Deactivate API keys
                keys_update = "UPDATE api_keys SET is_active = 0, updated_at = ? WHERE user_id = ?"
                self._execute_query(keys_update, (now, user['id']), fetch=False)

                print(f"\n✅ USER DEACTIVATED SUCCESSFULLY")
                print(f"👤 User: {email}")
                print(f"🔑 API keys deactivated: {active_keys}")
                print(f"🕒 Timestamp: {now}")
            else:
                print("🚫 Deactivation cancelled")

        except Exception as e:
            print(f"❌ Error deactivating user: {e}")

        self._pause()

    def _quick_user_lookup(self):
        """Quick user lookup."""
        print("\n🎯 QUICK USER LOOKUP")
        print("="*40)

        email = input("Enter user email: ").strip()
        if not email:
            print("❌ Email is required")
            self._pause()
            return

        try:
            # Get user details with related data
            user_query = """
                SELECT u.*,
                       COUNT(DISTINCT ak.id) as api_key_count,
                       COUNT(DISTINCT ul.id) as usage_count,
                       COALESCE(SUM(ul.total_cost), 0) as total_spent,
                       COUNT(DISTINCT b.id) as bill_count,
                       MAX(ul.created_at) as last_activity
                FROM users u
                LEFT JOIN api_keys ak ON u.id = ak.user_id AND ak.is_active = 1
                LEFT JOIN usage_logs ul ON u.id = ul.user_id
                LEFT JOIN bills b ON u.id = b.user_id
                WHERE u.email = ?
                GROUP BY u.id
            """
            users = self._execute_query(user_query, (email,))

            if not users:
                print(f"❌ User not found: {email}")
                self._pause()
                return

            user = users[0]

            # Display user information
            print(f"\n👤 USER PROFILE")
            print("="*30)
            print(f"Email: {user['email']}")
            print(f"Name: {user['name']}")
            print(f"Organization: {user['organization']}")
            print(f"Plan: {user['current_plan'].upper()}")
            status_text = "✅ Active" if user['is_active'] else "❌ Inactive"
            print(f"Status: {status_text}")
            print(f"Created: {user['created_at'][:19]}")

            print(f"\n📈 ACTIVITY SUMMARY")
            print("="*30)
            print(f"API Keys: {user['api_key_count']}")
            print(f"Total Jobs: {user['usage_count']}")
            print(f"Total Spent: ${user['total_spent']:.2f}")
            print(f"Bills Generated: {user['bill_count']}")

            if user['last_activity']:
                print(f"Last Activity: {user['last_activity'][:19]}")
            else:
                print("Last Activity: Never")

            # Get recent activity
            recent_query = """
                SELECT algorithm_type, shots_executed, total_cost, created_at
                FROM usage_logs
                WHERE user_id = ?
                ORDER BY created_at DESC
                LIMIT 5
            """
            recent_activity = self._execute_query(recent_query, (user['id'],))

            if recent_activity:
                print(f"\n🕒 RECENT ACTIVITY (Last 5 jobs)")
                print("="*30)

                activity_table = InteractiveTable(['Algorithm', 'Shots', 'Cost', 'Date'])
                for activity in recent_activity:
                    activity_table.add_row([
                        activity['algorithm_type'],
                        str(activity['shots_executed']),
                        f"${float(activity['total_cost']) if activity['total_cost'] else 0:.2f}",
                        activity['created_at'][:19]
                    ])

                activity_table.display()

            # Show quick actions
            print(f"\n🎯 QUICK ACTIONS")
            print("1. View full user details")
            print("2. View billing history")
            print("3. Create new API key")
            print("0. Back to menu")

            action = input("\nSelect action (0-3): ").strip()

            if action == '1':
                # Redirect to full user details
                self._user_details_by_email(email)
            elif action == '2':
                # Show billing for this user
                self._show_user_billing(email)
            elif action == '3':
                # Create API key
                self._create_api_key_for_user(email)

        except Exception as e:
            print(f"❌ Error looking up user: {e}")

        self._pause()

    def _show_user_billing(self, email):
        """Show billing summary for a user."""
        try:
            bills_query = """
                SELECT b.*, u.email
                FROM bills b
                JOIN users u ON b.user_id = u.id
                WHERE u.email = ?
                ORDER BY b.created_at DESC
                LIMIT 10
            """
            bills = self._execute_query(bills_query, (email,))

            if bills:
                print(f"\n📋 BILLING HISTORY: {email}")
                print("="*40)

                table = InteractiveTable(['ID', 'Amount', 'Status', 'Period', 'Created'])
                for bill in bills:
                    table.add_row([
                        bill['id'][:8] + '...',
                        f"${bill['total_amount']:.2f}",
                        bill['status'].upper(),
                        f"{bill['billing_period_start'][:10]} to {bill['billing_period_end'][:10]}",
                        bill['created_at'][:10]
                    ])

                table.display()
            else:
                print(f"\n📭 No billing history found for {email}")
        except Exception as e:
            print(f"❌ Error retrieving billing: {e}")

    def _create_api_key_for_user(self, email):
        """Create a new API key for a user."""
        try:
            # Get user ID
            user_query = "SELECT id FROM users WHERE email = ?"
            users = self._execute_query(user_query, (email,))

            if not users:
                print(f"❌ User not found: {email}")
                return

            user_id = users[0]['id']
            key_name = input("Enter API key name (e.g., 'Production Key'): ").strip()
            if not key_name:
                key_name = "Additional API Key"

            # Generate API key
            import uuid
            import secrets
            import hashlib
            from datetime import datetime

            api_key = f"bioql_{secrets.token_urlsafe(32)}"
            api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()
            api_key_id = str(uuid.uuid4())
            now = datetime.utcnow().isoformat()

            # Insert API key
            api_key_query = """
                INSERT INTO api_keys (id, user_id, key_name, key_hash, key_prefix, is_active, total_requests, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, 1, 0, ?, ?)
            """
            key_prefix = api_key[:12]  # First 12 characters as prefix
            self._execute_query(api_key_query, (api_key_id, user_id, key_name, api_key_hash, key_prefix, now, now), fetch=False)

            print(f"\n✅ API KEY CREATED SUCCESSFULLY")
            print("="*40)
            print(f"User: {email}")
            print(f"Key Name: {key_name}")
            print(f"API Key: {api_key}")
            print("\n⚠️ SAVE THE API KEY - IT WON'T BE SHOWN AGAIN!")

        except Exception as e:
            print(f"❌ Error creating API key: {e}")

    def _user_details_by_email(self, email):
        """Show full user details by email."""
        # This would redirect to the existing user details function
        # For now, just show a message
        print(f"\nℹ️ Redirecting to full user details for {email}...")
        print("(This would show the complete user profile with all details)")

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="BioQL Admin CLI - Interactive Mode")
    parser.add_argument("--db", help="Database file path", default="bioql_billing.db")

    args = parser.parse_args()

    try:
        cli = BioQLInteractiveCLI(database_path=args.db)
        cli.cmdloop()
    except KeyboardInterrupt:
        print("\n👋 ¡Hasta la vista!")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()