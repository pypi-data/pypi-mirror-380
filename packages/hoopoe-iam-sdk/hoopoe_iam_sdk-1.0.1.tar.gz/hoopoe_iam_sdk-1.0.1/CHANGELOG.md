# Changelog

All notable changes to the Hoopoe IAM SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure and PyPI package setup

## [1.0.0] - 2024-09-28

### Added
- Initial release of Hoopoe IAM SDK
- Complete IAM client for authentication and authorization
- Admin client for organization and application management
- FastAPI middleware integration
- Type-safe Pydantic models for all API responses
- Comprehensive error handling with custom exceptions
- Async/await support throughout the SDK
- Environment variable configuration support
- Full test coverage with pytest
- Complete documentation and examples
- PyPI package structure with proper metadata
- Development tooling (black, isort, mypy, flake8)
- Pre-commit hooks for code quality
- GitHub Actions workflow for automated testing and deployment

### Features
- **Authentication**: User login, token validation, refresh tokens
- **Authorization**: Permission checking, role-based access control
- **User Management**: User creation, profile management, account operations
- **Organization Management**: Organization CRUD operations
- **Application Management**: Application registration and configuration
- **API Key Management**: Secure API key generation and management
- **Audit Logging**: Comprehensive audit trail support
- **Device Management**: User device tracking and management
- **FastAPI Integration**: Drop-in middleware for FastAPI applications
- **Type Safety**: Full type hints and runtime validation
- **Async Support**: Modern async/await patterns throughout

### Security
- Secure token handling and validation
- API key-based authentication
- Bearer token support
- Configurable token expiration
- Secure credential storage patterns

### Documentation
- Comprehensive README with examples
- PyPI deployment guide
- API documentation
- Development setup instructions
- Contributing guidelines

[Unreleased]: https://github.com/eliff-tech/hoopoe-iam-sdk/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/eliff-tech/hoopoe-iam-sdk/releases/tag/v1.0.0
