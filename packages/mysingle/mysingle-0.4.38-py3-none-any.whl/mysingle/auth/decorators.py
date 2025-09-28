"""RBAC 데코레이터 모듈 - 간소화된 함수 레벨 권한 확인"""

import functools
from typing import Any

from fastapi import Request

from mysingle.auth.auth_utils import get_auth_context
from mysingle.auth.dependencies import get_iam_client_instance
from mysingle.core.exceptions import (
    AuthenticationError,
    AuthorizationError,
    PermissionDeniedError,
    RBACServiceUnavailableError,
    RBACTimeoutError,
    ServiceUnavailableError,
    TenantRequiredError,
)
from mysingle.core.logging import (
    PerformanceTimer,
    get_logger,
    log_security_event,
)

logger = get_logger(__name__)


def extract_tenant_from_request(
    request: Request, tenant_param: str = "tenant_id"
) -> str | None:
    """Request에서 테넌트 ID 추출 (JWT 토큰 우선, 파라미터 fallback)"""
    # 1순위: JWT 토큰에서 추출
    auth_context = get_auth_context(request)
    if (
        auth_context
        and hasattr(auth_context, "tenant_id")
        and auth_context.tenant_id
    ):
        return auth_context.tenant_id

    # 2순위: URL path에서 추출 (하위 호환성)
    path_params = getattr(request, "path_params", {})
    if tenant_param in path_params:
        return path_params[tenant_param]

    # 3순위: Query params에서 추출 (하위 호환성)
    if tenant_param in request.query_params:
        return request.query_params[tenant_param]

    return None


def require_permission(
    resource: str,
    action: str,
    tenant_param: str = "tenant_id",
    user_id_param: str = "user_id",
) -> Any:
    """
    함수 레벨 권한 확인 데코레이터

    FastAPI Dependencies를 사용할 수 없는 일반 함수에서 사용하세요.
    FastAPI 엔드포인트에서는 guardrails.require_permission Dependencies를 사용하세요.

    Args:
        resource: 권한 확인할 리소스
        action: 수행할 액션 (read, write, delete 등)
        tenant_param: 테넌트 ID 매개변수명
        user_id_param: 사용자 ID 매개변수명
    """

    def decorator(func: Any) -> Any:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Request 객체 찾기
            request = None
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break

            if not request:
                # Request가 없는 경우 매개변수에서 정보 추출
                user_id = kwargs.get(user_id_param)
                tenant_id = kwargs.get(tenant_param)
            else:
                # Request에서 정보 추출 (JWT 토큰 우선)
                auth_context = get_auth_context(request)
                user_id = auth_context.user_id if auth_context else None

                # JWT 토큰에서 tenant_id 추출 시도
                tenant_id = (
                    getattr(auth_context, "tenant_id", None)
                    if auth_context
                    else None
                )

                # JWT에 tenant_id가 없으면 fallback으로 파라미터에서 추출
                if not tenant_id:
                    tenant_id = extract_tenant_from_request(
                        request, tenant_param
                    )

            if not user_id:
                raise AuthenticationError("User ID not found")
            # 플랫폼 사용자의 경우 tenant_id가 없을 수 있음
            if (
                not tenant_id
                and auth_context
                and not getattr(auth_context, "is_platform_user", False)
            ):
                raise TenantRequiredError(
                    "Tenant ID required for non-platform users"
                )

            # 권한 확인 (통합 IAM 클라이언트 사용, 내부적으로 캐싱됨)
            try:
                with PerformanceTimer(
                    operation="rbac_permission_check",
                    user_id=user_id,
                    tenant_id=tenant_id,
                    resource=resource,
                    service="rbac",
                ) as _timer:  # 성능 측정용 (context manager)
                    client = await get_iam_client_instance()
                    result = await client.check_permission(
                        user_id=user_id,
                        resource=resource,
                        action=action,
                        tenant_id=tenant_id,
                    )

                    # timer는 자동으로 성능 측정됨

                    if not result.allowed:
                        # 권한 거부 보안 감사 로깅
                        log_security_event(
                            event_type="PERMISSION_DENIED",
                            success=False,
                            user_id=user_id,
                            tenant_id=tenant_id,
                            resource=resource,
                            action=action,
                            reason=result.reason or "Insufficient permissions",
                            service="rbac",
                        )

                        raise PermissionDeniedError(
                            user_id=user_id,
                            resource=resource,
                            action=action,
                            reason=result.reason or "Insufficient permissions",
                        )

                    # 권한 허용 보안 감사 로깅
                    log_security_event(
                        event_type="PERMISSION_GRANTED",
                        success=True,
                        user_id=user_id,
                        tenant_id=tenant_id,
                        resource=resource,
                        action=action,
                        service="rbac",
                    )

            except PermissionDeniedError:
                raise AuthorizationError("권한이 없습니다")
            except RBACTimeoutError:
                raise ServiceUnavailableError(
                    "RBAC Service", "권한 확인 서비스가 응답하지 않습니다"
                )
            except RBACServiceUnavailableError:
                raise ServiceUnavailableError(
                    "RBAC Service", "권한 확인 서비스를 사용할 수 없습니다"
                )
            except Exception as e:
                logger.error(f"Permission check failed: {e}")
                raise ServiceUnavailableError(
                    "Permission Service", "권한 확인 중 오류가 발생했습니다"
                )

            return await func(*args, **kwargs)

        return wrapper

    return decorator


def audit_log(action: str, resource_type: str):
    """
    감사 로그 데코레이터 (간소화된 버전)

    Args:
        action: 수행된 액션 (create, read, update, delete 등)
        resource_type: 리소스 타입 (users, journals 등)
    """

    def decorator(func: Any) -> Any:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            import time

            start_time = time.time()
            user_id = None
            tenant_id = None

            # Request에서 컨텍스트 추출
            request = None
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break

            if request:
                auth_context = get_auth_context(request)
                if auth_context:
                    user_id = auth_context.user_id
                    # JWT 토큰에서 tenant_id 추출 (플랫폼 사용자는 None일 수 있음)
                    tenant_id = getattr(auth_context, "tenant_id", None)
                    is_platform_user = getattr(
                        auth_context, "is_platform_user", False
                    )

                    # 플랫폼 사용자인 경우 로그에 표시
                    if is_platform_user:
                        tenant_id = tenant_id or "platform"

            try:
                # 함수 실행
                result = await func(*args, **kwargs)

                # 성공 로그
                execution_time = time.time() - start_time
                logger.info(
                    f"AUDIT: {action} {resource_type} - "
                    f"user_id={user_id}, tenant_id={tenant_id}, "
                    f"status=success, execution_time={execution_time:.3f}s"
                )
                return result

            except Exception as e:
                # 실패 로그
                execution_time = time.time() - start_time
                logger.error(
                    f"AUDIT: {action} {resource_type} - "
                    f"user_id={user_id}, tenant_id={tenant_id}, "
                    f"status=error, error={str(e)}, execution_time={execution_time:.3f}s"
                )
                raise

        return wrapper

    return decorator
