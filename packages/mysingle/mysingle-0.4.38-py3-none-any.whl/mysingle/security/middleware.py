"""Security middleware for FastAPI applications."""

from typing import Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class SecurityMiddleware(BaseHTTPMiddleware):
    """통합 보안 미들웨어."""

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: Callable
    ) -> Response:
        """보안 검사 및 로깅을 수행합니다."""

        # TODO: Rate limiting, audit logging, privacy protection
        response = await call_next(request)
        return response
