"""
cert2temp - SSL Certificate Temporary Folder Management Utility

Solves SSL certificate verification failures caused by non-ASCII characters (Korean, spaces, special characters) in certificate file paths.
Automatically creates safe ASCII-only temporary folders for each platform to copy certificates.

Features:
- Multi-platform support (Windows, Linux, macOS)
- Automatic SSL certificate temporary copying
- Smart folder cleanup (removes only folders we created)
- Automatic requests session configuration

Usage:
    from cert2temp import get_safe_cert_path, cleanup_temp_cert

    # Copy certificate file to safe path
    safe_cert_path = get_safe_cert_path(original_cert_path)

    # Use for SSL requests
    requests.get(url, verify=safe_cert_path)

    # Clean up after use
    cleanup_temp_cert(safe_cert_path)
"""

from .ssl_utils import (
    get_safe_cert_path,
    cleanup_temp_cert,
    cleanup_all_temp_certs,
    get_requests_session_with_safe_cert,
    get_platform_safe_temp_dir
)

__version__ = "0.1.0"
__author__ = "Minicom"
__email__ = "3387910@naver.com"
__description__ = "SSL Certificate Temporary Folder Management Utility"

__all__ = [
    'get_safe_cert_path',
    'cleanup_temp_cert',
    'cleanup_all_temp_certs',
    'get_requests_session_with_safe_cert',
    'get_platform_safe_temp_dir',
    '__version__',
    '__author__',
    '__description__'
]
