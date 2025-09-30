# Beem SMS Python SDK

A professional Python SDK for sending SMS via the Beem SMS API. This package provides a simple, robust, and feature-rich interface for integrating SMS functionality into your Python applications.

## Features

- **Easy to use** - Simple, intuitive API
- **Robust error handling** - Comprehensive exception handling and validation
- **Phone number validation** - Built-in phone number validation and formatting
- **Retry logic** - Automatic retry on failures with exponential backoff
- **Logging support** - Detailed logging for debugging and monitoring
- **Type hints** - Full type hint support for better IDE experience
- **Security** - Secure credential handling
- **Bulk SMS** - Efficient bulk SMS sending with batching
- **Well tested** - Comprehensive test suite
- **CLI tool** - Command-line interface for quick operations

## Installation

```bash
pip install beem-sms-python
```

### Development Installation

```bash
git clone https://github.com/islandkid-20/beem-sms-python.git
cd beem-sms-python
pip install -e .[dev]
```

## Quick Start

### Basic Usage

```python
from beem_sms import BeemSMSClient

# Initialize client
client = BeemSMSClient(
    api_key="your_api_key",
    secret_key="your_secret_key"
)

# Send SMS
response = client.send_sms(
    source_addr="YourApp",
    dest_addr="+255742892731",
    message="Hello from Beem SMS!"
)

if response.success:
    print(f"SMS sent! Request ID: {response.request_id}")
else:
    print(f"Failed: {response.message}")
```

### Using Context Manager

```python
from beem_sms import BeemSMSClient

with BeemSMSClient("api_key", "secret_key") as client:
    response = client.send_sms(
        source_addr="YourApp",
        dest_addr="+255742892731", 
        message="Hello World!"
    )
```

### Bulk SMS

```python
recipients = ["+255742892731", "+255783346386", "+255713521250"]

results = client.send_bulk_sms(
    source_addr="YourApp",
    recipients=recipients,
    message="Bulk SMS message",
    batch_size=10
)

successful = sum(1 for r in results if r.success)
print(f"Sent {successful}/{len(results)} batches successfully")
```

### Convenience Function

```python
from beem_sms import send_sms

response = send_sms(
    api_key="your_api_key",
    secret_key="your_secret_key",
    source_addr="YourApp",
    dest_addr="+255742892731",
    message="Quick SMS!"
)
```

## CLI Usage

The package includes a command-line tool for quick SMS operations:

### Send SMS

```bash
beem-sms send --api-key YOUR_KEY --secret-key YOUR_SECRET \
    --sender "YourApp" --message "Hello CLI!" \
    --recipients "+255742892731" "+255783346386"
```

### Send Bulk SMS from File

```bash
# Create recipients.txt with one phone number per line
echo "+255742892731" > recipients.txt
echo "+255783346386" >> recipients.txt

beem-sms send --sender "YourApp" --message "Bulk message" \
    --file recipients.txt --bulk --batch-size 50
```

### Validate Phone Numbers

```bash
beem-sms validate --numbers "+255742892731" "0783346386" "invalid"
```

### Configuration File

Create `~/.beem_sms.json`:

```json
{
    "api_key": "your_api_key",
    "secret_key": "your_secret_key"
}
```

Then use CLI without credentials:

```bash
beem-sms send --sender "YourApp" --message "Hello!" \
    --recipients "+255742892731"
```

## Error Handling

The SDK provides specific exceptions for different error scenarios:

```python
from beem_sms import (
    BeemSMSClient,
    AuthenticationError,
    ValidationError,
    APIError,
    NetworkError
)

client = BeemSMSClient("api_key", "secret_key")

try:
    response = client.send_sms(
        source_addr="YourApp",
        dest_addr="+255742892731",
        message="Test message"
    )
except AuthenticationError:
    print("Invalid API credentials")
except ValidationError as e:
    print(f"Invalid input: {e}")
except NetworkError:
    print("Network connection failed")
except APIError as e:
    print(f"API error: {e}")
```

## Phone Number Validation

```python
from beem_sms import PhoneNumberValidator

# Validate single number
is_valid = PhoneNumberValidator.validate("+255742892731")

# Clean and format number
clean_number = PhoneNumberValidator.clean("0742892731")
# Returns: "+255742892731"

# Validate batch
numbers = ["+255742892731", "invalid", "0783346386"]
results = PhoneNumberValidator.validate_batch(numbers)
# Returns: [True, False, True]
```

## Advanced Configuration

```python
import logging

# Custom logger
logger = logging.getLogger("my_app")

client = BeemSMSClient(
    api_key="your_api_key",
    secret_key="your_secret_key",
    base_url="https://custom-endpoint.com/v1/send",  # Custom endpoint
    timeout=60,  # 60 second timeout
    max_retries=5,  # 5 retry attempts
    logger=logger  # Custom logger
)
```

## API Reference

### BeemSMSClient

#### Methods

- `send_sms(source_addr, dest_addr, message, encoding=SMSEncoding.PLAIN_TEXT)` - Send SMS to single or multiple recipients
- `send_bulk_sms(source_addr, recipients, message, encoding, batch_size=100)` - Send bulk SMS with batching

#### Parameters

- `source_addr` (str): Sender ID or phone number
- `dest_addr` (str | List[str]): Recipient phone number(s)
- `message` (str): SMS message content
- `encoding` (SMSEncoding): Message encoding (PLAIN_TEXT or UNICODE)

### SMSResponse

Response object with the following attributes:

- `success` (bool): Whether the operation succeeded
- `status_code` (int): HTTP status code
- `message` (str): Response message
- `response_data` (dict): Raw API response data
- `request_id` (str): Request ID for tracking

### Exceptions

- `SMSError` - Base exception
- `AuthenticationError` - Invalid credentials
- `ValidationError` - Invalid input parameters
- `APIError` - API request failed
- `NetworkError` - Network/connection issues

## Testing

Run the test suite:

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test file
pytest tests/test_client.py -v
```

## Development

Set up development environment:

```bash
make dev-setup
```

Run code quality checks:

```bash
make check  # Runs format-check, lint, type-check, and test
```

Format code:

```bash
make format
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and code quality checks (`make check`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Email: j1997ames@gmail.com
- Issues: [GitHub Issues](https://github.com/islandkid-20/beem-sms-python/issues)
- Documentation: [Read the Docs](https://beem-sms-python.readthedocs.io/)

## Changelog

### v1.0.3

* Added Read the Docs documentation support:
  * Created `.readthedocs.yml` configuration file
  * Set up Sphinx documentation with MyST parser
  * Added documentation dependencies (sphinx, sphinx-rtd-theme, myst-parser)
  * Documentation now auto-syncs with README.md content
  * Added support for PDF and EPUB formats
  * Documentation available at: https://beem-sms-python.readthedocs.io/

### v1.0.2

* Adjusted message length limits to support multi-part SMS:
  * Increased `MAX_MESSAGE_LENGTH` from `160` to `153 * 3`
  * Increased `MAX_UNICODE_LENGTH` from `70` to `67 * 3`

### v1.0.1

- Initial release
- Basic SMS sending functionality
- Bulk SMS support
- Phone number validation
- CLI tool
- Comprehensive test suite