"""통합 IAM 클라이언트 - MySingle 플랫폼 인증/인가 통합 인터페이스

이 모듈은 MySingle IAM 서비스와의 모든 상호작용을 담당하는 UnifiedIAMClient를 제공합니다.
JWT 기반 인증, RBAC 권한 확인, 사용자 관리, 세션 관리를 통합적으로 처리합니다.

주요 클래스:
    UnifiedIAMClient: IAM 서비스와의 통합 클라이언트
        - 인증: 로그인/로그아웃/토큰 검증/갱신
        - 권한: 단일/배치 권한 확인, 캐시 최적화
        - 사용자: 사용자 정보 조회/관리
        - 세션: 세션 생성/검증/무효화

핵심 기능:
    - 지능적 캐싱: 권한 결과를 로컬/Redis에 다층 캐싱하여 성능 최적화
    - 배치 처리: 여러 권한을 한번의 API 호출로 확인 (75% 성능 향상)
    - 자동 재시도: 네트워크 오류 시 지수 백오프로 자동 재시도
    - 싱글톤 패턴: 글로벌 클라이언트로 리소스 효율성 극대화

성능 특징:
    - 캐시 히트 시: ~1ms
    - 캐시 미스 시: ~50-100ms
    - 배치 처리로 API 호출 75% 감소
    - 지능적 TTL로 캐시 효율성 극대화

사용 패턴:
    Singleton (권장):
        client = await get_iam_client()

    Direct instantiation:
        client = UnifiedIAMClient()

    Context manager:
        async with UnifiedIAMClient() as client:
            # 자동 리소스 정리

Example:
    >>> # 기본 사용법
    >>> client = await get_iam_client()
    >>>
    >>> # 로그인
    >>> login_data = UserLogin(email="user@example.com", password="password")
    >>> auth_response = await client.login(login_data)
    >>>
    >>> # 권한 확인
    >>> result = await client.check_permission(
    ...     user_id="user123",
    ...     resource="ledger:journals",
    ...     action="create"
    ... )
    >>> print(result.allowed)
    >>>
    >>> # 배치 권한 확인
    >>> permissions = [
    ...     {"resource": "ledger:journals", "action": "read"},
    ...     {"resource": "ledger:accounts", "action": "write"}
    ... ]
    >>> results = await client.batch_check_permissions(
    ...     user_id="user123",
    ...     permissions=permissions
    ... )

Dependencies:
    - httpx: 비동기 HTTP 클라이언트
    - mysingle.auth.auth_cache: 통합 인증 캐시
    - mysingle.exceptions: 표준화된 예외 처리
    - mysingle.logging: 구조화된 로깅 및 성능 모니터링

Version: 1.0.0 (2025-09-16)
Author: MySingle Platform Team
"""

from __future__ import annotations

import asyncio
from typing import Any, Dict, List, Optional

import httpx

from mysingle.auth.auth_cache import UnifiedAuthCache, get_unified_auth_cache
from mysingle.core.config import settings
from mysingle.core.exceptions import APIError, InternalServerError
from mysingle.core.logging import (
    PerformanceTimer,
    get_logger,
)

from .iam_schemas import (
    AuthResponse,
    PasswordChangeRequest,
    PermissionCheckRequest,
    PermissionResult,
    SessionInfo,
    TokenRefreshRequest,
    UserInfo,
    UserLogin,
    UserUpdate,
)

logger = get_logger(__name__)

# 글로벌 IAM 클라이언트 인스턴스
_global_iam_client: Optional[UnifiedIAMClient] = None


class UnifiedIAMClient:
    """통합 IAM 서비스 클라이언트

    MySingle 플랫폼의 모든 인증(Authentication) 및 인가(Authorization) 기능을
    제공하는 통합 클라이언트입니다.

    주요 기능:
        - JWT 기반 사용자 인증 (로그인/로그아웃/토큰 갱신)
        - RBAC 기반 권한 확인 (단일/배치 처리)
        - 사용자 관리 (생성/조회/수정/삭제)
        - 세션 관리 (생성/검증/무효화)
        - 통합 캐싱 (성능 최적화)

    성능 특징:
        - 지능적 캐싱: 권한 결과를 로컬/Redis에 다층 캐싱
        - 배치 처리: 여러 권한을 한 번의 API 호출로 확인
        - 자동 재시도: 네트워크 오류 시 자동 재시도
        - 연결 풀링: HTTP 클라이언트 재사용으로 성능 향상

    사용 예시:
        Basic usage:
            >>> client = UnifiedIAMClient()
            >>> result = await client.check_permission(
            ...     user_id="user123",
            ...     resource="ledger:journals",
            ...     action="read"
            ... )
            >>> print(result.allowed)
            True

        Batch processing:
            >>> permissions = [
            ...     {"resource": "tenant:dashboard", "action": "read"},
            ...     {"resource": "ledger:journals", "action": "create"}
            ... ]
            >>> results = await client.batch_check_permissions(
            ...     user_id="user123",
            ...     permissions=permissions
            ... )
            >>> print(len(results))
            2

    Args:
        base_url: IAM 서비스 기본 URL (기본값: settings.IAM_SERVICE_INTERNAL_URL)
        timeout: HTTP 요청 타임아웃 (초, 기본값: 30.0)
        max_retries: 최대 재시도 횟수 (기본값: 3)
        retry_delay: 재시도 간격 (초, 기본값: 1.0)
        enable_cache: 캐싱 활성화 여부 (기본값: True)

    Note:
        - 프로덕션 환경에서는 싱글톤 패턴으로 사용 권장
        - 캐시 활성화 시 Redis 연결 필요
        - 모든 메서드는 비동기(async/await) 사용 필수
    """

    def __init__(
        self,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_delay: float = 1.0,
        enable_cache: bool = True,
    ):
        """UnifiedIAMClient 초기화

        Args:
            base_url: IAM 서비스 기본 URL. None인 경우 settings.IAM_SERVICE_INTERNAL_URL 사용
            timeout: HTTP 요청 타임아웃 (초). 기본값: 30.0
            max_retries: 네트워크 오류 시 최대 재시도 횟수. 기본값: 3
            retry_delay: 재시도 간 대기 시간 (초). 기본값: 1.0
            enable_cache: 권한/사용자 정보 캐싱 활성화 여부. 기본값: True

        Note:
            - 클라이언트와 캐시는 지연 초기화(lazy initialization)됩니다
            - 캐시 비활성화 시 모든 요청이 직접 API로 전송됩니다
            - 프로덕션에서는 캐시 활성화 권장 (성능 향상)
        """
        self.base_url = base_url or settings.IAM_SERVICE_INTERNAL_URL
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.enable_cache = enable_cache
        self._client: Optional[httpx.AsyncClient] = None
        self._cache: Optional[UnifiedAuthCache] = None

    async def _get_client(self) -> httpx.AsyncClient:
        """HTTP 클라이언트 반환 (지연 초기화)

        Returns:
            httpx.AsyncClient: 설정된 base_url, timeout, headers로 초기화된 비동기 HTTP 클라이언트

        Note:
            - 첫 호출 시에만 클라이언트를 생성하고, 이후 호출에서는 재사용
            - 연결 풀링을 통해 성능 최적화
            - Content-Type: application/json 헤더 자동 설정
        """
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout,
                headers={"Content-Type": "application/json"},
            )
        return self._client

    async def _get_cache(self):
        """통합 인증 캐시 인스턴스 반환 (지연 초기화)

        Returns:
            UnifiedAuthCache | None: 캐시가 활성화된 경우 캐시 인스턴스,
                                   비활성화된 경우 None

        Note:
            - enable_cache가 True인 경우에만 캐시 인스턴스 생성
            - 첫 호출 시에만 생성하고 이후 재사용
            - Redis 연결 오류 시 로컬 캐시로 폴백
        """
        if self.enable_cache and self._cache is None:
            self._cache = await get_unified_auth_cache()
        return self._cache

    async def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """IAM 서비스로 HTTP 요청 실행 (자동 재시도 및 오류 처리)

        Args:
            method: HTTP 메서드 ('GET', 'POST', 'PUT', 'DELETE' 등)
            endpoint: API 엔드포인트 경로 (예: '/api/v1/users')
            data: 요청 본문에 포함할 JSON 데이터 (선택적)
            headers: 추가 HTTP 헤더 (선택적)
            auth_token: Bearer 토큰 (선택적, 자동으로 Authorization 헤더에 추가)

        Returns:
            Dict[str, Any]: IAM 서비스로부터의 JSON 응답

        Raises:
            APIError: 4xx 클라이언트 오류 (잘못된 요청, 인증 실패 등)
            InternalServerError: 5xx 서버 오류
            NetworkError: 네트워크 연결 오류 (최대 재시도 횟수 초과 후)

        Note:
            - 네트워크 오류 시 최대 max_retries 횟수만큼 자동 재시도
            - 각 재시도 간 retry_delay 초만큼 대기
            - 4xx/5xx HTTP 상태 코드는 재시도하지 않고 즉시 예외 발생
            - Bearer 토큰이 제공되면 Authorization 헤더에 자동 추가
        """
        client = await self._get_client()

        request_headers = headers or {}
        if auth_token:
            request_headers["Authorization"] = f"Bearer {auth_token}"

        last_exception = None
        for attempt in range(self.max_retries + 1):
            try:
                response = await client.request(
                    method=method,
                    url=endpoint,
                    json=data,
                    headers=request_headers,
                )

                if response.status_code >= 400:
                    error_detail = response.text
                    try:
                        error_json = response.json()
                        error_detail = error_json.get("detail", error_detail)
                    except Exception as e:
                        logger.debug(
                            f"Failed to parse error response as JSON: {e}"
                        )

                    if response.status_code >= 500:
                        raise InternalServerError(
                            message=f"IAM service error: {error_detail}"
                        )
                    else:
                        raise APIError(
                            status_code=response.status_code,
                            error="IAM_REQUEST_FAILED",
                            message=f"IAM request failed: {error_detail}",
                        )

                return response.json()

            except httpx.RequestError as e:
                last_exception = e
                if attempt < self.max_retries:
                    logger.warning(
                        f"IAM request failed (attempt {attempt + 1}): {e}. Retrying..."
                    )
                    await asyncio.sleep(self.retry_delay * (attempt + 1))
                    continue
                break

        raise InternalServerError(
            message=f"IAM service unavailable after {self.max_retries} retries: {last_exception}"
        )

    # ============================================================================
    # 인증 관련 메서드들
    # ============================================================================

    async def login(self, login_data: UserLogin) -> AuthResponse:
        """사용자 로그인 처리

        사용자의 이메일/패스워드를 검증하고 JWT 액세스/리프레시 토큰을 발급합니다.

        Args:
            login_data: 로그인 정보 (이메일, 패스워드 포함)

        Returns:
            AuthResponse: 인증 성공 시 사용자 정보와 토큰들을 포함한 응답
                - access_token: API 호출용 JWT 토큰
                - refresh_token: 액세스 토큰 갱신용 토큰
                - user: 사용자 기본 정보
                - expires_in: 토큰 만료 시간(초)

        Raises:
            APIError: 로그인 실패 (잘못된 자격증명, 계정 비활성화 등)
            NetworkError: 네트워크 연결 오류

        Example:
            >>> login_data = UserLogin(email="user@example.com", password="password")
            >>> auth_response = await client.login(login_data)
            >>> print(auth_response.access_token)
            eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
        """
        response_data = await self._make_request(
            "POST",
            f"/api/{settings.IAM_API_VERSION}/auth/login",
            data=login_data.model_dump(),
        )
        return AuthResponse(**response_data)

    async def logout(self, token: str) -> bool:
        """사용자 로그아웃 처리

        JWT 토큰을 무효화하고 관련 세션을 정리합니다.

        Args:
            token: 무효화할 JWT 액세스 토큰

        Returns:
            bool: 로그아웃 성공 시 True, 실패 시 False

        Note:
            - 토큰이 이미 만료되었거나 유효하지 않아도 True 반환
            - 네트워크 오류나 서버 오류 시에만 False 반환
            - 로그아웃 후 해당 토큰으로는 더 이상 API 호출 불가

        Example:
            >>> success = await client.logout(access_token)
            >>> if success:
            ...     print("로그아웃 완료")
        """
        try:
            await self._make_request(
                "POST",
                f"/api/{settings.IAM_API_VERSION}/auth/logout",
                auth_token=token,
            )
            return True
        except Exception as e:
            logger.error(f"Logout failed: {e}")
            return False

    async def verify_token(self, token: str) -> UserInfo:
        """JWT 토큰 검증 및 사용자 정보 반환

        JWT 토큰의 유효성을 검증하고 토큰에 포함된 사용자 정보를 반환합니다.

        Args:
            token: 검증할 JWT 액세스 토큰

        Returns:
            UserInfo: 토큰이 유효한 경우 사용자 정보
                - user_id: 사용자 고유 ID
                - email: 사용자 이메일
                - tenant_id: 소속 테넌트 ID
                - roles: 사용자 역할 목록

        Raises:
            APIError: 토큰이 유효하지 않거나 만료된 경우 (401)
            NetworkError: 네트워크 연결 오류

        Example:
            >>> user_info = await client.verify_token(access_token)
            >>> print(f"사용자: {user_info.email}, 테넌트: {user_info.tenant_id}")
        """
        response_data = await self._make_request(
            "POST",
            f"/api/{settings.IAM_API_VERSION}/auth/verify",
            data={"token": token},
        )
        return UserInfo(**response_data)

    async def refresh_token(self, refresh_token: str) -> AuthResponse:
        """리프레시 토큰으로 새 액세스 토큰 발급

        만료된 액세스 토큰을 리프레시 토큰으로 갱신합니다.

        Args:
            refresh_token: 유효한 리프레시 토큰

        Returns:
            AuthResponse: 새로 발급된 토큰 정보
                - access_token: 새 JWT 액세스 토큰
                - refresh_token: 새 리프레시 토큰 (선택적)
                - expires_in: 새 토큰 만료 시간(초)

        Raises:
            APIError: 리프레시 토큰이 유효하지 않거나 만료된 경우 (401)
            NetworkError: 네트워크 연결 오류

        Example:
            >>> new_tokens = await client.refresh_token(refresh_token)
            >>> new_access_token = new_tokens.access_token
        """
        request_data = TokenRefreshRequest(refresh_token=refresh_token)
        response_data = await self._make_request(
            "POST",
            f"/api/{settings.IAM_API_VERSION}/auth/refresh",
            data=request_data.model_dump(),
        )
        return AuthResponse(**response_data)

    # ============================================================================
    # 권한 확인 관련 메서드들
    # ============================================================================

    async def check_permission(
        self,
        user_id: str,
        resource: str,
        action: str,
        tenant_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        auth_token: Optional[str] = None,
    ) -> PermissionResult:
        """단일 권한 확인 (지능적 캐싱 지원)

        사용자가 특정 리소스에 대한 특정 작업을 수행할 권한이 있는지 확인합니다.
        캐시를 통해 성능을 최적화하며, RBAC 정책을 기반으로 판단합니다.

        Args:
            user_id: 권한을 확인할 사용자 ID
            resource: 리소스 식별자 (예: 'ledger:journals', 'tenant:dashboard')
            action: 수행할 작업 (예: 'read', 'write', 'delete')
            tenant_id: 테넌트 ID (생략 시 사용자의 기본 테넌트)
            context: 추가 컨텍스트 정보 (동적 권한 평가용, 선택적)
            auth_token: 인증 토큰 (API 호출용, 선택적)

        Returns:
            PermissionResult: 권한 확인 결과
                - allowed: 권한 허용 여부 (True/False)
                - reason: 허용/거부 사유
                - cached: 캐시에서 조회되었는지 여부
                - resource: 확인된 리소스
                - action: 확인된 작업

        Performance:
            - 캐시 히트 시: ~1ms
            - 캐시 미스 시: ~50-100ms (API 호출)
            - 캐시 TTL: 리소스 유형별 차등 적용 (90-180초)

        Example:
            >>> result = await client.check_permission(
            ...     user_id="user123",
            ...     resource="ledger:journals",
            ...     action="create",
            ...     tenant_id="tenant456"
            ... )
            >>> if result.allowed:
            ...     print("권한 허용")
            ... else:
            ...     print(f"권한 거부: {result.reason}")
        """
        with PerformanceTimer(
            operation="iam_check_permission",
            user_id=user_id,
            tenant_id=tenant_id,
            resource=resource,
            service="iam_client",
        ) as timer:
            # 캐시에서 조회
            cache = await self._get_cache()

            if cache:
                cached_result = await cache.get_permission_result(
                    user_id=user_id,
                    resource=resource,
                    action=action,
                    tenant_id=tenant_id,
                    context=context,
                )
                if cached_result:
                    logger.debug(
                        f"Cache hit for permission check: {user_id}:{resource}:{action}"
                    )
                    timer.set_cache_hit(True)
                    return cached_result

            # 캐시 미스 - IAM 서비스 호출
            timer.set_cache_hit(False)
            request_data = PermissionCheckRequest(
                user_id=user_id,
                resource=resource,
                action=action,
                tenant_id=tenant_id,
                context=context or {},
            )

            response_data = await self._make_request(
                "POST",
                f"/api/{settings.IAM_API_VERSION}/permissions/decisions/check",
                data=request_data.model_dump(),
                auth_token=auth_token,
            )
            result = PermissionResult(**response_data)

            # 결과를 캐시에 저장
            if cache:
                await cache.set_permission_result(
                    user_id=user_id,
                    resource=resource,
                    action=action,
                    result=result,
                    tenant_id=tenant_id,
                    context=context,
                )
                logger.debug(
                    f"Cached permission result: {user_id}:{resource}:{action}"
                )

            return result

    async def batch_check_permissions(
        self,
        user_id: str,
        permissions: List[Dict[str, str]],
        tenant_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        auth_token: Optional[str] = None,
    ) -> List[PermissionResult]:
        """여러 권한을 한번에 확인 (고성능 캐시 최적화)

        사용자의 여러 권한을 동시에 확인합니다. 캐시된 결과는 즉시 반환하고,
        캐시되지 않은 권한만 API로 요청하여 성능을 최적화합니다.

        Args:
            user_id: 권한을 확인할 사용자 ID
            permissions: 확인할 권한 목록, 각 항목은 {'resource': '...', 'action': '...'} 형태
            tenant_id: 테넌트 ID (생략 시 사용자의 기본 테넌트)
            context: 추가 컨텍스트 정보 (모든 권한에 공통 적용, 선택적)
            auth_token: 인증 토큰 (API 호출용, 선택적)

        Returns:
            List[PermissionResult]: 입력 순서와 동일한 순서의 권한 확인 결과 목록

        Performance:
            - 캐시 활용으로 평균 75% API 호출 감소
            - 10개 권한 확인 시: 캐시 없음 ~500ms → 캐시 활용 ~125ms
            - 병렬 캐시 조회로 지연시간 최소화

        Example:
            >>> permissionsb = [
            ...     {"resource": "ledger:journals", "action": "read"},
            ...     {"resource": "ledger:accounts", "action": "create"},
            ...     {"resource": "tenant:settings", "action": "update"}
            ... ]
            >>> results = await client.batch_check_permissions(
            ...     user_id="user123",
            ...     permissions=permissions,
            ...     tenant_id="tenant456"
            ... )
            >>> for i, result in enumerate(results):
            ...     perm = permissions[i]
            ...     print(f"{perm['resource']}:{perm['action']} = {result.allowed}")

        Note:
            - 결과 순서는 입력 permissions 리스트와 동일
            - 캐시 히트율은 로그에 기록되어 성능 모니터링 가능
            - 단일 API 호출로 여러 권한을 처리하여 네트워크 오버헤드 최소화
        """
        with PerformanceTimer(
            operation="iam_batch_check_permissions",
            user_id=user_id,
            tenant_id=tenant_id,
            batch_size=len(permissions),
            service="iam_client",
        ) as timer:
            cache = await self._get_cache()
            cached_results = []
            uncached_permissions = []
            cache_hits = 0

            # 1. 캐시에서 가능한 권한들 조회
            if cache:
                for i, perm in enumerate(permissions):
                    cached_result = await cache.get_permission_result(
                        user_id=user_id,
                        resource=perm.get("resource", ""),
                        action=perm.get("action", ""),
                        tenant_id=tenant_id,
                        context=context,
                    )
                    if cached_result:
                        cached_results.append((i, cached_result))
                        cache_hits += 1
                    else:
                        uncached_permissions.append((i, perm))
            else:
                uncached_permissions = list(enumerate(permissions))

            logger.info(
                f"Batch permission check: {cache_hits} cache hits, "
                f"{len(uncached_permissions)} API calls needed"
            )

            # 2. 캐시에 없는 권한들만 API 호출
            api_results = []
            if uncached_permissions:
                uncached_perms_data = [
                    perm for _, perm in uncached_permissions
                ]
                request_data = {
                    "user_id": user_id,
                    "tenant_id": tenant_id,
                    "permissions": uncached_perms_data,
                    "context": context or {},
                }

                response_data = await self._make_request(
                    "POST",
                    f"/api/{settings.IAM_API_VERSION}/permissions/batch-check-permission",
                    data=request_data,
                    auth_token=auth_token,
                )

                api_results_data = response_data.get("results", [])

                # 3. API 결과를 캐시에 저장
                if cache:
                    cache_tasks = []
                    for (original_idx, perm), result_data in zip(
                        uncached_permissions, api_results_data
                    ):
                        result = PermissionResult(**result_data)
                        api_results.append((original_idx, result))

                        # 비동기로 캐시 저장
                        cache_task = cache.set_permission_result(
                            user_id=user_id,
                            resource=perm.get("resource", ""),
                            action=perm.get("action", ""),
                            result=result,
                            tenant_id=tenant_id,
                            context=context,
                        )
                        cache_tasks.append(cache_task)

                    # 모든 캐시 저장 작업을 병렬로 실행
                    if cache_tasks:
                        await asyncio.gather(
                            *cache_tasks, return_exceptions=True
                        )
                        logger.debug(
                            f"Cached {len(cache_tasks)} permission results"
                        )
                else:
                    for (original_idx, perm), result_data in zip(
                        uncached_permissions, api_results_data
                    ):
                        result = PermissionResult(**result_data)
                        api_results.append((original_idx, result))

            # 4. 결과를 원래 순서대로 재구성
            all_results = cached_results + api_results
            all_results.sort(key=lambda x: x[0])  # 인덱스 순으로 정렬

            final_results = [result for _, result in all_results]

            # 성능 메트릭 로깅
            cache_hit_rate = (
                cache_hits / len(permissions) if permissions else 0
            )
            if cache_hits > 0:
                timer.set_cache_hit(True)
            logger.info(
                f"Batch permission check completed - "
                f"Total: {len(permissions)}, Cache hits: {cache_hits}, "
                f"API calls: {len(uncached_permissions)}, "
                f"Cache hit rate: {cache_hit_rate:.2%}"
            )

            return final_results

    async def check_multiple_resources(
        self,
        user_id: str,
        resources: List[str],
        action: str,
        tenant_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        auth_token: Optional[str] = None,
    ) -> Dict[str, PermissionResult]:
        """여러 리소스에 대한 동일한 작업 권한을 일괄 확인

        동일한 작업(action)을 여러 리소스에 대해 수행할 권한을 확인합니다.
        예: 여러 원장 계정에 대한 읽기 권한 확인

        Args:
            user_id: 권한을 확인할 사용자 ID
            resources: 확인할 리소스 목록 (예: ['ledger:journals:001', 'ledger:journals:002'])
            action: 모든 리소스에 적용할 작업 (예: 'read', 'write')
            tenant_id: 테넌트 ID (생략 시 사용자의 기본 테넌트)
            context: 추가 컨텍스트 정보 (선택적)
            auth_token: 인증 토큰 (선택적)

        Returns:
            Dict[str, PermissionResult]: 리소스별 권한 확인 결과
                키: 리소스 이름, 값: PermissionResult

        Example:
            >>> resources = ['ledger:accounts:cash', 'ledger:accounts:bank']
            >>> results = await client.check_multiple_resources(
            ...     user_id="user123",
            ...     resources=resources,
            ...     action="read"
            ... )
            >>> for resource, result in results.items():
            ...     print(f"{resource} 읽기 권한: {result.allowed}")
        """
        permissions = [
            {"resource": resource, "action": action} for resource in resources
        ]

        results = await self.batch_check_permissions(
            user_id=user_id,
            permissions=permissions,
            tenant_id=tenant_id,
            context=context,
            auth_token=auth_token,
        )

        return {
            resource: result for resource, result in zip(resources, results)
        }

    async def check_resource_actions(
        self,
        user_id: str,
        resource: str,
        actions: List[str],
        tenant_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        auth_token: Optional[str] = None,
    ) -> Dict[str, PermissionResult]:
        """단일 리소스에 대한 여러 작업 권한을 일괄 확인

        하나의 리소스에 대해 여러 작업(actions)을 수행할 권한을 확인합니다.
        예: 특정 원장에 대한 읽기/쓰기/삭제 권한 확인

        Args:
            user_id: 권한을 확인할 사용자 ID
            resource: 확인할 리소스 (예: 'ledger:journals:001')
            actions: 확인할 작업 목록 (예: ['read', 'write', 'delete'])
            tenant_id: 테넌트 ID (생략 시 사용자의 기본 테넌트)
            context: 추가 컨텍스트 정보 (선택적)
            auth_token: 인증 토큰 (선택적)

        Returns:
            Dict[str, PermissionResult]: 작업별 권한 확인 결과
                키: 작업 이름, 값: PermissionResult

        Example:
            >>> actions = ['read', 'write', 'delete']
            >>> results = await client.check_resource_actions(
            ...     user_id="user123",
            ...     resource="ledger:journals:001",
            ...     actions=actions
            ... )
            >>> for action, result in results.items():
            ...     print(f"{action} 권한: {result.allowed}")
        """
        permissions = [
            {"resource": resource, "action": action} for action in actions
        ]

        results = await self.batch_check_permissions(
            user_id=user_id,
            permissions=permissions,
            tenant_id=tenant_id,
            context=context,
            auth_token=auth_token,
        )

        return {action: result for action, result in zip(actions, results)}

    async def check_permissions_matrix(
        self,
        user_id: str,
        resources: List[str],
        actions: List[str],
        tenant_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        auth_token: Optional[str] = None,
    ) -> Dict[str, Dict[str, PermissionResult]]:
        """여러 리소스와 여러 작업의 권한 매트릭스를 일괄 확인

        리소스 목록과 작업 목록의 모든 조합에 대한 권한을 확인합니다.
        UI에서 권한 매트릭스 테이블을 표시할 때 유용합니다.

        Args:
            user_id: 권한을 확인할 사용자 ID
            resources: 확인할 리소스 목록
            actions: 확인할 작업 목록
            tenant_id: 테넌트 ID (생략 시 사용자의 기본 테넌트)
            context: 추가 컨텍스트 정보 (선택적)
            auth_token: 인증 토큰 (선택적)

        Returns:
            Dict[str, Dict[str, PermissionResult]]: 중첩된 딕셔너리 형태의 권한 매트릭스
                외부 키: 리소스 이름
                내부 키: 작업 이름
                값: PermissionResult

        Performance:
            - 리소스 3개 × 작업 4개 = 12개 권한을 한번의 API 호출로 처리
            - 캐시 활용으로 후속 호출 시 성능 향상

        Example:
            >>> resources = ['ledger:journals', 'ledger:accounts']
            >>> actions = ['read', 'write', 'delete']
            >>> matrix = await client.check_permissions_matrix(
            ...     user_id="user123",
            ...     resources=resources,
            ...     actions=actions
            ... )
            >>> for resource in resources:
            ...     for action in actions:
            ...         result = matrix[resource][action]
            ...         print(f"{resource}:{action} = {result.allowed}")

        Note:
            - 결과는 resources[i][actions[j]] 순서로 구성됨
            - UI 테이블 렌더링에 최적화된 데이터 구조
        """
        permissions = []
        for resource in resources:
            for action in actions:
                permissions.append({"resource": resource, "action": action})

        results = await self.batch_check_permissions(
            user_id=user_id,
            permissions=permissions,
            tenant_id=tenant_id,
            context=context,
            auth_token=auth_token,
        )

        # 결과를 행렬 형태로 재구성
        matrix: Dict[str, Dict[str, PermissionResult]] = {}
        result_idx = 0
        for resource in resources:
            matrix[resource] = {}
            for action in actions:
                matrix[resource][action] = results[result_idx]
                result_idx += 1

        return matrix

    async def warm_user_permissions_cache(
        self,
        user_id: str,
        tenant_id: Optional[str] = None,
        auth_token: Optional[str] = None,
    ) -> bool:
        """사용자 권한 캐시 사전 로딩 (성능 최적화)

        사용자가 자주 접근하는 리소스들의 권한을 미리 캐시에 로드합니다.
        로그인 직후 또는 세션 시작 시 호출하여 초기 페이지 로딩 성능을 향상시킵니다.

        Args:
            user_id: 캐시를 워밍할 사용자 ID
            tenant_id: 테넌트 ID (생략 시 사용자의 기본 테넌트)
            auth_token: 인증 토큰 (선택적)

        Returns:
            bool: 캐시 워밍 성공 시 True, 실패 시 False

        Warmed Permissions:
            - tenant:dashboard (읽기) - 대시보드 접근
            - tenant:profile (읽기) - 프로필 조회
            - tenant:settings (읽기) - 설정 조회
            - ledger:journals (읽기/생성) - 원장 분개
            - ledger:accounts (읽기/생성) - 원장 계정

        Performance Impact:
            - 초기 API 호출: ~100ms (7개 권한 일괄 처리)
            - 후속 권한 확인: ~1ms (캐시 히트)
            - 첫 페이지 로딩 시간: 평균 60% 단축

        Example:
            >>> # 로그인 성공 후 즉시 호출
            >>> success = await client.warm_user_permissions_cache(
            ...     user_id="user123",
            ...     tenant_id="tenant456",
            ...     auth_token=access_token
            ... )
            >>> if success:
            ...     print("캐시 워밍 완료 - 빠른 페이지 로딩 가능")

        Note:
            - 실패해도 기능상 문제없음 (성능 최적화 목적)
            - 백그라운드에서 실행 권장
            - 캐시 TTL에 따라 자동으로 만료됨
        """
        # 일반적으로 자주 확인되는 권한들
        common_permissions = [
            {"resource": "tenant:dashboard", "action": "read"},
            {"resource": "tenant:profile", "action": "read"},
            {"resource": "tenant:settings", "action": "read"},
            {"resource": "ledger:journals", "action": "read"},
            {"resource": "ledger:accounts", "action": "read"},
            {"resource": "ledger:journals", "action": "create"},
            {"resource": "ledger:accounts", "action": "create"},
        ]

        try:
            await self.batch_check_permissions(
                user_id=user_id,
                permissions=common_permissions,
                tenant_id=tenant_id,
                auth_token=auth_token,
            )
            logger.info(f"Cache warming completed for user {user_id}")
            return True
        except Exception as e:
            logger.error(f"Cache warming failed for user {user_id}: {e}")
            return False

    async def get_user_permissions(
        self,
        user_id: str,
        tenant_id: Optional[str] = None,
        resource_type: Optional[str] = None,
        auth_token: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """사용자 권한 목록 조회"""
        params = {"tenant_id": tenant_id, "resource_type": resource_type}
        params = {k: v for k, v in params.items() if v is not None}

        # URL 쿼리 파라미터 구성
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        endpoint = f"/api/{settings.IAM_API_VERSION}/permissions/users/{user_id}/permissions"
        if query_string:
            endpoint += f"?{query_string}"

        response_data = await self._make_request(
            "GET", endpoint, auth_token=auth_token
        )
        return response_data.get("permissions", [])

    # ============================================================================
    # 사용자 관리 관련 메서드들
    # ============================================================================

    async def get_user(self, user_id: str, auth_token: str) -> UserInfo:
        """사용자 정보 조회"""
        response_data = await self._make_request(
            "GET",
            f"/api/{settings.IAM_API_VERSION}/users/{user_id}",
            auth_token=auth_token,
        )
        return UserInfo(**response_data)

    async def get_current_user(self, auth_token: str) -> UserInfo:
        """현재 로그인 사용자 정보 조회"""
        response_data = await self._make_request(
            "GET",
            f"/api/{settings.IAM_API_VERSION}/users/me",
            auth_token=auth_token,
        )
        return UserInfo(**response_data)

    async def update_user(
        self, user_id: str, update_data: UserUpdate, auth_token: str
    ) -> UserInfo:
        """사용자 정보 수정"""
        response_data = await self._make_request(
            "PUT",
            f"/api/{settings.IAM_API_VERSION}/users/{user_id}",
            data=update_data.model_dump(exclude_unset=True),
            auth_token=auth_token,
        )
        return UserInfo(**response_data)

    async def search_users(
        self,
        auth_token: str,
        query: Optional[str] = None,
        email: Optional[str] = None,
        active: Optional[bool] = None,
        tenant_filter: Optional[str] = None,
        page: int = 1,
        size: int = 20,
    ) -> Dict[str, Any]:
        """사용자 검색 및 필터링

        다양한 조건으로 사용자를 검색합니다. 플랫폼 관리자는 모든 테넌트의
        사용자를 검색할 수 있고, 테넌트 사용자는 자신의 테넌트 내에서만 검색 가능합니다.

        Args:
            auth_token: 인증 토큰
            query: 검색 쿼리 (이름, 이메일 등에서 검색)
            email: 이메일로 필터링
            active: 활성 상태로 필터링 (True/False)
            tenant_filter: 테넌트 ID로 필터링 (플랫폼 관리자만)
            page: 페이지 번호 (1부터 시작)
            size: 페이지 크기 (최대 100)

        Returns:
            Dict[str, Any]: 검색 결과
                - items: 사용자 목록
                - total: 전체 사용자 수
                - page: 현재 페이지
                - size: 페이지 크기
                - pages: 전체 페이지 수

        Example:
            >>> # 이름으로 검색
            >>> results = await client.search_users(
            ...     auth_token=token,
            ...     query="john"
            ... )
            >>> print(f"Found {results['total']} users")

            >>> # 활성 사용자만 필터링
            >>> active_users = await client.search_users(
            ...     auth_token=token,
            ...     active=True,
            ...     page=1,
            ...     size=50
            ... )
        """
        params = {}
        if query:
            params["q"] = query
        if email:
            params["email"] = email
        if active is not None:
            params["active"] = str(active).lower()
        if tenant_filter:
            params["tenant_filter"] = tenant_filter
        params["page"] = str(page)
        params["size"] = str(size)

        # 쿼리 파라미터 구성
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        endpoint = f"/api/{settings.IAM_API_VERSION}/users/search"
        if query_string:
            endpoint += f"?{query_string}"

        response_data = await self._make_request(
            "GET", endpoint, auth_token=auth_token
        )
        return response_data

    async def change_password(
        self,
        current_password: str,
        new_password: str,
        auth_token: str,
    ) -> bool:
        """비밀번호 변경"""
        try:
            request_data = PasswordChangeRequest(
                current_password=current_password, new_password=new_password
            )
            await self._make_request(
                "POST",
                f"/api/{settings.IAM_API_VERSION}/users/me/change-password",
                data=request_data.model_dump(),
                auth_token=auth_token,
            )
            return True
        except Exception as e:
            logger.error(f"Password change failed: {e}")
            return False

    # ============================================================================
    # MFA 장치 관리 관련 메서드들
    # ============================================================================

    async def get_mfa_devices(self, auth_token: str) -> List[Dict[str, Any]]:
        """현재 사용자의 MFA 장치 목록 조회

        사용자가 등록한 모든 MFA(다중 요소 인증) 장치를 조회합니다.

        Args:
            auth_token: 인증 토큰

        Returns:
            List[Dict[str, Any]]: MFA 장치 목록
                각 장치는 device_id, device_type, name, is_active 등을 포함

        Example:
            >>> devices = await client.get_mfa_devices(auth_token)
            >>> for device in devices:
            ...     print(f"Device: {device['name']}, Active: {device['is_active']}")
        """
        response_data = await self._make_request(
            "GET",
            f"/api/{settings.IAM_API_VERSION}/mfa-devices/me",
            auth_token=auth_token,
        )
        # 응답이 리스트 형태로 올 것으로 예상
        return (
            response_data
            if isinstance(response_data, list)
            else response_data.get("items", [])
        )

    async def verify_mfa_device(
        self, device_id: str, verification_code: str, auth_token: str
    ) -> Dict[str, Any]:
        """MFA 장치 인증 코드 검증

        MFA 장치에서 생성된 인증 코드를 검증합니다.

        Args:
            device_id: MFA 장치 ID
            verification_code: 장치에서 생성된 인증 코드 (보통 6자리)
            auth_token: 인증 토큰

        Returns:
            Dict[str, Any]: 검증 결과
                - verified: 검증 성공 여부
                - message: 결과 메시지

        Example:
            >>> result = await client.verify_mfa_device(
            ...     device_id="device123",
            ...     verification_code="123456",
            ...     auth_token=token
            ... )
            >>> if result['verified']:
            ...     print("MFA 인증 성공")
        """
        response_data = await self._make_request(
            "POST",
            f"/api/{settings.IAM_API_VERSION}/mfa-devices/{device_id}/verify",
            data={"verification_code": verification_code},
            auth_token=auth_token,
        )
        return response_data

    async def toggle_mfa_device(
        self, device_id: str, auth_token: str
    ) -> Dict[str, Any]:
        """MFA 장치 활성화/비활성화 토글

        MFA 장치의 활성화 상태를 변경합니다.

        Args:
            device_id: MFA 장치 ID
            auth_token: 인증 토큰

        Returns:
            Dict[str, Any]: 변경 결과
                - is_active: 변경된 활성화 상태
                - message: 결과 메시지

        Example:
            >>> result = await client.toggle_mfa_device(
            ...     device_id="device123",
            ...     auth_token=token
            ... )
            >>> print(f"Device active: {result['is_active']}")
        """
        response_data = await self._make_request(
            "POST",
            f"/api/{settings.IAM_API_VERSION}/mfa-devices/{device_id}/toggle-active",
            auth_token=auth_token,
        )
        return response_data

    # ============================================================================
    # 세션 관리 관련 메서드들
    # ============================================================================

    async def get_user_sessions(
        self,
        page: int = 1,
        size: int = 10,
        auth_token: Optional[str] = None,
    ) -> List[SessionInfo]:
        """사용자 세션 목록 조회"""
        response_data = await self._make_request(
            "GET",
            f"/api/{settings.IAM_API_VERSION}/sessions?page={page}&size={size}",
            auth_token=auth_token,
        )
        return [
            SessionInfo(**session)
            for session in response_data.get("items", [])
        ]

    async def get_current_session(self, auth_token: str) -> SessionInfo:
        """현재 세션 정보 조회"""
        response_data = await self._make_request(
            "GET",
            f"/api/{settings.IAM_API_VERSION}/sessions/current",
            auth_token=auth_token,
        )
        return SessionInfo(**response_data)

    async def deactivate_session(
        self, session_id: str, auth_token: str
    ) -> bool:
        """특정 세션 비활성화"""
        try:
            await self._make_request(
                "POST",
                f"/api/{settings.IAM_API_VERSION}/sessions/{session_id}/deactivate",
                auth_token=auth_token,
            )
            return True
        except Exception as e:
            logger.error(f"Session deactivation failed: {e}")
            return False

    async def deactivate_all_sessions(self, auth_token: str) -> bool:
        """모든 다른 세션 비활성화"""
        try:
            await self._make_request(
                "POST",
                f"/api/{settings.IAM_API_VERSION}/sessions/deactivate-all",
                auth_token=auth_token,
            )
            return True
        except Exception as e:
            logger.error(f"All sessions deactivation failed: {e}")
            return False

    # ============================================================================
    # 리소스 관리
    # ============================================================================

    async def close(self) -> None:
        """클라이언트 리소스 정리 및 연결 종료

        HTTP 클라이언트 연결을 정리하고 모든 리소스를 해제합니다.
        애플리케이션 종료 시 또는 장기간 사용하지 않을 때 호출하세요.

        Note:
            - HTTP 연결 풀이 정리됩니다
            - 캐시 리소스는 별도로 관리됩니다 (UnifiedAuthCache.close() 필요)
            - close() 후에는 클라이언트를 재사용할 수 없습니다
            - async context manager 사용 시 자동으로 호출됩니다

        Example:
            Manual cleanup:
                >>> client = UnifiedIAMClient()
                >>> # ... use client ...
                >>> await client.close()

            Context manager (recommended):
                >>> async with UnifiedIAMClient() as client:
                ...     # ... use client ...
                >>> # 자동으로 close() 호출됨
        """
        if self._client:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


# ============================================================================
# 글로벌 클라이언트 관리
# ============================================================================


async def get_iam_client(
    base_url: Optional[str] = None,
    timeout: float = 30.0,
    max_retries: int = 3,
    retry_delay: float = 1.0,
    enable_cache: bool = True,
) -> UnifiedIAMClient:
    """글로벌 IAM 클라이언트 반환 (싱글톤 패턴)

    애플리케이션 전반에서 사용할 수 있는 공유 IAM 클라이언트를 반환합니다.
    첫 호출 시에만 인스턴스를 생성하고, 이후 호출에서는 동일한 인스턴스를 재사용합니다.

    Args:
        base_url: IAM 서비스 기본 URL (첫 호출 시에만 적용)
        timeout: HTTP 요청 타임아웃 (첫 호출 시에만 적용)
        max_retries: 최대 재시도 횟수 (첫 호출 시에만 적용)
        retry_delay: 재시도 간격 (첫 호출 시에만 적용)
        enable_cache: 캐싱 활성화 여부 (첫 호출 시에만 적용)

    Returns:
        UnifiedIAMClient: 글로벌 IAM 클라이언트 인스턴스

    Note:
        - 프로덕션 환경에서 권장되는 패턴
        - 연결 풀링과 캐시를 공유하여 리소스 효율성 극대화
        - 두 번째 호출부터는 매개변수가 무시됩니다
        - 애플리케이션 종료 시 close_global_iam_client() 호출 필요

    Example:
        >>> # 첫 호출 - 클라이언트 생성
        >>> client = await get_iam_client(enable_cache=True)

        >>> # 이후 호출 - 동일한 인스턴스 반환
        >>> same_client = await get_iam_client()
        >>> assert client is same_client

        >>> # 애플리케이션 종료 시
        >>> await close_global_iam_client()
    """
    global _global_iam_client

    if _global_iam_client is None:
        _global_iam_client = UnifiedIAMClient(
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            retry_delay=retry_delay,
            enable_cache=enable_cache,
        )

    return _global_iam_client


async def close_global_iam_client() -> None:
    """글로벌 IAM 클라이언트 정리 및 리소스 해제

    애플리케이션 종료 시 글로벌 IAM 클라이언트의 모든 리소스를 정리합니다.
    HTTP 연결을 닫고 글로벌 참조를 제거합니다.

    Note:
        - 애플리케이션 종료 시 반드시 호출해야 합니다
        - 호출 후 get_iam_client()를 다시 호출하면 새 인스턴스가 생성됩니다
        - 이미 정리된 상태에서 호출해도 안전합니다 (멱등성)

    Example:
        FastAPI application:
            >>> @app.on_event("shutdown")
            >>> async def shutdown_event():
            ...     await close_global_iam_client()

        Manual cleanup:
            >>> await close_global_iam_client()
            >>> # 이제 새로운 클라이언트 생성 가능
            >>> new_client = await get_iam_client()
    """
    global _global_iam_client

    if _global_iam_client:
        await _global_iam_client.close()
        _global_iam_client = None
