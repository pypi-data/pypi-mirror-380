"""
SSL Certificate Utility Module (Multi-platform Support)

Solves SSL certificate verification failures caused by non-ASCII characters (Korean, spaces, special characters) in certificate file paths.
Automatically creates safe ASCII-only temporary folders for each platform to copy certificates.

Supported Platforms:
- Windows: C:\Temp (always ASCII)
- Linux: /tmp (already ASCII)
- macOS: /tmp (already ASCII)
- Others: System default temporary directory

Usage:
    from cert2temp import get_safe_cert_path, cleanup_temp_cert

    # Copy certificate file to safe path
    safe_cert_path = get_safe_cert_path(original_cert_path)

    # Use for SSL requests
    requests.get(url, verify=safe_cert_path)

    # Clean up after use
    cleanup_temp_cert(safe_cert_path)
"""

import os
import tempfile
import shutil
import logging
import platform
from pathlib import Path
from typing import Optional, Dict
import atexit

logger = logging.getLogger(__name__)

# 전역 인증서 캐시 (한번 복사한 인증서를 재사용)
_cert_cache: Dict[str, str] = {}
_temp_cert_files: Dict[str, str] = {}

# 플랫폼별 기본 임시 폴더 생성 기록 (우리가 만든 폴더인지 추적)
_created_base_dirs: Dict[str, bool] = {}


def get_platform_safe_temp_dir() -> Path:
    """
    Returns a safe ASCII-only temporary directory path for each platform.

    Returns:
        Platform-specific safe temporary directory Path object

    Note:
        - Windows: C:\Temp (always ASCII)
        - Linux: /tmp (already ASCII)
        - macOS: /tmp (already ASCII)
        - Others: System default temporary directory
    """
    system = platform.system().lower()

    if system == "windows":
        # Windows: Use C:\Temp folder (always ASCII)
        safe_temp = Path("C:\\Temp")
    elif system == "linux":
        # Linux: Use /tmp (already ASCII)
        safe_temp = Path("/tmp")
    elif system == "darwin":  # macOS
        # macOS: Use /tmp (already ASCII)
        safe_temp = Path("/tmp")
    else:
        # Other platforms: Use system default temporary directory
        safe_temp = Path(tempfile.gettempdir())

    # Create directory if it doesn't exist (record creation status)
    base_dir_str = str(safe_temp)
    existed_before = safe_temp.exists()

    try:
        safe_temp.mkdir(parents=True, exist_ok=True)

        # Record whether we created the folder (if it didn't exist before)
        if not existed_before and safe_temp.exists():
            _created_base_dirs[base_dir_str] = True
            logger.debug(f"Platform safe temporary directory created: {safe_temp} ({system})")
        else:
            _created_base_dirs[base_dir_str] = False
            logger.debug(f"Platform safe temporary directory already exists: {safe_temp} ({system})")

    except (OSError, PermissionError) as e:
        logger.warning(f"Safe temporary directory creation failed, using system default: {e}")
        # fallback: system default temporary directory
        safe_temp = Path(tempfile.gettempdir())
        _created_base_dirs[str(safe_temp)] = False  # system default is not created by us

    return safe_temp


def get_safe_cert_path(cert_path: Optional[str] = None) -> Optional[str]:
    """
    Copy certificate file to temporary folder and return safe path.
    Once copied, certificates are cached and reused.

    Args:
        cert_path: Original certificate file path. Uses default certificate if None.

    Returns:
        Safe certificate file path. Returns None if copy fails.

    Note:
        Temporary files are automatically cleaned up when the program exits.
    """
    if cert_path is None:
        # Use default certificate path (certifi library)
        try:
            import certifi
            cert_path = certifi.where()
        except ImportError:
            logger.warning("certifi library not found, skipping certificate verification")
            return None

    # Check cache (if certificate already copied)
    if cert_path in _cert_cache:
        cached_path = _cert_cache[cert_path]
        if os.path.exists(cached_path):
            logger.debug(f"Using cached certificate file: {cached_path}")
            return cached_path

    if not os.path.exists(cert_path):
        logger.warning(f"Certificate file not found: {cert_path}")
        return None

    try:
        # Copy certificate file to temporary folder (solve Korean/special character path issues)
        # Create ASCII-safe path using Python tempfile

        # Get platform-safe temporary directory
        safe_temp_dir = get_platform_safe_temp_dir()

        # Create subfolder for certificate in safe temporary directory
        temp_dir = tempfile.mkdtemp(prefix="ssl_cert_", dir=str(safe_temp_dir))
        logger.debug(f"Created subfolder in platform-safe temp folder: {temp_dir}")

        temp_cert_path = os.path.join(temp_dir, "cacert.pem")

        # Copy file
        shutil.copy2(cert_path, temp_cert_path)

        # Store in cache
        _cert_cache[cert_path] = temp_cert_path
        _temp_cert_files[temp_cert_path] = temp_dir

        logger.info(f"Certificate file copied to safe path: {temp_cert_path}")
        return temp_cert_path

    except Exception as e:
        error_name = type(e).__name__
        logger.error(f"Certificate file copy failed: [{error_name}] {e}")
        return None


def cleanup_temp_cert(cert_path: str) -> bool:
    """
    Clean up temporary certificate file.

    Args:
        cert_path: Temporary certificate file path

    Returns:
        True if cleanup successful, False otherwise
    """
    if cert_path not in _temp_cert_files:
        return False

    try:
        temp_dir = _temp_cert_files[cert_path]

        # Delete temporary file
        if os.path.exists(cert_path):
            os.remove(cert_path)

        # Delete temporary subfolder (ssl_cert_xxxxx)
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)

        # Check if base folder (C:\Temp, etc.) was created by us and clean up
        # Check if parent folder of temp_dir is a base folder we created
        parent_dir = os.path.dirname(temp_dir)
        if parent_dir in _created_base_dirs and _created_base_dirs[parent_dir]:
            try:
                # Delete if it's a base folder we created
                if os.path.exists(parent_dir):
                    os.rmdir(parent_dir)
                    logger.info(f"Cleaned up base temporary folder we created: {parent_dir}")
                    del _created_base_dirs[parent_dir]
            except (OSError, FileNotFoundError):
                # Ignore if folder is not empty or already deleted
                pass

        # Remove from tracking list
        del _temp_cert_files[cert_path]

        logger.info(f"Temporary certificate file cleaned up: {cert_path}")
        return True

    except Exception as e:
        error_name = type(e).__name__
        logger.error(f"Temporary certificate file cleanup failed: [{error_name}] {e}")
        return False


def cleanup_all_temp_certs() -> int:
    """
    Clean up all temporary certificate files.

    Returns:
        Number of files cleaned up
    """
    cleaned_count = 0
    for cert_path in list(_temp_cert_files.keys()):
        if cleanup_temp_cert(cert_path):
            cleaned_count += 1

    if cleaned_count > 0:
        logger.info(f"Cleaned up {cleaned_count} temporary certificate files")

    return cleaned_count


def get_requests_session_with_safe_cert(cert_path: Optional[str] = None):
    """
    Create a requests session using safe certificate path.

    Args:
        cert_path: Original certificate file path

    Returns:
        requests.Session object
    """
    try:
        import requests

        session = requests.Session()
        safe_cert_path = get_safe_cert_path(cert_path)

        if safe_cert_path:
            session.verify = safe_cert_path
            logger.info("Set safe certificate path for requests session")
        else:
            # Disable SSL verification if safe certificate path not available
            session.verify = False
            logger.warning("Safe certificate path not available, disabling SSL verification")

        return session

    except ImportError:
        logger.error("requests library is not installed")
        return None


# Register automatic cleanup on program exit
atexit.register(cleanup_all_temp_certs)

# Expose cleanup functions at module level
__all__ = [
    'get_safe_cert_path',
    'cleanup_temp_cert',
    'cleanup_all_temp_certs',
    'get_requests_session_with_safe_cert'
]
