"""
Workspace privacy utilities for managing session-level privacy flags.
"""

from pathlib import Path

from fastmcp import Context

from aixtools.logging.logging_config import get_logger
from aixtools.server.path import get_workspace_path

logger = get_logger(__name__)

PRIVACY_FLAG_FILENAME = ".private_data_indicator"


def set_session_private(ctx: Context | tuple[str, str] | None = None) -> bool:
    """
    Set the current session as private by creating a privacy flag file.

    Creates an empty file in the session workspace directory
    and sets it as read-only to prevent accidental removal

    Args:
        ctx: FastMCP context for user/session identification.
             If None, uses current FastMCP request context from HTTP headers.
             If tuple, first part is a user id (username), second part is session id (aka conversation id)

    Returns:
        bool: True if privacy flag was successfully created, False otherwise.
    """
    try:
        workspace_path = Path(get_workspace_path(ctx=ctx))
        privacy_file = workspace_path / PRIVACY_FLAG_FILENAME
        workspace_path.mkdir(parents=True, exist_ok=True)
        privacy_file.touch(exist_ok=True)
        privacy_file.chmod(0o444)
        logger.warning("Session marked as private")
        return True
    except (OSError, ValueError, RuntimeError) as e:
        logger.error("Set current session as private: %s", str(e))
        return False


def is_session_private(ctx: Context | tuple[str, str] | None = None) -> bool:
    """
    Check if the current session is marked as private.

    Args:
        ctx: FastMCP context for user/session identification.
             If None, uses current FastMCP request context from HTTP headers.
             If tuple, first part is a user id (username), second part is session id (aka conversation id)

    Returns:
        bool: True if workspace is private (flag file exists), False otherwise.
    """
    try:
        workspace_path = Path(get_workspace_path(ctx=ctx))
        privacy_file = workspace_path / PRIVACY_FLAG_FILENAME
        is_private = privacy_file.exists()
        logger.info("Session privacy check, is private: %s", str(is_private))
        return is_private
    except (OSError, ValueError, RuntimeError) as e:
        logger.error("Check session privacy: %s, assuming not private!", str(e))
        return False
