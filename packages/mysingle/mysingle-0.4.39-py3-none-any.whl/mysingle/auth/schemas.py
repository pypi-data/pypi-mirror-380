"""
통합된 Auth 스키마

IAM과 RBAC 관련 모든 스키마를 통합한 모듈입니다.
"""

# IAM 스키마 임포트 (PermissionResult는 IAM 버전 사용)
from .iam_schemas import *

# RBAC 스키마 임포트 (PermissionResult, BatchPermissionRequest 제외 - IAM 버전 사용)
from .rbac_schemas import (
    PermissionRequest,
)

# 공통으로 사용할 스키마만 __all__에 포함
__all__ = [
    # User 관련 (from iam_schemas)
    "UserLogin",
    "UserInfo",
    "UserUpdate",
    "AuthResponse",
    "TokenRefreshRequest",
    "PasswordChangeRequest",
    "SessionInfo",
    # Permission 관련 (from iam_schemas + rbac_schemas)
    "PermissionCheckRequest",
    "PermissionRequest",
    "PermissionResult",  # IAM 스키마 버전 사용
    "BatchPermissionRequest",
    "BatchPermissionResponse",
    "UserPermissionsResponse",
]
