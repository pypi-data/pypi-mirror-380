#!/usr/bin/env python3
"""
BioQL Cloud Authentication - Required for all executions
Users must have valid API key from bioql.com
"""

import requests
import os
from typing import Optional, Dict, Any
from datetime import datetime

# Your authentication service URL (replace with your production URL)
BIOQL_AUTH_URL = os.getenv('BIOQL_AUTH_URL', 'https://api.bioql.com')
BIOQL_LOCAL_AUTH = os.getenv('BIOQL_LOCAL_AUTH', 'http://localhost:5001')

class BioQLAuthError(Exception):
    """Authentication error for BioQL"""
    pass

class BioQLUsageLimitError(Exception):
    """Usage limit exceeded for BioQL"""
    pass

def authenticate_api_key(api_key: str) -> Dict[str, Any]:
    """
    Authenticate API key with BioQL cloud service
    Returns user information if valid, raises exception if invalid
    """
    if not api_key:
        raise BioQLAuthError(
            "API key required. Get yours at https://bioql.com/signup\n"
            "Usage: quantum('Create Bell state', backend='simulator', api_key='your_key')"
        )

    # Try production first, then local (for testing)
    auth_urls = [BIOQL_AUTH_URL, BIOQL_LOCAL_AUTH]

    for auth_url in auth_urls:
        try:
            response = requests.post(
                f"{auth_url}/auth/validate",
                json={"api_key": api_key},
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "BioQL/2.1.0",
                    "ngrok-skip-browser-warning": "true"
                },
                timeout=10,
                verify=True
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise BioQLAuthError(
                    f"Invalid API key. Get yours at https://bioql.com/signup\n"
                    f"If you just signed up, check your email for the API key."
                )
            elif response.status_code == 429:
                raise BioQLUsageLimitError(
                    f"Rate limit exceeded. Upgrade your plan at https://bioql.com/pricing"
                )

        except requests.exceptions.RequestException:
            # Try next URL
            continue

    raise BioQLAuthError(
        "Unable to connect to BioQL authentication service.\n"
        "Please check your internet connection or try again later.\n"
        "If the problem persists, contact support at support@bioql.com"
    )

def check_usage_limits(api_key: str, shots: int, backend: str) -> Dict[str, Any]:
    """
    Check if user can execute the requested operation
    """
    if not api_key:
        raise BioQLAuthError("API key required")

    auth_urls = [BIOQL_AUTH_URL, BIOQL_LOCAL_AUTH]

    for auth_url in auth_urls:
        try:
            response = requests.post(
                f"{auth_url}/billing/check-limits",
                json={
                    "api_key": api_key,
                    "requested_shots": shots,
                    "backend": backend
                },
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "BioQL/2.1.0",
                    "ngrok-skip-browser-warning": "true"
                },
                timeout=10,
                verify=True
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                limit_data = response.json()
                error_msg = f"Usage limit exceeded: {limit_data.get('reason', 'Unknown limit')}"

                if limit_data.get('upgrade_required'):
                    error_msg += f"\nUpgrade your plan at https://bioql.com/pricing"

                if 'shots_remaining' in limit_data:
                    error_msg += f"\nShots remaining this month: {limit_data['shots_remaining']}"

                raise BioQLUsageLimitError(error_msg)

        except requests.exceptions.RequestException:
            continue

    raise BioQLAuthError("Unable to verify usage limits. Please try again.")

def record_usage(api_key: str, shots_executed: int, backend: str, cost: float, success: bool) -> None:
    """
    Record quantum execution for billing
    """
    if not api_key:
        return

    auth_urls = [BIOQL_AUTH_URL, BIOQL_LOCAL_AUTH]

    for auth_url in auth_urls:
        try:
            response = requests.post(
                f"{auth_url}/billing/record-usage",
                json={
                    "api_key": api_key,
                    "shots_executed": shots_executed,
                    "backend": backend,
                    "cost": cost,
                    "success": success,
                    "timestamp": datetime.utcnow().isoformat()
                },
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "BioQL/2.1.0",
                    "ngrok-skip-browser-warning": "true"  # Skip ngrok welcome page
                },
                timeout=10,
                verify=True  # Verify SSL certificates
            )

            if response.status_code == 200:
                return  # Successfully recorded

        except requests.exceptions.RequestException as e:
            # Log the error for debugging
            import logging
            logging.debug(f"Failed to record usage at {auth_url}: {e}")
            continue

    # If recording fails, don't prevent execution, but warn
    print("⚠️  Warning: Unable to record usage for billing. This may affect your quota tracking.")

def get_pricing_info() -> Dict[str, Any]:
    """Get current pricing information"""
    try:
        response = requests.get(f"{BIOQL_AUTH_URL}/pricing", timeout=5)
        if response.status_code == 200:
            return response.json()
    except:
        pass

    return {
        "message": "Visit https://bioql.com/pricing for current pricing",
        "free_tier": "1000 shots/month on simulator",
        "pro_tier": "$29/month - Real quantum hardware access",
        "enterprise": "$299/month - Unlimited access + priority support"
    }