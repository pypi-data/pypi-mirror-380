from typing import Annotated, Union

from pydantic import Discriminator

from .fs import FSOAuth2TokenStore
from .template import TemplateOAuth2TokenStore

OAuth2TokenStore = Annotated[
    Union[FSOAuth2TokenStore, TemplateOAuth2TokenStore],
    Discriminator("type"),
]
