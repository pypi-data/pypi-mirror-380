"""FastAPI middleware and dependencies for IAM integration."""

from typing import TYPE_CHECKING, Callable, List, Optional

from .client import IAMClient
from .exceptions import AuthenticationError, AuthorizationError, IAMError
from .models import UserInfo

FASTAPI_AVAILABLE = False


if TYPE_CHECKING:
    from fastapi import Depends, HTTPException, Request
    from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.responses import Response

    FASTAPI_AVAILABLE = True

else:
    try:
        from fastapi import Depends, HTTPException, Request
        from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
        from starlette.middleware.base import BaseHTTPMiddleware
        from starlette.responses import Response

        FASTAPI_AVAILABLE = True

    except ImportError:
        # Provide stub classes for when FastAPI is not available

        class Request:
            pass

        class HTTPException(Exception):
            pass

        class Depends:
            def __init__(self, dependency=None):
                self.dependency = dependency

        class HTTPBearer:
            def __call__(self, *args, **kwargs):
                raise ImportError(
                    "FastAPI is not installed. Install with: pip install hoopoe-iam-sdk[fastapi]"
                )

        class HTTPAuthorizationCredentials:
            def __init__(self, credentials: str = ""):
                self.credentials = credentials

        class BaseHTTPMiddleware:
            pass

        class Response:
            pass


if FASTAPI_AVAILABLE:
    security = HTTPBearer()

    class IAMMiddleware(BaseHTTPMiddleware):
        """FastAPI middleware for automatic IAM token extraction."""

        def __init__(self, app, iam_client: IAMClient):
            super().__init__(app)

            self.iam_client = iam_client

        async def dispatch(self, request: Request, call_next):
            """Process request and add IAM context."""

            # Extract token from Authorization header

            auth_header = request.headers.get("Authorization")

            if auth_header and auth_header.startswith("Bearer "):
                token = auth_header[7:]  # Remove "Bearer " prefix

                try:
                    # Validate token and get user info

                    user_info = await self.iam_client.validate_token(token)

                    # Add user info to request state

                    request.state.iam_user = user_info

                    request.state.iam_token = token

                except IAMError:
                    # Token validation failed, but continue without user info

                    request.state.iam_user = None

                    request.state.iam_token = None

            else:
                request.state.iam_user = None

                request.state.iam_token = None

            response = await call_next(request)

            return response

    class IAMDependency:
        """Dependency class for IAM authentication and authorization."""

        def __init__(self, iam_client: IAMClient, required: bool = True):
            self.iam_client = iam_client

            self.required = required

        async def __call__(
            self,
            credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
        ) -> Optional[UserInfo]:
            """Extract and validate user from token."""

            if not credentials:
                if self.required:
                    raise HTTPException(
                        status_code=401, detail="Authentication required"
                    )

                return None

            try:
                user_info = await self.iam_client.validate_token(
                    credentials.credentials
                )

                return user_info

            except AuthenticationError as e:
                raise HTTPException(status_code=401, detail=str(e))

            except IAMError as e:
                raise HTTPException(
                    status_code=500, detail=f"IAM service error: {str(e)}"
                )

        def require_permission(self, permission: str) -> Callable:
            """Create a dependency that requires a specific permission."""

            async def permission_dependency(
                user: UserInfo = Depends(self),
                credentials: HTTPAuthorizationCredentials = Depends(security),
            ) -> UserInfo:
                if not user:
                    raise HTTPException(
                        status_code=401, detail="Authentication required"
                    )

                try:
                    has_permission = await self.iam_client.check_permission(
                        credentials.credentials, permission
                    )

                    if not has_permission:
                        raise HTTPException(
                            status_code=403,
                            detail=f"Permission '{permission}' required",
                        )

                    return user

                except AuthorizationError as e:
                    raise HTTPException(status_code=403, detail=str(e))

                except IAMError as e:
                    raise HTTPException(
                        status_code=500, detail=f"Permission check failed: {str(e)}"
                    )

            return permission_dependency

        def require_permissions(
            self, permissions: List[str], require_all: bool = True
        ) -> Callable:
            """Create a dependency that requires multiple permissions."""

            async def permissions_dependency(
                user: UserInfo = Depends(self),
                credentials: HTTPAuthorizationCredentials = Depends(security),
            ) -> UserInfo:
                if not user:
                    raise HTTPException(
                        status_code=401, detail="Authentication required"
                    )

                try:
                    permission_results = []

                    for permission in permissions:
                        has_permission = await self.iam_client.check_permission(
                            credentials.credentials, permission
                        )

                        permission_results.append(has_permission)

                    if require_all:
                        # All permissions required

                        if not all(permission_results):
                            missing = [
                                p
                                for p, has in zip(permissions, permission_results)
                                if not has
                            ]

                            raise HTTPException(
                                status_code=403,
                                detail=f"Missing required permissions: {', '.join(missing)}",
                            )

                    else:
                        # At least one permission required

                        if not any(permission_results):
                            raise HTTPException(
                                status_code=403,
                                detail=f"At least one of these permissions required: {', '.join(permissions)}",
                            )

                    return user

                except AuthorizationError as e:
                    raise HTTPException(status_code=403, detail=str(e))

                except IAMError as e:
                    raise HTTPException(
                        status_code=500, detail=f"Permission check failed: {str(e)}"
                    )

            return permissions_dependency

        def require_role(self, role: str) -> Callable:
            """Create a dependency that requires a specific role."""

            return self.require_permission(f"role: {role}")

        def optional(self) -> Callable:
            """Create an optional dependency (user may be None)."""

            async def optional_dependency(
                credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
            ) -> Optional[UserInfo]:
                if not credentials:
                    return None

                try:
                    user_info = await self.iam_client.validate_token(
                        credentials.credentials
                    )

                    return user_info

                except (AuthenticationError, IAMError):
                    # Return None instead of raising exception for optional auth

                    return None

            return optional_dependency

    def create_iam_dependency(
        iam_client: IAMClient, required: bool = True
    ) -> IAMDependency:
        """Create an IAM dependency for FastAPI.

        Args:

            iam_client: IAM client instance (required)

            required: Whether authentication is required



        Returns:

            IAMDependency instance



        Raises:

            ValueError: If iam_client is None

        """

        if iam_client is None:
            raise ValueError(
                "iam_client is required. Create an IAMClient with appropriate credentials first."
            )

        return IAMDependency(iam_client, required=required)

    # Convenience functions for common use cases

    def get_current_user(iam_client: IAMClient) -> Callable:
        """Get a dependency function for the current authenticated user."""

        dependency = create_iam_dependency(iam_client, required=True)

        return dependency

    def get_optional_user(iam_client: IAMClient) -> Callable:
        """Get a dependency function for optional user authentication."""

        dependency = create_iam_dependency(iam_client, required=False)

        return dependency.optional()

    def require_permission(permission: str, iam_client: IAMClient) -> Callable:
        """Get a dependency function that requires a specific permission."""

        dependency = create_iam_dependency(iam_client, required=True)

        return dependency.require_permission(permission)

    def require_role(role: str, iam_client: IAMClient) -> Callable:
        """Get a dependency function that requires a specific role."""

        dependency = create_iam_dependency(iam_client, required=True)

        return dependency.require_role(role)

else:
    # Stub implementations when FastAPI is not available

    class IAMMiddleware:
        def __init__(self, *args, **kwargs):
            raise ImportError(
                "FastAPI is not installed. Install with: pip install hoopoe-iam-sdk[fastapi]"
            )

    class IAMDependency:
        def __init__(self, *args, **kwargs):
            raise ImportError(
                "FastAPI is not installed. Install with: pip install hoopoe-iam-sdk[fastapi]"
            )

    def create_iam_dependency(
        iam_client: IAMClient, required: bool = True
    ) -> IAMDependency:
        raise ImportError(
            "FastAPI is not installed. Install with: pip install hoopoe-iam-sdk[fastapi]"
        )

    def get_current_user(iam_client: IAMClient) -> Callable:
        raise ImportError(
            "FastAPI is not installed. Install with: pip install hoopoe-iam-sdk[fastapi]"
        )

    def get_optional_user(iam_client: IAMClient) -> Callable:
        raise ImportError(
            "FastAPI is not installed. Install with: pip install hoopoe-iam-sdk[fastapi]"
        )

    def require_permission(permission: str, iam_client: IAMClient) -> Callable:
        raise ImportError(
            "FastAPI is not installed. Install with: pip install hoopoe-iam-sdk[fastapi]"
        )

    def require_role(role: str, iam_client: IAMClient) -> Callable:
        raise ImportError(
            "FastAPI is not installed. Install with: pip install hoopoe-iam-sdk[fastapi]"
        )
