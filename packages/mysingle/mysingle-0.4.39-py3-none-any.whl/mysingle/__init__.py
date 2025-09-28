"""
MySingle Package

엔터프라이즈 SaaS Financial/General Ledger 플랫폼을 위한 공통 라이브러리
"""

# 새로운 구조화된 모듈들
from .api import PrometheusMiddleware, create_fastapi_app
from .auth import (
    EndpointAccessType,
    UnifiedIAMClient,
    get_access_context,
    require_permission,
)
from .core import (
    CommonSettings,
    create_health_routers,
    get_logger,
    setup_logging,
)
from .data import (
    BaseCRUDService,
    BaseDoc,
    BaseResponseSchema,
    create_crud_router,
    get_database_name,
    init_mongo,
)
from .security import SecurityMiddleware
from .services import BaseClient, StorageClient

__all__ = [
    # Core 모듈
    "CommonSettings",
    "get_logger",
    "setup_logging",
    "create_health_routers",
    # Data 모듈
    "BaseDoc",
    "BaseResponseSchema",
    "BaseCRUDService",
    "create_crud_router",
    "init_mongo",
    "get_database_name",
    # Auth 모듈
    "UnifiedIAMClient",
    "require_permission",
    "get_access_context",
    "EndpointAccessType",
    # API 모듈
    "create_fastapi_app",
    "PrometheusMiddleware",
    # Services 모듈
    "BaseClient",
    "StorageClient",
    # Security 모듈
    "SecurityMiddleware",
]
