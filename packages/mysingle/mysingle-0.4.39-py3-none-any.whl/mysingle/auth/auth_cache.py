"""통합 권한 캐시 전략 - 권한 확인 결과 캐싱"""

import hashlib
import json
import time
from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, Dict, List, Optional

try:
    import redis.asyncio as redis

    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False

from mysingle.core.config import settings
from mysingle.core.logging import get_logger

if TYPE_CHECKING:
    from mysingle.auth.iam_schemas import PermissionResult

logger = get_logger(__name__)


@dataclass
class CacheEntry:
    """캐시 엔트리"""

    value: Any
    expires_at: float
    created_at: float

    def is_expired(self) -> bool:
        """만료 여부 확인"""
        return time.time() > self.expires_at


class LocalCache:
    """로컬 메모리 캐시 (1분 TTL)"""

    def __init__(self, max_size: int = 1000, default_ttl: int = 60):
        self._cache: Dict[str, CacheEntry] = {}
        self._max_size = max_size
        self._default_ttl = default_ttl
        self._access_order: Dict[str, float] = {}  # LRU용

    def get(self, key: str) -> Optional[Any]:
        """캐시에서 값 조회"""
        if key in self._cache:
            entry = self._cache[key]
            if entry.is_expired():
                self._delete(key)
                return None

            # LRU 업데이트
            self._access_order[key] = time.time()
            return entry.value
        return None

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """캐시에 값 저장"""
        if ttl is None:
            ttl = self._default_ttl

        # 캐시 크기 제한
        if len(self._cache) >= self._max_size:
            self._evict_lru()

        now = time.time()
        entry = CacheEntry(value=value, expires_at=now + ttl, created_at=now)

        self._cache[key] = entry
        self._access_order[key] = now

    def has(self, key: str) -> bool:
        """키 존재 여부 확인"""
        if key in self._cache:
            entry = self._cache[key]
            if entry.is_expired():
                self._delete(key)
                return False
            return True
        return False

    def delete(self, key: str) -> None:
        """캐시에서 값 삭제"""
        self._delete(key)

    def clear(self) -> None:
        """캐시 전체 비우기"""
        self._cache.clear()
        self._access_order.clear()

    def _delete(self, key: str) -> None:
        """내부 삭제 메서드"""
        self._cache.pop(key, None)
        self._access_order.pop(key, None)

    def _evict_lru(self) -> None:
        """LRU 방식으로 캐시 엔트리 제거"""
        if not self._access_order:
            return

        # 가장 오래된 키 찾기
        oldest_key = min(
            self._access_order.keys(), key=lambda k: self._access_order[k]
        )
        self._delete(oldest_key)


class RedisCache:
    """Redis 캐시 (5분 TTL)"""

    def __init__(
        self, redis_url: str = "redis://localhost:6379", default_ttl: int = 300
    ):
        self._redis_url = redis_url
        self._default_ttl = default_ttl
        self._redis: Optional[redis.Redis] = None
        self._connected = False

    async def connect(self) -> bool:
        """Redis 연결"""
        if not HAS_REDIS:
            logger.warning("Redis not available, using local cache only")
            return False

        try:
            self._redis = redis.from_url(self._redis_url)
            await self._redis.ping()
            self._connected = True
            logger.info("Redis cache connected successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            self._connected = False
            return False

    async def get(self, key: str) -> Optional[Any]:
        """캐시에서 값 조회"""
        if not self._connected or not self._redis:
            return None

        try:
            value = await self._redis.get(key)
            if value:
                return json.loads(value.decode("utf-8"))
            return None
        except Exception as e:
            logger.error(f"Redis get error for key {key}: {e}")
            return None

    async def set(
        self, key: str, value: Any, ttl: Optional[int] = None
    ) -> bool:
        """캐시에 값 저장"""
        if not self._connected or not self._redis:
            return False

        if ttl is None:
            ttl = self._default_ttl

        try:
            serialized_value = json.dumps(value)
            await self._redis.setex(key, ttl, serialized_value)
            return True
        except Exception as e:
            logger.error(f"Redis set error for key {key}: {e}")
            return False

    async def has(self, key: str) -> bool:
        """키 존재 여부 확인"""
        if not self._connected or not self._redis:
            return False

        try:
            result = await self._redis.exists(key)
            return bool(result == 1)
        except Exception as e:
            logger.error(f"Redis exists check error for key {key}: {e}")
            return False

    async def delete(self, key: str) -> bool:
        """캐시에서 값 삭제"""
        if not self._connected or not self._redis:
            return False

        try:
            result = await self._redis.delete(key)
            return bool(result == 1)
        except Exception as e:
            logger.error(f"Redis delete error for key {key}: {e}")
            return False

    async def delete_pattern(self, pattern: str) -> int:
        """패턴에 매칭되는 모든 키 삭제"""
        if not self._connected or not self._redis:
            return 0

        try:
            # SCAN을 사용하여 패턴 매칭 키 찾기
            deleted_count = 0
            cursor = 0

            while True:
                cursor, keys = await self._redis.scan(
                    cursor=cursor, match=pattern, count=100
                )
                if keys:
                    deleted_count += await self._redis.delete(*keys)

                if cursor == 0:
                    break

            logger.debug(
                f"Deleted {deleted_count} keys matching pattern: {pattern}"
            )
            return deleted_count

        except Exception as e:
            logger.error(
                f"Redis delete pattern error for pattern {pattern}: {e}"
            )
            return 0

    async def close(self) -> None:
        """Redis 연결 종료"""
        if self._redis:
            await self._redis.close()
            self._connected = False


class CacheLevel(Enum):
    """캐시 레벨"""

    LOCAL_ONLY = "local"  # 로컬 메모리만
    REDIS_ONLY = "redis"  # Redis만
    DUAL_LAYER = "dual"  # 로컬 + Redis 다층


@dataclass
class AuthCacheConfig:
    """권한 캐시 설정"""

    cache_level: CacheLevel = CacheLevel.DUAL_LAYER

    # 기본 TTL 설정
    local_ttl: int = 60  # 로컬 캐시 TTL (1분)
    redis_ttl: int = 300  # Redis 캐시 TTL (5분)

    # 차별화된 TTL 전략
    platform_permission_ttl: int = 120  # 플랫폼 권한 TTL (2분) - 더 오래 캐싱
    tenant_permission_ttl: int = 90  # 테넌트 권한 TTL (1.5분)
    role_cache_ttl: int = 180  # 역할 정보 TTL (3분) - 자주 변경되지 않음

    max_local_size: int = 1000  # 로컬 캐시 최대 크기

    # 거부 결과 전략
    enable_negative_cache: bool = True  # 거부 결과 캐싱 여부
    negative_cache_ttl: int = 30  # 거부 결과 캐시 TTL

    # 성능 최적화 설정
    batch_invalidation_size: int = 100  # 배치 무효화 크기
    enable_cache_warming: bool = True  # 캐시 워밍 활성화
    cache_hit_threshold: float = 0.8  # 캐시 히트율 임계값


class UnifiedAuthCache:
    """통합 권한 캐시

    권한 확인 결과를 효율적으로 캐싱하여 성능을 향상시킵니다.
    로컬 메모리와 Redis를 조합한 다층 캐싱을 지원합니다.
    """

    def __init__(self, config: Optional[AuthCacheConfig] = None):
        self.config = config or AuthCacheConfig()

        # 로컬 캐시 초기화
        self.local_cache = LocalCache(
            max_size=self.config.max_local_size,
            default_ttl=self.config.local_ttl,
        )

        # Redis 캐시 초기화
        self.redis_cache = None
        if self.config.cache_level in [
            CacheLevel.REDIS_ONLY,
            CacheLevel.DUAL_LAYER,
        ]:
            redis_url = getattr(
                settings, "redis_url", "redis://localhost:6379"
            )
            self.redis_cache = RedisCache(
                redis_url=redis_url,
                default_ttl=self.config.redis_ttl,
            )

    async def connect(self) -> bool:
        """캐시 연결 초기화"""
        if self.redis_cache:
            return await self.redis_cache.connect()
        return True

    def _calculate_ttl(
        self, resource: str, user_context: Optional[Dict[str, Any]] = None
    ) -> tuple[int, int]:
        """리소스와 컨텍스트에 따른 최적화된 TTL 계산

        Returns:
            tuple[int, int]: (local_ttl, redis_ttl)
        """
        # 플랫폼 권한은 더 오래 캐싱
        if resource.startswith("platform:") or (
            user_context and user_context.get("is_platform_user")
        ):
            local_ttl = min(self.config.platform_permission_ttl, 120)
            redis_ttl = min(self.config.platform_permission_ttl * 2, 300)

        # 역할 정보는 중간 수준으로 캐싱
        elif "role" in resource.lower() or "permission" in resource.lower():
            local_ttl = self.config.role_cache_ttl
            redis_ttl = min(
                self.config.role_cache_ttl * 2, self.config.redis_ttl
            )

        # 테넌트별 권한은 기본 TTL
        else:
            local_ttl = self.config.tenant_permission_ttl
            redis_ttl = min(
                self.config.tenant_permission_ttl * 2, self.config.redis_ttl
            )

        return local_ttl, redis_ttl

    def _build_cache_key(
        self,
        user_id: str,
        resource: str,
        action: str,
        tenant_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        strategy: str = "default",
    ) -> str:
        """캐시 키 생성"""
        # 기본 키 요소
        key_parts = [
            f"auth:{strategy}",
            f"user:{user_id}",
            f"resource:{resource}",
            f"action:{action}",
        ]

        # 테넌트 ID 추가
        if tenant_id:
            key_parts.append(f"tenant:{tenant_id}")

        # 컨텍스트 해시 추가 (있는 경우)
        if context:
            context_str = json.dumps(context, sort_keys=True)
            # SHA256 사용 (보안적으로 더 안전하며 bandit 경고 없음)
            context_hash = hashlib.sha256(context_str.encode()).hexdigest()[:8]
            key_parts.append(f"ctx:{context_hash}")

        return ":".join(key_parts)

    async def get_permission_result(
        self,
        user_id: str,
        resource: str,
        action: str,
        tenant_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        strategy: str = "default",
    ) -> Optional["PermissionResult"]:
        """권한 확인 결과 조회"""
        from mysingle.auth.iam_schemas import PermissionResult

        cache_key = self._build_cache_key(
            user_id, resource, action, tenant_id, context, strategy
        )

        # 1. 로컬 캐시에서 조회
        if self.config.cache_level in [
            CacheLevel.LOCAL_ONLY,
            CacheLevel.DUAL_LAYER,
        ]:
            local_result = self.local_cache.get(cache_key)
            if local_result is not None:
                try:
                    result = PermissionResult(**local_result)
                    result.cached = True
                    logger.debug(f"Cache hit (local): {cache_key}")
                    return result
                except (TypeError, ValueError) as e:
                    logger.warning(f"Invalid cached data in local cache: {e}")
                    self.local_cache.delete(cache_key)

        # 2. Redis 캐시에서 조회
        if self.redis_cache and self.config.cache_level in [
            CacheLevel.REDIS_ONLY,
            CacheLevel.DUAL_LAYER,
        ]:
            redis_result = await self.redis_cache.get(cache_key)
            if redis_result is not None:
                try:
                    result = PermissionResult(**redis_result)
                    result.cached = True

                    # 로컬 캐시에도 저장 (다층 캐싱)
                    if self.config.cache_level == CacheLevel.DUAL_LAYER:
                        self.local_cache.set(cache_key, result.model_dump())

                    logger.debug(f"Cache hit (redis): {cache_key}")
                    return result
                except (TypeError, ValueError) as e:
                    logger.warning(f"Invalid cached data in Redis: {e}")
                    await self.redis_cache.delete(cache_key)

        return None

    async def set_permission_result(
        self,
        user_id: str,
        resource: str,
        action: str,
        result: "PermissionResult",
        tenant_id: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        strategy: str = "default",
    ) -> bool:
        """권한 확인 결과 저장"""
        # 거부 결과 캐싱 설정 확인
        if not result.allowed and not self.config.enable_negative_cache:
            return True

        cache_key = self._build_cache_key(
            user_id, resource, action, tenant_id, context, strategy
        )

        # 지능적 TTL 계산
        if not result.allowed and self.config.enable_negative_cache:
            # 거부 결과는 더 짧은 TTL
            local_ttl = self.config.negative_cache_ttl
            redis_ttl = self.config.negative_cache_ttl
        else:
            # 리소스와 컨텍스트에 따른 최적화된 TTL
            local_ttl, redis_ttl = self._calculate_ttl(resource, context)

        result_dict = result.model_dump()
        result_dict["cached"] = True

        success = True

        # 1. 로컬 캐시에 저장
        if self.config.cache_level in [
            CacheLevel.LOCAL_ONLY,
            CacheLevel.DUAL_LAYER,
        ]:
            try:
                self.local_cache.set(cache_key, result_dict, ttl=local_ttl)
                logger.debug(f"Cached to local: {cache_key}")
            except Exception as e:
                logger.error(f"Failed to cache to local: {e}")
                success = False

        # 2. Redis 캐시에 저장
        if self.redis_cache and self.config.cache_level in [
            CacheLevel.REDIS_ONLY,
            CacheLevel.DUAL_LAYER,
        ]:
            try:
                await self.redis_cache.set(
                    cache_key, result_dict, ttl=redis_ttl
                )
                logger.debug(f"Cached to redis: {cache_key}")
            except Exception as e:
                logger.error(f"Failed to cache to Redis: {e}")
                success = False

        return success

    async def invalidate_user_cache(self, user_id: str) -> bool:
        """사용자별 캐시 무효화"""
        pattern = f"auth:*:user:{user_id}:*"

        # 로컬 캐시 무효화
        if self.config.cache_level in [
            CacheLevel.LOCAL_ONLY,
            CacheLevel.DUAL_LAYER,
        ]:
            keys_to_delete = [
                key
                for key in self.local_cache._cache.keys()
                if f"user:{user_id}" in key
            ]
            for key in keys_to_delete:
                self.local_cache.delete(key)

        # Redis 캐시 무효화
        if self.redis_cache and self.config.cache_level in [
            CacheLevel.REDIS_ONLY,
            CacheLevel.DUAL_LAYER,
        ]:
            try:
                # Redis 패턴 삭제 기능 사용
                deleted_count = await self.redis_cache.delete_pattern(pattern)
                logger.info(
                    f"Deleted {deleted_count} Redis keys for user {user_id}"
                )
            except Exception as e:
                logger.error(
                    f"Failed to invalidate Redis cache for user {user_id}: {e}"
                )
                return False

        logger.info(f"Invalidated cache for user: {user_id}")
        return True

    async def clear_all_cache(self) -> bool:
        """모든 캐시 삭제"""
        success = True

        # 로컬 캐시 삭제
        if self.config.cache_level in [
            CacheLevel.LOCAL_ONLY,
            CacheLevel.DUAL_LAYER,
        ]:
            try:
                self.local_cache.clear()
            except Exception as e:
                logger.error(f"Failed to clear local cache: {e}")
                success = False

        # Redis 캐시 삭제
        if self.redis_cache and self.config.cache_level in [
            CacheLevel.REDIS_ONLY,
            CacheLevel.DUAL_LAYER,
        ]:
            try:
                # 모든 auth:* 패턴 키 삭제
                deleted_count = await self.redis_cache.delete_pattern("auth:*")
                logger.info(f"Deleted {deleted_count} Redis auth cache keys")
            except Exception as e:
                logger.error(f"Failed to clear Redis cache: {e}")
                success = False

        logger.info("Cleared all auth cache")
        return success

    async def get_cache_stats(self) -> Dict[str, Any]:
        """캐시 통계 조회 (개선된 버전)"""
        stats = {
            "config": {
                "cache_level": self.config.cache_level.value,
                "local_ttl": self.config.local_ttl,
                "redis_ttl": self.config.redis_ttl,
                "platform_permission_ttl": self.config.platform_permission_ttl,
                "tenant_permission_ttl": self.config.tenant_permission_ttl,
                "role_cache_ttl": self.config.role_cache_ttl,
                "max_local_size": self.config.max_local_size,
                "enable_negative_cache": self.config.enable_negative_cache,
                "negative_cache_ttl": self.config.negative_cache_ttl,
                "batch_invalidation_size": self.config.batch_invalidation_size,
                "enable_cache_warming": self.config.enable_cache_warming,
                "cache_hit_threshold": self.config.cache_hit_threshold,
            },
            "local_cache": {
                "size": len(self.local_cache._cache),
                "max_size": self.local_cache._max_size,
                "usage_ratio": len(self.local_cache._cache)
                / self.local_cache._max_size,
            },
            "timestamp": time.time(),
        }

        if self.redis_cache:
            try:
                # Redis 연결 상태 확인
                if self.redis_cache._connected:
                    stats["redis_cache"] = {
                        "connected": True,
                        "default_ttl": getattr(
                            self.redis_cache,
                            "_default_ttl",
                            self.config.redis_ttl,
                        ),
                    }
                else:
                    stats["redis_cache"] = {"connected": False}
            except Exception:
                stats["redis_cache"] = {"connected": False, "error": True}

        return stats

    async def batch_invalidate_users(
        self, user_ids: List[str]
    ) -> Dict[str, bool]:
        """배치로 여러 사용자 캐시 무효화"""
        results = {}

        # 배치 크기로 나누어 처리
        for i in range(0, len(user_ids), self.config.batch_invalidation_size):
            batch = user_ids[i : i + self.config.batch_invalidation_size]

            for user_id in batch:
                try:
                    success = await self.invalidate_user_cache(user_id)
                    results[user_id] = success
                except Exception as e:
                    logger.error(
                        f"Failed to invalidate cache for user {user_id}: {e}"
                    )
                    results[user_id] = False

        success_count = sum(1 for success in results.values() if success)
        logger.info(
            f"Batch invalidated {success_count}/{len(user_ids)} user caches"
        )

        return results

    async def warm_cache_for_user(
        self, user_id: str, tenant_id: Optional[str] = None
    ) -> bool:
        """사용자 캐시 워밍 - 자주 사용되는 권한을 미리 캐싱"""
        if not self.config.enable_cache_warming:
            return False

        try:
            # IAM 클라이언트가 있다면 캐시 워밍 수행
            # 여기서는 로깅만 수행 (실제 구현은 UnifiedIAMClient에서)
            logger.info(
                f"Cache warming initiated for user {user_id}, tenant: {tenant_id}"
            )
            return True

        except Exception as e:
            logger.error(f"Cache warming failed for user {user_id}: {e}")
            return False

    def _should_cache_result(
        self, result: "PermissionResult", resource: str
    ) -> bool:
        """결과가 캐싱할 가치가 있는지 판단"""
        # 거부 결과이고 negative 캐싱이 비활성화된 경우
        if not result.allowed and not self.config.enable_negative_cache:
            return False

        # 일회성 권한이나 임시 권한은 캐싱하지 않음
        if "temp:" in resource or "one-time:" in resource:
            return False

        return True

    async def optimize_cache_performance(self) -> Dict[str, Any]:
        """캐시 성능 최적화 실행"""
        optimization_results = {
            "local_cache_optimized": False,
            "expired_keys_removed": 0,
            "optimization_time": 0.0,
        }

        start_time = time.time()

        try:
            # 로컬 캐시에서 만료된 엔트리 정리
            expired_count = 0
            current_time = time.time()

            expired_keys = []
            for key, entry in self.local_cache._cache.items():
                if (
                    hasattr(entry, "expires_at")
                    and entry.expires_at < current_time
                ):
                    expired_keys.append(key)

            for key in expired_keys:
                del self.local_cache._cache[key]
                expired_count += 1

            optimization_results["expired_keys_removed"] = expired_count
            optimization_results["local_cache_optimized"] = True

            logger.info(
                f"Cache optimization completed: removed {expired_count} expired entries"
            )

        except Exception as e:
            logger.error(f"Cache optimization failed: {e}")

        optimization_results["optimization_time"] = time.time() - start_time
        return optimization_results


# 전역 캐시 인스턴스 (싱글톤)
_unified_cache: Optional[UnifiedAuthCache] = None


async def get_unified_auth_cache(
    config: Optional[AuthCacheConfig] = None,
) -> UnifiedAuthCache:
    """통합 권한 캐시 싱글톤 인스턴스 반환"""
    global _unified_cache
    if _unified_cache is None:
        _unified_cache = UnifiedAuthCache(config)
        await _unified_cache.connect()
    return _unified_cache
