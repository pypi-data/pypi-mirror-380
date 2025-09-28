"""공통 예외 처리 모듈."""

from typing import Any, Dict, Optional

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """API 에러 응답 모델."""

    error: str
    message: str
    details: Optional[Dict[str, Any]] = None
    request_id: Optional[str] = None


class AppError(Exception):
    """공통 앱 에러 클래스."""

    def __init__(self, msg: str, *, code: str = "APP_ERROR"):
        """앱 에러 초기화."""
        super().__init__(msg)
        self.code = code


class APIError(HTTPException):
    """공통 API 에러 클래스."""

    def __init__(
        self,
        status_code: int,
        error: str,
        message: str,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """API 에러 초기화."""
        self.error = error
        self.message = message
        self.details = details
        super().__init__(status_code=status_code, detail=message)


class ValidationError(APIError):
    """검증 에러."""

    def __init__(
        self, message: str, details: Optional[Dict[str, Any]] = None
    ) -> None:
        """검증 에러 초기화."""
        super().__init__(
            status_code=422,
            error="VALIDATION_ERROR",
            message=message,
            details=details,
        )


class NotFoundError(APIError):
    """리소스 없음 에러."""

    def __init__(self, resource: str, resource_id: str) -> None:
        """리소스 없음 에러 초기화."""
        super().__init__(
            status_code=404,
            error="NOT_FOUND",
            message=f"{resource} not found",
            details={"resource": resource, "id": resource_id},
        )


class ConflictError(APIError):
    """충돌 에러."""

    def __init__(
        self, message: str, details: Optional[Dict[str, Any]] = None
    ) -> None:
        """충돌 에러 초기화."""
        super().__init__(
            status_code=409,
            error="CONFLICT",
            message=message,
            details=details,
        )


class InternalServerError(APIError):
    """내부 서버 에러."""

    def __init__(self, message: str = "Internal server error") -> None:
        """내부 서버 에러 초기화."""
        super().__init__(
            status_code=500,
            error="INTERNAL_SERVER_ERROR",
            message=message,
        )


class RBACError(Exception):
    """RBAC 기본 예외"""

    def __init__(self, message: str, code: str = "RBAC_ERROR"):
        self.message = message
        self.code = code
        super().__init__(message)


class PermissionDeniedError(RBACError):
    """권한 거부 예외"""

    def __init__(
        self,
        user_id: str,
        resource: str,
        action: str,
        reason: str = "Permission denied",
    ):
        self.user_id = user_id
        self.resource = resource
        self.action = action
        message = f"Permission denied for user {user_id} on {resource}:{action} - {reason}"
        super().__init__(message, "PERMISSION_DENIED")


class RBACServiceUnavailableError(RBACError):
    """RBAC 서비스 사용 불가 예외"""

    def __init__(self, service_url: str, reason: str = "Service unavailable"):
        self.service_url = service_url
        message = f"RBAC service unavailable at {service_url}: {reason}"
        super().__init__(message, "RBAC_SERVICE_UNAVAILABLE")


class RBACTimeoutError(RBACError):
    """RBAC 서비스 타임아웃 예외"""

    def __init__(self, timeout_seconds: float, operation: str = "unknown"):
        self.timeout_seconds = timeout_seconds
        self.operation = operation
        message = (
            f"RBAC operation '{operation}' timed out after {timeout_seconds}s"
        )
        super().__init__(message, "RBAC_TIMEOUT")


# 인증/권한 관련 표준 API 예외 클래스들


class AuthenticationError(APIError):
    """인증 실패 예외 (401)"""

    def __init__(
        self,
        message: str = "Authentication required",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            status_code=401,
            error="AUTHENTICATION_ERROR",
            message=message,
            details=details,
        )


class AuthorizationError(APIError):
    """권한 부족 예외 (403)"""

    def __init__(
        self,
        message: str = "Insufficient permissions",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            status_code=403,
            error="AUTHORIZATION_ERROR",
            message=message,
            details=details,
        )


class TenantRequiredError(APIError):
    """테넌트 ID 필수 예외 (400)"""

    def __init__(self, message: str = "Tenant ID required"):
        super().__init__(
            status_code=400,
            error="TENANT_REQUIRED",
            message=message,
            details={"required_header": "X-Tenant-Id"},
        )


class PlatformOnlyError(APIError):
    """플랫폼 전용 접근 예외 (403)"""

    def __init__(self, message: str = "Platform admin access required"):
        super().__init__(
            status_code=403,
            error="PLATFORM_ONLY",
            message=message,
        )


class TenantOnlyError(APIError):
    """테넌트 전용 접근 예외 (403)"""

    def __init__(self, message: str = "Tenant user access required"):
        super().__init__(
            status_code=403,
            error="TENANT_ONLY",
            message=message,
        )


class ServiceUnavailableError(APIError):
    """서비스 사용 불가 예외 (503)"""

    def __init__(
        self,
        service_name: str,
        message: str = "Service temporarily unavailable",
    ):
        super().__init__(
            status_code=503,
            error="SERVICE_UNAVAILABLE",
            message=f"{service_name}: {message}",
            details={"service": service_name},
        )


async def api_error_handler(request: Request, exc: APIError) -> JSONResponse:
    """API 에러 핸들러."""
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=exc.error,
            message=exc.message,
            details=exc.details,
            request_id=getattr(request.state, "request_id", None),
        ).model_dump(exclude_none=True),
    )


async def http_exception_handler(
    request: Request, exc: HTTPException
) -> JSONResponse:
    """일반 HTTP 예외 핸들러."""
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error="HTTP_EXCEPTION",
            message=exc.detail,
            request_id=getattr(request.state, "request_id", None),
        ).model_dump(exclude_none=True),
    )


async def general_exception_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    """일반 예외 핸들러."""
    # 실제 환경에서는 로깅 처리
    _ = exc  # 미사용 인자 처리
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="INTERNAL_SERVER_ERROR",
            message="Internal server error",
            request_id=getattr(request.state, "request_id", None),
        ).model_dump(exclude_none=True),
    )


def register_exception_handlers(app: Any) -> None:
    """앱에 예외 핸들러들을 등록합니다."""
    app.add_exception_handler(APIError, api_error_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)
