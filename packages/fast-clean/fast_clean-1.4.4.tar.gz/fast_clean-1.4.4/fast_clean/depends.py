"""
Модуль, содержащий зависимости.
"""

import json
from collections.abc import AsyncIterator, Sequence
from typing import Annotated

from dishka import Provider, Scope, provide
from fastapi import Depends, Request
from faststream.kafka import KafkaBroker
from flatten_dict import unflatten
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from starlette.datastructures import FormData
from stringcase import snakecase

from .broker import BrokerFactory
from .db import SessionFactory, SessionManagerImpl, SessionManagerProtocol
from .repositories import (
    CacheManager,
    CacheRepositoryProtocol,
    LocalStorageParamsSchema,
    S3StorageParamsSchema,
    SettingsRepositoryFactoryImpl,
    SettingsRepositoryFactoryProtocol,
    SettingsRepositoryProtocol,
    SettingsSourceEnum,
    StorageRepositoryFactoryImpl,
    StorageRepositoryFactoryProtocol,
    StorageRepositoryProtocol,
    StorageTypeEnum,
)
from .schemas import PaginationRequestSchema
from .services import (
    CryptographicAlgorithmEnum,
    CryptographyServiceFactory,
    CryptographyServiceProtocol,
    LockServiceProtocol,
    RedisLockService,
    SeedService,
    TransactionService,
)
from .settings import CoreCacheSettingsSchema, CoreKafkaSettingsSchema, CoreSettingsSchema, CoreStorageSettingsSchema


async def get_nested_form_data(request: Request) -> FormData:
    """
    Получаем форму, позволяющую использовать вложенные словари.
    """
    dot_data = {k.replace('[', '.').replace(']', ''): v for k, v in (await request.form()).items()}
    nested_data = unflatten(dot_data, 'dot')
    for k, v in nested_data.items():
        if isinstance(v, dict):
            nested_data[k] = json.dumps(v)
    return FormData(nested_data)


def get_pagination(page: int | None = None, page_size: int | None = None) -> PaginationRequestSchema:
    """
    Получаем входные данные пагинации.
    """
    return PaginationRequestSchema(page=page or 1, page_size=page_size or 10)


def get_sorting(sorting: str | None = None) -> Sequence[str]:
    """
    Получаем входные данные сортировки.
    """
    if not sorting:
        return []
    return [s[0] + snakecase(s[1:]) if s[0] == '-' else snakecase(s) for s in sorting.split(',')]


NestedFormData = Annotated[FormData, Depends(get_nested_form_data)]
Pagination = Annotated[PaginationRequestSchema, Depends(get_pagination)]
Sorting = Annotated[Sequence[str], Depends(get_sorting)]


class CoreProvider(Provider):
    """
    Провайдер зависимостей.
    """

    scope = Scope.REQUEST

    # --- repositories ---

    settings_repository_factory = provide(
        SettingsRepositoryFactoryImpl, provides=SettingsRepositoryFactoryProtocol, scope=Scope.APP
    )
    storage_repository_factory = provide(
        StorageRepositoryFactoryImpl, provides=StorageRepositoryFactoryProtocol, scope=Scope.APP
    )

    @provide(scope=Scope.APP)
    @staticmethod
    async def get_settings_repository(
        settings_repository_factory: SettingsRepositoryFactoryProtocol,
    ) -> SettingsRepositoryProtocol:
        """
        Получаем репозиторий настроек.
        """
        return await settings_repository_factory.make(SettingsSourceEnum.ENV)

    @provide(scope=Scope.APP)
    @staticmethod
    async def get_settings(settings_repository: SettingsRepositoryProtocol) -> CoreSettingsSchema:
        """
        Получаем настройки.
        """
        return await settings_repository.get(CoreSettingsSchema)

    @provide(scope=Scope.APP)
    @staticmethod
    async def get_cache_settings(settings_repository: SettingsRepositoryProtocol) -> CoreCacheSettingsSchema:
        """
        Получаем настройки кеша.
        """
        return await settings_repository.get(CoreCacheSettingsSchema)

    @provide
    @staticmethod
    async def get_broker_repository(settings_repository: SettingsRepositoryProtocol) -> AsyncIterator[KafkaBroker]:
        """
        Получаем репозиторий брокера сообщений.
        """
        kafka_settings = await settings_repository.get(CoreKafkaSettingsSchema)
        yield BrokerFactory.make_static(kafka_settings)

    @provide(scope=Scope.APP)
    @staticmethod
    async def get_cache_repository(settings_repository: SettingsRepositoryProtocol) -> CacheRepositoryProtocol:
        """
        Получаем репозиторий кеша.
        """
        cache_settings = await settings_repository.get(CoreCacheSettingsSchema)
        return CacheManager.init(cache_settings)

    @provide
    @staticmethod
    async def get_storage_repository(
        settings_repository: SettingsRepositoryProtocol,
        storage_repository_factory: StorageRepositoryFactoryProtocol,
    ) -> AsyncIterator[StorageRepositoryProtocol]:
        """
        Получаем репозиторий файлового хранилища.
        """
        storage_settings = await settings_repository.get(CoreStorageSettingsSchema)
        if storage_settings.provider == 's3' and storage_settings.s3 is not None:
            storage_repository = await storage_repository_factory.make(
                StorageTypeEnum.S3,
                S3StorageParamsSchema.model_validate(storage_settings.s3.model_dump()),
            )
            async with storage_repository:
                yield storage_repository
        elif storage_settings.provider == 'local':
            storage_repository = await storage_repository_factory.make(
                StorageTypeEnum.LOCAL, LocalStorageParamsSchema(path=storage_settings.dir)
            )
            async with storage_repository:
                yield storage_repository
        else:
            raise NotImplementedError(f'Storage {storage_settings.provider} is not allowed')

    # --- db ---

    @provide(scope=Scope.APP)
    @staticmethod
    async def get_async_sessionmaker(
        settings_repository: SettingsRepositoryProtocol,
    ) -> async_sessionmaker[AsyncSession]:
        return await SessionFactory.make_async_session_dynamic(settings_repository)

    @provide
    @staticmethod
    async def get_async_session(session_maker: async_sessionmaker[AsyncSession]) -> AsyncIterator[AsyncSession]:
        """
        Получаем асинхронную сессию.
        """
        async with session_maker() as session:
            yield session

    @provide
    @staticmethod
    def get_session_manager(session: AsyncSession) -> SessionManagerProtocol:
        """
        Получаем менеджер сессий.
        """
        return SessionManagerImpl(session)

    # --- services ---

    seed_service = provide(SeedService, scope=Scope.REQUEST)
    transaction_service = provide(TransactionService)

    @provide(scope=Scope.APP)
    @staticmethod
    def get_cryptography_service_factory(settings: CoreSettingsSchema) -> CryptographyServiceFactory:
        """
        Получаем фабрику сервисов криптографии.
        """
        return CryptographyServiceFactory(settings.secret_key)

    @provide
    @staticmethod
    async def get_cryptography_service(
        cryptography_service_factory: CryptographyServiceFactory,
    ) -> CryptographyServiceProtocol:
        """
        Получаем сервис криптографии.
        """
        return await cryptography_service_factory.make(CryptographicAlgorithmEnum.AES_GCM)

    @provide(scope=Scope.APP)
    @staticmethod
    def get_lock_service(cache_settings: CoreCacheSettingsSchema) -> LockServiceProtocol:
        """
        Получаем сервис распределенной блокировки.
        """
        redis_client = CacheManager.init(cache_settings)
        return RedisLockService(redis_client)  # type: ignore


provider = CoreProvider()
