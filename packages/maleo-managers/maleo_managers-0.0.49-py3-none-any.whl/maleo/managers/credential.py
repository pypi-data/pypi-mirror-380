from Crypto.PublicKey.RSA import RsaKey
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel, Field
from typing_extensions import Annotated
from uuid import UUID
from maleo.crypto.token import encode
from maleo.enums.environment import Environment
from maleo.google.secret import Format, GoogleSecretManager
from maleo.schemas.security.authentication import (
    SystemCredentials,
    AuthenticatedUser,
    SystemAuthentication,
)
from maleo.schemas.security.authorization import BearerTokenAuthorization
from maleo.schemas.security.token import Domain, SystemToken
from maleo.types.string import ListOfStrings
from maleo.types.uuid import OptionalUUID
from maleo.utils.loaders.yaml import from_string


class Credential(BaseModel):
    id: Annotated[int, Field(..., description="ID", ge=1)]
    uuid: Annotated[UUID, Field(..., description="UUID")]
    username: Annotated[str, Field(..., description="Username", max_length=50)]
    email: Annotated[str, Field(..., description="Email", max_length=255)]
    password: Annotated[str, Field(..., description="Password", max_length=255)]
    roles: Annotated[ListOfStrings, Field(..., description="Roles", min_length=1)]


class CredentialManager:
    def __init__(
        self,
        environment: Environment,
        private_key: RsaKey,
        secret_manager: GoogleSecretManager,
        operation_id: OptionalUUID = None,
    ) -> None:
        self._private_key = private_key
        self._secret_manager = secret_manager

        name = f"maleo-internal-credentials-{environment}"
        read_secret = secret_manager.read(
            Format.STRING, name=name, operation_id=operation_id
        )
        data = from_string(read_secret.data.value)
        self.credential = Credential.model_validate(data)

    @property
    def token(self) -> SystemToken:
        now = datetime.now(tz=timezone.utc)
        return SystemToken(
            iss=None,
            sub=self.credential.uuid,
            aud=None,
            exp=int(now.timestamp()),
            iat=int((now + timedelta(minutes=15)).timestamp()),
            r=self.credential.roles,
        )

    @property
    def token_str(self) -> str:
        return encode(self.token.model_dump(mode="json"), key=self._private_key)

    @property
    def authentication(self) -> SystemAuthentication:
        scopes = [f"{Domain.SYSTEM}:{role}" for role in self.credential.roles]
        return SystemAuthentication(
            credentials=SystemCredentials(
                user_id=self.credential.uuid,
                roles=self.credential.roles,
                scopes=["authenticated"] + scopes,
            ),
            user=AuthenticatedUser(
                display_name=self.credential.username,
                identity=self.credential.email,
            ),
        )

    @property
    def authorization(self) -> BearerTokenAuthorization:
        return BearerTokenAuthorization(credentials=self.token_str)
