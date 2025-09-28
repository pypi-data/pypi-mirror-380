"""Database utilities for MongoDB and Redis."""

import os
from typing import List, Type

from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from mysingle.core.config import settings


async def init_mongo(
    models: List[Type[Document]], service_name: str
) -> AsyncIOMotorClient:
    """Initialize MongoDB with given models and return the client."""
    # MongoDB connection configuration
    admin_user = settings.INFRA_SERVICE_SUPERUSER_ID
    admin_password = settings.INFRA_SERVICE_SUPERUSER_PASSWORD

    if settings.ENVIRONMENT in ["production", "staging"]:
        mongodb_url = (
            f"mongodb+srv://{admin_user}:{admin_password}"
            f"@{settings.MONGODB_SERVER}/{service_name}?"
            f"retryWrites=true&w=majority&appName=mysingle"
        )
    else:
        mongodb_url = (
            f"mongodb://{admin_user}:{admin_password}"
            f"@{settings.MONGODB_SERVER}/{service_name}?"
            f"authSource=admin"
        )

    # Create Motor client
    client: AsyncIOMotorClient = AsyncIOMotorClient(
        mongodb_url, uuidRepresentation="standard"
    )

    # Initialize Beanie with the models
    # Motor의 database 타입이 Beanie와 호환되지 않지만 실제로는 작동합니다
    await init_beanie(
        database=client.get_default_database(),  # type: ignore[arg-type]
        document_models=models,
    )

    return client


def get_mongodb_url(service_name: str) -> str:
    """Get MongoDB connection URL."""
    admin_user = settings.INFRA_SERVICE_SUPERUSER_ID
    admin_password = settings.INFRA_SERVICE_SUPERUSER_PASSWORD
    service_name = service_name or os.getenv("SERVICE_NAME", "mysingle")

    if settings.ENVIRONMENT in ["production", "staging"]:
        mongodb_url = (
            f"mongodb+srv://{admin_user}:{admin_password}"
            f"@{settings.MONGODB_SERVER}/{service_name}?"
            f"retryWrites=true&w=majority&appName=mysingle"
        )
    else:
        mongodb_url = (
            f"mongodb://{admin_user}:{admin_password}"
            f"@{settings.MONGODB_SERVER}/{service_name}?"
            f"authSource=admin"
        )
    return mongodb_url


def get_redis_url() -> str:
    """Get Redis connection URL."""
    return settings.redis_url


def get_database_name(service_name: str) -> str:
    """Get database name."""
    return service_name
