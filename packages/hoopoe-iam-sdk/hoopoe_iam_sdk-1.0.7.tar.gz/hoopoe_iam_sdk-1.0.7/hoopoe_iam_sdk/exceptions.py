"""Exception classes for Hoopoe IAM SDK."""

from typing import Any, Dict, Optional


class IAMError(Exception):
    """Base exception for all IAM SDK errors."""

    def __init__(
        self,
        message: str,
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
        status_code: Optional[int] = None,
    ):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details or {}
        self.status_code = status_code

    def __str__(self) -> str:
        if self.error_code:
            return f"[{self.error_code}] {self.message}"
        return self.message

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"message='{self.message}', "
            f"error_code='{self.error_code}', "
            f"status_code={self.status_code})"
        )


class AuthenticationError(IAMError):
    """Raised when authentication fails."""

    def __init__(
        self,
        message: str = "Authentication failed",
        error_code: Optional[str] = "AUTH_FAILED",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message, error_code=error_code, details=details, status_code=401
        )


class AuthorizationError(IAMError):
    """Raised when authorization fails (insufficient permissions)."""

    def __init__(
        self,
        message: str = "Access denied",
        error_code: Optional[str] = "ACCESS_DENIED",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message, error_code=error_code, details=details, status_code=403
        )


class ValidationError(IAMError):
    """Raised when request validation fails."""

    def __init__(
        self,
        message: str = "Validation failed",
        error_code: Optional[str] = "VALIDATION_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message, error_code=error_code, details=details, status_code=422
        )


class NotFoundError(IAMError):
    """Raised when a resource is not found."""

    def __init__(
        self,
        message: str = "Resource not found",
        error_code: Optional[str] = "NOT_FOUND",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message, error_code=error_code, details=details, status_code=404
        )


class ConflictError(IAMError):
    """Raised when there's a conflict (e.g., duplicate resource)."""

    def __init__(
        self,
        message: str = "Conflict occurred",
        error_code: Optional[str] = "CONFLICT",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message, error_code=error_code, details=details, status_code=409
        )


class RateLimitError(IAMError):
    """Raised when rate limit is exceeded."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        error_code: Optional[str] = "RATE_LIMIT_EXCEEDED",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message, error_code=error_code, details=details, status_code=429
        )


class ServerError(IAMError):
    """Raised when there's a server error."""

    def __init__(
        self,
        message: str = "Internal server error",
        error_code: Optional[str] = "SERVER_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message, error_code=error_code, details=details, status_code=500
        )


class IAMConnectionError(IAMError):
    """Raised when there's a connection error."""

    def __init__(
        self,
        message: str = "Connection failed",
        error_code: Optional[str] = "CONNECTION_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message, error_code=error_code, details=details, status_code=None
        )


class IAMTimeoutError(IAMError):
    """Raised when a request times out."""

    def __init__(
        self,
        message: str = "Request timed out",
        error_code: Optional[str] = "TIMEOUT",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message, error_code=error_code, details=details, status_code=None
        )
