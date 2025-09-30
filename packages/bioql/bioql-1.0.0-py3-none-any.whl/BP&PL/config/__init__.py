"""
Configuration management for BioQL billing system.
"""

import os
import yaml
from typing import Dict, Any, Optional
from pathlib import Path


class ConfigManager:
    """Centralized configuration management."""

    def __init__(self, config_dir: Optional[str] = None):
        """
        Initialize configuration manager.

        Args:
            config_dir: Directory containing configuration files
        """
        if config_dir:
            self.config_dir = Path(config_dir)
        else:
            self.config_dir = Path(__file__).parent

        self._configs: Dict[str, Any] = {}
        self._load_all_configs()

    def _load_all_configs(self):
        """Load all YAML configuration files."""
        config_files = ['pricing.yaml', 'database.yaml', 'api.yaml']

        for config_file in config_files:
            config_path = self.config_dir / config_file
            if config_path.exists():
                config_name = config_file.replace('.yaml', '')
                self._configs[config_name] = self._load_yaml(config_path)

    def _load_yaml(self, file_path: Path) -> Dict[str, Any]:
        """Load YAML configuration file."""
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    def get_pricing_config(self) -> Dict[str, Any]:
        """Get pricing configuration."""
        return self._configs.get('pricing', {})

    def get_database_config(self) -> Dict[str, Any]:
        """Get database configuration."""
        config = self._configs.get('database', {})

        # Override with environment variables if present
        env_url = os.getenv('DATABASE_URL')
        if env_url:
            config['database'] = config.get('database', {})
            config['database']['primary'] = config['database'].get('primary', {})
            config['database']['primary']['url'] = env_url

        return config

    def get_api_config(self) -> Dict[str, Any]:
        """Get API configuration."""
        config = self._configs.get('api', {})

        # Override with environment variables
        env_overrides = {
            'server.host': os.getenv('API_HOST'),
            'server.port': os.getenv('API_PORT'),
            'server.debug': os.getenv('API_DEBUG', '').lower() == 'true',
            'authentication.jwt.secret_key': os.getenv('JWT_SECRET_KEY'),
            'security.force_https': os.getenv('FORCE_HTTPS', '').lower() == 'true'
        }

        for key, value in env_overrides.items():
            if value is not None:
                self._set_nested_value(config, key, value)

        return config

    def get_stripe_config(self) -> Dict[str, Any]:
        """Get Stripe configuration from environment."""
        return {
            'secret_key': os.getenv('STRIPE_SECRET_KEY'),
            'publishable_key': os.getenv('STRIPE_PUBLISHABLE_KEY'),
            'webhook_secret': os.getenv('STRIPE_WEBHOOK_SECRET'),
            'enabled': bool(os.getenv('STRIPE_SECRET_KEY'))
        }

    def get_redis_config(self) -> Dict[str, Any]:
        """Get Redis configuration."""
        return {
            'url': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
            'enabled': bool(os.getenv('REDIS_URL'))
        }

    def _set_nested_value(self, config: Dict[str, Any], key: str, value: Any):
        """Set nested configuration value using dot notation."""
        keys = key.split('.')
        current = config

        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]

        current[keys[-1]] = value


# Global configuration instance
config = ConfigManager()


def get_pricing_config() -> Dict[str, Any]:
    """Get pricing configuration."""
    return config.get_pricing_config()


def get_database_config() -> Dict[str, Any]:
    """Get database configuration."""
    return config.get_database_config()


def get_api_config() -> Dict[str, Any]:
    """Get API configuration."""
    return config.get_api_config()


def get_stripe_config() -> Dict[str, Any]:
    """Get Stripe configuration."""
    return config.get_stripe_config()


def get_redis_config() -> Dict[str, Any]:
    """Get Redis configuration."""
    return config.get_redis_config()