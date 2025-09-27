from abc import ABC, abstractmethod
from typing import Optional

from pydantic import BaseModel

from ab_core.auth_client.oauth2.schema.token import OAuth2Token


class OAuth2TokenStoreBase(BaseModel, ABC):
    @abstractmethod
    def load(self, user_id: str, connection_id: str) -> Optional[OAuth2Token]: ...

    @abstractmethod
    def save(
        self,
        user_id: str,
        connection_id: str,
        tokens: OAuth2Token,
    ) -> None: ...

    @abstractmethod
    def clear(self, user_id: str, connection_id: str) -> None: ...
