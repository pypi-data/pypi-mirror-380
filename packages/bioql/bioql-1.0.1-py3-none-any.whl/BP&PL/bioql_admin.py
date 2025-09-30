#!/usr/bin/env python3
"""
BioQL Admin CLI - Interactive Administration Tool

This CLI tool provides a comprehensive interface for managing the BioQL
billing and payment system. It allows administrators to manage users,
subscriptions, billing, quotas, and generate reports.

Usage:
    python bioql_admin.py
    python bioql_admin.py --db-url sqlite:///bioql_billing.db
    python bioql_admin.py --config /path/to/config.json
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from decimal import Decimal
import cmd
import shlex
from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Database imports
try:
    from sqlalchemy import create_engine, func
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.exc import SQLAlchemyError

    # Import all models with absolute imports
    import models.user as user_models
    import models.subscription as subscription_models
    import models.billing as billing_models
    import models.usage as usage_models
    import models.quota as quota_models

    # Import services
    import services.billing_engine as billing_engine_module
    import services.usage_tracker as usage_tracker_module
    import services.quota_manager as quota_manager_module

    # Extract specific classes
    User = user_models.User
    APIKey = user_models.APIKey
    UserPlanEnum = user_models.UserPlanEnum

    Plan = subscription_models.Plan
    Subscription = subscription_models.Subscription
    PlanFeature = subscription_models.PlanFeature
    PlanTypeEnum = subscription_models.PlanTypeEnum
    SubscriptionStatusEnum = subscription_models.SubscriptionStatusEnum
    BillingIntervalEnum = subscription_models.BillingIntervalEnum

    Bill = billing_models.Bill
    BillItem = billing_models.BillItem
    Payment = billing_models.Payment
    PaymentMethod = billing_models.PaymentMethod
    BillStatusEnum = billing_models.BillStatusEnum
    PaymentStatusEnum = billing_models.PaymentStatusEnum

    UsageLog = usage_models.UsageLog
    UsageSession = usage_models.UsageSession
    QuantumJob = usage_models.QuantumJob
    AlgorithmTypeEnum = usage_models.AlgorithmTypeEnum
    BackendTypeEnum = usage_models.BackendTypeEnum

    Quota = quota_models.Quota
    QuotaUsage = quota_models.QuotaUsage
    QuotaTypeEnum = quota_models.QuotaTypeEnum

    BillingEngine = billing_engine_module.BillingEngine
    UsageTracker = usage_tracker_module.UsageTracker
    QuotaManager = quota_manager_module.QuotaManager

    DB_AVAILABLE = True
except ImportError as e:
    print(f"❌ Database components not available: {e}")
    print("Please ensure all dependencies are installed and the BP&PL models are accessible.")
    print(f"Current directory: {current_dir}")
    print(f"Python path: {sys.path[:3]}")
    sys.exit(1)

# Setup logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class BioQLAdminCLI(cmd.Cmd):
    """Interactive CLI for BioQL administration."""

    intro = """
🧬 BioQL Administration Console
==============================
Welcome to the BioQL billing and user management system.
Type 'help' or '?' to list commands.
Type 'help <command>' for detailed command information.
"""

    prompt = "bioql-admin> "

    def __init__(self, database_url: str = None, config: Dict[str, Any] = None):
        super().__init__()
        self.console = Console()
        self.database_url = database_url or "sqlite:///bioql_billing.db"
        self.config = config or {}
        self.session = None
        self.billing_engine = None
        self.usage_tracker = None
        self.quota_manager = None

        # Initialize database connection
        self._connect_database()

        # Display startup info
        self._show_startup_info()

    def _connect_database(self):
        """Connect to the database and initialize services."""
        try:
            self.engine = create_engine(self.database_url)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()

            # Test connection
            self.session.execute("SELECT 1")

            # Initialize services
            pricing_config = self._get_pricing_config()
            self.billing_engine = BillingEngine(self.session, pricing_config)
            self.usage_tracker = UsageTracker(self.session, pricing_config)
            self.quota_manager = QuotaManager(self.session)

            self.console.print("✅ Database connection established", style="green")

        except SQLAlchemyError as e:
            self.console.print(f"❌ Database connection failed: {e}", style="red")
            sys.exit(1)

    def _get_pricing_config(self) -> Dict[str, Any]:
        """Get pricing configuration."""
        return {
            'simulator_cost_per_shot': '0.001',
            'hardware_cost_per_shot': '0.01',
            'algorithm_multipliers': {
                'basic': 1.0,
                'vqe': 3.0,
                'grover': 3.0,
                'shor': 3.0,
                'qaoa': 2.0,
                'custom': 1.5
            },
            'complexity_multipliers': {
                'base_qubit_cost': 0.1,
                'depth_multiplier': 0.05
            }
        }

    def _show_startup_info(self):
        """Display startup information."""
        # Get database stats
        try:
            user_count = self.session.query(User).count()
            active_subs = self.session.query(Subscription).filter_by(status=SubscriptionStatusEnum.ACTIVE).count()
            total_usage = self.session.query(UsageLog).count()
            pending_bills = self.session.query(Bill).filter_by(status=BillStatusEnum.PENDING).count()

            info_panel = Panel(
                f"Database: {self.database_url}\n"
                f"Users: {user_count} | Active Subscriptions: {active_subs}\n"
                f"Usage Logs: {total_usage} | Pending Bills: {pending_bills}",
                title="System Status",
                border_style="blue"
            )
            self.console.print(info_panel)

        except Exception as e:
            self.console.print(f"⚠️  Could not load system stats: {e}", style="yellow")

    # === USER MANAGEMENT COMMANDS ===

    def do_list_users(self, args):
        """List all users in the system.

        Usage: list_users [--plan PLAN] [--status STATUS] [--limit N]

        Options:
            --plan PLAN     Filter by plan type (free, basic, pro, enterprise)
            --status STATUS Filter by status (active, inactive)
            --limit N       Limit results to N users
        """
        try:
            # Parse arguments
            parsed_args = self._parse_args(args, [
                ('--plan', str),
                ('--status', str),
                ('--limit', int)
            ])

            query = self.session.query(User)

            # Apply filters
            if parsed_args.get('plan'):
                plan_enum = UserPlanEnum[parsed_args['plan'].upper()]
                query = query.filter(User.current_plan == plan_enum)

            if parsed_args.get('status') == 'active':
                query = query.filter(User.is_active == True)
            elif parsed_args.get('status') == 'inactive':
                query = query.filter(User.is_active == False)

            if parsed_args.get('limit'):
                query = query.limit(parsed_args['limit'])

            users = query.all()

            if not users:
                self.console.print("No users found.", style="yellow")
                return

            # Create table
            table = Table(title="BioQL Users")
            table.add_column("ID", style="cyan")
            table.add_column("Email", style="green")
            table.add_column("Name", style="white")
            table.add_column("Organization", style="blue")
            table.add_column("Plan", style="magenta")
            table.add_column("Status", style="yellow")
            table.add_column("Created", style="dim")

            for user in users:
                status = "🟢 Active" if user.is_active else "🔴 Inactive"
                table.add_row(
                    user.id[:8],
                    user.email,
                    user.name or "-",
                    user.organization or "-",
                    user.current_plan.value,
                    status,
                    user.created_at.strftime("%Y-%m-%d")
                )

            self.console.print(table)

        except Exception as e:
            self.console.print(f"❌ Error listing users: {e}", style="red")

    def do_create_user(self, args):
        """Create a new user.

        Usage: create_user <email> <name> <organization> [--plan PLAN]

        Arguments:
            email        User's email address
            name         User's full name
            organization User's organization

        Options:
            --plan PLAN  Initial plan (free, basic, pro, enterprise) [default: free]
        """
        try:
            # Parse arguments
            parts = shlex.split(args)
            if len(parts) < 3:
                self.console.print("❌ Usage: create_user <email> <name> <organization> [--plan PLAN]", style="red")
                return

            email, name, organization = parts[0], parts[1], parts[2]

            # Parse plan option
            plan = UserPlanEnum.FREE
            if '--plan' in parts:
                plan_idx = parts.index('--plan')
                if plan_idx + 1 < len(parts):
                    plan_str = parts[plan_idx + 1].upper()
                    plan = UserPlanEnum[plan_str]

            # Check if user already exists
            existing = self.session.query(User).filter_by(email=email).first()
            if existing:
                self.console.print(f"❌ User with email {email} already exists", style="red")
                return

            # Create user
            user = User(
                email=email,
                name=name,
                organization=organization,
                current_plan=plan,
                is_active=True
            )

            # Generate API key
            api_key = user.create_api_key(name="Default API Key")

            self.session.add(user)
            self.session.commit()

            # Display success
            success_panel = Panel(
                f"Email: {email}\n"
                f"Name: {name}\n"
                f"Organization: {organization}\n"
                f"Plan: {plan.value}\n"
                f"API Key: {api_key.key}\n\n"
                f"⚠️  Save the API key - it won't be shown again!",
                title="✅ User Created Successfully",
                border_style="green"
            )
            self.console.print(success_panel)

        except ValueError as e:
            self.console.print(f"❌ Invalid plan. Valid options: {[p.value for p in UserPlanEnum]}", style="red")
        except Exception as e:
            self.console.print(f"❌ Error creating user: {e}", style="red")

    def do_user_details(self, args):
        """Show detailed information about a user.

        Usage: user_details <email_or_id>
        """
        if not args.strip():
            self.console.print("❌ Usage: user_details <email_or_id>", style="red")
            return

        try:
            identifier = args.strip()

            # Try to find user by email or ID
            user = None
            if '@' in identifier:
                user = self.session.query(User).filter_by(email=identifier).first()
            else:
                user = self.session.query(User).filter(User.id.startswith(identifier)).first()

            if not user:
                self.console.print(f"❌ User not found: {identifier}", style="red")
                return

            # Get user's API keys
            api_keys = self.session.query(APIKey).filter_by(user_id=user.id).all()

            # Get user's subscriptions
            subscriptions = self.session.query(Subscription).filter_by(user_id=user.id).all()

            # Get usage summary
            usage_count = self.session.query(UsageLog).filter_by(user_id=user.id).count()
            total_cost = self.session.query(func.sum(func.cast(UsageLog.total_cost, Decimal))).filter_by(user_id=user.id).scalar() or 0

            # Get billing summary
            bills = self.session.query(Bill).filter_by(user_id=user.id).all()

            # Create detailed display
            user_info = f"""
User ID: {user.id}
Email: {user.email}
Name: {user.name or 'Not set'}
Organization: {user.organization or 'Not set'}
Plan: {user.current_plan.value}
Status: {'🟢 Active' if user.is_active else '🔴 Inactive'}
Created: {user.created_at.strftime('%Y-%m-%d %H:%M:%S')}

API Keys: {len(api_keys)} active
Subscriptions: {len(subscriptions)}
Total Usage: {usage_count} quantum executions
Total Spent: ${float(total_cost):.2f}
Bills: {len(bills)} ({len([b for b in bills if b.status == BillStatusEnum.PENDING])} pending)
"""

            user_panel = Panel(user_info.strip(), title="User Details", border_style="blue")
            self.console.print(user_panel)

            # Show API keys table
            if api_keys:
                api_table = Table(title="API Keys")
                api_table.add_column("Key Prefix", style="cyan")
                api_table.add_column("Name", style="white")
                api_table.add_column("Created", style="dim")
                api_table.add_column("Last Used", style="yellow")
                api_table.add_column("Usage Count", style="green")

                for key in api_keys:
                    last_used = key.last_used_at.strftime('%Y-%m-%d') if key.last_used_at else 'Never'
                    api_table.add_row(
                        key.key[:12] + "...",
                        key.name,
                        key.created_at.strftime('%Y-%m-%d'),
                        last_used,
                        str(key.usage_count)
                    )

                self.console.print(api_table)

        except Exception as e:
            self.console.print(f"❌ Error getting user details: {e}", style="red")

    def do_deactivate_user(self, args):
        """Deactivate a user account.

        Usage: deactivate_user <email_or_id>
        """
        if not args.strip():
            self.console.print("❌ Usage: deactivate_user <email_or_id>", style="red")
            return

        try:
            identifier = args.strip()

            # Find user
            user = None
            if '@' in identifier:
                user = self.session.query(User).filter_by(email=identifier).first()
            else:
                user = self.session.query(User).filter(User.id.startswith(identifier)).first()

            if not user:
                self.console.print(f"❌ User not found: {identifier}", style="red")
                return

            if not user.is_active:
                self.console.print(f"⚠️  User {user.email} is already inactive", style="yellow")
                return

            # Confirm action
            confirm = input(f"Are you sure you want to deactivate {user.email}? (y/N): ")
            if confirm.lower() != 'y':
                self.console.print("❌ Cancelled", style="yellow")
                return

            # Deactivate user
            user.is_active = False
            self.session.commit()

            self.console.print(f"✅ User {user.email} has been deactivated", style="green")

        except Exception as e:
            self.console.print(f"❌ Error deactivating user: {e}", style="red")

    # === SUBSCRIPTION MANAGEMENT ===

    def do_list_plans(self, args):
        """List all subscription plans.

        Usage: list_plans [--active-only]
        """
        try:
            query = self.session.query(Plan)

            if '--active-only' in args:
                query = query.filter_by(is_active=True)

            plans = query.order_by(Plan.sort_order).all()

            if not plans:
                self.console.print("No plans found.", style="yellow")
                return

            table = Table(title="Subscription Plans")
            table.add_column("Type", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Monthly", style="yellow")
            table.add_column("Yearly", style="yellow")
            table.add_column("Shot Limit", style="blue")
            table.add_column("Hardware", style="magenta")
            table.add_column("Status", style="white")

            for plan in plans:
                hardware = "✅" if plan.allow_hardware_access else "❌"
                status = "🟢 Active" if plan.is_active else "🔴 Inactive"
                shot_limit = str(plan.monthly_shot_limit) if plan.monthly_shot_limit else "Unlimited"

                table.add_row(
                    plan.plan_type.value,
                    plan.name,
                    f"${plan.price_monthly}",
                    f"${plan.price_yearly}",
                    shot_limit,
                    hardware,
                    status
                )

            self.console.print(table)

        except Exception as e:
            self.console.print(f"❌ Error listing plans: {e}", style="red")

    def do_create_subscription(self, args):
        """Create a subscription for a user.

        Usage: create_subscription <user_email> <plan_type> [--billing monthly|yearly]
        """
        try:
            parts = shlex.split(args)
            if len(parts) < 2:
                self.console.print("❌ Usage: create_subscription <user_email> <plan_type> [--billing monthly|yearly]", style="red")
                return

            user_email, plan_type = parts[0], parts[1]

            # Parse billing interval
            billing_interval = 'monthly'
            if '--billing' in parts:
                billing_idx = parts.index('--billing')
                if billing_idx + 1 < len(parts):
                    billing_interval = parts[billing_idx + 1]

            # Find user
            user = self.session.query(User).filter_by(email=user_email).first()
            if not user:
                self.console.print(f"❌ User not found: {user_email}", style="red")
                return

            # Find plan
            plan_enum = PlanTypeEnum[plan_type.upper()]
            plan = self.session.query(Plan).filter_by(plan_type=plan_enum).first()
            if not plan:
                self.console.print(f"❌ Plan not found: {plan_type}", style="red")
                return

            # Check for existing active subscription
            existing = self.session.query(Subscription).filter_by(
                user_id=user.id,
                status=SubscriptionStatusEnum.ACTIVE
            ).first()

            if existing:
                self.console.print(f"❌ User already has an active subscription", style="red")
                return

            # Create subscription
            from models.subscription import BillingIntervalEnum
            billing_enum = BillingIntervalEnum.MONTHLY if billing_interval == 'monthly' else BillingIntervalEnum.YEARLY
            price = plan.price_monthly if billing_interval == 'monthly' else plan.price_yearly

            subscription = Subscription(
                user_id=user.id,
                plan_id=plan.id,
                billing_interval=billing_enum,
                price=price,
                status=SubscriptionStatusEnum.ACTIVE
            )

            self.session.add(subscription)

            # Update user plan
            user.current_plan = UserPlanEnum[plan_type.upper()]

            self.session.commit()

            self.console.print(f"✅ Subscription created for {user_email} - {plan.name} (${price}/{billing_interval})", style="green")

        except KeyError:
            self.console.print(f"❌ Invalid plan type. Valid options: {[p.value for p in PlanTypeEnum]}", style="red")
        except Exception as e:
            self.console.print(f"❌ Error creating subscription: {e}", style="red")

    # === BILLING MANAGEMENT ===

    def do_generate_bills(self, args):
        """Generate bills for users with unbilled usage.

        Usage: generate_bills [--user EMAIL] [--period YYYY-MM]
        """
        try:
            # Parse arguments
            parsed_args = self._parse_args(args, [
                ('--user', str),
                ('--period', str)
            ])

            # Determine billing period
            if parsed_args.get('period'):
                try:
                    year, month = map(int, parsed_args['period'].split('-'))
                    period_start = datetime(year, month, 1)
                    next_month = month + 1 if month < 12 else 1
                    next_year = year if month < 12 else year + 1
                    period_end = datetime(next_year, next_month, 1) - timedelta(days=1)
                except ValueError:
                    self.console.print("❌ Invalid period format. Use YYYY-MM", style="red")
                    return
            else:
                # Last month
                today = datetime.now()
                period_start = datetime(today.year, today.month, 1) - timedelta(days=1)
                period_start = period_start.replace(day=1)
                period_end = datetime(today.year, today.month, 1) - timedelta(days=1)

            # Get users to bill
            query = self.session.query(User).filter_by(is_active=True)
            if parsed_args.get('user'):
                query = query.filter_by(email=parsed_args['user'])

            users = query.all()
            bills_created = 0

            for user in users:
                # Get unbilled usage for the period
                unbilled_usage = self.session.query(UsageLog).filter(
                    UsageLog.user_id == user.id,
                    UsageLog.billed == False,
                    UsageLog.success == True,
                    UsageLog.created_at >= period_start,
                    UsageLog.created_at <= period_end
                ).all()

                if not unbilled_usage:
                    continue

                # Create bill
                bill = Bill(
                    user_id=user.id,
                    period_start=period_start,
                    period_end=period_end
                )

                # Add usage charges
                bill.add_usage_charges(unbilled_usage)
                bill.finalize()

                self.session.add(bill)
                bills_created += 1

                self.console.print(f"📄 Bill created for {user.email}: ${bill.total_float:.2f}")

            self.session.commit()

            self.console.print(f"✅ Generated {bills_created} bills for period {period_start.strftime('%Y-%m')}", style="green")

        except Exception as e:
            self.console.print(f"❌ Error generating bills: {e}", style="red")

    def do_list_bills(self, args):
        """List bills in the system.

        Usage: list_bills [--user EMAIL] [--status STATUS] [--limit N]
        """
        try:
            # Parse arguments
            parsed_args = self._parse_args(args, [
                ('--user', str),
                ('--status', str),
                ('--limit', int)
            ])

            query = self.session.query(Bill).join(User)

            # Apply filters
            if parsed_args.get('user'):
                query = query.filter(User.email == parsed_args['user'])

            if parsed_args.get('status'):
                status_enum = BillStatusEnum[parsed_args['status'].upper()]
                query = query.filter(Bill.status == status_enum)

            query = query.order_by(Bill.created_at.desc())

            if parsed_args.get('limit'):
                query = query.limit(parsed_args['limit'])

            bills = query.all()

            if not bills:
                self.console.print("No bills found.", style="yellow")
                return

            table = Table(title="Bills")
            table.add_column("Bill #", style="cyan")
            table.add_column("User", style="green")
            table.add_column("Period", style="blue")
            table.add_column("Amount", style="yellow")
            table.add_column("Status", style="white")
            table.add_column("Due Date", style="red")

            for bill in bills:
                user = self.session.query(User).filter_by(id=bill.user_id).first()
                status_color = {
                    BillStatusEnum.DRAFT: "gray",
                    BillStatusEnum.PENDING: "yellow",
                    BillStatusEnum.PAID: "green",
                    BillStatusEnum.OVERDUE: "red",
                    BillStatusEnum.CANCELLED: "red"
                }.get(bill.status, "white")

                table.add_row(
                    bill.bill_number,
                    user.email if user else "Unknown",
                    bill.period_start.strftime('%Y-%m'),
                    f"${bill.total_float:.2f}",
                    f"[{status_color}]{bill.status.value}[/{status_color}]",
                    bill.due_at.strftime('%Y-%m-%d') if bill.due_at else "-"
                )

            self.console.print(table)

        except Exception as e:
            self.console.print(f"❌ Error listing bills: {e}", style="red")

    # === USAGE ANALYTICS ===

    def do_usage_stats(self, args):
        """Show usage statistics.

        Usage: usage_stats [--user EMAIL] [--period days]
        """
        try:
            # Parse arguments
            parsed_args = self._parse_args(args, [
                ('--user', str),
                ('--period', int)
            ])

            # Determine time period
            period_days = parsed_args.get('period', 30)
            start_date = datetime.now() - timedelta(days=period_days)

            query = self.session.query(UsageLog).filter(UsageLog.created_at >= start_date)

            if parsed_args.get('user'):
                user = self.session.query(User).filter_by(email=parsed_args['user']).first()
                if user:
                    query = query.filter_by(user_id=user.id)
                else:
                    self.console.print(f"❌ User not found: {parsed_args['user']}", style="red")
                    return

            usage_logs = query.all()

            if not usage_logs:
                self.console.print("No usage data found for the specified period.", style="yellow")
                return

            # Calculate statistics
            total_jobs = len(usage_logs)
            successful_jobs = len([log for log in usage_logs if log.success])
            total_shots = sum(log.shots_executed for log in usage_logs if log.success)
            total_cost = sum(log.cost_float for log in usage_logs if log.success)

            # Backend distribution
            backend_stats = {}
            algorithm_stats = {}

            for log in usage_logs:
                if log.success:
                    # Backend stats
                    backend = log.backend_used
                    if backend not in backend_stats:
                        backend_stats[backend] = {'jobs': 0, 'shots': 0, 'cost': 0}
                    backend_stats[backend]['jobs'] += 1
                    backend_stats[backend]['shots'] += log.shots_executed
                    backend_stats[backend]['cost'] += log.cost_float

                    # Algorithm stats
                    algorithm = log.algorithm_type.value if log.algorithm_type else 'unknown'
                    if algorithm not in algorithm_stats:
                        algorithm_stats[algorithm] = {'jobs': 0, 'shots': 0, 'cost': 0}
                    algorithm_stats[algorithm]['jobs'] += 1
                    algorithm_stats[algorithm]['shots'] += log.shots_executed
                    algorithm_stats[algorithm]['cost'] += log.cost_float

            # Display overall stats
            stats_info = f"""
Period: Last {period_days} days
Total Jobs: {total_jobs:,}
Successful Jobs: {successful_jobs:,} ({successful_jobs/total_jobs*100:.1f}%)
Total Shots: {total_shots:,}
Total Cost: ${total_cost:.2f}
Average Cost per Job: ${total_cost/successful_jobs:.4f}
Average Shots per Job: {total_shots/successful_jobs:.0f}
"""

            stats_panel = Panel(stats_info.strip(), title="Usage Statistics", border_style="blue")
            self.console.print(stats_panel)

            # Backend distribution table
            if backend_stats:
                backend_table = Table(title="Backend Distribution")
                backend_table.add_column("Backend", style="cyan")
                backend_table.add_column("Jobs", style="yellow")
                backend_table.add_column("Shots", style="green")
                backend_table.add_column("Cost", style="red")
                backend_table.add_column("% of Total", style="blue")

                for backend, stats in sorted(backend_stats.items(), key=lambda x: x[1]['cost'], reverse=True):
                    percentage = stats['cost'] / total_cost * 100 if total_cost > 0 else 0
                    backend_table.add_row(
                        backend,
                        f"{stats['jobs']:,}",
                        f"{stats['shots']:,}",
                        f"${stats['cost']:.2f}",
                        f"{percentage:.1f}%"
                    )

                self.console.print(backend_table)

            # Algorithm distribution table
            if algorithm_stats:
                algorithm_table = Table(title="Algorithm Distribution")
                algorithm_table.add_column("Algorithm", style="cyan")
                algorithm_table.add_column("Jobs", style="yellow")
                algorithm_table.add_column("Avg Cost/Job", style="red")

                for algorithm, stats in sorted(algorithm_stats.items(), key=lambda x: x[1]['jobs'], reverse=True):
                    avg_cost = stats['cost'] / stats['jobs'] if stats['jobs'] > 0 else 0
                    algorithm_table.add_row(
                        algorithm.upper(),
                        f"{stats['jobs']:,}",
                        f"${avg_cost:.4f}"
                    )

                self.console.print(algorithm_table)

        except Exception as e:
            self.console.print(f"❌ Error generating usage stats: {e}", style="red")

    # === QUOTA MANAGEMENT ===

    def do_list_quotas(self, args):
        """List all quotas in the system.

        Usage: list_quotas [--user EMAIL] [--type TYPE]
        """
        try:
            # Parse arguments
            parsed_args = self._parse_args(args, [
                ('--user', str),
                ('--type', str)
            ])

            query = self.session.query(Quota)

            if parsed_args.get('user'):
                user = self.session.query(User).filter_by(email=parsed_args['user']).first()
                if user:
                    query = query.filter_by(user_id=user.id)
                else:
                    self.console.print(f"❌ User not found: {parsed_args['user']}", style="red")
                    return

            if parsed_args.get('type'):
                quota_type = QuotaTypeEnum[parsed_args['type'].upper()]
                query = query.filter_by(quota_type=quota_type)

            quotas = query.all()

            if not quotas:
                self.console.print("No quotas found.", style="yellow")
                return

            table = Table(title="Quotas")
            table.add_column("Name", style="cyan")
            table.add_column("Type", style="green")
            table.add_column("Applies To", style="blue")
            table.add_column("Limit", style="yellow")
            table.add_column("Period", style="white")
            table.add_column("Status", style="red")

            for quota in quotas:
                applies_to = "Global"
                if quota.user_id:
                    user = self.session.query(User).filter_by(id=quota.user_id).first()
                    applies_to = f"User: {user.email if user else 'Unknown'}"
                elif quota.plan_id:
                    plan = self.session.query(Plan).filter_by(id=quota.plan_id).first()
                    applies_to = f"Plan: {plan.name if plan else 'Unknown'}"
                elif quota.api_key_id:
                    applies_to = "API Key"

                period_hours = quota.period_seconds / 3600
                period_str = f"{period_hours:.0f}h" if period_hours < 24 else f"{period_hours/24:.0f}d"
                status = "🟢 Active" if quota.is_active else "🔴 Inactive"

                table.add_row(
                    quota.name,
                    quota.quota_type.value,
                    applies_to,
                    str(quota.limit_value),
                    period_str,
                    status
                )

            self.console.print(table)

        except Exception as e:
            self.console.print(f"❌ Error listing quotas: {e}", style="red")

    # === API KEY MANAGEMENT ===

    def do_create_api_key(self, args):
        """Create a new API key for a user.

        Usage: create_api_key <user_email> <key_name>
        """
        try:
            parts = shlex.split(args)
            if len(parts) < 2:
                self.console.print("❌ Usage: create_api_key <user_email> <key_name>", style="red")
                return

            user_email, key_name = parts[0], parts[1]

            # Find user
            user = self.session.query(User).filter_by(email=user_email).first()
            if not user:
                self.console.print(f"❌ User not found: {user_email}", style="red")
                return

            # Create API key
            api_key = user.create_api_key(name=key_name)
            self.session.commit()

            success_panel = Panel(
                f"User: {user.email}\n"
                f"Key Name: {key_name}\n"
                f"API Key: {api_key.key}\n\n"
                f"⚠️  Save this key - it won't be shown again!",
                title="✅ API Key Created",
                border_style="green"
            )
            self.console.print(success_panel)

        except Exception as e:
            self.console.print(f"❌ Error creating API key: {e}", style="red")

    def do_list_api_keys(self, args):
        """List API keys for a user.

        Usage: list_api_keys <user_email>
        """
        if not args.strip():
            self.console.print("❌ Usage: list_api_keys <user_email>", style="red")
            return

        try:
            user_email = args.strip()

            # Find user
            user = self.session.query(User).filter_by(email=user_email).first()
            if not user:
                self.console.print(f"❌ User not found: {user_email}", style="red")
                return

            # Get API keys
            api_keys = self.session.query(APIKey).filter_by(user_id=user.id).all()

            if not api_keys:
                self.console.print(f"No API keys found for {user_email}", style="yellow")
                return

            table = Table(title=f"API Keys for {user_email}")
            table.add_column("Key Prefix", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Created", style="blue")
            table.add_column("Last Used", style="yellow")
            table.add_column("Usage Count", style="white")
            table.add_column("Status", style="red")

            for key in api_keys:
                last_used = key.last_used_at.strftime('%Y-%m-%d %H:%M') if key.last_used_at else 'Never'
                status = "🟢 Active" if key.is_valid() else "🔴 Expired"

                table.add_row(
                    key.key[:12] + "...",
                    key.name,
                    key.created_at.strftime('%Y-%m-%d'),
                    last_used,
                    str(key.usage_count),
                    status
                )

            self.console.print(table)

        except Exception as e:
            self.console.print(f"❌ Error listing API keys: {e}", style="red")

    # === UTILITY METHODS ===

    def _parse_args(self, args_str: str, arg_definitions: List[tuple]) -> Dict[str, Any]:
        """Parse command line arguments."""
        parts = shlex.split(args_str)
        parsed = {}

        i = 0
        while i < len(parts):
            part = parts[i]

            # Check if this is a flag
            for flag, arg_type in arg_definitions:
                if part == flag and i + 1 < len(parts):
                    value = parts[i + 1]
                    if arg_type == int:
                        parsed[flag.lstrip('-')] = int(value)
                    else:
                        parsed[flag.lstrip('-')] = value
                    i += 2
                    break
            else:
                i += 1

        return parsed

    # === SYSTEM COMMANDS ===

    def do_status(self, args):
        """Show system status and statistics."""
        self._show_startup_info()

    def do_backup(self, args):
        """Create a backup of the database.

        Usage: backup [filename]
        """
        try:
            filename = args.strip() or f"bioql_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"

            if self.database_url.startswith('sqlite'):
                # For SQLite, copy the file
                import shutil
                db_file = self.database_url.replace('sqlite:///', '')
                shutil.copy2(db_file, filename)
                self.console.print(f"✅ Database backed up to {filename}", style="green")
            else:
                self.console.print("❌ Backup only supported for SQLite databases", style="red")

        except Exception as e:
            self.console.print(f"❌ Backup failed: {e}", style="red")

    def do_exit(self, args):
        """Exit the admin console."""
        self.console.print("👋 Goodbye!", style="blue")
        return True

    def do_quit(self, args):
        """Exit the admin console."""
        return self.do_exit(args)


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="BioQL Admin CLI")
    parser.add_argument("--db-url", help="Database URL", default="sqlite:///bioql_billing.db")
    parser.add_argument("--config", help="Configuration file path")

    args = parser.parse_args()

    # Load config if provided
    config = {}
    if args.config and os.path.exists(args.config):
        with open(args.config, 'r') as f:
            config = json.load(f)

    try:
        # Create and run CLI
        cli = BioQLAdminCLI(database_url=args.db_url, config=config)
        cli.cmdloop()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()