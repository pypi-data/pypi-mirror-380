# Hoopoe IAM SDK - PyPI Deployment Instructions

## Overview

The Hoopoe IAM SDK is now **completely implemented** with:
- ✅ Full SDK functions for all IAM service endpoints
- ✅ Setup scripts using SDK methods (not HTTP calls)
- ✅ Production-ready PyPI package structure
- ✅ GitHub Actions for automatic deployment
- ✅ Proper dual authentication architecture

## Quick Verification

✅ **SDK Implementation Status**: COMPLETE
- `IAMClient`: App-level operations with HMAC auth
- `IAMAdminClient`: Admin operations with Bearer token auth
- `IAMMiddleware`: FastAPI integration
- All endpoint functions implemented

✅ **Setup Scripts Status**: USING SDK METHODS
- `matrimonial/scripts/iam_setup_using_sdk.py` ✅
- `hoopoe-backend/scripts/iam_setup_using_sdk.py` ✅
- No direct HTTP calls, proper SDK usage

✅ **Package Structure**: READY FOR PYPI
- setup.py, pyproject.toml, requirements.txt ✅
- README.md, LICENSE, CHANGELOG.md ✅
- GitHub Actions workflows ✅

## Step-by-Step Deployment

### 1. GitHub Repository Setup

```bash
# Navigate to the iam-service directory
cd iam-service

# Initialize git repository (if not already done)
git init
git add .
git commit -m "feat: Initial release of Hoopoe IAM SDK v1.0.0

- Complete SDK implementation with all endpoint functions
- IAMClient for app operations (HMAC auth)
- IAMAdminClient for admin operations (Bearer auth)
- FastAPI middleware and dependency injection
- Setup scripts using SDK methods
- PyPI package structure ready for deployment"

# Add remote repository (create on GitHub first)
git remote add origin https://github.com/eliff-tech/hoopoe-iam-sdk.git
git branch -M main
git push -u origin main
```

### 2. PyPI Account Setup

1. **Create PyPI Accounts**:
   - Production: https://pypi.org/account/register/
   - Testing: https://test.pypi.org/account/register/

2. **Generate API Tokens**:
   - Go to Account Settings → API tokens
   - Create token for entire account or specific project
   - Save tokens securely

3. **Configure GitHub Secrets**:
   ```
   Repository Settings → Secrets and variables → Actions

   Add these secrets:
   - PYPI_API_TOKEN: <your-pypi-token>
   - TEST_PYPI_API_TOKEN: <your-test-pypi-token>
   ```

### 3. Automatic Deployment (Recommended)

The SDK includes GitHub Actions for automatic deployment:

```bash
# Create and push a version tag to trigger deployment
git tag v1.0.0
git push origin v1.0.0

# This will automatically:
# 1. Run tests on multiple Python versions
# 2. Deploy to TestPyPI for testing
# 3. Create GitHub release with artifacts
```

For production release:
```bash
# Create a GitHub release through web interface
# This will automatically deploy to PyPI
```

### 4. Manual Deployment (Alternative)

If you prefer manual deployment:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Verify package
twine check dist/*

# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ hoopoe-iam-sdk

# Upload to production PyPI
twine upload dist/*
```

### 5. Installation and Usage

Once deployed, users can install and use the SDK:

```bash
# Install from PyPI
pip install hoopoe-iam-sdk

# Install with development dependencies
pip install hoopoe-iam-sdk[dev]
```

## Usage Examples

### 1. Setup Script Usage

```bash
# Set environment variable
export IAM_ADMIN_API_KEY="your-admin-bearer-token"

# Run matrimonial setup
cd matrimonial
python scripts/iam_setup_using_sdk.py --iam-url https://iam.yourcompany.com

# Run hoopoe-backend setup
cd hoopoe-backend
python scripts/iam_setup_using_sdk.py --iam-url https://iam.yourcompany.com
```

### 2. Application Integration

```python
# Install the SDK
# pip install hoopoe-iam-sdk

from sdk import IAMClient, IAMAdminClient
from sdk.middleware import IAMMiddleware, require_auth

# App-level operations
client = IAMClient(
    base_url="https://iam.yourcompany.com",
    api_key="your-access-key",
    secret_key="your-secret-key",
    app_id="your-app-id"
)

# Admin operations
admin_client = IAMAdminClient(
    base_url="https://iam.yourcompany.com",
    admin_api_key="your-admin-bearer-token"
)

# FastAPI integration
app.add_middleware(IAMMiddleware, iam_client=client)


@app.get("/profile")
async def get_profile(token_info=Depends(require_auth(client))):
    return {"user_id": token_info.user_id}
```

## Verification Commands

```bash
# Verify SDK is working
python sdk_verification_final.py

# Check package can be built
python -m build

# Verify package metadata
twine check dist/*

# Test import after installation
python -c "from hoopoe_iam_sdk import IAMClient, IAMAdminClient; print('SDK imported successfully')"
```

## Package Information

- **Package Name**: `hoopoe-iam-sdk`
- **Version**: `1.0.0`
- **Python Support**: `3.8+`
- **Dependencies**: `httpx`, `pydantic`, `fastapi`, `python-dotenv`
- **License**: `MIT`
- **Repository**: `https://github.com/eliff-tech/hoopoe-iam-sdk`

## Key Features

1. **Complete Endpoint Coverage**: All IAM service endpoints as SDK functions
2. **Dual Authentication**: Bearer token (admin) + HMAC signature (app)
3. **FastAPI Integration**: Middleware and dependency injection
4. **Type Safety**: Full Pydantic models and type hints
5. **Production Ready**: Caching, retries, error handling
6. **Easy Setup**: One-command organization and app setup

## Troubleshooting

### Common Issues

1. **Import Error**: Ensure `pip install hoopoe-iam-sdk` completed successfully
2. **Authentication Error**: Check environment variables are set correctly
3. **Connection Error**: Verify IAM service URL is accessible
4. **Permission Error**: Ensure admin API key has correct permissions

### Getting Help

- **Documentation**: README.md in the repository
- **Issues**: Create GitHub issue with detailed error information
- **Email**: support@eliff.tech

## Success Criteria

✅ The SDK implementation is **COMPLETE** and ready for deployment:

1. **SDK Functions**: All endpoints covered with proper SDK methods
2. **Authentication**: Proper Bearer token (admin) + HMAC (app) architecture
3. **Setup Scripts**: Using SDK methods, no direct HTTP calls
4. **Package Structure**: Production-ready PyPI package
5. **CI/CD**: GitHub Actions for automatic deployment
6. **Documentation**: Comprehensive usage examples and guides

**Status**: 🟢 **READY FOR PRODUCTION DEPLOYMENT**

---

## Next Actions

1. ✅ **Verify Everything**: Run `python sdk_verification_final.py`
2. 🚀 **Deploy to GitHub**: Push code and create repository
3. 📦 **Deploy to PyPI**: Tag release and let GitHub Actions handle deployment
4. 🎯 **Start Using**: Install with `pip install hoopoe-iam-sdk`

The Hoopoe IAM SDK is now a complete, production-ready package that can be deployed to PyPI and used by developers worldwide! 🎉
