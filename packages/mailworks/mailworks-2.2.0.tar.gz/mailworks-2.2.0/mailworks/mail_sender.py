"""
Mail Email Sender

A class for sending emails using any SMTP server with STARTTLS support.

This module supports any email provider that offers SMTP with STARTTLS encryption,
including but not limited to:
- Gmail (smtp.gmail.com:587)
- Outlook/Hotmail (smtp-mail.outlook.com:587)
- Yahoo (smtp.mail.yahoo.com:587)
- ProtonMail (mail.protonmail.ch:587)
- Zoho (smtp.zoho.com:587)
- SendGrid (smtp.sendgrid.net:587)
- Amazon SES (email-smtp.region.amazonaws.com:587)
- Internal/Corporate SMTP servers (with or without authentication)

Default configuration is set for Gmail for convenience.
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from typing import List, Optional, Union
from pathlib import Path

from .exceptions import AuthenticationError, SendError, ConfigurationError


class MailSender:
    """
    A class for sending emails using any SMTP server with STARTTLS support.

    This class provides a simple interface for sending emails through any SMTP provider
    that supports STARTTLS encryption. Also supports internal SMTP servers without authentication.
    Defaults to Gmail settings for convenience.
    """

    def __init__(self,
                 email: Optional[str] = None,
                 password: Optional[str] = None,
                 smtp_server: Optional[str] = None,
                 smtp_port: Optional[int] = None,
                 auth_required: Optional[bool] = None,
                 use_tls: Optional[bool] = None):
        """
        Initialize the Mail sender.

        Args:
            email: Email address. If not provided, will look for EMAIL env var
            password: Email password/app password. If not provided, will look for PASSWORD env var (ignored if auth_required=False)
            smtp_server: SMTP server address. If not provided, will look for SMTP_SERVER env var or default to Gmail
            smtp_port: SMTP port number. If not provided, will look for SMTP_PORT env var or default to 587
            auth_required: Whether SMTP authentication is required. If not provided, will look for AUTH_REQUIRED env var or default to True
            use_tls: Whether to use STARTTLS encryption. If not provided, will look for USE_TLS env var or default to True

        Raises:
            ConfigurationError: If email is not provided or if password is missing when auth_required=True
        """
        self.email = email or os.getenv('EMAIL')
        self.password = password or os.getenv('PASSWORD')
        self.smtp_server = smtp_server or os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = smtp_port or int(os.getenv('SMTP_PORT', '587'))

        # Handle auth_required parameter
        if auth_required is not None:
            self.auth_required = auth_required
        else:
            auth_env = os.getenv('AUTH_REQUIRED', 'true').lower()
            self.auth_required = auth_env in ('true', '1', 'yes', 'on')

        # Handle use_tls parameter
        if use_tls is not None:
            self.use_tls = use_tls
        else:
            tls_env = os.getenv('USE_TLS', 'true').lower()
            self.use_tls = tls_env in ('true', '1', 'yes', 'on')

        if not self.email:
            raise ConfigurationError("Email is required. Provide it as parameter or set EMAIL environment variable.")

        if self.auth_required and not self.password:
            raise ConfigurationError("Password is required when authentication is enabled. Provide it as parameter or set PASSWORD environment variable, or set auth_required=False for servers that don't require authentication.")

    def send_email(self,
                   to_emails: Union[str, List[str]],
                   subject: str,
                   message: str,
                   html_message: Optional[str] = None,
                   attachments: Optional[List[Union[str, Path]]] = None) -> bool:
        """
        Send an email using SMTP with STARTTLS.

        Args:
            to_emails: Recipient email address(es)
            subject: Email subject
            message: Plain text message body
            html_message: Optional HTML message body
            attachments: Optional list of file paths to attach

        Returns:
            bool: True if email was sent successfully

        Raises:
            AuthenticationError: If SMTP authentication fails
            SendError: If email sending fails
        """
        try:
            # Convert single email to list
            if isinstance(to_emails, str):
                to_emails = [to_emails]

            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = self.email
            msg['To'] = ', '.join(to_emails)
            msg['Subject'] = subject

            # Add plain text part
            text_part = MIMEText(message, 'plain')
            msg.attach(text_part)

            # Add HTML part if provided
            if html_message:
                html_part = MIMEText(html_message, 'html')
                msg.attach(html_part)

            # Add attachments if provided
            if attachments:
                for attachment_path in attachments:
                    self._add_attachment(msg, attachment_path)

            # Create SMTP session
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                # Enable TLS encryption if required
                if self.use_tls:
                    server.starttls()

                # Only authenticate if required
                if self.auth_required:
                    try:
                        server.login(self.email, self.password)
                    except smtplib.SMTPAuthenticationError as e:
                        raise AuthenticationError(f"Failed to authenticate with SMTP server: {str(e)}")

                # Send email
                text = msg.as_string()
                server.sendmail(self.email, to_emails, text)

            return True

        except AuthenticationError:
            raise
        except Exception as e:
            raise SendError(f"Failed to send email: {str(e)}")

    def _add_attachment(self, msg: MIMEMultipart, file_path: Union[str, Path]) -> None:
        """
        Add an attachment to the email message.

        Args:
            msg: The email message object
            file_path: Path to the file to attach

        Raises:
            SendError: If attachment cannot be added
        """
        try:
            file_path = Path(file_path)

            if not file_path.exists():
                raise SendError(f"Attachment file not found: {file_path}")

            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {file_path.name}'
            )

            # Attach the part to message
            msg.attach(part)

        except Exception as e:
            raise SendError(f"Failed to add attachment {file_path}: {str(e)}")

    def send_simple_email(self, to_email: str, subject: str, message: str) -> bool:
        """
        Send a simple text email to a single recipient.

        Args:
            to_email: Recipient email address
            subject: Email subject
            message: Plain text message body

        Returns:
            bool: True if email was sent successfully
        """
        return self.send_email(to_email, subject, message)

    def test_connection(self) -> bool:
        """
        Test the connection to the SMTP server.

        Returns:
            bool: True if connection and authentication successful (if required)

        Raises:
            AuthenticationError: If authentication fails
            SendError: If connection fails
        """
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                # Enable TLS encryption if required
                if self.use_tls:
                    server.starttls()

                # Only test authentication if required
                if self.auth_required:
                    server.login(self.email, self.password)
            return True
        except smtplib.SMTPAuthenticationError as e:
            raise AuthenticationError(f"Authentication failed: {str(e)}")
        except Exception as e:
            raise SendError(f"Connection test failed: {str(e)}")
