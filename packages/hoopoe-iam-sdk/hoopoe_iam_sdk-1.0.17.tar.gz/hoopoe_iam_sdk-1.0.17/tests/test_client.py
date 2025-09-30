"""
Basic tests for the IAM client functionality.
"""
import datetime
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from hoopoe_iam_sdk import AuthenticationError, IAMClient, IAMError
from hoopoe_iam_sdk.models import TokenInfo, UserInfo, UserResponse


class TestIAMClient:
    """Test cases for IAMClient."""

    def test_client_initialization(self):
        """Test IAM client can be initialized."""
        client = IAMClient(
            base_url="https://test.com",
            access_key="test-key",
            secret_key="test-secret",
            app_id="test-app",
        )
        assert client.base_url == "https://test.com"
        assert client.app_id == "test-app"

    def test_client_initialization_admin(self):
        """Test IAM client initialization with admin credentials."""
        client = IAMClient(base_url="https://admin-test.com", admin_api_key="admin-key")
        assert client.base_url == "https://admin-test.com"
        assert client._can_admin == True

    def test_headers_admin_auth(self):
        """Test admin authentication headers."""
        client = IAMClient(base_url="https://test.com", admin_api_key="admin-key")
        headers = client._get_headers()
        assert headers["Authorization"] == "Bearer admin-key"
        assert "X-Access-Key" not in headers
        assert "X-Secret-Key" not in headers

    def test_headers_app_auth(self):
        """Test app authentication headers."""
        client = IAMClient(
            base_url="https://test.com",
            access_key="test-access-key",
            secret_key="test-secret-key",
            app_id="test-app",
        )
        headers = client._get_headers()
        assert headers["X-IAM-Access-Key"] == "test-access-key"
        assert headers["X-IAM-Secret-Key"] == "test-secret-key"
        assert headers["X-App-ID"] == "test-app"
        assert "Authorization" not in headers

    @pytest.mark.asyncio
    async def test_authenticate_success(self):
        """Test successful authentication."""
        client = IAMClient(
            base_url="https://test.com",
            access_key="test-key",
            secret_key="test-secret",
            app_id="test-app",
            app_slug="test-app-slug",
            org_slug="test-org-slug",
        )

        mock_response = {
            "access_token": "test-token",
            "refresh_token": "test-refresh",
            "token_type": "Bearer",
            "expires_in": 3600,
        }

        with patch("httpx.AsyncClient.request", new_callable=AsyncMock) as mock_request:
            mock_response_obj = MagicMock()
            mock_response_obj.json.return_value = mock_response
            mock_response_obj.status_code = 200
            mock_request.return_value = mock_response_obj

            result = await client.authenticate("testuser", "testpass")

            assert isinstance(result, TokenInfo)
            assert result.access_token == "test-token"
            assert result.refresh_token == "test-refresh"

    @pytest.mark.asyncio
    async def test_authenticate_failure(self):
        """Test authentication failure."""
        client = IAMClient(
            base_url="https://test.com",
            access_key="test-key",
            secret_key="test-secret",
            app_id="test-app",
            app_slug="test-app-slug",
            org_slug="test-org-slug",
        )

        with patch("httpx.AsyncClient.request", new_callable=AsyncMock) as mock_request:
            mock_response_obj = MagicMock()
            mock_response_obj.status_code = 401
            mock_response_obj.json.return_value = {"detail": "Invalid credentials"}
            mock_response_obj.content = b'{"detail": "Invalid credentials"}'
            mock_request.return_value = mock_response_obj

            with pytest.raises(AuthenticationError):
                await client.authenticate("invalid", "invalid")

    @pytest.mark.asyncio
    async def test_validate_token_success(self):
        """Test successful token validation."""
        client = IAMClient(
            base_url="https://test.com",
            access_key="test-key",
            secret_key="test-secret",
            app_id="test-app",
            app_slug="test-app-slug",
            org_slug="test-org-slug",
        )

        mock_response = {
            "user_id": "123",
            "username": "testuser",
            "email": "test@example.com",
            "active": True,
        }

        with patch(
            "httpx.AsyncClient.post", new_callable=AsyncMock
        ) as mock_post, patch(
            "httpx.AsyncClient.get", new_callable=AsyncMock
        ) as mock_get:
            introspect_response = MagicMock()
            introspect_response.json.return_value = {
                "user_id": "123",
                "username": "testuser",
                "email": "test@example.com",
                "active": True,
            }
            introspect_response.status_code = 200
            introspect_response.content = b'{"active": true}'
            mock_post.return_value = introspect_response

            user_response = MagicMock()
            user_response.json.return_value = {
                "id": "123",
                "external_user_id": None,
                "username": "testuser",
                "first_name": "Test",
                "middle_name": None,
                "last_name": "User",
                "email": "test@example.com",
                "primary_phone_number": "1234567890",
                "secondary_phone_number": None,
                "status_message": None,
                "user_type": "ORGANIC",
                "is_email_verified": True,
                "is_phone_verified": True,
                "verification_status": "Verified",
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-02T00:00:00Z",
                "roles": [
                    {
                        "role_id": "role-123",
                        "role_slug": "test-role",
                        "role_name": "Test Role",
                        "scope": "global",
                        "level": "ADMIN",
                        "organization_id": None,
                    }
                ],
                "profile_metadata": {},
            }
            user_response.status_code = 200
            user_response.content = b'{"id": "123"}'
            mock_get.return_value = user_response

            result = await client.validate_token(token="test-token")

            assert isinstance(result, UserResponse)
            assert result.username == "testuser"
            assert result.email == "test@example.com"

    @pytest.mark.asyncio
    async def test_check_permission_success(self):
        """Test successful permission check."""
        client = IAMClient(
            base_url="https://test.com",
            access_key="test-key",
            secret_key="test-secret",
            app_id="test-app",
            app_slug="test-app-slug",
            org_slug="test-org-slug",
        )

        with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
            mock_response_obj = MagicMock()
            mock_response_obj.json.return_value = {"has_permission": True}
            mock_response_obj.status_code = 200
            mock_get.return_value = mock_response_obj

            result = await client.check_permission("test-token", "users:read")

            assert result is True

    @pytest.mark.asyncio
    async def test_check_permission_denied(self):
        """Test permission check denied."""
        client = IAMClient(
            base_url="https://test.com",
            access_key="test-key",
            secret_key="test-secret",
            app_id="test-app",
            app_slug="test-app-slug",
            org_slug="test-org-slug",
        )

        with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
            mock_response_obj = MagicMock()
            mock_response_obj.json.return_value = {"has_permission": False}
            mock_response_obj.status_code = 200
            mock_get.return_value = mock_response_obj

            result = await client.check_permission("test-token", "admin:write")

            assert result is False
