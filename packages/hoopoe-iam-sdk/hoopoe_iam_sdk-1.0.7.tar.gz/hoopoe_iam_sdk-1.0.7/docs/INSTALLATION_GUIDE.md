# Hoopoe IAM SDK Installation Guide

This guide provides detailed instructions for installing and setting up the Hoopoe IAM SDK in different environments.

## Table of Contents

1. [Quick Installation](#quick-installation)
2. [Development Installation](#development-installation)
3. [Installation from Source](#installation-from-source)
4. [Docker Installation](#docker-installation)
5. [Virtual Environment Setup](#virtual-environment-setup)
6. [Configuration](#configuration)
7. [Verification](#verification)
8. [Troubleshooting](#troubleshooting)

## Quick Installation

### From PyPI (Recommended)

```bash
# Basic installation
pip install hoopoe-iam-sdk

# With FastAPI support
pip install hoopoe-iam-sdk[fastapi]

# With all optional dependencies
pip install hoopoe-iam-sdk[fastapi,dev]
```

### Requirements

- Python 3.8 or higher
- pip (Python package installer)
- Active internet connection

## Development Installation

### For Contributors

```bash
# Clone the repository
git clone https://github.com/eliff-tech/hoopoe-iam-sdk.git
cd hoopoe-iam-sdk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install

# Run tests to verify installation
pytest
```

### For Local Development

If you're working with a local copy of the SDK:

```bash
# Navigate to the SDK directory
cd hoopoe-iam-sdk

# Install in editable mode
pip install -e .

# Or with development dependencies
pip install -e .[dev]
```

## Installation from Source

### Download and Install

```bash
# Download the source
wget https://github.com/eliff-tech/hoopoe-iam-sdk/archive/main.zip
unzip main.zip
cd hoopoe-iam-sdk-main

# Install
pip install .
```

### Build from Source

```bash
# Clone repository
git clone https://github.com/eliff-tech/hoopoe-iam-sdk.git
cd hoopoe-iam-sdk

# Build package
python -m build

# Install built package
pip install dist/sdk-*.whl
```

## Docker Installation

### Using Docker Container

```dockerfile
FROM python:3.11-slim

# Install SDK
RUN pip install hoopoe-iam-sdk[fastapi]

# Copy your application
COPY . /app
WORKDIR /app

# Install application dependencies
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

### Docker Compose Example

```yaml
version: '3.8'
services:
  app:
    build: .
    environment:
      - IAM_SERVICE_URL=http://iam-service:9100
      - IAM_API_KEY=your-api-key
      - IAM_SECRET_KEY=your-secret-key
      - IAM_APP_ID=your-app-id
    ports:
      - "8000:8000"
    depends_on:
      - iam-service

  iam-service:
    image: eliff/hoopoe-iam:latest
    ports:
      - "9100:9100"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/iam
```

## Virtual Environment Setup

### Using venv

```bash
# Create virtual environment
python -m venv hoopoe-iam-env

# Activate (Linux/macOS)
source hoopoe-iam-env/bin/activate

# Activate (Windows)
hoopoe-iam-env\Scripts\activate

# Install SDK
pip install hoopoe-iam-sdk

# Deactivate when done
deactivate
```

### Using conda

```bash
# Create conda environment
conda create -n hoopoe-iam python=3.11

# Activate environment
conda activate hoopoe-iam

# Install SDK
pip install hoopoe-iam-sdk

# Deactivate when done
conda deactivate
```

### Using pipenv

```bash
# Initialize Pipenv
pipenv install hoopoe-iam-sdk

# With development dependencies
pipenv install hoopoe-iam-sdk[dev] --dev

# Activate shell
pipenv shell
```

## Configuration

### Environment Variables

Create a `.env` file in your project root:

```bash
# Required configuration
IAM_SERVICE_URL=http://localhost:9100
IAM_API_KEY=your-api-key
IAM_SECRET_KEY=your-secret-key
IAM_APP_ID=your-app-slug

# Optional configuration
IAM_TIMEOUT=30.0
IAM_CACHE_TTL=300

# Admin configuration (if needed)
IAM_ADMIN_API_KEY=your-admin-api-key
```

### Configuration File

Create `iam_config.json`:

```json
{
  "base_url": "http://localhost:9100",
  "api_key": "your-api-key",
  "secret_key": "your-secret-key",
  "app_id": "your-app-slug",
  "timeout": 30.0,
  "cache_ttl": 300
}
```

### Programmatic Configuration

```python
from sdk import IAMClient

# Direct configuration
client = IAMClient(
    base_url="http://localhost:9100",
    api_key="your-api-key",
    secret_key="your-secret-key",
    app_id="your-app-slug"
)

# From configuration file
import json

with open('iam_config.json') as f:
    config = json.load(f)
    client = IAMClient(**config)
```

## Verification

### Quick Test

```python
import asyncio
from sdk import IAMClient


async def test_installation():
    client = IAMClient(
        base_url="http://localhost:9100",
        api_key="test-key",
        secret_key="test-secret",
        app_id="test-app"
    )

    try:
        # This will test the connection
        connected = await client.test_connection()
        print(f"Connection test: {'✓ Passed' if connected else '✗ Failed'}")
    except Exception as e:
        print(f"Connection test failed: {e}")


# Run test
asyncio.run(test_installation())
```

### Version Check

```bash
# Check installed version
python -c "from hoopoe_iam_sdk import __version__; print(__version__)"

# Check all available functions
python -c "from hoopoe_iam_sdk import *; print(dir())"
```

### Run Examples

```bash
# Run basic usage example
cd hoopoe-iam-sdk/examples
python basic_usage.py

# Run FastAPI example (if FastAPI is installed)
python fastapi_integration.py
```

## Troubleshooting

### Common Issues

#### 1. Import Error

**Error**: `ModuleNotFoundError: No module named 'hoopoe_iam_sdk'`

**Solution**:
```bash
# Verify installation
pip list | grep hoopoe-iam-sdk

# Reinstall if necessary
pip uninstall hoopoe-iam-sdk
pip install hoopoe-iam-sdk
```

#### 2. Version Conflicts

**Error**: `pip` dependency resolution errors

**Solution**:
```bash
# Check for conflicts
pip check

# Create clean environment
python -m venv clean_env
source clean_env/bin/activate
pip install hoopoe-iam-sdk
```

#### 3. SSL/TLS Issues

**Error**: SSL certificate verification errors

**Solution**:
```bash
# Update certificates
pip install --upgrade certifi

# Or configure client to handle SSL
from sdk import IAMClient
import ssl

client = IAMClient(
    base_url="https://your-iam-service.com",
    api_key="your-key",
    verify_ssl=False  # Only for development
)
```

#### 4. Connection Issues

**Error**: Cannot connect to IAM service

**Solution**:
1. Verify IAM service is running
2. Check network connectivity
3. Verify URL and credentials
4. Check firewall settings

```bash
# Test connectivity
curl http://localhost:9100/health

# Check DNS resolution
nslookup your-iam-service.com
```

#### 5. Permission Issues

**Error**: Permission denied or authorization errors

**Solution**:
1. Verify API keys are correct
2. Check user permissions in IAM service
3. Ensure application is registered
4. Verify organization/application mapping

### Debug Mode

Enable debug logging:

```python
import logging
from sdk import IAMClient

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

client = IAMClient(
    base_url="http://localhost:9100",
    api_key="your-key",
    debug=True  # Enable debug mode
)
```

### Getting Help

1. **Documentation**: Check the [README.md](README.md) and [API documentation](https://hoopoe-iam-sdk.readthedocs.io/)
2. **Examples**: Review the [examples/](examples/) directory
3. **Issues**: Report bugs at [GitHub Issues](https://github.com/eliff-tech/hoopoe-iam-sdk/issues)
4. **Support**: Email support@eliff.tech

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.8 | 3.11+ |
| Memory | 128MB | 256MB+ |
| Storage | 10MB | 50MB+ |
| Network | HTTP/HTTPS | HTTPS with TLS 1.2+ |

### Performance Tips

1. **Connection Pooling**: The SDK uses connection pooling by default
2. **Caching**: Enable token caching for better performance
3. **Async Usage**: Use async/await patterns for better concurrency
4. **Batch Operations**: Use admin client for bulk operations

```python
# Good: Async usage
async with IAMClient() as client:
    result = await client.authenticate("user", "pass")

# Good: Context manager
with IAMClient() as client:
    # Synchronous operations if needed
    pass
```

---

For more detailed information, see the [README.md](README.md) and [API documentation](https://hoopoe-iam-sdk.readthedocs.io/).
