# Hoopoe IAM SDK - Deployment and Usage Guide

This guide provides comprehensive instructions for deploying and using the Hoopoe IAM SDK in production environments.

## Table of Contents

1. [Package Deployment](#package-deployment)
2. [Installation and Setup](#installation-and-setup)
3. [Production Configuration](#production-configuration)
4. [Integration Examples](#integration-examples)
5. [Monitoring and Troubleshooting](#monitoring-and-troubleshooting)
6. [Security Best Practices](#security-best-practices)

## Package Deployment

### 1. GitHub Repository Setup

First, create a GitHub repository for the SDK:

```bash
# Initialize git repository in iam-service directory
cd iam-service
git init
git add .
git commit -m "Initial commit: Hoopoe IAM SDK v1.0.0"

# Add remote origin (replace with your GitHub repo URL)
git remote add origin https://github.com/eliff-tech/hoopoe-iam-sdk.git
git branch -M main
git push -u origin main
```

### 2. PyPI Account Setup

1. Create accounts on both PyPI and TestPyPI:
   - [PyPI](https://pypi.org/account/register/)
   - [TestPyPI](https://test.pypi.org/account/register/)

2. Generate API tokens:
   - Go to Account Settings → API tokens
   - Create tokens for both PyPI and TestPyPI
   - Store tokens securely

### 3. GitHub Secrets Configuration

Configure the following secrets in your GitHub repository:

```bash
# Go to GitHub repo → Settings → Secrets and variables → Actions
# Add the following repository secrets:

PYPI_API_TOKEN          # Your PyPI API token
TEST_PYPI_API_TOKEN     # Your TestPyPI API token
CODECOV_TOKEN           # Codecov token for coverage reports (optional)
```

### 4. Manual Package Build and Upload

For manual deployment or testing:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Check the package
twine check dist/*

# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Upload to PyPI (production)
twine upload dist/*
```

### 5. Automated Deployment

The SDK includes GitHub Actions workflows for automated deployment:

- **CI Workflow** (`.github/workflows/ci.yml`): Runs on every push/PR
- **PyPI Deployment** (`.github/workflows/publish-to-pypi.yml`): Runs on tags/releases

To trigger deployment:

```bash
# Create and push a version tag
git tag v1.0.0
git push origin v1.0.0

# Or create a GitHub release through the web interface
```

## Installation and Setup

### 1. Install the SDK

```bash
# Basic installation
pip install hoopoe-iam-sdk

# With development dependencies
pip install hoopoe-iam-sdk[dev]

# With all optional dependencies
pip install hoopoe-iam-sdk[dev,docs,test]
```

### 2. Environment Configuration

Create a `.env` file for your application:

```bash
# .env file
IAM_SERVICE_URL=https://iam.yourcompany.com
IAM_ACCESS_KEY=your-application-access-key
IAM_SECRET_KEY=your-application-secret-key
IAM_APP_ID=your-application-id

# Admin credentials (for setup scripts only)
IAM_ADMIN_API_KEY=your-admin-bearer-token
```

### 3. Initial Setup

Run the setup scripts for your applications:

```bash
# For matrimonial application
cd matrimonial
python scripts/iam_setup_using_sdk.py --iam-url https://iam.yourcompany.com

# For hoopoe-backend application
cd hoopoe-backend
python scripts/iam_setup_using_sdk.py --iam-url https://iam.yourcompany.com
```

## Production Configuration

### 1. FastAPI Application Integration

```python
# main.py
import os
from fastapi import FastAPI, Depends
from sdk import IAMClient
from sdk.middleware import IAMMiddleware, require_auth
from sdk.models import TokenInfo

app = FastAPI(title="Your Application")

# Initialize IAM client with production settings
iam_client = IAMClient(
    base_url=os.getenv("IAM_SERVICE_URL"),
    api_key=os.getenv("IAM_ACCESS_KEY"),
    secret_key=os.getenv("IAM_SECRET_KEY"),
    app_id=os.getenv("IAM_APP_ID"),
    timeout=30.0,
    max_retries=3,
    cache_ttl=300,
    verify_ssl=True  # Always True in production
)

# Add IAM middleware
app.add_middleware(
    IAMMiddleware,
    iam_client=iam_client,
    excluded_paths=["/health", "/docs", "/redoc", "/openapi.json", "/metrics"],
    auto_validate=True
)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "iam_connected": await iam_client.health_check()}


@app.get("/profile")
async def get_profile(token_info: TokenInfo = Depends(require_auth(iam_client))):
    return {
        "user_id": token_info.user_id,
        "username": token_info.username,
        "email": token_info.email
    }


# Graceful shutdown
@app.on_event("shutdown")
async def shutdown_event():
    await iam_client.close()
```

### 2. Docker Configuration

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install Hoopoe IAM SDK
RUN pip install hoopoe-iam-sdk

# Copy application code
COPY . .

# Set environment variables
ENV IAM_SERVICE_URL=""
ENV IAM_ACCESS_KEY=""
ENV IAM_SECRET_KEY=""
ENV IAM_APP_ID=""

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 3. Kubernetes Deployment

```yaml
# k8s-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: your-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: your-app
  template:
    metadata:
      labels:
        app: your-app
    spec:
      containers:
      - name: your-app
        image: your-registry/your-app:latest
        ports:
        - containerPort: 8000
        env:
        - name: IAM_SERVICE_URL
          valueFrom:
            secretKeyRef:
              name: iam-config
              key: service-url
        - name: IAM_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: iam-config
              key: access-key
        - name: IAM_SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: iam-config
              key: secret-key
        - name: IAM_APP_ID
          valueFrom:
            secretKeyRef:
              name: iam-config
              key: app-id
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5

---
apiVersion: v1
kind: Secret
metadata:
  name: iam-config
type: Opaque
stringData:
  service-url: "https://iam.yourcompany.com"
  access-key: "your-access-key"
  secret-key: "your-secret-key"
  app-id: "your-app-id"
```

## Integration Examples

### 1. Permission-Based Route Protection

```python
from sdk.middleware import require_permissions


@app.post("/admin/users")
async def create_user(
        user_data: dict,
        token_info: TokenInfo = Depends(require_permissions(
            iam_client,
            ["user:create:organization", "admin:access:organization"]
        ))
):
    # User has required permissions
    return {"message": "User created", "admin": token_info.username}


@app.delete("/messages/{message_id}")
async def delete_message(
        message_id: str,
        token_info: TokenInfo = Depends(require_permissions(
            iam_client,
            ["message:delete:organization"]
        ))
):
    # Check additional context-specific permissions
    checker = PermissionChecker(iam_client)
    await checker.check(
        user_id=token_info.user_id,
        resource="message",
        action="delete",
        scope="own",
        context={"message_id": message_id}
    )

    return {"deleted": message_id}
```

### 2. Admin Operations

```python
from sdk import IAMAdminClient


async def setup_new_tenant(org_name: str, admin_email: str):
    admin_client = IAMAdminClient(
        base_url=os.getenv("IAM_SERVICE_URL"),
        admin_api_key=os.getenv("IAM_ADMIN_API_KEY")
    )

    async with admin_client:
        # Create organization
        org = await admin_client.create_organization(OrganizationCreateRequest(
            name=org_name,
            slug=org_name.lower().replace(" ", "-"),
            attributes={"admin_email": admin_email}
        ))

        # Create default roles
        admin_role = await admin_client.create_role(RoleCreateRequest(
            org_id=org.id,
            name="Admin",
            slug="admin",
            description="Organization administrator"
        ))

        return org, admin_role
```

### 3. Error Handling

```python
from sdk.exceptions import (
    IAMError, AuthenticationError, AuthorizationError, NetworkError
)


@app.middleware("http")
async def iam_error_handler(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except AuthenticationError as e:
        return JSONResponse(
            status_code=401,
            content={"error": "Authentication failed", "message": str(e)}
        )
    except AuthorizationError as e:
        return JSONResponse(
            status_code=403,
            content={"error": "Access denied", "message": str(e)}
        )
    except NetworkError as e:
        logger.error(f"IAM service network error: {e}")
        return JSONResponse(
            status_code=503,
            content={"error": "Service temporarily unavailable"}
        )
    except IAMError as e:
        logger.error(f"IAM service error: {e}")
        return JSONResponse(
            status_code=500,
            content={"error": "Internal service error"}
        )
```

## Monitoring and Troubleshooting

### 1. Health Checks

```python
@app.get("/health/detailed")
async def detailed_health_check():
    try:
        # Test IAM connectivity
        iam_health = await iam_client.health_check()

        # Test token cache
        cache_size = len(iam_client._token_cache)

        return {
            "status": "healthy",
            "iam_service": {
                "connected": True,
                "response_time": "< 100ms",
                "cache_size": cache_size
            },
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }
```

### 2. Logging Configuration

```python
import logging
from sdk.middleware import IAMMiddleware

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Custom middleware with logging
class LoggingIAMMiddleware(IAMMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()

        try:
            response = await super().dispatch(request, call_next)

            # Log successful auth
            if hasattr(request.state, 'token_info'):
                logger.info(f"Authenticated request: {request.state.token_info.user_id}")

            return response
        except Exception as e:
            # Log auth failures
            logger.warning(f"Authentication failed for {request.url}: {e}")
            raise
        finally:
            duration = time.time() - start_time
            logger.info(f"Request processed in {duration:.3f}s")
```

### 3. Metrics and Monitoring

```python
from prometheus_client import Counter, Histogram, generate_latest

# Metrics
auth_requests = Counter('iam_auth_requests_total', 'Total auth requests', ['status'])
auth_duration = Histogram('iam_auth_duration_seconds', 'Auth request duration')

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    if request.url.path == "/metrics":
        return Response(generate_latest(), media_type="text/plain")

    with auth_duration.time():
        try:
            response = await call_next(request)
            auth_requests.labels(status='success').inc()
            return response
        except Exception as e:
            auth_requests.labels(status='error').inc()
            raise
```

## Security Best Practices

### 1. Credential Management

```python
# Use environment variables or secure vaults
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_iam_credentials():
    if os.getenv("ENVIRONMENT") == "production":
        # Use Azure Key Vault in production
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url="https://your-vault.vault.azure.net/", credential=credential)

        return {
            "access_key": client.get_secret("iam-access-key").value,
            "secret_key": client.get_secret("iam-secret-key").value,
        }
    else:
        # Use environment variables in development
        return {
            "access_key": os.getenv("IAM_ACCESS_KEY"),
            "secret_key": os.getenv("IAM_SECRET_KEY"),
        }
```

### 2. Rate Limiting

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/auth/login")
@limiter.limit("5/minute")
async def login(request: Request, credentials: LoginRequest):
    # Rate-limited login endpoint
    pass
```

### 3. SSL/TLS Configuration

```python
# Always verify SSL in production
iam_client = IAMClient(
    base_url="https://iam.yourcompany.com",
    verify_ssl=True,  # Never set to False in production
    timeout=30.0
)

# Use SSL context for additional security
import ssl
import httpx

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = True
ssl_context.verify_mode = ssl.CERT_REQUIRED

custom_client = httpx.AsyncClient(verify=ssl_context)
```

---

## Support and Resources

- **Documentation**: [https://docs.eliff.tech/iam-sdk](https://docs.eliff.tech/iam-sdk)
- **GitHub Issues**: [https://github.com/eliff-tech/hoopoe-iam-sdk/issues](https://github.com/eliff-tech/hoopoe-iam-sdk/issues)
- **PyPI Package**: [https://pypi.org/project/hoopoe-iam-sdk/](https://pypi.org/project/hoopoe-iam-sdk/)
- **Email Support**: support@eliff.tech

For production deployment assistance or enterprise support, contact: enterprise@eliff.tech
