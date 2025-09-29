from datetime import datetime, timezone
from sqlalchemy import Select, select
from sqlalchemy.orm import selectinload
from starlette.authentication import AuthenticationError
from typing import Tuple, Union
from uuid import UUID
from maleo.database.enums import CacheOrigin, CacheLayer, Connection
from maleo.database.handlers import PostgreSQLHandler, RedisHandler
from maleo.database.utils import build_cache_key
from maleo.enums.expiration import Expiration
from maleo.enums.status import DataStatus
from maleo.schemas.connection import ConnectionContext
from maleo.schemas.security.authentication import OptionalAnyAuthentication
from maleo.schemas.security.authorization import OptionalAnyAuthorization
from maleo.schemas.security.impersonation import OptionalImpersonation
from maleo.types.datetime import OptionalDatetime
from .models import (
    Base,
    User as UserModel,
    Organization as OrganizationModel,
    UserOrganization as UserOrganizationModel,
    UserOrganizationRole as UserOrganizationRoleModel,
)
from .schemas import User as UserSchema, UserOrganization as UserOrganizationSchema


class IdentityProvider:
    def __init__(
        self,
        *,
        database: PostgreSQLHandler[Base],
        cache: RedisHandler,
    ) -> None:
        self._database = database
        self._cache = cache
        self._namespace = self._cache.config.additional.build_namespace(
            "identity",
            use_self_base=True,
            origin=CacheOrigin.SERVICE,
            layer=CacheLayer.MIDDLEWARE,
        )

    def _build_get_user_statement(
        self, user_id: Union[int, UUID]
    ) -> Select[Tuple[UserModel]]:
        base = (
            select(UserModel)
            .options(selectinload(UserModel.system_roles))
            .where(UserModel.status == DataStatus.ACTIVE)
        )
        if isinstance(user_id, int):
            return base.where(UserModel.id == user_id)
        elif isinstance(user_id, UUID):
            return base.where(UserModel.uuid == user_id)

    async def get_user(
        self,
        user_id: Union[int, UUID],
        exp: OptionalDatetime = None,
        *,
        operation_id: UUID,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthentication = None,
        authorization: OptionalAnyAuthorization = None,
        impersonation: OptionalImpersonation = None,
    ) -> UserSchema:
        cache_key = build_cache_key("user", str(user_id), namespace=self._namespace)
        redis = self._cache.manager.client.get(Connection.ASYNC)
        redis_data = await redis.get(cache_key)
        if redis_data is not None:
            return UserSchema.model_validate_json(redis_data)

        async with self._database.manager.session.get(
            Connection.ASYNC,
            operation_id=operation_id,
            connection_context=connection_context,
            authentication=authentication,
            authorization=authorization,
            impersonation=impersonation,
        ) as session:
            stmt = self._build_get_user_statement(user_id)

            # Execute and fetch results
            result = await session.execute(stmt)
            row = result.scalars().one_or_none()

            if row is None:
                raise AuthenticationError(
                    f"Can not find active User with ID: {user_id}"
                )

            system_roles = row.get_system_roles([DataStatus.ACTIVE])
            data = UserSchema(
                id=row.id,
                uuid=row.uuid,
                status=row.status,
                username=row.username,
                email=row.email,
                system_roles=system_roles,
            )

        if exp is None:
            ex = Expiration.EXP_1WK.value
        else:
            now = datetime.now(tz=timezone.utc)
            if exp <= now:
                raise AuthenticationError("Cache expiry is less then now")
            ex = min(int((exp - now).total_seconds()), Expiration.EXP_1WK.value)
        await redis.set(cache_key, data.model_dump_json(), ex)

        return data

    def _build_get_user_organization_statement(
        self, user_id: Union[int, UUID], organization_id: Union[int, UUID]
    ) -> Select[Tuple[UserOrganizationModel]]:
        base = (
            select(UserOrganizationModel)
            .options(
                selectinload(
                    UserOrganizationModel.user_organization_roles
                ).selectinload(UserOrganizationRoleModel.organization_role)
            )
            .join(UserModel, UserOrganizationModel.user_id == UserModel.id)
            .join(
                OrganizationModel,
                UserOrganizationModel.organization_id == OrganizationModel.id,
            )
            .where(
                UserOrganizationModel.status == DataStatus.ACTIVE,
                UserModel.status == DataStatus.ACTIVE,
                OrganizationModel.status == DataStatus.ACTIVE,
            )
        )
        if isinstance(user_id, int) and isinstance(organization_id, int):
            return base.where(
                UserModel.id == user_id,
                OrganizationModel.id == organization_id,
            )
        elif isinstance(user_id, UUID) and isinstance(organization_id, UUID):
            return base.where(
                UserModel.uuid == user_id,
                OrganizationModel.uuid == organization_id,
            )

        raise TypeError(
            f"user_id and organization_id must be of the same type (both int or both UUID), "
            f"got {type(user_id).__name__} and {type(organization_id).__name__}"
        )

    async def get_user_organization(
        self,
        user_id: Union[int, UUID],
        organization_id: Union[int, UUID],
        exp: OptionalDatetime = None,
        *,
        operation_id: UUID,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthentication = None,
        authorization: OptionalAnyAuthorization = None,
        impersonation: OptionalImpersonation = None,
    ) -> UserOrganizationSchema:
        cache_key = build_cache_key(
            "user_organization",
            str(user_id),
            str(organization_id),
            namespace=self._namespace,
        )
        redis = self._cache.manager.client.get(Connection.ASYNC)
        redis_data = await redis.get(cache_key)
        if redis_data is not None:
            return UserOrganizationSchema.model_validate_json(redis_data)

        async with self._database.manager.session.get(
            Connection.ASYNC,
            operation_id=operation_id,
            connection_context=connection_context,
            authentication=authentication,
            authorization=authorization,
            impersonation=impersonation,
        ) as session:
            stmt = self._build_get_user_organization_statement(user_id, organization_id)

            # Execute and fetch results
            result = await session.execute(stmt)
            row = result.scalars().one_or_none()

            if row is None:
                raise AuthenticationError(
                    f"Can not find active relation for User '{user_id}' and Organization '{organization_id}'"
                )

            user_organization_roles = row.get_user_organization_roles(
                [DataStatus.ACTIVE]
            )
            data = UserOrganizationSchema(
                id=row.id,
                uuid=row.uuid,
                status=row.status,
                user_id=row.user_id,
                organization_id=row.organization_id,
                user_organization_roles=user_organization_roles,
            )

        if exp is None:
            ex = Expiration.EXP_1WK.value
        else:
            now = datetime.now(tz=timezone.utc)
            if exp <= now:
                raise AuthenticationError("Cache expiry is less then now")
            ex = min(int((exp - now).total_seconds()), Expiration.EXP_1WK.value)
        await redis.set(cache_key, data.model_dump_json(), ex)

        return data
