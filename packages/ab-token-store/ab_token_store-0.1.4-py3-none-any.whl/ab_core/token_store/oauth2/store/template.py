from typing import Literal, Optional, override

from ab_core.auth_client.oauth2.schema.token import OAuth2Token
from ab_core.token_store.oauth2.schema.store_type import (
    StoreType,
)

from .base import OAuth2TokenStoreBase


class TemplateOAuth2TokenStore(OAuth2TokenStoreBase):
    type: Literal[StoreType.TEMPLATE] = StoreType.TEMPLATE

    @override
    def load(self, user_id: str, connection_id: str) -> Optional[OAuth2Token]:
        raise NotImplementedError()

    @override
    def save(
        self,
        user_id: str,
        connection_id: str,
        tokens: OAuth2Token,
    ) -> None:
        raise NotImplementedError()

    @override
    def clear(self, user_id: str, connection_id: str) -> None:
        raise NotImplementedError()
