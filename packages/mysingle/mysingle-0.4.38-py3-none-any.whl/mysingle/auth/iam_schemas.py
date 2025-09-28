"""IAM 서비스 관련 스키마 정의"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, EmailStr, Field


class UserLogin(BaseModel):
    """사용자 로그인 요청"""

    username: EmailStr  # IAM 서비스에서 username 필드 사용
    password: str
    remember_me: bool = False


class AuthResponse(BaseModel):
    """인증 응답"""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
    user: Optional["UserInfo"] = None  # IAM 서비스에서 Optional로 정의됨


class UserInfo(BaseModel):
    """사용자 정보"""

    id: str
    email: EmailStr
    fullname: str  # IAM 서비스에서 필수 필드
    is_active: bool = True
    is_verified: bool = False
    avatar_url: Optional[str] = None
    last_login_at: Optional[datetime] = None
    tenant_id: Optional[str] = None  # 테넌트 ID는 JWT에서 관리


class UserUpdate(BaseModel):
    """사용자 정보 수정"""

    fullname: Optional[str] = None
    avatar_url: Optional[str] = None
    is_active: Optional[bool] = None  # IAM 서비스와 일치


class PasswordChangeRequest(BaseModel):
    """비밀번호 변경 요청"""

    current_password: str
    new_password: str


class TokenRefreshRequest(BaseModel):
    """토큰 갱신 요청"""

    refresh_token: str


class PermissionCheckRequest(BaseModel):
    """권한 확인 요청"""

    user_id: str
    resource: str
    action: str
    tenant_id: Optional[str] = None
    context: Dict[str, Any] = Field(default_factory=dict)


class PermissionResult(BaseModel):
    """권한 확인 결과"""

    allowed: bool
    user_id: str
    resource: str
    action: str
    tenant_id: Optional[str] = None
    decision_id: Optional[str] = None
    timestamp: Optional[datetime] = None
    context: Dict[str, Any] = Field(default_factory=dict)
    cached: bool = False
    reason: Optional[str] = None


class SessionInfo(BaseModel):
    """세션 정보"""

    id: str
    user_id: str
    tenant_id: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    device_info: Optional[str] = None
    is_active: bool = True
    expires_at: datetime
    created_at: datetime
    last_accessed_at: Optional[datetime] = None


class BatchPermissionRequest(BaseModel):
    """배치 권한 확인 요청"""

    user_id: str
    tenant_id: Optional[str] = None
    permissions: List[Dict[str, str]]


class BatchPermissionResponse(BaseModel):
    """배치 권한 확인 응답"""

    user_id: str
    tenant_id: Optional[str] = None
    results: List[PermissionResult]
    timestamp: datetime


class UserPermissionsResponse(BaseModel):
    """사용자 권한 목록 응답"""

    user_id: str
    tenant_id: Optional[str] = None
    resource_type: Optional[str] = None
    permissions: List[Dict[str, Any]]
    timestamp: datetime


# Forward reference 해결
AuthResponse.model_rebuild()
