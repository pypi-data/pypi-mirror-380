"""통합 FastAPI 권한 확인 의존성 - JWT 토큰 기반 접근 제어"""

from enum import Enum
from typing import Any, Awaitable, Callable, Dict, List, Optional

from fastapi import Depends, Request
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
    OAuth2PasswordBearer,
)

from mysingle.auth.auth_utils import get_auth_context
from mysingle.auth.client import UnifiedIAMClient
from mysingle.auth.iam_schemas import UserInfo
from mysingle.core.config import settings
from mysingle.core.exceptions import (
    APIError,
    AuthenticationError,
    AuthorizationError,
    PermissionDeniedError,
    PlatformOnlyError,
    RBACServiceUnavailableError,
    RBACTimeoutError,
    ServiceUnavailableError,
    TenantOnlyError,
    TenantRequiredError,
)
from mysingle.core.logging import (
    PerformanceTimer,
    get_logger,
    log_security_event,
)

logger = get_logger(__name__)


class EndpointAccessType(str, Enum):
    """엔드포인트 접근 유형 정의"""

    TENANT_ONLY = "tenant_only"  # 테넌트 사용자만 접근 가능
    PLATFORM_ADMIN = "platform_admin"  # 플랫폼 관리자만 접근 가능
    HYBRID = "hybrid"  # 테넌트와 플랫폼 모두 접근 가능
    TENANT_WITH_APPROVAL = (
        "tenant_with_approval"  # 테넌트 소유자 승인 필요 (미래)
    )


# JWT 토큰 추출용 OAuth2 스키마 (Swagger UI 인증 지원)
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"/api/{settings.IAM_API_VERSION}/auth/login",  # 상대 경로 사용
    scheme_name="JWT Bearer Token",
    description="JWT Bearer 토큰을 입력하세요 (Bearer 접두사 없이)",
    auto_error=False,
)

# HTTP Bearer 스키마 (대안적 인증 방법)
http_bearer = HTTPBearer(
    scheme_name="Bearer Token",
    description="HTTP Bearer 인증 (Authorization: Bearer <token>)",
    auto_error=False,
)


async def get_auth_token(
    token: str = Depends(reusable_oauth2),
) -> Optional[str]:
    """의존성 주입용 JWT 토큰 추출 함수 (OAuth2PasswordBearer)"""
    if not token:
        raise AuthenticationError("Access Token required")
    return token


async def get_bearer_token(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> Optional[str]:
    """의존성 주입용 Bearer 토큰 추출 함수 (HTTPBearer)"""
    if not credentials:
        raise AuthenticationError("Bearer Token required")
    return credentials.credentials


async def get_token_flexible(
    request: Request,
    oauth_token: Optional[str] = Depends(reusable_oauth2),
    bearer_credentials: Optional[HTTPAuthorizationCredentials] = Depends(
        http_bearer
    ),
) -> str:
    """유연한 토큰 추출 - OAuth2, Bearer, 헤더에서 모두 지원"""

    # OAuth2 토큰이 있으면 우선 사용
    if oauth_token:
        return oauth_token

    # Bearer 토큰 확인
    if bearer_credentials:
        return bearer_credentials.credentials

    # Authorization 헤더에서 직접 추출
    if request:
        auth_header = request.headers.get("authorization", "")
        if auth_header.startswith("Bearer "):
            return auth_header.split(" ", 1)[1]

    raise AuthenticationError("Authentication token required")


# 전역 클라이언트 (캐싱 활성화)
_iam_client: Optional[UnifiedIAMClient] = None


async def get_iam_client_instance() -> UnifiedIAMClient:
    """IAM 클라이언트 인스턴스 반환 (싱글톤, 캐싱 활성화)"""
    global _iam_client
    if _iam_client is None:
        _iam_client = UnifiedIAMClient(enable_cache=True)
    return _iam_client


async def get_access_context(
    request: Request,
    access_type: EndpointAccessType,
    required_resource: Optional[str] = None,
    required_action: Optional[str] = None,
    token: str = Depends(get_token_flexible),
) -> Dict[str, Any]:
    """
    JWT 토큰을 기반으로 엔드포인트별 접근 컨텍스트를 제공하는 핵심 함수

    Args:
        request: FastAPI Request 객체
        access_type: 엔드포인트 접근 유형 (TENANT_ONLY, PLATFORM_ADMIN, etc.)
        required_resource: 권한 확인이 필요한 경우 리소스명
        required_action: 권한 확인이 필요한 경우 액션명

    Returns:
        Dict containing user_id, tenant_id, is_platform_user, access_type

    Raises:
        HTTPException: 인증 실패, 권한 부족, 접근 불가 등
    """
    # JWT 토큰에서 인증 컨텍스트 추출
    auth_context = get_auth_context(request)
    if not auth_context:
        log_security_event(
            event_type="AUTH_FAILURE",
            success=False,
            reason="JWT token missing",
            source_ip=request.client.host if request.client else None,
            user_agent=request.headers.get("user-agent"),
            service="guardrails",
        )
        raise AuthenticationError("JWT token required for authentication")

    user_id = auth_context.user_id
    tenant_id = getattr(auth_context, "tenant_id", None)
    is_platform_user = getattr(auth_context, "is_platform_user", False)

    # 접근 유형별 로직 처리
    if access_type == EndpointAccessType.TENANT_ONLY:
        # 테넌트 사용자만 접근 가능
        if is_platform_user:
            log_security_event(
                event_type="ACCESS_DENIED",
                success=False,
                user_id=user_id,
                tenant_id=tenant_id,
                reason="Platform user accessing tenant-only endpoint",
                source_ip=request.client.host if request.client else None,
                user_agent=request.headers.get("user-agent"),
                service="guardrails",
            )
            raise TenantOnlyError(
                "Platform users cannot access tenant-only endpoints"
            )
        if not tenant_id:
            log_security_event(
                event_type="ACCESS_DENIED",
                success=False,
                user_id=user_id,
                reason="Missing tenant ID for tenant-only access",
                source_ip=request.client.host if request.client else None,
                user_agent=request.headers.get("user-agent"),
                service="guardrails",
            )
            raise TenantRequiredError(
                "Tenant ID required for tenant-only access"
            )

    elif access_type == EndpointAccessType.PLATFORM_ADMIN:
        # 플랫폼 관리자만 접근 가능
        if not is_platform_user:
            log_security_event(
                event_type="ACCESS_DENIED",
                success=False,
                user_id=user_id,
                tenant_id=tenant_id,
                reason="Non-platform user accessing platform-only endpoint",
                source_ip=request.client.host if request.client else None,
                user_agent=request.headers.get("user-agent"),
                service="guardrails",
            )
            raise PlatformOnlyError("Platform admin access required")
        # 플랫폼 사용자의 권한 확인
        if required_resource and required_action:
            has_permission = await check_platform_permission(
                user_id=user_id,
                resource=required_resource,
                action=required_action,
            )
            if not has_permission:
                raise AuthorizationError(
                    f"Insufficient platform permissions for {required_resource}:{required_action}",
                    details={
                        "resource": required_resource,
                        "action": required_action,
                        "user_type": "platform_admin",
                    },
                )

    elif access_type == EndpointAccessType.HYBRID:
        # 테넌트와 플랫폼 모두 접근 가능
        if is_platform_user:
            # 플랫폼 사용자는 추가 권한 확인
            if required_resource and required_action:
                has_permission = await check_platform_permission(
                    user_id=user_id,
                    resource=required_resource,
                    action=required_action,
                )
                if not has_permission:
                    raise AuthorizationError(
                        f"Insufficient platform permissions for {required_resource}:{required_action}",
                        details={
                            "resource": required_resource,
                            "action": required_action,
                            "user_type": "platform_admin",
                            "access_type": "hybrid",
                        },
                    )
        else:
            # 테넌트 사용자는 기본 테넌트 권한 확인
            if not tenant_id:
                raise TenantRequiredError(
                    "Tenant ID required for tenant user access"
                )

    elif access_type == EndpointAccessType.TENANT_WITH_APPROVAL:
        # TODO: 테넌트 소유자 승인 기반 접근 (미래 구현)
        return await _handle_approval_based_access(
            user_id, tenant_id, is_platform_user
        )

    return {
        "user_id": user_id,
        "tenant_id": tenant_id,
        "is_platform_user": is_platform_user,
        "access_type": access_type.value,
    }


async def check_platform_permission(
    user_id: str,
    resource: str,
    action: str,
) -> bool:
    """
    플랫폼 사용자의 리소스별 권한을 확인하는 함수

    Args:
        user_id: 플랫폼 사용자 ID
        resource: 접근하려는 리소스 (예: "tenant:management", "ledger:global_view")
        action: 수행하려는 액션 (create, read, update, delete)

    Returns:
        bool: 권한이 있으면 True, 없으면 False
    """
    with PerformanceTimer(
        operation="check_platform_permission",
        user_id=user_id,
        resource=resource,
        service="guardrails",
    ) as _timer:  # 성능 측정용 (context manager)
        try:
            client = await get_iam_client_instance()
            permission_result = await client.check_permission(
                user_id=user_id,
                resource=resource,
                action=action,
                tenant_id=None,  # 플랫폼 레벨 권한은 tenant_id 없음
            )

            # 권한 확인 결과 로깅
            log_security_event(
                event_type="PERMISSION_CHECK",
                success=permission_result.allowed,
                user_id=user_id,
                resource=resource,
                action=action,
                reason=(
                    permission_result.reason
                    if not permission_result.allowed
                    else None
                ),
                service="guardrails",
            )

            return permission_result.allowed
        except Exception as e:
            logger.error(
                f"Platform permission check failed for user {user_id}: {e}"
            )
            log_security_event(
                event_type="PERMISSION_CHECK_ERROR",
                success=False,
                user_id=user_id,
                resource=resource,
                action=action,
                reason=str(e),
                service="guardrails",
            )
            return False


async def _handle_approval_based_access(
    user_id: str, tenant_id: Optional[str], is_platform_user: bool
) -> Dict[str, Any]:
    """
    승인 기반 접근 처리 (미래 구현용 스켈레톤)

    TODO: 테넌트 소유자의 승인을 받은 플랫폼 사용자만 접근할 수 있는 로직 구현
    - 승인 요청 생성
    - 승인 상태 확인
    - 승인된 권한 범위 확인
    """
    raise APIError(
        status_code=501,
        error="NOT_IMPLEMENTED",
        message="Approval-based access not yet implemented",
    )


async def get_current_user(
    request: Request,
) -> UserInfo:
    """현재 인증된 사용자 정보 반환 (JWT 토큰 기반)"""
    auth_context = get_auth_context(request)
    if not auth_context:
        raise AuthenticationError("JWT authentication token required")

    # Authorization 헤더에서 토큰 추출
    auth_header = request.headers.get("authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise AuthenticationError("Bearer token required")

    auth_token = auth_header.split(" ")[1]

    try:
        client = await get_iam_client_instance()
        user_info = await client.get_current_user(auth_token)
        return user_info
    except Exception as e:
        logger.error(f"Failed to get current user: {e}")
        raise AuthenticationError("Invalid authentication token")


async def get_current_active_user(current_user=Depends(get_current_user)):
    if not current_user.is_active:
        raise AuthorizationError(
            "User account is inactive",
            details={"user_id": current_user.id, "is_active": False},
        )
    return current_user


async def get_current_active_verified_user(
    current_user=Depends(get_current_active_user),
):
    if not current_user.is_verified:
        raise AuthorizationError(
            "Email verification required",
            details={"user_id": current_user.id, "is_verified": False},
        )
    return current_user


async def get_user_permissions(
    request: Request,
    user_id: str,
    tenant_id: Optional[str] = None,
    resource_type: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """사용자 권한 목록 조회 (JWT 토큰 기반)"""
    # Authorization 헤더에서 토큰 추출
    auth_header = request.headers.get("authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise AuthenticationError("Bearer token required")

    auth_token = auth_header.split(" ")[1]

    try:
        client = await get_iam_client_instance()
        permissions = await client.get_user_permissions(
            user_id=user_id,
            tenant_id=tenant_id,
            resource_type=resource_type,
            auth_token=auth_token,
        )
        return permissions
    except Exception as e:
        logger.error(f"Failed to get user permissions: {e}")
        raise ServiceUnavailableError(
            "IAM Service", "Failed to retrieve user permissions"
        )


def create_permission_dependency(
    resource: str,
    action: str,
    tenant_from_path: bool = True,
    user_id_from_token: bool = True,
    context_builder: Optional[Callable] = None,
    fail_open: bool = False,
) -> Callable[[Request], Awaitable[None]]:
    """
    통합된 권한 확인 의존성 팩토리

    가드레일과 RBAC 기능을 모두 지원하는 통합 의존성 생성기

    Args:
        resource: 리소스 명 (예: "ledger:journals")
        action: 액션 (create|read|update|delete)
        tenant_from_path: 경로/헤더에서 tenant_id 추출 여부
        user_id_from_token: JWT 토큰에서 user_id 추출 여부
        context_builder: 추가 컨텍스트 빌더 함수
        fail_open: 권한 확인 실패 시 접근 허용 여부 (개발용)

    Returns:
        FastAPI 의존성 함수
    """

    async def permission_dependency(request: Request) -> None:
        """실제 권한 확인을 수행하는 의존성 함수"""
        try:
            # 사용자 ID 추출 (통합 인증 유틸리티 사용)
            user_id = None
            tenant_id = None

            if user_id_from_token:
                auth_context = get_auth_context(request)
                if auth_context:
                    user_id = auth_context.user_id
                    tenant_id = auth_context.tenant_id

            if not user_id:
                raise AuthenticationError("Authentication context not found")

            # 테넌트 ID 추출 (헤더에서 우선)
            if tenant_from_path and not tenant_id:
                tenant_id = request.headers.get("x-tenant-id")
                if not tenant_id:
                    raise TenantRequiredError("X-Tenant-Id header required")

            # 추가 컨텍스트 빌드
            context = {}
            if context_builder:
                additional_context = context_builder(request)
                context.update(additional_context)

            # UnifiedIAMClient로 권한 확인 (내부적으로 UnifiedAuthCache 사용)
            with PerformanceTimer(
                operation="permission_check",
                user_id=user_id,
                tenant_id=tenant_id,
                resource=resource,
                service="guardrails",
            ) as _timer:  # 성능 측정용 (context manager)
                try:
                    client = await get_iam_client_instance()
                    permission_result = await client.check_permission(
                        user_id=user_id,
                        resource=resource,
                        action=action,
                        tenant_id=tenant_id,
                        context=context if context else None,
                    )

                    # 캐시 히트 여부는 클라이언트 내부에서 결정됨
                    # TODO: 캐시 히트 정보를 permission_result에서 추출 가능하다면 설정

                except TimeoutError as e:
                    logger.error(f"IAM service timeout: {e}")
                    if fail_open:
                        logger.warning("IAM timeout, but fail_open=True")
                        return
                    raise RBACTimeoutError(
                        timeout_seconds=30.0, operation="check_permission"
                    )
                except Exception as e:
                    logger.error(f"IAM service error: {e}")
                    if fail_open:
                        logger.warning(f"IAM error, but fail_open=True: {e}")
                        return
                    raise RBACServiceUnavailableError(
                        "IAM service unavailable"
                    )

            if not permission_result.allowed:
                logger.warning(
                    f"Permission denied: user={user_id}, resource={resource}, "
                    f"action={action}, tenant_id={tenant_id}"
                )

                # 권한 거부 보안 감사 로깅
                log_security_event(
                    event_type="PERMISSION_DENIED",
                    success=False,
                    user_id=user_id,
                    tenant_id=tenant_id,
                    resource=resource,
                    action=action,
                    reason=getattr(
                        permission_result, "reason", "Insufficient permissions"
                    ),
                    service="guardrails",
                )

                if fail_open:
                    logger.warning(
                        "fail_open=True, allowing access despite denial"
                    )
                    return

                raise PermissionDeniedError(
                    user_id=user_id,
                    resource=resource,
                    action=action,
                    reason="Insufficient permissions",
                )

            logger.debug(
                f"Permission granted: user={user_id}, resource={resource}, "
                f"action={action}"
            )

            # 권한 허용 보안 감사 로깅
            log_security_event(
                event_type="PERMISSION_GRANTED",
                success=True,
                user_id=user_id,
                tenant_id=tenant_id,
                resource=resource,
                action=action,
                service="guardrails",
            )

        except PermissionDeniedError:
            raise AuthorizationError("권한이 없습니다")
        except RBACTimeoutError as e:
            logger.error(f"RBAC timeout: {e}")
            raise ServiceUnavailableError(
                "RBAC Service", "권한 확인 서비스가 응답하지 않습니다"
            )
        except RBACServiceUnavailableError as e:
            logger.error(f"RBAC service unavailable: {e}")
            raise ServiceUnavailableError(
                "RBAC Service", "권한 확인 서비스를 사용할 수 없습니다"
            )
        except (
            AuthenticationError,
            AuthorizationError,
            TenantRequiredError,
            APIError,
        ):
            # 이미 표준화된 예외들은 그대로 전파
            raise
        except Exception as e:
            logger.error(f"Unexpected error in permission check: {e}")
            if fail_open:
                logger.warning(f"Unexpected error, but fail_open=True: {e}")
                return
            raise ServiceUnavailableError(
                "Permission Service", "권한 확인 중 오류가 발생했습니다"
            )

    return permission_dependency


async def check_permission(
    resource: str,
    action: str,
    request: Request,
    context: Optional[Dict[str, Any]] = None,
) -> None:
    """권한 확인 의존성 (JWT 토큰 기반)"""
    try:
        auth_context = get_auth_context(request)
        if not auth_context:
            raise AuthenticationError("JWT authentication context not found")

        # 테넌트 ID는 JWT 토큰에서 추출
        tenant_id = getattr(auth_context, "tenant_id", None)

        client = await get_iam_client_instance()
        permission_result = await client.check_permission(
            user_id=auth_context.user_id,
            resource=resource,
            action=action,
            tenant_id=tenant_id,
        )

        if not permission_result.allowed:
            raise AuthorizationError(
                "Permission denied",
                details={
                    "resource": resource,
                    "action": action,
                    "user_id": auth_context.user_id,
                    "tenant_id": tenant_id,
                },
            )

    except (AuthenticationError, AuthorizationError, APIError):
        raise
    except Exception as e:
        logger.error(f"Authorization system error: {e}")
        raise ServiceUnavailableError(
            "Authorization Service", "Authorization system error"
        )


def require_permission(
    resource: str,
    action: str,
    tenant_from_path: bool = True,
    user_id_from_token: bool = True,
    context_builder: Optional[Callable] = None,
    fail_open: bool = False,
) -> Any:
    """
    통합된 권한 확인 의존성

    Usage:
        # FastAPI Dependencies 방식 (권장)
        _auth: None = Depends(require_permission("ledger:journals", "create"))

        # 가드레일 방식 (하위 호환)
        _auth: None = require_permission("ledger:journals", "create")
    """
    return Depends(
        create_permission_dependency(
            resource=resource,
            action=action,
            tenant_from_path=tenant_from_path,
            user_id_from_token=user_id_from_token,
            context_builder=context_builder,
            fail_open=fail_open,
        )
    )


# ============================================================================
# Swagger 문서 지원을 위한 인증 설정
# ============================================================================


def get_swagger_auth_config() -> Dict[str, Any]:
    """Swagger UI에서 사용할 보안 스키마 설정 반환

    FastAPI 앱 설정 시 사용:
        app = FastAPI(
            title="MySingle API",
            swagger_ui_init_oauth={
                "clientId": "swagger-ui",
                "appName": "MySingle API",
                "usePkceWithAuthorizationCodeGrant": True,
            }
        )

        # 보안 스키마 추가
        security_config = get_swagger_auth_config()
        app.openapi_schema = {**app.openapi(), **security_config}
    """
    return {
        "components": {
            "securitySchemes": {
                "OAuth2PasswordBearer": {
                    "type": "oauth2",
                    "flows": {
                        "password": {
                            "tokenUrl": f"/api/{settings.IAM_API_VERSION}/auth/login",
                            "scopes": {
                                "read": "읽기 권한",
                                "write": "쓰기 권한",
                                "admin": "관리자 권한",
                            },
                        }
                    },
                    "description": "이메일과 비밀번호로 로그인하여 JWT 토큰을 받으세요",
                },
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                    "description": "JWT Bearer 토큰 인증",
                },
            }
        },
        "security": [{"OAuth2PasswordBearer": []}, {"BearerAuth": []}],
    }


def create_swagger_test_token(
    user_id: str = "test_user",
    tenant_id: str = "test_tenant",
    roles: Optional[List[str]] = None,
    permissions: Optional[List[str]] = None,
    expires_in: int = 3600,  # 1 hour
) -> str:
    """
    Swagger UI 테스트용 토큰 생성

    Args:
        user_id: 사용자 ID
        tenant_id: 테넌트 ID
        roles: 사용자 역할 목록
        permissions: 사용자 권한 목록
        expires_in: 토큰 만료 시간 (초)

    Returns:
        JWT 토큰 문자열
    """
    import os
    from datetime import datetime, timedelta

    import jwt

    if roles is None:
        roles = ["user"]
    if permissions is None:
        permissions = ["read:basic"]

    # JWT secret key from environment or default
    secret_key = os.getenv("JWT_SECRET_KEY", "mysingle-dev-secret-key")

    payload = {
        "user_id": user_id,
        "tenant_id": tenant_id,
        "roles": roles,
        "permissions": permissions,
        "exp": datetime.utcnow() + timedelta(seconds=expires_in),
        "iat": datetime.utcnow(),
        "type": "access_token",
    }

    return jwt.encode(payload, secret_key, algorithm="HS256")


# 편의 의존성 함수들
