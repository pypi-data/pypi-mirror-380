"""
Utility functions for the Entangle Matrix SDK.
"""

import mimetypes
from pathlib import Path
from typing import Optional


def get_content_type(file_path: Path) -> str:
    """
    Get MIME type for a file.

    Args:
        file_path: Path to the file

    Returns:
        MIME type string, defaults to 'application/octet-stream'
    """
    content_type, _ = mimetypes.guess_type(str(file_path))
    return content_type or "application/octet-stream"


def validate_room_id(room_id: str) -> bool:
    """
    Validate Matrix room ID format.

    Args:
        room_id: Room ID to validate

    Returns:
        True if valid room ID format
    """
    # Matrix room IDs start with ! and contain a colon
    return room_id.startswith("!") and ":" in room_id


def validate_user_id(user_id: str) -> bool:
    """
    Validate Matrix user ID format.

    Args:
        user_id: User ID to validate

    Returns:
        True if valid user ID format
    """
    # Matrix user IDs start with @ and contain a colon
    return user_id.startswith("@") and ":" in user_id


def validate_file_size(file_path: Path, max_size_mb: int = 10) -> bool:
    """
    Validate file size is within limits.

    Args:
        file_path: Path to the file
        max_size_mb: Maximum size in megabytes

    Returns:
        True if file size is within limits
    """
    if not file_path.exists():
        return False

    file_size = file_path.stat().st_size
    max_size_bytes = max_size_mb * 1024 * 1024
    return file_size <= max_size_bytes


def is_image_file(file_path: Path) -> bool:
    """
    Check if file is an image based on MIME type.

    Args:
        file_path: Path to the file

    Returns:
        True if file is an image
    """
    content_type = get_content_type(file_path)
    return content_type.startswith("image/")


def is_audio_file(file_path: Path) -> bool:
    """
    Check if file is an audio file based on MIME type.

    Args:
        file_path: Path to the file

    Returns:
        True if file is an audio file
    """
    content_type = get_content_type(file_path)
    return content_type.startswith("audio/")


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human readable format.

    Args:
        size_bytes: File size in bytes

    Returns:
        Formatted file size string
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"