#!/usr/bin/env python3
"""
BioQL Billing Database Setup Script

This script initializes the BioQL billing database with all required tables,
sample data, and configuration. It supports both SQLite (development) and
PostgreSQL (production) databases.

Usage:
    # SQLite setup (development)
    python setup_billing_database.py --database sqlite --file bioql_billing.db

    # PostgreSQL setup (production)
    python setup_billing_database.py --database postgresql --url postgresql://user:pass@localhost/bioql_billing

    # Reset existing database
    python setup_billing_database.py --database sqlite --file bioql_billing.db --reset

    # Sample data only
    python setup_billing_database.py --database sqlite --file bioql_billing.db --sample-data-only
"""

import argparse
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, Any
import logging

# Add BP&PL to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

# Import all models to ensure they're registered
from models.base import Base
from models.user import User, APIKey, UserPlan, UserPlanEnum
from models.billing import Bill, BillItem, PaymentMethod, Payment, BillStatusEnum, PaymentMethodTypeEnum
from models.usage import UsageSession, QuantumJob, UsageLog, BackendTypeEnum, AlgorithmTypeEnum
from models.subscription import Plan, PlanFeature, Subscription, PlanTypeEnum, BillingIntervalEnum, SubscriptionStatusEnum
from models.quota import Quota, QuotaUsage, QuotaTypeEnum

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class BillingDatabaseSetup:
    """Handles database initialization and sample data creation."""

    def __init__(self, database_url: str):
        """Initialize with database URL."""
        self.database_url = database_url
        self.engine = None
        self.session = None

    def create_connection(self):
        """Create database connection."""
        try:
            logger.info(f"Connecting to database: {self.database_url}")
            self.engine = create_engine(
                self.database_url,
                echo=False,  # Set to True for SQL debugging
                pool_pre_ping=True  # Verify connections before use
            )

            # Test connection
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            logger.info("Database connection successful")

            # Create session
            Session = sessionmaker(bind=self.engine)
            self.session = Session()

        except SQLAlchemyError as e:
            logger.error(f"Failed to connect to database: {e}")
            raise

    def create_tables(self, reset: bool = False):
        """Create all database tables."""
        try:
            if reset:
                logger.info("Dropping existing tables...")
                Base.metadata.drop_all(bind=self.engine)

            logger.info("Creating database tables...")
            Base.metadata.create_all(bind=self.engine)
            logger.info("Database tables created successfully")

        except SQLAlchemyError as e:
            logger.error(f"Failed to create tables: {e}")
            raise

    def create_sample_plans(self):
        """Create sample subscription plans."""
        logger.info("Creating sample subscription plans...")

        plans_data = [
            {
                'name': 'Free Tier',
                'plan_type': PlanTypeEnum.FREE,
                'description': 'Perfect for learning and small experiments',
                'price_monthly': '0.00',
                'price_yearly': '0.00',
                'monthly_shot_limit': 1000,
                'daily_shot_limit': 100,
                'hourly_shot_limit': 20,
                'api_calls_per_minute': 10,
                'api_calls_per_hour': 100,
                'api_calls_per_day': 1000,
                'allow_hardware_access': False,
                'max_qubits': 4,
                'max_circuit_depth': 100,
                'priority_support': False,
                'analytics_access': False,
                'sort_order': 1
            },
            {
                'name': 'Basic Research',
                'plan_type': PlanTypeEnum.BASIC,
                'description': 'For individual researchers and small teams',
                'price_monthly': '99.00',
                'price_yearly': '990.00',
                'monthly_shot_limit': 50000,
                'daily_shot_limit': 5000,
                'hourly_shot_limit': 500,
                'api_calls_per_minute': 60,
                'api_calls_per_hour': 1000,
                'api_calls_per_day': 10000,
                'allow_hardware_access': True,
                'max_qubits': 8,
                'max_circuit_depth': 500,
                'priority_support': False,
                'analytics_access': True,
                'sort_order': 2
            },
            {
                'name': 'Professional',
                'plan_type': PlanTypeEnum.PRO,
                'description': 'For professional research teams and biotech companies',
                'price_monthly': '499.00',
                'price_yearly': '4990.00',
                'monthly_shot_limit': 500000,
                'daily_shot_limit': 50000,
                'hourly_shot_limit': 5000,
                'api_calls_per_minute': 120,
                'api_calls_per_hour': 5000,
                'api_calls_per_day': 50000,
                'allow_hardware_access': True,
                'max_qubits': 16,
                'max_circuit_depth': 2000,
                'priority_support': True,
                'analytics_access': True,
                'sort_order': 3
            },
            {
                'name': 'Enterprise',
                'plan_type': PlanTypeEnum.ENTERPRISE,
                'description': 'For large pharmaceutical companies and research institutions',
                'price_monthly': '2999.00',
                'price_yearly': '29990.00',
                'monthly_shot_limit': None,  # Unlimited
                'daily_shot_limit': None,
                'hourly_shot_limit': None,
                'api_calls_per_minute': 300,
                'api_calls_per_hour': 20000,
                'api_calls_per_day': 200000,
                'allow_hardware_access': True,
                'max_qubits': None,  # Unlimited
                'max_circuit_depth': None,  # Unlimited
                'priority_support': True,
                'analytics_access': True,
                'sort_order': 4
            }
        ]

        for plan_data in plans_data:
            plan = Plan(**plan_data)
            self.session.add(plan)

        # Add plan features
        self._create_plan_features()

        self.session.commit()
        logger.info(f"Created {len(plans_data)} subscription plans")

    def _create_plan_features(self):
        """Create features for each plan."""
        # Get plans
        free_plan = self.session.query(Plan).filter_by(plan_type=PlanTypeEnum.FREE).first()
        basic_plan = self.session.query(Plan).filter_by(plan_type=PlanTypeEnum.BASIC).first()
        pro_plan = self.session.query(Plan).filter_by(plan_type=PlanTypeEnum.PRO).first()
        enterprise_plan = self.session.query(Plan).filter_by(plan_type=PlanTypeEnum.ENTERPRISE).first()

        # Define features for each plan
        features_data = {
            free_plan.id: [
                ('Quantum Simulators', 'Access to quantum simulators', True),
                ('Basic Algorithms', 'Standard quantum algorithms', True),
                ('Community Support', 'Community forum support', True),
                ('Real Hardware', 'Access to quantum hardware', False),
                ('Priority Support', 'Priority customer support', False),
                ('Advanced Analytics', 'Usage analytics and insights', False)
            ],
            basic_plan.id: [
                ('Quantum Simulators', 'Access to quantum simulators', True),
                ('Basic Algorithms', 'Standard quantum algorithms', True),
                ('Advanced Algorithms', 'VQE, QAOA, and optimization algorithms', True),
                ('Real Hardware', 'Access to IBM Quantum and IonQ', True),
                ('Usage Analytics', 'Basic usage tracking and reports', True),
                ('Email Support', 'Email-based customer support', True),
                ('Priority Support', 'Priority customer support', False)
            ],
            pro_plan.id: [
                ('All Basic Features', 'Everything in Basic plan', True),
                ('Advanced Hardware', 'Access to latest quantum processors', True),
                ('Custom Algorithms', 'Support for custom quantum algorithms', True),
                ('Advanced Analytics', 'Detailed analytics and cost optimization', True),
                ('Priority Support', 'Priority email and chat support', True),
                ('Team Management', 'Multi-user team features', True),
                ('API Rate Limits', 'Higher API rate limits', True)
            ],
            enterprise_plan.id: [
                ('All Pro Features', 'Everything in Professional plan', True),
                ('Unlimited Usage', 'No monthly shot limits', True),
                ('Dedicated Support', 'Dedicated customer success manager', True),
                ('Custom Pricing', 'Volume discounts and custom rates', True),
                ('On-Premise Deployment', 'Private cloud deployment options', True),
                ('Custom Integration', 'Tailored API and workflow integration', True),
                ('SLA Guarantee', '99.9% uptime service level agreement', True)
            ]
        }

        for plan_id, features in features_data.items():
            for i, (name, description, included) in enumerate(features):
                feature = PlanFeature(
                    plan_id=plan_id,
                    name=name,
                    description=description,
                    included=included,
                    sort_order=i
                )
                self.session.add(feature)

    def create_sample_users(self):
        """Create sample users with different plans."""
        logger.info("Creating sample users...")

        users_data = [
            {
                'email': 'researcher@university.edu',
                'username': 'quantum_researcher',
                'first_name': 'Dr. Alice',
                'last_name': 'Chen',
                'organization': 'University Research Lab',
                'current_plan': UserPlanEnum.FREE,
                'is_verified': True,
                'password': 'demo_password_123'
            },
            {
                'email': 'lab@biotech.com',
                'username': 'biotech_lab',
                'first_name': 'Bob',
                'last_name': 'Martinez',
                'organization': 'BioTech Innovations Inc.',
                'current_plan': UserPlanEnum.BASIC,
                'is_verified': True,
                'password': 'demo_password_456'
            },
            {
                'email': 'team@pharma.com',
                'username': 'pharma_team',
                'first_name': 'Dr. Carol',
                'last_name': 'Johnson',
                'organization': 'PharmaCorp Research Division',
                'current_plan': UserPlanEnum.PRO,
                'is_verified': True,
                'password': 'demo_password_789'
            },
            {
                'email': 'enterprise@megacorp.com',
                'username': 'enterprise_user',
                'first_name': 'David',
                'last_name': 'Kim',
                'organization': 'MegaCorp Pharmaceutical',
                'current_plan': UserPlanEnum.ENTERPRISE,
                'is_verified': True,
                'password': 'demo_password_enterprise'
            }
        ]

        for user_data in users_data:
            password = user_data.pop('password')
            user = User(**user_data)
            user.set_password(password)
            self.session.add(user)
            self.session.flush()  # Get user ID

            # Create API key for each user
            api_key_value = APIKey.generate_key()
            api_key = APIKey(
                user_id=user.id,
                key_name=f"{user.username}_default_key",
                rate_limit_per_minute=60,
                rate_limit_per_hour=1000,
                rate_limit_per_day=10000
            )
            api_key.set_key(api_key_value)
            self.session.add(api_key)

            # Store the actual key for display (in real deployment, this would be shown only once)
            logger.info(f"Created user {user.email} with API key: {api_key_value}")

        self.session.commit()
        logger.info(f"Created {len(users_data)} sample users with API keys")

    def create_sample_subscriptions(self):
        """Create sample subscriptions for users."""
        logger.info("Creating sample subscriptions...")

        # Get users and plans
        users = self.session.query(User).all()
        plans = {plan.plan_type: plan for plan in self.session.query(Plan).all()}

        subscriptions_created = 0
        for user in users:
            if user.current_plan != UserPlanEnum.FREE:
                # Convert UserPlanEnum to PlanTypeEnum by matching the string value
                plan_type = None
                for pt in PlanTypeEnum:
                    if pt.value == user.current_plan.value:
                        plan_type = pt
                        break

                if plan_type and plan_type in plans:
                    plan = plans[plan_type]
                else:
                    logger.warning(f"No matching plan found for user {user.email} with plan {user.current_plan}")
                    continue

                # Create active subscription
                subscription = Subscription(
                    user_id=user.id,
                    plan_id=plan.id,
                    status=SubscriptionStatusEnum.ACTIVE,
                    billing_interval=BillingIntervalEnum.MONTHLY,
                    price=plan.price_monthly,
                    current_period_start=datetime.utcnow() - timedelta(days=15),
                    current_period_end=datetime.utcnow() + timedelta(days=15)
                )
                self.session.add(subscription)
                subscriptions_created += 1

        self.session.commit()
        logger.info(f"Created {subscriptions_created} sample subscriptions")

    def create_sample_usage_data(self):
        """Create sample usage data for demonstration."""
        logger.info("Creating sample usage data...")

        users = self.session.query(User).all()
        usage_logs_created = 0

        for user in users:
            api_key = self.session.query(APIKey).filter_by(user_id=user.id).first()

            # Create usage session
            session = UsageSession(
                user_id=user.id,
                api_key_id=api_key.id,
                session_name=f"Research Session - {user.organization}",
                description="Sample quantum computations for demonstration",
                client_ip="192.168.1.100",
                user_agent=f"BioQL Client - {user.organization}",
                started_at=datetime.utcnow() - timedelta(hours=2),
                ended_at=datetime.utcnow() - timedelta(hours=1)
            )
            self.session.add(session)
            self.session.flush()

            # Create sample usage logs
            sample_computations = [
                {
                    'program_text': 'Create a Bell state and measure both qubits',
                    'circuit_qubits': 2,
                    'circuit_depth': 3,
                    'algorithm_type': AlgorithmTypeEnum.BASIC,
                    'biological_context': 'general',
                    'backend_used': 'qasm_simulator',
                    'backend_type': BackendTypeEnum.SIMULATOR,
                    'shots_requested': 1024,
                    'shots_executed': 1024
                },
                {
                    'program_text': 'Protein folding simulation using VQE algorithm',
                    'circuit_qubits': 4,
                    'circuit_depth': 12,
                    'algorithm_type': AlgorithmTypeEnum.VQE,
                    'biological_context': 'protein_folding',
                    'backend_used': 'qasm_simulator',
                    'backend_type': BackendTypeEnum.SIMULATOR,
                    'shots_requested': 2048,
                    'shots_executed': 2048
                },
                {
                    'program_text': 'Drug discovery molecular binding simulation',
                    'circuit_qubits': 6,
                    'circuit_depth': 20,
                    'algorithm_type': AlgorithmTypeEnum.QAOA,
                    'biological_context': 'drug_discovery',
                    'backend_used': 'qasm_simulator',
                    'backend_type': BackendTypeEnum.SIMULATOR,
                    'shots_requested': 4096,
                    'shots_executed': 4096
                }
            ]

            for comp in sample_computations:
                usage_log = UsageLog(
                    user_id=user.id,
                    session_id=session.id,
                    api_key_id=api_key.id,
                    program_text=comp['program_text'],
                    program_hash=f"hash_{comp['program_text'][:10]}",
                    circuit_qubits=comp['circuit_qubits'],
                    circuit_depth=comp['circuit_depth'],
                    circuit_gates=comp['circuit_depth'] * 2,  # Simplified
                    algorithm_type=comp['algorithm_type'],
                    biological_context=comp['biological_context'],
                    backend_requested=comp['backend_used'],
                    backend_used=comp['backend_used'],
                    backend_type=comp['backend_type'],
                    shots_requested=comp['shots_requested'],
                    shots_executed=comp['shots_executed'],
                    success=True,
                    execution_time=2.5,
                    created_at=datetime.utcnow() - timedelta(hours=1, minutes=30)
                )

                # Calculate cost using standard pricing
                usage_log.calculate_cost({
                    'simulator_cost_per_shot': '0.001',
                    'hardware_cost_per_shot': '0.01',
                    'algorithm_multipliers': {
                        'basic': 1.0,
                        'vqe': 3.0,
                        'grover': 3.0,
                        'shor': 3.0,
                        'qaoa': 2.0,
                        'custom': 1.5
                    }
                })

                self.session.add(usage_log)
                usage_logs_created += 1

        self.session.commit()
        logger.info(f"Created {usage_logs_created} sample usage logs")

    def create_sample_quotas(self):
        """Create sample quotas for different user plans."""
        logger.info("Creating sample quotas...")

        plans = self.session.query(Plan).all()
        quotas_created = 0

        for plan in plans:
            # Define quotas based on plan type
            if plan.plan_type == PlanTypeEnum.FREE:
                quota_configs = [
                    (QuotaTypeEnum.SHOTS_PER_HOUR, 20, 3600),
                    (QuotaTypeEnum.SHOTS_PER_DAY, 100, 86400),
                    (QuotaTypeEnum.SHOTS_PER_MONTH, 1000, 2592000),
                    (QuotaTypeEnum.API_CALLS_PER_MINUTE, 10, 60)
                ]
            elif plan.plan_type == PlanTypeEnum.BASIC:
                quota_configs = [
                    (QuotaTypeEnum.SHOTS_PER_HOUR, 500, 3600),
                    (QuotaTypeEnum.SHOTS_PER_DAY, 5000, 86400),
                    (QuotaTypeEnum.SHOTS_PER_MONTH, 50000, 2592000),
                    (QuotaTypeEnum.API_CALLS_PER_MINUTE, 60, 60)
                ]
            elif plan.plan_type == PlanTypeEnum.PRO:
                quota_configs = [
                    (QuotaTypeEnum.SHOTS_PER_HOUR, 5000, 3600),
                    (QuotaTypeEnum.SHOTS_PER_DAY, 50000, 86400),
                    (QuotaTypeEnum.SHOTS_PER_MONTH, 500000, 2592000),
                    (QuotaTypeEnum.API_CALLS_PER_MINUTE, 120, 60)
                ]
            else:  # Enterprise
                quota_configs = [
                    (QuotaTypeEnum.API_CALLS_PER_MINUTE, 300, 60)
                    # No shot limits for enterprise
                ]

            for quota_type, limit, period in quota_configs:
                quota = Quota(
                    name=f"{plan.name} - {quota_type.value}",
                    quota_type=quota_type,
                    plan_id=plan.id,
                    limit_value=limit,
                    period_seconds=period,
                    is_active=True,
                    is_hard_limit=True
                )
                self.session.add(quota)
                quotas_created += 1

        self.session.commit()
        logger.info(f"Created {quotas_created} sample quotas")

    def display_setup_summary(self):
        """Display a summary of the created data."""
        logger.info("Database setup completed successfully!")

        # Count records
        user_count = self.session.query(User).count()
        api_key_count = self.session.query(APIKey).count()
        plan_count = self.session.query(Plan).count()
        subscription_count = self.session.query(Subscription).count()
        usage_log_count = self.session.query(UsageLog).count()
        quota_count = self.session.query(Quota).count()

        print("\n" + "="*60)
        print("BioQL Billing Database Setup Summary")
        print("="*60)
        print(f"Database URL: {self.database_url}")
        print(f"Users created: {user_count}")
        print(f"API keys created: {api_key_count}")
        print(f"Subscription plans: {plan_count}")
        print(f"Active subscriptions: {subscription_count}")
        print(f"Usage logs: {usage_log_count}")
        print(f"Quotas defined: {quota_count}")
        print("\nSample Users and API Keys:")
        print("-" * 40)

        users = self.session.query(User).all()
        for user in users:
            api_key = self.session.query(APIKey).filter_by(user_id=user.id).first()
            print(f"{user.email}")
            print(f"  Plan: {user.current_plan.value}")
            print(f"  Organization: {user.organization}")
            print(f"  API Key Prefix: {api_key.key_prefix}...")
            print()

        print("Next Steps:")
        print("1. Copy the API keys for testing")
        print("2. Update your .env file with database connection")
        print("3. Run the billing demo script to test functionality")
        print("4. Review the pricing documentation")
        print("\n" + "="*60)

    def close(self):
        """Close database connection."""
        if self.session:
            self.session.close()
        if self.engine:
            self.engine.dispose()


def main():
    """Main setup function."""
    parser = argparse.ArgumentParser(description='Setup BioQL Billing Database')
    parser.add_argument('--database', choices=['sqlite', 'postgresql'],
                       default='sqlite', help='Database type')
    parser.add_argument('--file', help='SQLite database file path')
    parser.add_argument('--url', help='PostgreSQL connection URL')
    parser.add_argument('--reset', action='store_true',
                       help='Reset existing database')
    parser.add_argument('--sample-data-only', action='store_true',
                       help='Only create sample data (database must exist)')

    args = parser.parse_args()

    # Determine database URL
    if args.database == 'sqlite':
        db_file = args.file or 'bioql_billing.db'
        database_url = f'sqlite:///{db_file}'
    else:
        if not args.url:
            print("PostgreSQL URL required. Example:")
            print("postgresql://username:password@localhost:5432/bioql_billing")
            sys.exit(1)
        database_url = args.url

    # Setup database
    setup = BillingDatabaseSetup(database_url)

    try:
        setup.create_connection()

        if not args.sample_data_only:
            setup.create_tables(reset=args.reset)

        # Create sample data
        setup.create_sample_plans()
        setup.create_sample_users()
        setup.create_sample_subscriptions()
        setup.create_sample_usage_data()
        setup.create_sample_quotas()

        setup.display_setup_summary()

    except Exception as e:
        logger.error(f"Setup failed: {e}")
        sys.exit(1)
    finally:
        setup.close()


if __name__ == '__main__':
    main()