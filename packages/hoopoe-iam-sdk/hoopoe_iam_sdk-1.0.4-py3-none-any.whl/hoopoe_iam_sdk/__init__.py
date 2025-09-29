"""
Hoopoe IAM SDK - Official Python SDK for Hoopoe IAM Service

This SDK provides a comprehensive Python interface for interacting with the
Hoopoe IAM Service, including authentication, user management, organization
management, and admin operations.

Version: 1.0.4
License: MIT
"""

from .client import IAMClient
from .exceptions import (
    AuthenticationError,
    AuthorizationError,
    ConflictError,
    IAMConnectionError,
    IAMError,
    IAMTimeoutError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from .middleware import IAMMiddleware, create_iam_dependency
from .models import (
    AccountInfo,
    APIKeyCreateRequest,
    APIKeyInfo,
    ApplicationCreateRequest,
    ApplicationInfo,
    OrganizationCreateRequest,
    OrganizationInfo,
    PermissionInfo,
    RoleInfo,
    TokenInfo,
    UserCreateRequest,
    UserInfo,
)
from .version import __version__


# Backward compatibility: IAMAdminClient is now just IAMClient with admin credentials
class IAMAdminClient(IAMClient):
    """
    Backward compatibility class for IAMAdminClient.

    This is now just a wrapper around IAMClient with admin credentials.
    Use IAMClient directly with admin_api_key for new code.
    """

    def __init__(
        self,
        base_url=None,
        admin_api_key=None,
        timeout=30.0,
        verify_ssl=True,
        cache_ttl=300,
    ):
        """
        Initialize admin client (backward compatibility).

        Args:
            base_url: IAM service base URL
            admin_api_key: Admin API key
            timeout: Request timeout in seconds
            verify_ssl: Whether to verify SSL certificates
            cache_ttl: Cache TTL in seconds
        """
        super().__init__(
            base_url=base_url,
            admin_api_key=admin_api_key,
            timeout=timeout,
            verify_ssl=verify_ssl,
            cache_ttl=cache_ttl,
        )


__all__ = [
    # Main client (unified)
    "IAMClient",
    # Backward compatibility
    "IAMAdminClient",
    # Exceptions
    "IAMError",
    "AuthenticationError",
    "AuthorizationError",
    "ValidationError",
    "NotFoundError",
    "ConflictError",
    "RateLimitError",
    "ServerError",
    "IAMConnectionError",
    "IAMTimeoutError",
    # FastAPI integration
    "IAMMiddleware",
    "create_iam_dependency",
    # Models
    "TokenInfo",
    "UserInfo",
    "AccountInfo",
    "OrganizationInfo",
    "ApplicationInfo",
    "PermissionInfo",
    "RoleInfo",
    "APIKeyInfo",
    # Request models
    "OrganizationCreateRequest",
    "ApplicationCreateRequest",
    "UserCreateRequest",
    "APIKeyCreateRequest",
    # Version
    "__version__",
]

# SDK metadata
__title__ = "hoopoe-iam-sdk"
__author__ = "Eliff Technology Solutions"
__email__ = "support@eliff.tech"
__description__ = "Official Python SDK for Hoopoe IAM Service"
__url__ = "https://github.com/eliff-tech/hoopoe-iam-sdk"
