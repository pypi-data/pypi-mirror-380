# MailWorks

A Python package for sending emails using any SMTP server with STARTTLS support. This package provides a simple, secure, and reliable way to send emails through any email provider including Gmail, Outlook, Yahoo, and more. Defaults to Gmail for convenience.

## Features

- ✅ **Universal SMTP Support** - Works with any SMTP provider (Gmail, Outlook, Yahoo, ProtonMail, etc.)
- ✅ **STARTTLS Security** - Secure email transmission with TLS encryption
- ✅ **Gmail Defaults** - Pre-configured for Gmail, works out of the box
- ✅ Support for plain text and HTML emails
- ✅ File attachments
- ✅ Multiple recipients
- ✅ Environment variable configuration
- ✅ Configuration file support
- ✅ Connection testing
- ✅ Comprehensive error handling
- ✅ No external dependencies (uses Python standard library only)
- ✅ Backward compatibility (GmailSender alias available)

## Installation

### From source (development)

```bash
# Clone the repository
git clone https://github.com/antoniocostabr/mailworks.git
cd mailworks

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### From PyPI (when published)

```bash
pip install mailworks
```

## Supported Email Providers

MailWorks supports any email provider that offers SMTP with STARTTLS encryption:

| Provider | SMTP Server | Port | Notes |
|----------|-------------|------|-------|
| **Gmail** | smtp.gmail.com | 587 | Default configuration |
| **Outlook/Hotmail** | smtp-mail.outlook.com | 587 | Microsoft email services |
| **Yahoo** | smtp.mail.yahoo.com | 587 | Requires app password |
| **ProtonMail** | mail.protonmail.ch | 587 | Secure email provider |
| **Zoho** | smtp.zoho.com | 587 | Business email |
| **SendGrid** | smtp.sendgrid.net | 587 | Email delivery service |
| **Amazon SES** | email-smtp.region.amazonaws.com | 587 | AWS email service |
| **Internal/Corporate** | mail.company.com | 25/587 | No authentication required |
| **Custom** | your.smtp.server | 587 | Any SMTP server with STARTTLS |

## Gmail Setup (if using Gmail)

For Gmail users, you need to set up App Passwords:

### Step 1: Enable 2-Factor Authentication

1. Go to [Google Account settings](https://myaccount.google.com/)
2. Navigate to "Security" > "2-Step Verification"
3. Enable 2-Step Verification if not already enabled

### Step 2: Generate App Password

1. Go to [Google Account settings](https://myaccount.google.com/)
2. Navigate to "Security" > "2-Step Verification" > "App passwords"
3. Select "Mail" and your device
4. Generate the app password
5. **Important**: Use this 16-character app password, not your regular Gmail password

## Quick Start

### Basic Usage (Gmail - Default)

```python
from mailworks import MailSender

# Using environment variables (Gmail defaults)
# Set environment variables:
# export EMAIL="your.email@gmail.com"
# export PASSWORD="your_app_password"

sender = MailSender()

# Send a simple email
success = sender.send_simple_email(
    to_email="recipient@example.com",
    subject="Hello from Python!",
    message="This is a test email sent from Python."
)

if success:
    print("Email sent successfully!")
```

### Using Other Email Providers

```python
from mailworks import MailSender

# Outlook/Hotmail
sender = MailSender(
    email="your.email@outlook.com",
    password="your_password",
    smtp_server="smtp-mail.outlook.com",
    smtp_port=587
)

# Yahoo
sender = MailSender(
    email="your.email@yahoo.com",
    password="your_app_password",
    smtp_server="smtp.mail.yahoo.com",
    smtp_port=587
)

# Custom SMTP server
sender = MailSender(
    email="your.email@yourdomain.com",
    password="your_password",
    smtp_server="mail.yourdomain.com",
    smtp_port=587
)
```

### Internal/Corporate SMTP Servers (No Authentication)

For internal corporate SMTP servers that don't require authentication or TLS:

> **⚠️ Security Note**: Authentication and TLS are enabled by default for security. Only disable them (`auth_required=False`, `use_tls=False`) for trusted internal SMTP servers within your corporate network.

```python
from mailworks import MailSender

# Corporate SMTP server without authentication or TLS
sender = MailSender(
    email="noreply@company.com",
    smtp_server="mail.company.com",
    smtp_port=25,  # Common for internal servers
    auth_required=False,  # Disable authentication
    use_tls=False  # Disable TLS for plain text internal servers
)

# Environment variables approach
# export EMAIL="noreply@company.com"
# export SMTP_SERVER="mail.company.com"
# export SMTP_PORT="25"
# export AUTH_REQUIRED="false"
# export USE_TLS="false"
sender = MailSender()

# Send HTML email with attachments to multiple recipients
success = sender.send_email(
    to_emails=["recipient1@example.com", "recipient2@example.com"],
    subject="Advanced Email Example",
    message="Plain text version of the email.",
    html_message="""
    <html>
        <body>
            <h2>Hello!</h2>
            <p>This is an <b>HTML email</b> with formatting.</p>
        </body>
    </html>
    """,
    attachments=["document.pdf", "image.png"]
)
```

## Configuration Options

### 1. Environment Variables (Recommended)

Set these environment variables:

```bash
# Required
export EMAIL="your.email@anyprovider.com"
export PASSWORD="your_app_password"  # Not required if AUTH_REQUIRED=false

# Optional (defaults to Gmail if not specified)
export SMTP_SERVER="smtp.anyprovider.com"
export SMTP_PORT="587"
export AUTH_REQUIRED="true"  # Set to "false" for servers without authentication
export USE_TLS="true"  # Set to "false" for plain text internal servers
```

### 2. Configuration File

Create a config file (e.g., `email_config.txt`):

```
EMAIL=your.email@anyprovider.com
PASSWORD=your_app_password
SMTP_SERVER=smtp.anyprovider.com
SMTP_PORT=587
AUTH_REQUIRED=true
USE_TLS=true
```

Use it in your code:

```python
from mailworks.config import ConfigManager

config_manager = ConfigManager.from_file("email_config.txt")
sender = MailSender(
    email=config_manager.config.email,
    password=config_manager.config.password,
    smtp_server=config_manager.config.smtp_server,
    smtp_port=config_manager.config.smtp_port
)
```

### 3. Direct Parameters

```python
from mailworks import MailSender

# Any SMTP provider
sender = MailSender(
    email="your.email@anyprovider.com",
    password="your_password",
    smtp_server="smtp.anyprovider.com",
    smtp_port=587
)

# Gmail (using defaults)
sender = MailSender(
    email="your.email@gmail.com",
    password="your_app_password"
)
```

## API Reference

### MailSender Class

#### Constructor

```python
MailSender(email=None, password=None, smtp_server=None, smtp_port=None, auth_required=None, use_tls=None)
```

- `email` (str, optional): Email address. If not provided, reads from `EMAIL` environment variable.
- `password` (str, optional): Email password/app password. If not provided, reads from `PASSWORD` environment variable. Not required if `auth_required=False`.
- `smtp_server` (str, optional): SMTP server address. If not provided, reads from `SMTP_SERVER` environment variable or defaults to Gmail.
- `smtp_port` (int, optional): SMTP port number. If not provided, reads from `SMTP_PORT` environment variable or defaults to 587.
- `auth_required` (bool, optional): Whether SMTP authentication is required. **Defaults to `True` for security**. If not provided, reads from `AUTH_REQUIRED` environment variable or defaults to `True`. Set to `False` only for trusted internal SMTP servers.
- `use_tls` (bool, optional): Whether to use STARTTLS encryption. **Defaults to `True` for security**. If not provided, reads from `USE_TLS` environment variable or defaults to `True`. Set to `False` only for plain text internal SMTP servers that don't support TLS.

#### Methods

##### `send_email(to_emails, subject, message, html_message=None, attachments=None)`

Send an email with advanced options.

**Parameters:**
- `to_emails` (str or list): Recipient email address(es)
- `subject` (str): Email subject
- `message` (str): Plain text message body
- `html_message` (str, optional): HTML message body
- `attachments` (list, optional): List of file paths to attach

**Returns:** `bool` - True if successful

##### `send_simple_email(to_email, subject, message)`

Send a simple text email to a single recipient.

**Parameters:**
- `to_email` (str): Recipient email address
- `subject` (str): Email subject
- `message` (str): Plain text message body

**Returns:** `bool` - True if successful

##### `test_connection()`

Test the connection to the configured SMTP server.

**Returns:** `bool` - True if connection successful

### GmailSender Class (Backward Compatibility)

For backward compatibility, `GmailSender` is available as an alias to `MailSender`:

```python
from mailworks import GmailSender  # Same as MailSender

sender = GmailSender(email="your@gmail.com", password="app_password")
```

### Exception Classes

- `EmailSenderError`: Base exception class
- `AuthenticationError`: Raised when SMTP authentication fails
- `SendError`: Raised when email sending fails
- `ConfigurationError`: Raised when configuration is invalid

## Examples

See the `examples/` directory for complete working examples:

- `basic_example.py`: Simple email sending using environment variables
- `advanced_example.py`: HTML emails with attachments and multiple recipients
- `smtp_providers_example.py`: Examples for different email providers
- `internal_smtp_example.py`: Using internal/corporate SMTP servers without authentication
- `config_example.py`: Different configuration methods

## Error Handling

```python
from mailworks import MailSender, AuthenticationError, SendError

try:
    sender = MailSender()
    sender.test_connection()

    success = sender.send_simple_email(
        to_email="recipient@example.com",
        subject="Test Email",
        message="Hello, World!"
    )

except AuthenticationError as e:
    print(f"Authentication failed: {e}")
    print("Check your email and password")

except SendError as e:
    print(f"Failed to send email: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
```

## Security Best Practices

1. **Use App Passwords**: Never use your regular Gmail password. Always use Gmail App Passwords.

2. **Environment Variables**: Store credentials in environment variables, not in your code.

3. **Config Files**: If using config files, add them to `.gitignore` to avoid committing credentials.

4. **Permissions**: Keep your app passwords secure and rotate them regularly.

## Common Issues & Solutions

### Authentication Error (535)

**Problem**: `smtplib.SMTPAuthenticationError: (535, '5.7.8 Username and Password not accepted')`

**Solutions**:
- Ensure you're using an App Password, not your regular Gmail password
- Check that 2-Factor Authentication is enabled on your Gmail account
- Verify the email address is correct
- Try generating a new App Password

### Connection Issues

**Problem**: Connection timeouts or failures

**Solutions**:
- Check your internet connection
- Ensure port 587 is not blocked by your firewall
- Try using a different network
- Verify SMTP server settings for your provider

### File Attachment Issues

**Problem**: Attachments not working

**Solutions**:
- Check that file paths exist and are accessible
- Ensure files are not too large (most providers have limits like 25MB for Gmail)
- Verify file permissions

## Migration Guide

### From v1.x (GmailSender only)

If you were using the old Gmail-only version:

```python
# Old way (still works)
from mailworks import GmailSender
sender = GmailSender(email="user@gmail.com", password="password")

# New recommended way
from mailworks import MailSender
sender = MailSender(email="user@gmail.com", password="password")
```

### Environment Variables

```bash
# Old variables (still supported for backward compatibility)
export GMAIL_EMAIL="your.email@gmail.com"
export GMAIL_PASSWORD="your_app_password"

# New recommended variables
export EMAIL="your.email@anyprovider.com"
export PASSWORD="your_app_password"
export SMTP_SERVER="smtp.anyprovider.com"  # Optional
export SMTP_PORT="587"                     # Optional
```

## Development

### Running Examples

```bash
# Set your credentials
export EMAIL="your.email@anyprovider.com"
export PASSWORD="your_app_password"

# Run examples
python examples/basic_example.py
python examples/advanced_example.py
python examples/config_example.py
```

### Testing

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests (when available)
pytest

# Code formatting
black mailworks/
black examples/

# Type checking
mypy mailworks/
```

## What's New in v2.0

🎉 **Universal SMTP Support**: No longer limited to Gmail! Now works with any email provider.

### Key Improvements:

- ✅ **Any SMTP Provider**: Gmail, Outlook, Yahoo, ProtonMail, custom servers, etc.
- ✅ **Clean Package Name**: `mailworks` instead of `email_sender`
- ✅ **Better Class Names**: `MailSender` instead of `GmailSender`
- ✅ **Simplified Configuration**: Generic environment variables (`EMAIL`, `PASSWORD`)
- ✅ **Backward Compatible**: Existing code continues to work
- ✅ **Enhanced Documentation**: Comprehensive examples for all providers

### Quick Comparison:

```python
# v1.x - Gmail only
from email_sender import GmailSender
sender = GmailSender(email="user@gmail.com", password="password")

# v2.x - Any provider
from mailworks import MailSender
sender = MailSender(
    email="user@outlook.com",
    password="password",
    smtp_server="smtp-mail.outlook.com",
    smtp_port=587
)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes and version information.

## Support

If you encounter any issues or have questions:

1. Check the [Common Issues](#common-issues--solutions) section
2. Look at the [examples](examples/) for usage patterns
3. Open an issue on [GitHub](https://github.com/antoniocostabr/mailworks/issues)

### v1.0.0
- Initial release
- Gmail SMTP support
- HTML email support
- File attachments
- Multiple recipients
- Configuration management
- Comprehensive error handling
