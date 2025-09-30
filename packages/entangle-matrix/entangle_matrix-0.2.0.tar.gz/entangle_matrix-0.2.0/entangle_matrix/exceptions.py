"""
Custom exceptions for the Entangle Matrix SDK.
"""


class EntangleMatrixError(Exception):
    """Base exception for all Entangle Matrix SDK errors."""

    def __init__(self, message: str, status_code: int = None) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class AuthenticationError(EntangleMatrixError):
    """Raised when authentication fails."""

    def __init__(self, message: str = "Authentication failed") -> None:
        super().__init__(message, status_code=401)


class NetworkError(EntangleMatrixError):
    """Raised when a network error occurs."""

    def __init__(self, message: str = "Network error occurred") -> None:
        super().__init__(message, status_code=503)


class ValidationError(EntangleMatrixError):
    """Raised when request validation fails."""

    def __init__(self, message: str = "Validation error") -> None:
        super().__init__(message, status_code=400)


class NotFoundError(EntangleMatrixError):
    """Raised when a resource is not found."""

    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(message, status_code=404)


class RateLimitError(EntangleMatrixError):
    """Raised when rate limit is exceeded."""

    def __init__(self, message: str = "Rate limit exceeded") -> None:
        super().__init__(message, status_code=429)


class ServerError(EntangleMatrixError):
    """Raised when server error occurs."""

    def __init__(self, message: str = "Internal server error") -> None:
        super().__init__(message, status_code=500)