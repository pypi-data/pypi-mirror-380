"""Common authentication utilities for middleware."""

from typing import Any, Dict, Optional

from fastapi import Request

from mysingle.auth.client import UnifiedIAMClient
from mysingle.core.exceptions import AuthenticationError
from mysingle.core.logging import get_logger

logger = get_logger(__name__)


class AuthenticationContext:
    """인증 컨텍스트 클래스 - 미들웨어 간 인증 정보 공유"""

    def __init__(
        self,
        user_id: str,
        tenant_id: Optional[str] = None,
        token: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        roles: Optional[list[str]] = None,
        permissions: Optional[list[str]] = None,
        is_platform_user: bool = False,
    ):
        self.user_id = user_id
        self.tenant_id = tenant_id
        self.token = token
        self.payload = payload or {}
        self.roles = roles or []
        self.permissions = permissions or []
        self.is_platform_user = is_platform_user


# AuthenticationError는 mysingle.exceptions에서 import됨


async def extract_auth_context(
    request: Request,
) -> Optional[AuthenticationContext]:
    """
    요청에서 인증 컨텍스트 추출 (공통 JWT 처리 로직)

    Args:
        request: FastAPI Request 객체

    Returns:
        AuthenticationContext 또는 None

    Raises:
        AuthenticationError: 인증 실패 시
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise AuthenticationError(
            "Authorization header missing or invalid format"
        )

    token = auth_header[7:]  # "Bearer " 제거

    try:
        # UnifiedIAMClient를 사용하여 토큰 검증
        iam_client = UnifiedIAMClient()
        user_info = await iam_client.verify_token(token)
    except Exception as e:
        logger.error(f"Failed to verify JWT token: {e}")
        raise AuthenticationError("Invalid or expired token")

    # JWT 페이로드에서 추가 정보 추출
    payload = user_info.model_dump()
    is_platform_user = payload.get("is_platform_user", False)

    # TODO: JWT에서 roles와 permissions 추출 (향후 구현)
    # 현재는 IAM 서비스에서 별도 조회 필요
    roles = payload.get("roles", [])
    permissions = payload.get("permissions", [])

    # 인증 컨텍스트 생성
    context = AuthenticationContext(
        user_id=user_info.id,
        tenant_id=user_info.tenant_id,
        token=token,
        payload=payload,
        roles=roles,
        permissions=permissions,
        is_platform_user=is_platform_user,
    )

    return context


def get_auth_context(request: Request) -> Optional[AuthenticationContext]:
    """
    request.state에서 인증 컨텍스트 조회

    Args:
        request: FastAPI Request 객체

    Returns:
        AuthenticationContext 또는 None
    """
    return getattr(request.state, "auth_context", None)


def set_auth_context(request: Request, context: AuthenticationContext) -> None:
    """
    request.state에 인증 컨텍스트 설정

    Args:
        request: FastAPI Request 객체
        context: 설정할 인증 컨텍스트
    """
    request.state.auth_context = context


def is_public_path(path: str, public_paths: list[str]) -> bool:
    """
    공개 경로 여부 확인

    Args:
        path: 확인할 경로
        public_paths: 공개 경로 목록

    Returns:
        bool: 공개 경로 여부
    """
    return any(path.startswith(public_path) for public_path in public_paths)
