"""
Entangle Matrix SDK

Python SDK for Entangle Matrix API - Create and manage AI-powered digital twins.
"""

from .client import EntangleMatrixClient
from .models import (
    MatrixMessage,
    MatrixUpload,
    MatrixRoom,
    MessageRequest,
    CreateRoomRequest,
    JoinRoomRequest,
)
from .exceptions import (
    EntangleMatrixError,
    AuthenticationError,
    NetworkError,
    ValidationError,
    NotFoundError,
)

__version__ = "0.2.0"
__author__ = "QBit Codes"
__email__ = "hello@qbitcodes.com"

__all__ = [
    "EntangleMatrixClient",
    "MatrixMessage",
    "MatrixUpload",
    "MatrixRoom",
    "MessageRequest",
    "CreateRoomRequest",
    "JoinRoomRequest",
    "EntangleMatrixError",
    "AuthenticationError",
    "NetworkError",
    "ValidationError",
    "NotFoundError",
]