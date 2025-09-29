# Hoopoe IAM SDK Authentication

The Hoopoe IAM SDK supports two types of authentication depending on the operation level:

## Admin-Level Authentication

For administrative operations (user management, organization setup, etc.), use admin API key authentication:

```python
from hoopoe_iam_sdk import IAMClient

# Admin client uses Authorization Bearer header
admin_client = IAMClient(
    base_url="https://iam.example.com",
    admin_api_key="your-admin-api-key"
)
```

**HTTP Headers Generated:**
- `Authorization: Bearer {admin_api_key}`
- `Content-Type: application/json`
- `Accept: application/json`
- `User-Agent: hoopoe-iam-sdk/1.0.0`

## Application-Level Authentication

For application operations (user authentication, permission checks, etc.), use access key and secret key authentication:

```python
from hoopoe_iam_sdk import IAMClient

# App client uses X-Access-Key and X-Secret-Key headers
app_client = IAMClient(
    base_url="https://iam.example.com",
    access_key="your-access-key",
    secret_key="your-secret-key",
    app_id="your-app-id",
    org_id="your-org-id"  # optional
)
```

**HTTP Headers Generated:**
- `X-Access-Key: {access_key}`
- `X-Secret-Key: {secret_key}`
- `X-App-ID: {app_id}`
- `X-Org-ID: {org_id}` (if provided)
- `Content-Type: application/json`
- `Accept: application/json`
- `User-Agent: hoopoe-iam-sdk/1.0.0`

## Authentication Flow

1. **Admin Operations:** Use `admin_api_key` for setup, user management, and administrative tasks
2. **App Operations:** Use `access_key` + `secret_key` for application runtime authentication and authorization

## Security Notes

- Never include sensitive credentials in environment files that are deployed to PyPI
- Always pass credentials explicitly as parameters to the IAMClient constructor
- Admin API keys should be kept secure and rotated regularly
- Access keys and secret keys are generated per application and should be unique
