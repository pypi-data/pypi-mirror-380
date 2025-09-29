"""Pydantic models for Hoopoe IAM SDK."""

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class TokenInfo(BaseModel):
    """Token information returned by authentication."""

    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "Bearer"
    expires_in: int = Field(..., description="Token expiration time in seconds")
    scope: Optional[str] = None
    issued_at: Optional[datetime] = None


class UserInfo(BaseModel):
    """User information."""

    user_id: str
    username: str
    email: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class AccountInfo(BaseModel):
    """Account information."""

    account_id: str
    user_id: str
    account_type: str
    is_primary: bool = False
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class OrganizationInfo(BaseModel):
    """Organization information."""

    id: str
    name: str
    slug: str
    external_id: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    attributes: Optional[Dict[str, Any]] = None


class ApplicationInfo(BaseModel):
    """Application information."""

    id: str
    org_id: str
    name: str
    slug: str
    description: Optional[str] = None
    api_url: Optional[str] = None
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class PermissionInfo(BaseModel):
    """Permission information."""

    id: str
    name: str
    resource: str
    action: str
    description: Optional[str] = None
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class RoleInfo(BaseModel):
    """Role information."""

    id: str
    app_id: Optional[str] = None
    organization_id: Optional[str] = None
    name: str
    slug: str
    description: Optional[str] = None
    scope: str
    level: str
    is_default: bool = False
    permissions: List[str] = Field(default_factory=list)
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class APIKeyInfo(BaseModel):
    """API key information."""

    id: str
    name: str
    access_key: str
    description: Optional[str] = None
    scope: str = "APPLICATION"
    app_id: Optional[str] = None
    organization_id: Optional[str] = None
    is_active: bool = True
    expires_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    last_used: Optional[datetime] = None


class AuditLogInfo(BaseModel):
    """Audit log information."""

    id: str
    user_id: Optional[str] = None
    account_id: Optional[str] = None
    api_key_id: Optional[str] = None
    action: str
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    application_id: Optional[str] = None
    organization_id: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    request_id: Optional[str] = None
    status: str
    description: Optional[str] = None
    error_message: Optional[str] = None
    event_metadata: Optional[Dict[str, Any]] = None
    risk_score: Optional[str] = None
    timestamp: datetime
    duration_ms: Optional[str] = None


class DeviceInfo(BaseModel):
    """Device information."""

    id: str
    user_id: str
    device_name: str
    device_type: str
    device_fingerprint: str
    is_trusted: bool = False
    is_active: bool = True
    last_seen: Optional[datetime] = None
    created_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


# Request models for admin operations
class OrganizationCreateRequest(BaseModel):
    """Request model for creating an organization."""

    name: str
    slug: str
    external_id: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    attributes: Optional[Dict[str, Any]] = None


class ApplicationCreateRequest(BaseModel):
    """Request model for creating an application."""

    org_id: str
    name: str
    slug: str
    description: Optional[str] = None
    api_url: Optional[str] = None
    is_active: bool = True
    metadata: Optional[Dict[str, Any]] = None


class APIKeyCreateRequest(BaseModel):
    """Request model for creating an API key."""

    name: str
    description: Optional[str] = None
    scope: str = "APPLICATION"
    app_id: Optional[str] = None
    organization_id: Optional[str] = None
    expires_in_days: Optional[int] = None


class UserCreateRequest(BaseModel):
    """Request model for creating a user."""

    username: str
    email: str
    password: str
    full_name: Optional[str] = None
    is_active: bool = True
    metadata: Optional[Dict[str, Any]] = None


class AuditLogCreateRequest(BaseModel):
    """Request model for creating an audit log entry."""

    user_id: Optional[str] = None
    account_id: Optional[str] = None
    api_key_id: Optional[str] = None
    action: str = Field(..., min_length=1, max_length=128)
    resource_type: Optional[str] = Field(None, max_length=64)
    resource_id: Optional[str] = Field(None, max_length=36)
    application_id: Optional[str] = None
    organization_id: Optional[str] = None
    ip_address: Optional[str] = Field(None, max_length=64)
    user_agent: Optional[str] = Field(None, max_length=512)
    request_id: Optional[str] = Field(None, max_length=64)
    status: str = Field(..., max_length=32)
    description: Optional[str] = None
    error_message: Optional[str] = None
    event_metadata: Optional[Dict[str, Any]] = None
    risk_score: Optional[str] = Field(None, max_length=16)
    duration_ms: Optional[str] = Field(None, max_length=16)


class AuditLogSearchRequest(BaseModel):
    """Request model for searching audit logs."""

    user_id: Optional[str] = None
    account_id: Optional[str] = None
    application_id: Optional[str] = None
    organization_id: Optional[str] = None
    action: Optional[str] = None
    status: Optional[str] = None
    ip_address: Optional[str] = None
    risk_score: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    limit: Optional[int] = Field(default=100, ge=1, le=1000)


class AuditLogListResponse(BaseModel):
    """Paginated audit logs response."""

    logs: List[AuditLogInfo]
    total_count: int
    page: int
    limit: int


class AuditLogStats(BaseModel):
    """Audit log statistics."""

    total_logs: int
    success_count: int
    failure_count: int
    warning_count: int
    high_risk_count: int
    critical_risk_count: int
    recent_actions: List[str]
    top_users: List[Dict[str, str]]
    top_applications: List[Dict[str, str]]


# Response models
class PaginatedResponse(BaseModel):
    """Paginated response wrapper."""

    items: List[Any]
    total: int
    page: int = 1
    size: int = 10
    pages: int = Field(..., description="Total number of pages")

    @classmethod
    def create(cls, items: List[Any], total: int, page: int = 1, size: int = 10):
        """Create a paginated response."""
        pages = (total + size - 1) // size  # Ceiling division
        return cls(items=items, total=total, page=page, size=size, pages=pages)


class HealthCheckResponse(BaseModel):
    """Health check response."""

    status: str = "healthy"
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    version: str
    database: str = "connected"
    cache: Optional[str] = None
