"""
Custom exceptions for the email sender package.
"""


class EmailSenderError(Exception):
    """Base exception class for email sender errors."""
    pass


class AuthenticationError(EmailSenderError):
    """Raised when authentication with Gmail fails."""
    pass


class SendError(EmailSenderError):
    """Raised when email sending fails."""
    pass


class ConfigurationError(EmailSenderError):
    """Raised when configuration is invalid or missing."""
    pass
