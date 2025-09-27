"""
MailWorks - Universal SMTP Email Sender

A Python package for sending emails using any SMTP server with STARTTLS support.
This package provides a simple, secure, and reliable way to send emails through
any email provider including Gmail, Outlook, Yahoo, and more.
"""

from .mail_sender import MailSender
from .exceptions import SendError, ConfigurationError

# Maintain backward compatibility with the old class name
GmailSender = MailSender

__version__ = "2.2.0"
