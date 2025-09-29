"""Version information for Hoopoe IAM SDK."""

__version__ = "1.0.3"
__version_info__ = (1, 0, 3)

# API version compatibility
SUPPORTED_API_VERSIONS = ["v1", "v1.0"]
DEFAULT_API_VERSION = "v1"

# Backward compatibility mapping
COMPATIBILITY_MATRIX = {
    "1.0.0": {
        "min_iam_service_version": "0.1.0",
        "supported_features": [
            "auth",
            "users",
            "admin",
            "api_keys",
            "verifications",
            "accounts",
            "organizations",
            "applications",
            "permissions",
            "roles",
            "audit_logging",
            "token_introspection",
        ],
        "deprecated_features": [],
        "breaking_changes": [],
    }
}


def get_version():
    """Return the current SDK version."""
    return __version__


def is_compatible_with_service(service_version: str) -> bool:
    """Check if SDK version is compatible with IAM service version."""
    current_compat = COMPATIBILITY_MATRIX.get(__version__)
    if not current_compat:
        return False

    min_version = current_compat["min_iam_service_version"]
    # Simple version comparison - in production, use proper version comparison
    return service_version >= min_version
