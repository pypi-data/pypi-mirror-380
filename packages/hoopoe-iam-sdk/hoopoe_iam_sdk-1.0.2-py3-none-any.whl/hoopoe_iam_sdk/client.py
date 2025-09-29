"""
Unified IAM Client for Hoopoe IAM Service

This module provides a unified client that can handle both application-level
and administrative operations based on the provided credentials.
"""

import os
from enum import Enum
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import httpx
from pydantic import ValidationError as PydanticValidationError

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
from .models import (
    AccountInfo,
    APIKeyCreateRequest,
    APIKeyInfo,
    ApplicationCreateRequest,
    ApplicationInfo,
    AuditLogCreateRequest,
    AuditLogInfo,
    AuditLogListResponse,
    AuditLogSearchRequest,
    AuditLogStats,
    OrganizationCreateRequest,
    OrganizationInfo,
    RoleInfo,
    TokenInfo,
    UserCreateRequest,
    UserInfo,
)


class CredentialType(Enum):
    """Types of credentials that can be used with the IAM client."""

    ADMIN_API_KEY = "admin_api_key"
    APP_CREDENTIALS = "app_credentials"


class IAMClient:
    """
    Unified IAM client for both application and administrative operations.

    The client supports two authentication modes:
    1. Admin mode: Using admin_api_key for administrative operations
    2. App mode: Using access_key + secret_key for application operations

    Admin mode allows both admin and app operations (if app_id/org_id provided).
    App mode only allows application-level operations (requires app_id).
    """

    def __init__(
        self,
        base_url: Optional[str] = None,
        admin_api_key: Optional[str] = None,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        app_id: Optional[str] = None,
        org_id: Optional[str] = None,
        timeout: float = 30.0,
        cache_ttl: int = 300,
        verify_ssl: bool = True,
    ):
        """
        Initialize the IAM client.

        Args:
            base_url: IAM service base URL (can use IAM_SERVICE_URL env var if not provided)
            admin_api_key: Admin API key for administrative operations
            access_key: Application access key (used with secret_key)
            secret_key: Application secret key (used with access_key)
            app_id: Application ID (required for app-level operations)
            org_id: Organization ID (optional, for scoping operations)
            timeout: Request timeout in seconds
            cache_ttl: Cache TTL in seconds for token validation
            verify_ssl: Whether to verify SSL certificates

        Raises:
            ValueError: If invalid credential combination is provided
        """
        # Base URL can come from environment if not provided
        self.base_url = base_url or os.getenv("IAM_SERVICE_URL")
        if not self.base_url:
            raise ValueError(
                "base_url must be provided or IAM_SERVICE_URL environment variable must be set"
            )

        # Validate and set credentials
        self._validate_credentials(admin_api_key, access_key, secret_key, app_id)

        self.admin_api_key = admin_api_key
        self.access_key = access_key
        self.secret_key = secret_key
        self.app_id = app_id
        self.org_id = org_id
        self.timeout = timeout
        self.cache_ttl = cache_ttl
        self.verify_ssl = verify_ssl

        # Ensure base URL doesn't have trailing slash
        self.base_url = self.base_url.rstrip("/")

        # Determine credential type and capabilities
        self._credential_type = self._determine_credential_type()
        self._can_admin = self._credential_type == CredentialType.ADMIN_API_KEY
        self._can_app = bool(self.app_id)  # App operations require app_id

        # Initialize HTTP client
        self._client: Optional[httpx.AsyncClient] = None
        self._token_cache: Dict[str, Any] = {}

    def _validate_credentials(
        self,
        admin_api_key: Optional[str],
        access_key: Optional[str],
        secret_key: Optional[str],
        app_id: Optional[str],
    ) -> None:
        """Validate credential combinations."""
        has_admin = bool(admin_api_key)
        has_app_creds = bool(access_key and secret_key)

        if not has_admin and not has_app_creds:
            raise ValueError(
                "Either admin_api_key or both access_key and secret_key must be provided"
            )

        if has_app_creds and not access_key:
            raise ValueError("access_key is required when using app credentials")

        if has_app_creds and not secret_key:
            raise ValueError("secret_key is required when using app credentials")

        # For app credentials, app_id is mandatory for most operations
        if has_app_creds and not has_admin and not app_id:
            raise ValueError(
                "app_id is required when using app credentials without admin access"
            )

    def _determine_credential_type(self) -> CredentialType:
        """Determine the type of credentials being used."""
        if self.admin_api_key:
            return CredentialType.ADMIN_API_KEY
        else:
            return CredentialType.APP_CREDENTIALS

    @property
    def can_admin(self) -> bool:
        """Check if this client can perform administrative operations."""
        return self._can_admin

    @property
    def can_app(self) -> bool:
        """Check if this client can perform application operations."""
        return self._can_app

    def _require_admin(self) -> None:
        """Raise an error if admin operations are not available."""
        if not self.can_admin:
            raise AuthorizationError(
                "Admin operations require admin_api_key",
                error_code="ADMIN_ACCESS_REQUIRED",
            )

    def _require_app(self) -> None:
        """Raise an error if app operations are not available."""
        if not self.can_app:
            raise AuthorizationError(
                "Application operations require app_id", error_code="APP_ID_REQUIRED"
            )

    async def __aenter__(self):
        """Async context manager entry."""
        await self._ensure_client()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    async def _ensure_client(self):
        """Ensure HTTP client is initialized."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                timeout=httpx.Timeout(self.timeout), verify=self.verify_ssl
            )

    async def close(self):
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None

    def _get_headers(self, include_auth: bool = True) -> Dict[str, str]:
        """Get request headers with appropriate authentication."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "hoopoe-iam-sdk/1.0.0",
        }

        if include_auth:
            if self.admin_api_key:
                # Admin operations use Bearer token authentication
                headers["Authorization"] = f"Bearer {self.admin_api_key}"
            elif self.access_key and self.secret_key:
                # Client/app operations use access key and secret key headers
                headers["X-IAM-Access-Key"] = self.access_key
                headers["X-IAM-Secret-Key"] = self.secret_key

        if self.app_id:
            headers["X-App-ID"] = self.app_id

        if self.org_id:
            headers["X-Org-ID"] = self.org_id

        return headers

    async def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        include_auth: bool = True,
    ) -> Dict[str, Any]:
        """Make an HTTP request to the IAM service."""
        await self._ensure_client()

        url = urljoin(self.base_url + "/", endpoint.lstrip("/"))
        headers = self._get_headers(include_auth=include_auth)

        try:
            response = await self._client.request(
                method=method, url=url, headers=headers, json=data, params=params
            )

            # Handle different response status codes
            if response.status_code in (200, 201):
                return response.json() if response.content else {}
            elif response.status_code == 204:
                return {}
            elif response.status_code == 400:
                error_data = response.json() if response.content else {}
                raise ValidationError(
                    error_data.get("detail", "Bad request"), details=error_data
                )
            elif response.status_code == 401:
                error_data = response.json() if response.content else {}
                raise AuthenticationError(
                    error_data.get("detail", "Authentication failed"),
                    details=error_data,
                )
            elif response.status_code == 403:
                error_data = response.json() if response.content else {}
                raise AuthorizationError(
                    error_data.get("detail", "Access denied"), details=error_data
                )
            elif response.status_code == 404:
                error_data = response.json() if response.content else {}
                raise NotFoundError(
                    error_data.get("detail", "Resource not found"), details=error_data
                )
            elif response.status_code == 409:
                error_data = response.json() if response.content else {}
                raise ConflictError(
                    error_data.get("detail", "Conflict occurred"), details=error_data
                )
            elif response.status_code == 429:
                error_data = response.json() if response.content else {}
                raise RateLimitError(
                    error_data.get("detail", "Rate limit exceeded"), details=error_data
                )
            elif response.status_code >= 500:
                error_data = response.json() if response.content else {}
                raise ServerError(
                    error_data.get("detail", "Internal server error"),
                    details=error_data,
                )
            else:
                error_data = response.json() if response.content else {}
                raise IAMError(
                    f"Unexpected response: {response.status_code}",
                    status_code=response.status_code,
                    details=error_data,
                )

        except httpx.ConnectError as e:
            raise IAMConnectionError(f"Failed to connect to IAM service: {e}")
        except httpx.TimeoutException as e:
            raise IAMTimeoutError(f"Request timed out: {e}")
        except httpx.HTTPStatusError as e:
            raise IAMError(f"HTTP error: {e}")
        except PydanticValidationError as e:
            raise ValidationError(f"Response validation error: {e}")

    # ==========================================
    # HEALTH CHECK AND CONNECTION
    # ==========================================

    async def test_connection(self) -> bool:
        """Test connection to the IAM service."""
        try:
            await self._make_request("GET", "/test-admin-bypass", include_auth=False)
            return True
        except Exception:
            return False

    async def validate_admin_access(self) -> bool:
        """Validate admin access (requires admin credentials)."""
        self._require_admin()
        try:
            await self._make_request("GET", "/test-admin")
            return True
        except (AuthenticationError, AuthorizationError):
            return False

    # ==========================================
    # AUTHENTICATION OPERATIONS (App Mode)
    # ==========================================

    async def authenticate(self, username: str, password: str) -> TokenInfo:
        """
        Authenticate user credentials and get access token.
        Requires app_id to be set.
        """
        self._require_app()
        data = {"username": username, "password": password}
        response = await self._make_request(
            "POST", "/auth/login", data=data, include_auth=False
        )
        return TokenInfo(**response)

    async def refresh_token(self, refresh_token: str) -> TokenInfo:
        """Refresh an access token using a refresh token."""
        self._require_app()
        data = {"refresh_token": refresh_token}
        response = await self._make_request(
            "POST", "/auth/refresh", data=data, include_auth=False
        )
        return TokenInfo(**response)

    async def validate_token(self, token: str) -> UserInfo:
        """Validate an access token and get user information."""
        headers = {"Authorization": f"Bearer {token}"}
        # Create a temporary client with the token for validation
        await self._ensure_client()
        url = urljoin(self.base_url + "/", "auth/me")
        response = await self._client.get(url, headers=headers)

        if response.status_code == 200:
            return UserInfo(**response.json())
        else:
            raise AuthenticationError("Token validation failed")

    async def logout(self, token: str) -> bool:
        """Logout and invalidate the access token."""
        headers = {"Authorization": f"Bearer {token}"}
        await self._ensure_client()
        url = urljoin(self.base_url + "/", "auth/logout")
        response = await self._client.post(url, headers=headers)
        return response.status_code in (200, 204)

    async def check_permission(self, token: str, permission: str) -> bool:
        """Check if a user has a specific permission."""
        headers = {"Authorization": f"Bearer {token}"}
        params = {"permission": permission}

        try:
            await self._ensure_client()
            url = urljoin(self.base_url + "/", "auth/check-permission")
            response = await self._client.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                return data.get("has_permission", False)
            else:
                return False
        except (AuthorizationError, NotFoundError):
            return False

    # ==========================================
    # USER OPERATIONS (App Mode)
    # ==========================================

    async def get_user_info(self, token: str) -> UserInfo:
        """Get detailed user information."""
        self._require_app()
        headers = {"Authorization": f"Bearer {token}"}
        await self._ensure_client()
        url = urljoin(self.base_url + "/", "users/me")
        response = await self._client.get(url, headers=headers)

        if response.status_code == 200:
            return UserInfo(**response.json())
        else:
            raise AuthenticationError("Failed to get user info")

    async def get_user_accounts(self, token: str) -> List[AccountInfo]:
        """Get user's accounts."""
        self._require_app()
        headers = {"Authorization": f"Bearer {token}"}
        await self._ensure_client()
        url = urljoin(self.base_url + "/", "accounts/")
        response = await self._client.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return [AccountInfo(**account) for account in data.get("items", [])]
        else:
            return []

    async def create_account(
        self, token: str, account_data: Dict[str, Any]
    ) -> AccountInfo:
        """Create a new account for the user."""
        self._require_app()
        headers = {"Authorization": f"Bearer {token}"}
        await self._ensure_client()
        url = urljoin(self.base_url + "/", "accounts/")
        response = await self._client.post(url, headers=headers, json=account_data)

        if response.status_code == 201:
            return AccountInfo(**response.json())
        else:
            raise IAMError("Failed to create account")

    # ==========================================
    # ADMIN OPERATIONS (Admin Mode Only)
    # ==========================================

    async def create_organization(
        self, request: OrganizationCreateRequest
    ) -> OrganizationInfo:
        """Create a new organization (admin only)."""
        self._require_admin()
        data = request.dict()
        response = await self._make_request("POST", "/admin/organizations", data=data)
        return OrganizationInfo(**response)

    async def get_organization_by_id(self, org_id: str) -> OrganizationInfo:
        """Get organization by ID (admin only)."""
        self._require_admin()
        response = await self._make_request("GET", f"/admin/organizations/{org_id}")
        return OrganizationInfo(**response)

    async def get_organization_by_slug(self, slug: str) -> Optional[OrganizationInfo]:
        """Get organization by slug (admin only)."""
        self._require_admin()
        try:
            # Get all organizations and find by slug
            response = await self._make_request("GET", "/admin/organizations")
            organizations = (
                response if isinstance(response, list) else response.get("items", [])
            )

            for org_data in organizations:
                if org_data.get("slug") == slug:
                    return OrganizationInfo(**org_data)
            return None
        except Exception:
            return None

    async def list_organizations(
        self, page: int = 1, size: int = 10
    ) -> List[OrganizationInfo]:
        """List organizations (admin only)."""
        self._require_admin()
        params = {"page": page, "size": size}
        response = await self._make_request(
            "GET", "/admin/organizations", params=params
        )
        items = response.get("items", [])
        return [OrganizationInfo(**item) for item in items]

    async def update_organization(
        self, org_id: str, updates: Dict[str, Any]
    ) -> OrganizationInfo:
        """Update an organization (admin only)."""
        self._require_admin()
        response = await self._make_request(
            "PUT", f"/admin/organizations/{org_id}", data=updates
        )
        return OrganizationInfo(**response)

    async def delete_organization(self, org_id: str) -> bool:
        """Delete an organization (admin only)."""
        self._require_admin()
        await self._make_request("DELETE", f"/admin/organizations/{org_id}")
        return True

    async def create_application(
        self, request: ApplicationCreateRequest
    ) -> ApplicationInfo:
        """Create a new application (admin only)."""
        self._require_admin()
        data = request.dict()
        response = await self._make_request("POST", "/admin/applications", data=data)
        return ApplicationInfo(**response)

    async def get_application_by_id(self, app_id: str) -> ApplicationInfo:
        """Get application by ID (admin only)."""
        self._require_admin()
        response = await self._make_request("GET", f"/admin/applications/{app_id}")
        return ApplicationInfo(**response)

    async def get_application_by_slug(self, slug: str) -> Optional[ApplicationInfo]:
        """Get application by slug (admin only)."""
        self._require_admin()
        try:
            # Get all applications and find by slug
            response = await self._make_request("GET", "/admin/applications")
            applications = (
                response if isinstance(response, list) else response.get("items", [])
            )

            for app_data in applications:
                if app_data.get("slug") == slug:
                    return ApplicationInfo(**app_data)
            return None
        except Exception:
            return None

    async def list_applications(
        self, org_id: Optional[str] = None, page: int = 1, size: int = 10
    ) -> List[ApplicationInfo]:
        """List applications (admin only)."""
        self._require_admin()
        params = {"page": page, "size": size}
        if org_id:
            params["org_id"] = org_id
        response = await self._make_request("GET", "/admin/applications", params=params)
        items = response.get("items", [])
        return [ApplicationInfo(**item) for item in items]

    async def update_application(
        self, app_id: str, updates: Dict[str, Any]
    ) -> ApplicationInfo:
        """Update an application (admin only)."""
        self._require_admin()
        response = await self._make_request(
            "PUT", f"/admin/applications/{app_id}", data=updates
        )
        return ApplicationInfo(**response)

    async def delete_application(self, app_id: str) -> bool:
        """Delete an application (admin only)."""
        self._require_admin()
        await self._make_request("DELETE", f"/admin/applications/{app_id}")
        return True

    async def create_user(self, request: UserCreateRequest) -> UserInfo:
        """Create a new user (admin only)."""
        self._require_admin()
        data = request.dict()
        response = await self._make_request("POST", "/admin/users", data=data)
        return UserInfo(**response)

    async def get_user_by_id(self, user_id: str) -> UserInfo:
        """Get user by ID (admin only)."""
        self._require_admin()
        response = await self._make_request("GET", f"/admin/users/{user_id}")
        return UserInfo(**response)

    async def get_user_by_username(self, username: str) -> Optional[UserInfo]:
        """Get user by username (admin only)."""
        self._require_admin()
        try:
            response = await self._make_request(
                "GET", f"/admin/users/username/{username}"
            )
            return UserInfo(**response)
        except NotFoundError:
            return None

    async def list_users(self, page: int = 1, size: int = 10) -> List[UserInfo]:
        """List users (admin only)."""
        self._require_admin()
        params = {"page": page, "size": size}
        response = await self._make_request("GET", "/admin/users", params=params)
        items = response.get("items", [])
        return [UserInfo(**item) for item in items]

    async def update_user(self, user_id: str, updates: Dict[str, Any]) -> UserInfo:
        """Update a user (admin only)."""
        self._require_admin()
        response = await self._make_request(
            "PUT", f"/admin/users/{user_id}", data=updates
        )
        return UserInfo(**response)

    async def delete_user(self, user_id: str) -> bool:
        """Delete a user (admin only)."""
        self._require_admin()
        await self._make_request("DELETE", f"/admin/users/{user_id}")
        return True

    async def create_api_key(self, request: APIKeyCreateRequest) -> APIKeyInfo:
        """Create a new API key (admin only)."""
        self._require_admin()
        data = request.dict()
        response = await self._make_request("POST", "/api-keys/", data=data)
        return APIKeyInfo(**response)

    async def get_api_key_by_id(self, key_id: str) -> APIKeyInfo:
        """Get API key by ID (admin only)."""
        self._require_admin()
        response = await self._make_request("GET", f"/admin/api-keys/{key_id}")
        return APIKeyInfo(**response)

    async def list_api_keys(
        self, app_id: Optional[str] = None, page: int = 1, size: int = 10
    ) -> List[APIKeyInfo]:
        """List API keys (admin only)."""
        self._require_admin()
        params = {"page": page, "size": size}
        if app_id:
            params["app_id"] = app_id
        response = await self._make_request("GET", "/admin/api-keys", params=params)
        items = response.get("items", [])
        return [APIKeyInfo(**item) for item in items]

    async def update_api_key(self, key_id: str, updates: Dict[str, Any]) -> APIKeyInfo:
        """Update an API key (admin only)."""
        self._require_admin()
        response = await self._make_request(
            "PUT", f"/admin/api-keys/{key_id}", data=updates
        )
        return APIKeyInfo(**response)

    async def delete_api_key(self, key_id: str) -> bool:
        """Delete an API key (admin only)."""
        self._require_admin()
        await self._make_request("DELETE", f"/admin/api-keys/{key_id}")
        return True

    async def revoke_api_key(self, key_id: str) -> bool:
        """Revoke an API key (admin only)."""
        self._require_admin()
        await self._make_request("POST", f"/admin/api-keys/{key_id}/revoke")
        return True

    # ==========================================
    # ROLE MANAGEMENT OPERATIONS (Admin Mode)
    # ==========================================

    async def create_role(self, request: Dict[str, Any]) -> "RoleInfo":
        """Create a new role (admin only)."""
        self._require_admin()
        response = await self._make_request("POST", "/admin/roles", data=request)
        return RoleInfo(**response)

    async def list_roles(
        self, app_id: Optional[str] = None, org_id: Optional[str] = None
    ) -> List["RoleInfo"]:
        """List roles (admin only)."""
        self._require_admin()
        params = {}
        if app_id:
            params["app_id"] = app_id
        if org_id:
            params["org_id"] = org_id
        response = await self._make_request("GET", "/admin/roles", params=params)
        roles = response if isinstance(response, list) else response.get("items", [])
        return [RoleInfo(**role) for role in roles]

    async def get_role_by_id(self, role_id: str) -> "RoleInfo":
        """Get role by ID (admin only)."""
        self._require_admin()
        response = await self._make_request("GET", f"/admin/roles/{role_id}")
        return RoleInfo(**response)

    async def update_role(self, role_id: str, updates: Dict[str, Any]) -> "RoleInfo":
        """Update a role (admin only)."""
        self._require_admin()
        response = await self._make_request(
            "PUT", f"/admin/roles/{role_id}", data=updates
        )
        return RoleInfo(**response)

    async def delete_role(self, role_id: str) -> bool:
        """Delete a role (admin only)."""
        self._require_admin()
        await self._make_request("DELETE", f"/admin/roles/{role_id}")
        return True

    # ==========================================
    # AUDIT LOG OPERATIONS (Admin Mode Only)
    # ==========================================

    async def create_audit_log(self, request: AuditLogCreateRequest) -> AuditLogInfo:
        """Create a new audit log entry (admin only)."""
        self._require_admin()
        data = request.dict()
        response = await self._make_request("POST", "/audit-logs/", data=data)
        return AuditLogInfo(**response)

    async def get_audit_logs(
        self, page: int = 1, limit: int = 100
    ) -> AuditLogListResponse:
        """Get paginated list of audit logs (admin only)."""
        self._require_admin()
        params = {"page": page, "limit": limit}
        response = await self._make_request("GET", "/audit-logs/", params=params)
        return AuditLogListResponse(**response)

    async def search_audit_logs(
        self, search_params: AuditLogSearchRequest
    ) -> AuditLogListResponse:
        """Search audit logs with filters (admin only)."""
        self._require_admin()
        data = search_params.dict(exclude_none=True)
        response = await self._make_request("POST", "/audit-logs/search", data=data)
        return AuditLogListResponse(**response)

    async def get_audit_log_by_id(self, audit_log_id: str) -> AuditLogInfo:
        """Get specific audit log by ID (admin only)."""
        self._require_admin()
        response = await self._make_request("GET", f"/audit-logs/{audit_log_id}")
        return AuditLogInfo(**response)

    async def get_user_audit_logs(
        self, user_id: str, limit: int = 100
    ) -> List[AuditLogInfo]:
        """Get audit logs for a specific user (admin only)."""
        self._require_admin()
        params = {"limit": limit}
        response = await self._make_request(
            "GET", f"/audit-logs/user/{user_id}", params=params
        )
        return [AuditLogInfo(**log) for log in response]

    async def get_application_audit_logs(
        self, application_id: str, limit: int = 100
    ) -> List[AuditLogInfo]:
        """Get audit logs for a specific application (admin only)."""
        self._require_admin()
        params = {"limit": limit}
        response = await self._make_request(
            "GET", f"/audit-logs/application/{application_id}", params=params
        )
        return [AuditLogInfo(**log) for log in response]

    async def get_organization_audit_logs(
        self, organization_id: str, limit: int = 100
    ) -> List[AuditLogInfo]:
        """Get audit logs for a specific organization (admin only)."""
        self._require_admin()
        params = {"limit": limit}
        response = await self._make_request(
            "GET", f"/audit-logs/organization/{organization_id}", params=params
        )
        return [AuditLogInfo(**log) for log in response]

    async def get_audit_stats(self) -> AuditLogStats:
        """Get audit log statistics overview (admin only)."""
        self._require_admin()
        response = await self._make_request("GET", "/audit-logs/stats/overview")
        return AuditLogStats(**response)

    # ==========================================
    # UTILITY METHODS
    # ==========================================

    def __repr__(self) -> str:
        """String representation of the client."""
        cred_type = "Admin" if self.can_admin else "App"
        return f"IAMClient(base_url='{self.base_url}', type='{cred_type}', app_id='{self.app_id}')"
