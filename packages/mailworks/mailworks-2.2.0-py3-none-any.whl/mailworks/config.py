"""
Configuration management for the email sender package.
"""

import os
from typing import Optional
from dataclasses import dataclass
from pathlib import Path

from .exceptions import ConfigurationError


@dataclass
class EmailConfig:
    """Configuration for SMTP email settings."""
    email: str
    password: str
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587


class ConfigManager:
    """
    Manages configuration for the email sender package.

    Handles loading configuration from environment variables,
    config files, or direct parameters.
    """

    def __init__(self):
        self._config = None

    @classmethod
    def from_env(cls) -> 'ConfigManager':
        """
        Create a ConfigManager using environment variables.

        Expected environment variables:
        - EMAIL: Email address
        - PASSWORD: Email app password
        - SMTP_SERVER: SMTP server (optional, defaults to smtp.gmail.com)
        - SMTP_PORT: SMTP port (optional, defaults to 587)

        Returns:
            ConfigManager: Configured instance

        Raises:
            ConfigurationError: If required environment variables are missing
        """
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.getenv('SMTP_PORT', '587'))

        if not email:
            raise ConfigurationError("EMAIL environment variable is required")
        if not password:
            raise ConfigurationError("PASSWORD environment variable is required")

        manager = cls()
        manager._config = EmailConfig(
            email=email,
            password=password,
            smtp_server=smtp_server,
            smtp_port=smtp_port
        )
        return manager

    @classmethod
    def from_file(cls, config_path: str) -> 'ConfigManager':
        """
        Create a ConfigManager using a configuration file.

        The config file should be in the format:
        EMAIL=your.email@anyprovider.com
        PASSWORD=your_app_password
        SMTP_SERVER=smtp.anyprovider.com
        SMTP_PORT=587

        Args:
            config_path: Path to the configuration file

        Returns:
            ConfigManager: Configured instance

        Raises:
            ConfigurationError: If config file is invalid or missing required values
        """
        config_file = Path(config_path)
        if not config_file.exists():
            raise ConfigurationError(f"Configuration file not found: {config_path}")

        config_vars = {}
        try:
            with open(config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        config_vars[key.strip()] = value.strip()
        except Exception as e:
            raise ConfigurationError(f"Failed to read config file: {str(e)}")

        email = config_vars.get('EMAIL')
        password = config_vars.get('PASSWORD')
        smtp_server = config_vars.get('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(config_vars.get('SMTP_PORT', '587'))

        if not email:
            raise ConfigurationError("EMAIL is required in config file")
        if not password:
            raise ConfigurationError("PASSWORD is required in config file")

        manager = cls()
        manager._config = EmailConfig(
            email=email,
            password=password,
            smtp_server=smtp_server,
            smtp_port=smtp_port
        )
        return manager

    @classmethod
    def from_parameters(cls, email: str, password: str,
                       smtp_server: str = "smtp.gmail.com",
                       smtp_port: int = 587) -> 'ConfigManager':
        """
        Create a ConfigManager using direct parameters.

        Args:
            email: Email address for any SMTP provider
            password: Email app password or regular password
            smtp_server: SMTP server address (defaults to Gmail)
            smtp_port: SMTP port number (defaults to 587 for STARTTLS)

        Returns:
            ConfigManager: Configured instance
        """
        manager = cls()
        manager._config = EmailConfig(
            email=email,
            password=password,
            smtp_server=smtp_server,
            smtp_port=smtp_port
        )
        return manager

    @property
    def config(self) -> Optional[EmailConfig]:
        """Get the current configuration."""
        return self._config

    def validate(self) -> bool:
        """
        Validate the current configuration.

        Returns:
            bool: True if configuration is valid

        Raises:
            ConfigurationError: If configuration is invalid
        """
        if not self._config:
            raise ConfigurationError("No configuration loaded")

        if not self._config.email:
            raise ConfigurationError("Email is required")

        if not self._config.password:
            raise ConfigurationError("Password is required")

        if '@' not in self._config.email:
            raise ConfigurationError("Invalid email format")

        return True
