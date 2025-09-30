# cert2temp

SSL Certificate Temporary Folder Management Utility

[![PyPI version](https://badge.fury.io/py/cert2temp.svg)](https://pypi.org/project/cert2temp/)
[![Python versions](https://img.shields.io/pypi/pyversions/cert2temp.svg)](https://pypi.org/project/cert2temp/)
[![License](https://img.shields.io/pypi/l/cert2temp.svg)](https://pypi.org/project/cert2temp/)

## Problem Solved

Solves SSL certificate verification failures caused by non-ASCII characters (Korean, spaces, special characters) in certificate file paths.
Automatically creates safe ASCII-only temporary folders for each platform to copy certificates.

### Supported Platforms

- **Windows**: `C:\Temp` (always ASCII)
- **Linux**: `/tmp` (already ASCII)
- **macOS**: `/tmp` (already ASCII)
- **Others**: System default temporary directory

## Installation

```bash
pip install cert2temp
```

## Usage

### Basic Usage

```python
from cert2temp import get_safe_cert_path, cleanup_temp_cert

# Copy certificate file to safe path
safe_cert_path = get_safe_cert_path(original_cert_path)

# Use for SSL requests
import requests
response = requests.get(url, verify=safe_cert_path)

# Clean up after use
cleanup_temp_cert(safe_cert_path)
```

### Using with requests Session

```python
from cert2temp import get_requests_session_with_safe_cert

# Create requests session with safe certificate
session = get_requests_session_with_safe_cert()
response = session.get(url)
```

### Using with Yahoo Finance API

```python
import yfinance as yf
from cert2temp import get_requests_session_with_safe_cert

# Bypass Yahoo Finance 429 errors with curl_cffi session
session = get_requests_session_with_safe_cert()
ticker = yf.Ticker("AAPL", session=session)
data = ticker.history(period="1mo")
```

## API Reference

### `get_safe_cert_path(cert_path=None)`

Copy certificate file to temporary folder and return safe path.

**Parameters:**
- `cert_path` (str, optional): Original certificate file path. Uses default certificate if None

**Returns:**
- Safe certificate file path (str)

### `cleanup_temp_cert(cert_path)`

Clean up temporary certificate file.

**Parameters:**
- `cert_path` (str): Temporary certificate file path

**Returns:**
- True if cleanup successful, False otherwise (bool)

### `cleanup_all_temp_certs()`

Clean up all temporary certificate files.

**Returns:**
- Number of files cleaned up (int)

### `get_requests_session_with_safe_cert(cert_path=None)`

Create a requests session using safe certificate path.

**Parameters:**
- `cert_path` (str, optional): Original certificate file path

**Returns:**
- requests.Session object

### `get_platform_safe_temp_dir()`

Returns a safe ASCII-only temporary directory path for each platform.

**Returns:**
- Platform-specific safe temporary directory Path object

## Advanced Features

### Smart Folder Cleanup

cert2temp handles temporary folder cleanup intelligently:

- **Original folders**: Preserved (user folders)
- **Empty folders we created**: Removed (automatic cleanup)

### Multi-platform Support

Works with the same API on all major platforms:

```python
# Windows uses C:\Temp
# Linux/macOS uses /tmp
safe_dir = get_platform_safe_temp_dir()
```

### Caching Feature

Copies and reuses the same certificate file only once:

```python
# First call: File copy
path1 = get_safe_cert_path("cert.pem")

# Second call: Return cached path
path2 = get_safe_cert_path("cert.pem")
assert path1 == path2  # True
```

## License

MIT License

## Contributing

Bug reports and feature requests are welcome at [GitHub Issues](https://github.com/minicom365/cert2temp/issues).

## Developer Information

- **Author**: Minicom
- **Email**: 3387910@naver.com
- **GitHub**: https://github.com/minicom365/cert2temp
