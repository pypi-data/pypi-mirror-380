# Hoopoe IAM SDK

[![PyPI version](https://badge.fury.io/py/hoopoe-iam-sdk.svg)](https://badge.fury.io/py/hoopoe-iam-sdk)
[![Python Support](https://img.shields.io/pypi/pyversions/hoopoe-iam-sdk.svg)](https://pypi.org/project/hoopoe-iam-sdk/)
[![License](https://img.shields.io/github/license/eliff-tech/hoopoe-iam-sdk.svg)](https://github.com/eliff-tech/hoopoe-iam-sdk/blob/main/LICENSE)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](https://hoopoe-iam-sdk.readthedocs.io/)

Official Python SDK for Hoopoe IAM Service - Identity and Access Management made simple.

## Features

- 🔐 **Complete IAM Integration**: Full support for authentication, authorization, and user management
- 🚀 **Async/Await Support**: Built with modern Python async/await patterns
- 🔧 **Admin Operations**: Comprehensive admin client for managing organizations, applications, and users
- 🌐 **FastAPI Integration**: Built-in middleware for FastAPI applications
- 📊 **Type Safety**: Full type hints and Pydantic models for better development experience
- 🛡️ **Security First**: Secure token handling and validation
- 📖 **Well Documented**: Comprehensive documentation and examples

## Installation

### Basic Installation

```bash
pip install hoopoe-iam-sdk
```

### With FastAPI Support

```bash
pip install hoopoe-iam-sdk[fastapi]
```

### Development Installation

```bash
pip install hoopoe-iam-sdk[dev]
```

## Quick Start

### Basic Client Usage

```python
import asyncio
from sdk import IAMClient


async def main():
    # Initialize the client
    client = IAMClient(
        base_url="https://your-iam-service.com",
        api_key="your-api-key",
        secret_key="your-secret-key",
        app_id="your-app-slug"
    )

    # Authenticate a user
    token_info = await client.authenticate("username", "password")
    print(f"Access token: {token_info.access_token}")

    # Validate a token
    user_info = await client.validate_token(token_info.access_token)
    print(f"User: {user_info.username}")

    # Check permissions
    has_permission = await client.check_permission(
        token_info.access_token,
        "users:read"
    )
    print(f"Has permission: {has_permission}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Admin Client Usage

```python
import asyncio
from sdk import IAMAdminClient
from sdk.admin import OrganizationCreateRequest, ApplicationCreateRequest


async def main():
    # Initialize admin client
    admin_client = IAMAdminClient(
        base_url="https://your-iam-service.com",
        admin_api_key="your-admin-api-key"
    )

    # Create an organization
    org_request = OrganizationCreateRequest(
        name="My Company",
        slug="my-company",
        external_id="company-001",
        attributes={"website": "https://mycompany.com"},
        is_active=True
    )

    organization = await admin_client.create_organization(org_request)
    print(f"Created organization: {organization.name}")

    # Create an application
    app_request = ApplicationCreateRequest(
        org_id=organization.id,
        name="My App",
        slug="my-app",
        description="My application",
        api_url="https://myapp.com",
        is_active=True
    )

    application = await admin_client.create_application(app_request)
    print(f"Created application: {application.name}")


if __name__ == "__main__":
    asyncio.run(main())
```

### FastAPI Integration

```python
from fastapi import FastAPI, Depends
from sdk import IAMClient, create_iam_dependency
from sdk.middleware import IAMMiddleware
from sdk.models import UserInfo

app = FastAPI()

# Initialize IAM client
iam_client = IAMClient(
    base_url="https://your-iam-service.com",
    api_key="your-api-key",
    secret_key="your-secret-key",
    app_id="your-app-slug"
)

# Add IAM middleware
app.add_middleware(IAMMiddleware, iam_client=iam_client)

# Create dependency for authenticated users
get_current_user = create_iam_dependency(iam_client)


@app.get("/protected")
async def protected_endpoint(current_user: UserInfo = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}!"}


@app.get("/admin-only")
async def admin_endpoint(
        current_user: UserInfo = Depends(get_current_user.require_permission("admin:access"))
):
    return {"message": "Admin access granted"}
```

## Configuration

### Environment Variables

The SDK supports configuration via environment variables:

```bash
# Basic configuration
IAM_SERVICE_URL=https://your-iam-service.com
IAM_API_KEY=your-api-key
IAM_SECRET_KEY=your-secret-key
IAM_APP_ID=your-app-slug

# Admin configuration
IAM_ADMIN_API_KEY=your-admin-api-key

# Optional settings
IAM_TIMEOUT=30.0
IAM_CACHE_TTL=300
```

### Using .env Files

```python
from dotenv import load_dotenv
from sdk import IAMClient

load_dotenv()  # Load environment variables from .env file

# Client will automatically use environment variables
client = IAMClient()
```

## API Reference

### IAMClient

The main client for application-level operations:

- `authenticate(username, password)` - Authenticate user credentials
- `validate_token(token)` - Validate and decode access token
- `refresh_token(refresh_token)` - Refresh access token
- `check_permission(token, permission)` - Check user permission
- `get_user_info(token)` - Get user information
- `logout(token)` - Logout and invalidate token

### IAMAdminClient

Admin client for management operations:

- `create_organization(request)` - Create new organization
- `create_application(request)` - Create new application
- `create_user(request)` - Create new user
- `create_api_key(request)` - Create API key
- `get_organization_by_slug(slug)` - Get organization by slug
- `get_application_by_slug(slug)` - Get application by slug

### Models

All API responses use Pydantic models for type safety:

- `TokenInfo` - Token information and metadata
- `UserInfo` - User profile and account details
- `OrganizationInfo` - Organization details
- `ApplicationInfo` - Application configuration
- `PermissionInfo` - Permission details
- `RoleInfo` - Role configuration
- `APIKeyInfo` - API key information

## Error Handling

The SDK provides specific exception types:

```python
from sdk import IAMClient, IAMError, AuthenticationError, AuthorizationError

try:
    client = IAMClient(base_url="https://iam.example.com")
    result = await client.authenticate("user", "pass")
except AuthenticationError:
    print("Invalid credentials")
except AuthorizationError:
    print("Access denied")
except IAMError as e:
    print(f"IAM error: {e}")
```

## Testing

Run the test suite:

```bash
# Install development dependencies
pip install -e .[dev]

# Run tests
pytest

# Run with coverage
pytest --cov=sdk --cov-report=html
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone the repository
git clone https://github.com/eliff-tech/hoopoe-iam-sdk.git
cd hoopoe-iam-sdk

# Install in development mode
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install

# Run tests
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [https://hoopoe-iam-sdk.readthedocs.io/](https://hoopoe-iam-sdk.readthedocs.io/)
- **Issues**: [GitHub Issues](https://github.com/eliff-tech/hoopoe-iam-sdk/issues)
- **Email**: support@eliff.tech

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

---

Made with ❤️ by [Eliff Technology Solutions](https://eliff.tech)
