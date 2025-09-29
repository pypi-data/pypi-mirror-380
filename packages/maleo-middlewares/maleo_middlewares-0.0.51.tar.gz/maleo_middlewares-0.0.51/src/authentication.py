from Crypto.PublicKey.RSA import RsaKey
from datetime import datetime
from fastapi.requests import HTTPConnection
from starlette.authentication import AuthenticationBackend, AuthenticationError
from typing import Optional, Tuple
from uuid import UUID
from maleo.database.handlers import PostgreSQLHandler, RedisHandler
from maleo.enums.system_role import Key as SystemRoleKey
from maleo.schemas.connection import ConnectionContext
from maleo.schemas.security.authentication import (
    RequestCredentials,
    RequestUser,
    BaseAuthentication,
    BaseCredentials,
    BaseUser,
    is_authenticated,
    is_tenant,
    is_system,
)
from maleo.schemas.security.authorization import (
    Scheme,
    BaseAuthorization,
    OptionalAnyAuthorization,
)
from maleo.schemas.security.impersonation import (
    Impersonation,
    OptionalImpersonation,
)
from maleo.schemas.security.token import Domain
from maleo.types.datetime import OptionalDatetime
from maleo.types.string import OptionalListOfStrings
from maleo.types.uuid import OptionalUUID
from .identity import IdentityProvider
from .models import Base
from .schemas import User as UserSchema, UserOrganization as UserOrganizationSchema


class Backend(AuthenticationBackend):
    def __init__(
        self,
        *,
        database: PostgreSQLHandler[Base],
        cache: RedisHandler,
        public_key: RsaKey,
    ):
        super().__init__()
        self._database = database
        self._cache = cache
        self._identity_provider = IdentityProvider(database=database, cache=cache)
        self._public_key = public_key

    async def _get_credentials(
        self,
        user_id: UUID,
        organization_id: OptionalUUID,
        roles: OptionalListOfStrings = None,
        exp: OptionalDatetime = None,
        *,
        operation_id: UUID,
        connection_context: ConnectionContext,
        authorization: OptionalAnyAuthorization = None,
        impersonation: OptionalImpersonation = None,
    ) -> Tuple[UserSchema, Optional[UserOrganizationSchema]]:
        user = await self._identity_provider.get_user(
            user_id,
            exp,
            operation_id=operation_id,
            connection_context=connection_context,
            authorization=authorization,
            impersonation=impersonation,
        )

        if organization_id is None:
            user_organization = None

            if roles is not None:
                for role in roles:
                    if role not in user.system_roles:
                        raise AuthenticationError(
                            f"User is not assigned to role '{role}' in the database"
                        )
        else:
            user_organization = await self._identity_provider.get_user_organization(
                user_id,
                organization_id,
                exp,
                operation_id=operation_id,
                connection_context=connection_context,
                authorization=authorization,
                impersonation=impersonation,
            )

            if roles is not None:
                for role in roles:
                    if role not in user_organization.user_organization_roles:
                        raise AuthenticationError(
                            f"User is not assigned to role '{role}' in the database"
                        )

        return user, user_organization

    async def _authenticate(
        self,
        authorization: BaseAuthorization,
        *,
        operation_id: UUID,
        connection_context: ConnectionContext,
        impersonation: OptionalImpersonation = None,
    ) -> Tuple[RequestCredentials, RequestUser]:
        if authorization.scheme is Scheme.API_KEY:
            raise AuthenticationError("API Key authentication is not yet implemented")

        token = authorization.parse_token(key=self._public_key)

        user, user_organization = await self._get_credentials(
            token.sub,
            token.o,
            token.r,
            datetime.fromtimestamp(token.exp),
            operation_id=operation_id,
            connection_context=connection_context,
            authorization=authorization,
            impersonation=impersonation,
        )

        organization_id = None if user_organization is None else user_organization.uuid
        roles = (
            user.system_roles
            if user_organization is None
            else user_organization.user_organization_roles
        )
        domain = Domain.SYSTEM if user_organization is None else Domain.TENANT
        scopes = [f"{domain}:{role}" for role in roles]

        request_credentials = RequestCredentials(
            domain=domain,
            user_id=user.uuid,
            organization_id=organization_id,
            roles=roles,
            scopes=["authenticated"] + scopes,
        )

        request_user = RequestUser(
            authenticated=True, username=user.username, email=user.email
        )

        return request_credentials, request_user

    async def _validate_impersonation(
        self,
        operation_id: UUID,
        connection_context: ConnectionContext,
        authentication: BaseAuthentication,
        authorization: BaseAuthorization,
        impersonation: Impersonation,
    ):
        _, impersonated_user_organization = await self._get_credentials(
            impersonation.user_id,
            impersonation.organization_id,
            operation_id=operation_id,
            connection_context=connection_context,
            authorization=authorization,
        )

        if not is_authenticated(authentication):
            raise AuthenticationError(
                "Can not perform impersonation if user is unauthenticated"
            )
        if is_system(authentication):
            if (
                SystemRoleKey.ADMINISTRATOR not in authentication.credentials.roles
                or f"{Domain.SYSTEM}:{SystemRoleKey.ADMINISTRATOR}"
                not in authentication.credentials.scopes
            ):
                raise AuthenticationError(
                    "You must have administrator role to perform impersonation"
                )
        elif is_tenant(authentication):
            if (
                impersonation.organization_id is None
                or impersonated_user_organization is None
            ):
                raise AuthenticationError("Can not impersonate system-level user")

            role_scope = (
                ("owner", f"{Domain.TENANT}:owner"),
                ("administrator", f"{Domain.TENANT}:administrator"),
            )
            for role, scope in role_scope:
                if (
                    role not in authentication.credentials.roles
                    or scope not in authentication.credentials.scopes
                ):
                    raise AuthenticationError(
                        f"You must have '{role}' role and '{scope}' scope to perform impersonation"
                    )

    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[RequestCredentials, RequestUser]:
        """Authentication flow"""
        operation_id = getattr(conn.state, "operation_id", None)
        if not operation_id or not isinstance(operation_id, UUID):
            raise AuthenticationError("Unable to determine operation_id")

        connection_context = ConnectionContext.from_connection(conn)
        authorization = BaseAuthorization.extract(conn=conn, auto_error=False)
        impersonation = Impersonation.extract(conn=conn)

        if authorization is None:
            if impersonation is not None:
                raise AuthenticationError(
                    "Can not perform impersonation if user is unauthorized"
                )
            return RequestCredentials(), RequestUser()

        request_credentials, request_user = await self._authenticate(
            authorization,
            operation_id=operation_id,
            connection_context=connection_context,
            impersonation=impersonation,
        )

        authentication = BaseAuthentication(
            credentials=BaseCredentials.model_validate(
                request_credentials, from_attributes=True
            ),
            user=BaseUser.model_validate(request_user, from_attributes=True),
        )

        if impersonation is not None:
            await self._validate_impersonation(
                operation_id=operation_id,
                connection_context=connection_context,
                authentication=authentication,
                authorization=authorization,
                impersonation=impersonation,
            )

        return request_credentials, request_user
