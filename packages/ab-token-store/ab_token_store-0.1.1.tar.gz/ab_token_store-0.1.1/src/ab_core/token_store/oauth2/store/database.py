import json
import os
from typing import Literal, Optional, override

from ab_core.auth_client.oauth2.schema.token import OAuth2Token
from ab_core.token_store.oauth2.schema.store_type import (
    StoreType,
)

from .base import OAuth2TokenStoreBase


class DatabaseOAuth2TokenStore(OAuth2TokenStoreBase):
    type: Literal[StoreType.DATABASE] = StoreType.DATABASE
    template: str

    @override
    def load(self, user_id: str, connection_id: str) -> Optional[OAuth2Token]:
        path = self._path(user_id, connection_id)
        if not os.path.isfile(path):
            return None
        with open(path, "r") as f:
            data = json.load(f)
        return OAuth2Token.model_validate(data)

    @override
    def save(
        self,
        user_id: str,
        connection_id: str,
        tokens: OAuth2Token,
    ) -> None:
        path = self._path(user_id, connection_id)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        base = None
        if os.path.isfile(path):
            with open(path, "r") as f:
                base = json.load(f)
        data = tokens.model_dump()
        # preserve the refresh token when the new token does not have one
        if base and "refresh_token" in base and "refresh_token" not in data:
            data["refresh_token"] = base["refresh_token"]
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    @override
    def clear(self, user_id: str, connection_id: str) -> None:
        path = self._path(user_id, connection_id)
        if os.path.isfile(path):
            os.remove(path)
