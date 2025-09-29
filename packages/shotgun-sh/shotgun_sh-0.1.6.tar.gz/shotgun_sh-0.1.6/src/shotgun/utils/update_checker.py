"""Auto-update functionality for shotgun-sh CLI."""

import json
import subprocess
import sys
import threading
from collections.abc import Callable
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx
from packaging import version
from pydantic import BaseModel, Field, ValidationError

from shotgun import __version__
from shotgun.logging_config import get_logger
from shotgun.utils.file_system_utils import get_shotgun_home

logger = get_logger(__name__)

# Configuration constants
UPDATE_CHECK_INTERVAL = timedelta(hours=24)
PYPI_API_URL = "https://pypi.org/pypi/shotgun-sh/json"
REQUEST_TIMEOUT = 5.0  # seconds


def get_cache_file() -> Path:
    """Get the path to the update cache file.

    Returns:
        Path to the cache file in the shotgun home directory.
    """
    return get_shotgun_home() / "check-update.json"


class UpdateCache(BaseModel):
    """Model for update check cache data."""

    last_check: datetime = Field(description="Last time update check was performed")
    latest_version: str = Field(description="Latest version available on PyPI")
    current_version: str = Field(description="Current installed version at check time")
    update_available: bool = Field(
        default=False, description="Whether an update is available"
    )


def is_dev_version(version_str: str | None = None) -> bool:
    """Check if the current or given version is a development version.

    Args:
        version_str: Version string to check. If None, uses current version.

    Returns:
        True if version contains 'dev', False otherwise.
    """
    check_version = version_str or __version__
    return "dev" in check_version.lower()


def load_cache() -> UpdateCache | None:
    """Load the update check cache from disk.

    Returns:
        UpdateCache model if cache exists and is valid, None otherwise.
    """
    cache_file = get_cache_file()
    if not cache_file.exists():
        return None

    try:
        with open(cache_file) as f:
            data = json.load(f)
            return UpdateCache.model_validate(data)
    except (json.JSONDecodeError, OSError, PermissionError, ValidationError) as e:
        logger.debug(f"Failed to load cache: {e}")
        return None


def save_cache(cache_data: UpdateCache) -> None:
    """Save update check cache to disk.

    Args:
        cache_data: UpdateCache model containing cache data to save.
    """
    cache_file = get_cache_file()

    try:
        # Ensure the parent directory exists
        cache_file.parent.mkdir(parents=True, exist_ok=True)

        with open(cache_file, "w") as f:
            json.dump(cache_data.model_dump(mode="json"), f, indent=2, default=str)
    except (OSError, PermissionError) as e:
        logger.debug(f"Failed to save cache: {e}")


def should_check_for_updates(no_update_check: bool = False) -> bool:
    """Determine if we should check for updates.

    Args:
        no_update_check: If True, skip update checks.

    Returns:
        True if update check should be performed, False otherwise.
    """
    # Skip if explicitly disabled
    if no_update_check:
        return False

    # Skip if development version
    if is_dev_version():
        logger.debug("Skipping update check for development version")
        return False

    # Check cache to see if enough time has passed
    cache = load_cache()
    if not cache:
        return True

    now = datetime.now(timezone.utc)
    time_since_check = now - cache.last_check
    return time_since_check >= UPDATE_CHECK_INTERVAL


def get_latest_version() -> str | None:
    """Fetch the latest version from PyPI.

    Returns:
        Latest version string if successful, None otherwise.
    """
    try:
        with httpx.Client(timeout=REQUEST_TIMEOUT) as client:
            response = client.get(PYPI_API_URL)
            response.raise_for_status()

            data = response.json()
            latest = data.get("info", {}).get("version")

            if latest:
                logger.debug(f"Latest version from PyPI: {latest}")
                return str(latest)

    except (httpx.RequestError, httpx.HTTPStatusError, json.JSONDecodeError) as e:
        logger.debug(f"Failed to fetch latest version: {e}")

    return None


def compare_versions(current: str, latest: str) -> bool:
    """Compare version strings to determine if update is available.

    Args:
        current: Current version string.
        latest: Latest available version string.

    Returns:
        True if latest version is newer than current, False otherwise.
    """
    try:
        current_v = version.parse(current)
        latest_v = version.parse(latest)
        return latest_v > current_v
    except Exception as e:
        logger.debug(f"Error comparing versions: {e}")
        return False


def detect_installation_method() -> str:
    """Detect how shotgun-sh was installed.

    Returns:
        Installation method: 'pipx', 'pip', 'venv', or 'unknown'.
    """
    # Check for pipx installation
    try:
        result = subprocess.run(
            ["pipx", "list", "--short"],  # noqa: S607
            capture_output=True,
            text=True,
            timeout=30,  # noqa: S603
        )
        if "shotgun-sh" in result.stdout:
            logger.debug("Detected pipx installation")
            return "pipx"
    except (subprocess.SubprocessError, FileNotFoundError):
        pass

    # Check if we're in a virtual environment
    if hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ):
        logger.debug("Detected virtual environment installation")
        return "venv"

    # Check for user installation
    import site

    user_site = site.getusersitepackages()
    if user_site and Path(user_site).exists():
        shotgun_path = Path(user_site) / "shotgun"
        if shotgun_path.exists() or any(
            p.exists() for p in Path(user_site).glob("shotgun_sh*")
        ):
            logger.debug("Detected pip --user installation")
            return "pip"

    # Default to pip if we can't determine
    logger.debug("Could not detect installation method, defaulting to pip")
    return "pip"


def get_update_command(method: str) -> list[str]:
    """Get the appropriate update command based on installation method.

    Args:
        method: Installation method ('pipx', 'pip', 'venv', or 'unknown').

    Returns:
        Command list to execute for updating.
    """
    commands = {
        "pipx": ["pipx", "upgrade", "shotgun-sh"],
        "pip": [sys.executable, "-m", "pip", "install", "--upgrade", "shotgun-sh"],
        "venv": [sys.executable, "-m", "pip", "install", "--upgrade", "shotgun-sh"],
        "unknown": [sys.executable, "-m", "pip", "install", "--upgrade", "shotgun-sh"],
    }
    return commands.get(method, commands["unknown"])


def perform_update(force: bool = False) -> tuple[bool, str]:
    """Perform the actual update of shotgun-sh.

    Args:
        force: If True, update even if it's a dev version (with confirmation).

    Returns:
        Tuple of (success, message).
    """
    # Check if dev version and not forced
    if is_dev_version() and not force:
        return False, "Cannot auto-update development version. Use --force to override."

    # Get latest version
    latest = get_latest_version()
    if not latest:
        return False, "Failed to fetch latest version from PyPI"

    # Check if update is needed
    if not compare_versions(__version__, latest):
        return False, f"Already at latest version ({__version__})"

    # Store current version for comparison
    current_version = __version__

    # Detect installation method
    method = detect_installation_method()
    command = get_update_command(method)

    # Perform update
    try:
        logger.info(f"Updating shotgun-sh using {method}...")
        logger.debug(f"Running command: {' '.join(command)}")

        result = subprocess.run(command, capture_output=True, text=True, timeout=60)  # noqa: S603

        # Log output for debugging
        if result.stdout:
            logger.debug(f"Update stdout: {result.stdout}")
        if result.stderr:
            logger.debug(f"Update stderr: {result.stderr}")
        logger.debug(f"Update return code: {result.returncode}")

        # Check for success patterns in output (pipx specific)
        output_combined = (result.stdout or "") + (result.stderr or "")

        # For pipx, check if it mentions successful upgrade or already at latest
        pipx_success_patterns = [
            "successfully upgraded",
            "is already at latest version",
            f"installed package shotgun-sh {latest}",
            "upgrading shotgun-sh...",
        ]

        pipx_success = method == "pipx" and any(
            pattern.lower() in output_combined.lower()
            for pattern in pipx_success_patterns
        )

        # Verify actual installation by checking version
        update_successful = False

        # For pipx with return code 0, trust it succeeded
        if method == "pipx" and result.returncode == 0:
            update_successful = True
            logger.debug("Pipx returned 0, trusting update succeeded")
        elif result.returncode == 0 or pipx_success:
            # Give the system a moment to update the package metadata
            import time

            time.sleep(1)

            # Try to verify the installed version
            try:
                # For pipx, we need to check differently
                if method == "pipx":
                    # Use pipx list to verify the installed version
                    verify_result = subprocess.run(
                        ["pipx", "list", "--json"],  # noqa: S607
                        capture_output=True,
                        text=True,
                        timeout=5,  # noqa: S603
                    )
                    if verify_result.returncode == 0:
                        try:
                            pipx_data = json.loads(verify_result.stdout)
                            venvs = pipx_data.get("venvs", {})
                            shotgun_info = venvs.get("shotgun-sh", {})
                            metadata = shotgun_info.get("metadata", {})
                            main_package = metadata.get("main_package", {})
                            installed_version = main_package.get("package_version", "")
                            if installed_version == latest:
                                update_successful = True
                                logger.debug(
                                    f"Pipx verification successful: version {installed_version}"
                                )
                        except (json.JSONDecodeError, KeyError) as e:
                            logger.debug(
                                f"Pipx JSON parsing failed: {e}, trusting patterns"
                            )
                            update_successful = pipx_success
                    else:
                        # Fallback to checking with command
                        import shutil

                        shotgun_path = shutil.which("shotgun")
                        if shotgun_path:
                            verify_result = subprocess.run(  # noqa: S603
                                [shotgun_path, "--version"],
                                capture_output=True,
                                text=True,
                                timeout=5,
                            )
                            if (
                                verify_result.returncode == 0
                                and latest in verify_result.stdout
                            ):
                                update_successful = True
                                logger.debug(
                                    f"Version verification successful: {verify_result.stdout.strip()}"
                                )
                        else:
                            update_successful = pipx_success
                else:
                    # For pip/venv, check with python module
                    verify_result = subprocess.run(  # noqa: S603
                        [sys.executable, "-m", "shotgun", "--version"],
                        capture_output=True,
                        text=True,
                        timeout=5,
                    )
                    if verify_result.returncode == 0 and latest in verify_result.stdout:
                        update_successful = True
                        logger.debug(
                            f"Version verification successful: {verify_result.stdout.strip()}"
                        )
            except Exception as e:
                logger.debug(f"Version verification failed: {e}")
                # If verification fails but initial command succeeded, trust it
                if not update_successful:
                    update_successful = result.returncode == 0 or pipx_success

        if update_successful:
            message = f"Successfully updated from {current_version} to {latest}"
            logger.info(message)

            # Clear cache to trigger fresh check next time
            cache_file = get_cache_file()
            if cache_file.exists():
                cache_file.unlink()

            return True, message
        else:
            # Only use stderr for error message, stdout often contains normal progress
            if result.stderr:
                error_msg = f"Update failed: {result.stderr}"
            elif result.returncode != 0:
                error_msg = f"Update failed with exit code {result.returncode}: {result.stdout or 'No output'}"
            else:
                error_msg = "Update verification failed but command may have succeeded"
            logger.error(error_msg)
            return False, error_msg

    except subprocess.TimeoutExpired:
        return False, "Update command timed out"
    except Exception as e:
        return False, f"Update failed: {e}"


def format_update_notification(current: str, latest: str) -> str:
    """Format a user-friendly update notification message.

    Args:
        current: Current version.
        latest: Latest available version.

    Returns:
        Formatted notification string.
    """
    return f"Update available: {current} → {latest}. Run 'shotgun update' to upgrade."


def format_update_status(
    status: str, current: str | None = None, latest: str | None = None
) -> str:
    """Format update status messages.

    Args:
        status: Status type ('installing', 'success', 'failed', 'checking').
        current: Current version (optional).
        latest: Latest version (optional).

    Returns:
        Formatted status message.
    """
    if status == "checking":
        return "Checking for updates..."
    elif status == "installing" and current and latest:
        return f"Installing update: {current} → {latest}..."
    elif status == "success" and latest:
        return f"✓ Successfully updated to version {latest}. Restart your terminal to use the new version."
    elif status == "failed":
        return "Update failed. Run 'shotgun update' to try manually."
    else:
        return ""


def check_for_updates_sync(no_update_check: bool = False) -> str | None:
    """Synchronously check for updates and return notification if available.

    Args:
        no_update_check: If True, skip update checks.

    Returns:
        Update notification string if update available, None otherwise.
    """
    if not should_check_for_updates(no_update_check):
        # Check cache for existing notification
        cache = load_cache()
        if cache and cache.update_available:
            current = cache.current_version
            latest = cache.latest_version
            if compare_versions(current, latest):
                return format_update_notification(current, latest)
        return None

    latest_version = get_latest_version()
    if not latest_version:
        return None
    latest = latest_version  # Type narrowing - we know it's not None here

    # Update cache
    now = datetime.now(timezone.utc)
    update_available = compare_versions(__version__, latest)

    cache_data = UpdateCache(
        last_check=now,
        latest_version=latest,
        current_version=__version__,
        update_available=update_available,
    )
    save_cache(cache_data)

    if update_available:
        return format_update_notification(__version__, latest)

    return None


def check_and_install_updates_sync(no_update_check: bool = False) -> tuple[str, bool]:
    """Synchronously check for updates and install if available.

    Args:
        no_update_check: If True, skip update checks and installation.

    Returns:
        Tuple of (status message, success boolean).
    """
    if no_update_check:
        return "", False

    if not should_check_for_updates(no_update_check):
        return "", False

    # Skip auto-install for development versions
    if is_dev_version():
        logger.debug("Skipping auto-install for development version")
        return "", False

    latest_version = get_latest_version()
    if not latest_version:
        return "", False
    latest = latest_version  # Type narrowing

    # Check if update is needed
    if not compare_versions(__version__, latest):
        # Already up to date, update cache
        now = datetime.now(timezone.utc)
        cache_data = UpdateCache(
            last_check=now,
            latest_version=latest,
            current_version=__version__,
            update_available=False,
        )
        save_cache(cache_data)
        return "", False

    # Perform the update
    logger.info(f"Auto-installing update: {__version__} → {latest}")
    success, message = perform_update(force=False)

    if success:
        # Clear cache on successful update
        cache_file = get_cache_file()
        if cache_file.exists():
            cache_file.unlink()
        return format_update_status("success", latest=latest), True
    else:
        # Update cache to mark that we tried and failed
        # This prevents repeated attempts within the check interval
        now = datetime.now(timezone.utc)
        cache_data = UpdateCache(
            last_check=now,
            latest_version=latest,
            current_version=__version__,
            update_available=True,  # Still available, but we failed to install
        )
        save_cache(cache_data)
        logger.warning(f"Auto-update failed: {message}")
        return format_update_status("failed"), False


def check_for_updates_async(
    callback: Callable[[str], None] | None = None, no_update_check: bool = False
) -> threading.Thread:
    """Asynchronously check for updates in a background thread.

    Args:
        callback: Optional callback function to call with notification string.
        no_update_check: If True, skip update checks.

    Returns:
        The thread object that was started.
    """

    def _check_updates() -> None:
        try:
            notification = check_for_updates_sync(no_update_check)
            if notification and callback:
                callback(notification)
        except Exception as e:
            logger.debug(f"Error in async update check: {e}")

    thread = threading.Thread(target=_check_updates, daemon=True)
    thread.start()
    return thread


def check_and_install_updates_async(
    callback: Callable[[str], None] | None = None,
    no_update_check: bool = False,
    progress_callback: Callable[[str], None] | None = None,
) -> threading.Thread:
    """Asynchronously check for updates and install in a background thread.

    Args:
        callback: Optional callback function to call with final status message.
        no_update_check: If True, skip update checks and installation.
        progress_callback: Optional callback for progress updates.

    Returns:
        The thread object that was started.
    """

    def _check_and_install() -> None:
        try:
            # Send checking status if progress callback provided
            if progress_callback:
                progress_callback(format_update_status("checking"))

            # Skip if disabled
            if no_update_check:
                return

            # Skip for dev versions
            if is_dev_version():
                logger.debug("Skipping auto-install for development version")
                return

            # Check if we should check for updates
            if not should_check_for_updates(no_update_check):
                # Check cache to see if update is still pending
                cache = load_cache()
                if cache and cache.update_available:
                    # We have a pending update from a previous check
                    # Don't retry installation automatically to avoid repeated failures
                    if callback:
                        callback(
                            format_update_notification(
                                cache.current_version, cache.latest_version
                            )
                        )
                return

            # Get latest version
            latest_version = get_latest_version()
            if not latest_version:
                return
            latest = latest_version  # Type narrowing

            # Check if update is needed
            if not compare_versions(__version__, latest):
                # Already up to date, update cache
                now = datetime.now(timezone.utc)
                cache_data = UpdateCache(
                    last_check=now,
                    latest_version=latest,
                    current_version=__version__,
                    update_available=False,
                )
                save_cache(cache_data)
                logger.debug(f"Already at latest version ({__version__})")
                return

            # Send installing status
            if progress_callback:
                progress_callback(
                    format_update_status(
                        "installing", current=__version__, latest=latest
                    )
                )

            # Perform the update
            logger.info(f"Auto-installing update: {__version__} → {latest}")
            success, message = perform_update(force=False)

            if success:
                # Clear cache on successful update
                cache_file = get_cache_file()
                if cache_file.exists():
                    cache_file.unlink()

                if callback:
                    callback(format_update_status("success", latest=latest))
            else:
                # Update cache to mark that we tried and failed
                now = datetime.now(timezone.utc)
                cache_data = UpdateCache(
                    last_check=now,
                    latest_version=latest,
                    current_version=__version__,
                    update_available=True,
                )
                save_cache(cache_data)
                logger.warning(f"Auto-update failed: {message}")

                if callback:
                    callback(format_update_status("failed"))

        except Exception as e:
            logger.debug(f"Error in async update check and install: {e}")
            if callback:
                callback(format_update_status("failed"))

    thread = threading.Thread(target=_check_and_install, daemon=True)
    thread.start()
    return thread


__all__ = [
    "UpdateCache",
    "is_dev_version",
    "should_check_for_updates",
    "get_latest_version",
    "detect_installation_method",
    "perform_update",
    "check_for_updates_async",
    "check_for_updates_sync",
    "check_and_install_updates_async",
    "check_and_install_updates_sync",
    "format_update_notification",
    "format_update_status",
]
