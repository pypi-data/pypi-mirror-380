"""
MySingle Auth Module

통합 인증/인가 시스템을 담당하는 모듈입니다.
"""

from .auth_cache import CacheEntry, CacheLevel, LocalCache, RedisCache
from .auth_utils import (
    AuthenticationContext,
    extract_auth_context,
    get_auth_context,
    is_public_path,
    set_auth_context,
)
from .client import UnifiedIAMClient, close_global_iam_client, get_iam_client
from .decorators import (
    audit_log,
    extract_tenant_from_request,
    require_permission,
)
from .dependencies import (
    EndpointAccessType,
    create_swagger_test_token,
    get_access_context,
    get_auth_token,
    get_swagger_auth_config,
    get_token_flexible,
    http_bearer,
    reusable_oauth2,
)
from .middleware import AuthMiddleware
from .rbac_middleware import RBACMiddleware
from .schemas import (
    AuthResponse,
    BatchPermissionRequest,
    BatchPermissionResponse,
    PasswordChangeRequest,
    PermissionCheckRequest,
    PermissionRequest,
    PermissionResult,
    SessionInfo,
    TokenRefreshRequest,
    UserInfo,
    UserLogin,
    UserPermissionsResponse,
    UserUpdate,
)

__all__ = [
    # Client
    "UnifiedIAMClient",
    "get_iam_client",
    "close_global_iam_client",
    # Schemas - 통합된 스키마들
    "UserLogin",
    "UserInfo",
    "UserUpdate",
    "AuthResponse",
    "TokenRefreshRequest",
    "PasswordChangeRequest",
    "SessionInfo",
    "PermissionCheckRequest",
    "PermissionRequest",
    "PermissionResult",
    "BatchPermissionRequest",
    "BatchPermissionResponse",
    "UserPermissionsResponse",
    # Decorators
    "extract_tenant_from_request",
    "require_permission",
    "audit_log",
    # Dependencies
    "EndpointAccessType",
    "get_auth_token",
    "get_token_flexible",
    "get_access_context",
    "get_swagger_auth_config",
    "create_swagger_test_token",
    "reusable_oauth2",
    "http_bearer",
    # Middleware
    "AuthMiddleware",
    "RBACMiddleware",
    # Cache
    "CacheEntry",
    "LocalCache",
    "RedisCache",
    "CacheLevel",
    # Utils
    "AuthenticationContext",
    "extract_auth_context",
    "get_auth_context",
    "set_auth_context",
    "is_public_path",
]
