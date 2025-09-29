from typing import Generic
from maleo.google.secret import Format, GoogleSecretManager
from maleo.schemas.application import ApplicationSettingsT
from maleo.schemas.key.rsa import Keys
from maleo.types.uuid import OptionalUUID


class RSAKeyManager(Generic[ApplicationSettingsT]):
    def __init__(
        self,
        settings: ApplicationSettingsT,
        secret_manager: GoogleSecretManager,
        operation_id: OptionalUUID = None,
    ) -> None:
        if settings.KEY_PASSWORD is not None:
            password = settings.KEY_PASSWORD
        else:
            read_key_password = secret_manager.read(
                Format.STRING,
                name="maleo-key-password",
                operation_id=operation_id,
            )
            password = read_key_password.data.value

        if settings.PRIVATE_KEY is not None:
            private_raw = settings.PRIVATE_KEY
        else:
            read_private_key = secret_manager.read(
                Format.STRING, name="maleo-private-key", operation_id=operation_id
            )
            private_raw = read_private_key.data.value

        if settings.PUBLIC_KEY is not None:
            public_raw = settings.PUBLIC_KEY
        else:
            read_public_key = secret_manager.read(
                Format.STRING, name="maleo-public-key", operation_id=operation_id
            )
            public_raw = read_public_key.data.value

        self.keys = Keys(
            password=password, private_raw=private_raw, public_raw=public_raw
        )
