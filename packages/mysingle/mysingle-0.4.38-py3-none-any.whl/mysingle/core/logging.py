"""Centralized logging configuration for all services."""

import json
import logging
import sys
import time
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration."""

    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    service_name: Optional[str] = None


class SecurityAuditLog(BaseModel):
    """보안 감사 로그 모델"""

    timestamp: Optional[str] = None
    event_type: str  # AUTH_SUCCESS, AUTH_FAILURE, PERMISSION_DENIED, etc.
    user_id: Optional[str] = None
    tenant_id: Optional[str] = None
    resource: Optional[str] = None
    action: Optional[str] = None
    source_ip: Optional[str] = None
    user_agent: Optional[str] = None
    success: bool = True
    reason: Optional[str] = None
    request_id: Optional[str] = None
    service: Optional[str] = None

    def __init__(self, **data):
        if "timestamp" not in data:
            data["timestamp"] = datetime.utcnow().isoformat()
        super().__init__(**data)


class PerformanceLog(BaseModel):
    """성능 모니터링 로그 모델"""

    timestamp: Optional[str] = None
    operation: str
    duration_ms: float
    user_id: Optional[str] = None
    tenant_id: Optional[str] = None
    resource: Optional[str] = None
    cache_hit: Optional[bool] = None
    request_id: Optional[str] = None
    service: Optional[str] = None

    def __init__(self, **data):
        if "timestamp" not in data:
            data["timestamp"] = datetime.utcnow().isoformat()
        super().__init__(**data)


def setup_logging(
    service_name: Optional[str] = None,
    level: str = "INFO",
    log_format: Optional[str] = None,
) -> None:
    """Configure centralized logging for services.

    Args:
        service_name: Name of the service for log identification
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_format: Custom log format string
    """
    # Default format with service name
    if log_format is None:
        if service_name:
            log_format = f"%(asctime)s - {service_name} - %(name)s - %(levelname)s - %(message)s"
        else:
            log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=log_format,
        stream=sys.stdout,
        force=True,  # Override any existing configuration
    )

    # Set specific loggers to appropriate levels
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("fastapi").setLevel(logging.INFO)
    logging.getLogger("beanie").setLevel(logging.WARNING)
    logging.getLogger("motor").setLevel(logging.WARNING)
    logging.getLogger("pymongo").setLevel(logging.WARNING)

    if service_name:
        logger = logging.getLogger(service_name)
        logger.info("Logging configured for service: %s", service_name)


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Configured logger instance
    """
    return logging.getLogger(name)


# 전역 보안 감사 및 성능 로거
_security_logger = None
_performance_logger = None


def get_security_logger() -> logging.Logger:
    """보안 감사 로거 반환"""
    global _security_logger
    if _security_logger is None:
        _security_logger = logging.getLogger("mysingle.security.audit")
        _security_logger.setLevel(logging.INFO)
    return _security_logger


def get_performance_logger() -> logging.Logger:
    """성능 모니터링 로거 반환"""
    global _performance_logger
    if _performance_logger is None:
        _performance_logger = logging.getLogger("mysingle.performance")
        _performance_logger.setLevel(logging.INFO)
    return _performance_logger


def log_security_event(
    event_type: str,
    success: bool = True,
    user_id: Optional[str] = None,
    tenant_id: Optional[str] = None,
    resource: Optional[str] = None,
    action: Optional[str] = None,
    reason: Optional[str] = None,
    source_ip: Optional[str] = None,
    user_agent: Optional[str] = None,
    request_id: Optional[str] = None,
    service: Optional[str] = None,
    **kwargs,
) -> None:
    """보안 감사 이벤트 로깅"""
    audit_log = SecurityAuditLog(
        event_type=event_type,
        success=success,
        user_id=user_id,
        tenant_id=tenant_id,
        resource=resource,
        action=action,
        reason=reason,
        source_ip=source_ip,
        user_agent=user_agent,
        request_id=request_id,
        service=service,
        **kwargs,
    )

    logger = get_security_logger()
    log_data = audit_log.model_dump(exclude_none=True)
    logger.info(f"SECURITY_AUDIT: {json.dumps(log_data)}")


def log_performance_metric(
    operation: str,
    duration_ms: float,
    user_id: Optional[str] = None,
    tenant_id: Optional[str] = None,
    resource: Optional[str] = None,
    cache_hit: Optional[bool] = None,
    request_id: Optional[str] = None,
    service: Optional[str] = None,
    **kwargs,
) -> None:
    """성능 메트릭 로깅"""
    perf_log = PerformanceLog(
        operation=operation,
        duration_ms=duration_ms,
        user_id=user_id,
        tenant_id=tenant_id,
        resource=resource,
        cache_hit=cache_hit,
        request_id=request_id,
        service=service,
        **kwargs,
    )

    logger = get_performance_logger()
    log_data = perf_log.model_dump(exclude_none=True)
    logger.info(f"PERFORMANCE_METRIC: {json.dumps(log_data)}")


class PerformanceTimer:
    """성능 측정을 위한 컨텍스트 매니저"""

    def __init__(
        self,
        operation: str,
        user_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
        resource: Optional[str] = None,
        service: Optional[str] = None,
        **kwargs,
    ):
        self.operation = operation
        self.user_id = user_id
        self.tenant_id = tenant_id
        self.resource = resource
        self.service = service
        self.kwargs = kwargs
        self.start_time: Optional[float] = None
        self.cache_hit: Optional[bool] = None

    def __enter__(self):
        self.start_time = time.time() * 1000  # milliseconds
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.start_time:
            duration_ms = (time.time() * 1000) - self.start_time
            log_performance_metric(
                operation=self.operation,
                duration_ms=duration_ms,
                user_id=self.user_id,
                tenant_id=self.tenant_id,
                resource=self.resource,
                cache_hit=self.cache_hit,
                service=self.service,
                **self.kwargs,
            )

    def set_cache_hit(self, cache_hit: bool):
        """캐시 히트 여부 설정"""
        self.cache_hit = cache_hit
