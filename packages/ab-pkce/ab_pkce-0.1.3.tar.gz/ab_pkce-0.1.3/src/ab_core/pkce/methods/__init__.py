from typing import Annotated, Union

from pydantic import Discriminator

from .plain import PlainPKCE
from .s256 import S256PKCE
from .template import TemplatePKCE

PKCE = Annotated[
    Union[PlainPKCE, S256PKCE, TemplatePKCE],
    Discriminator("method"),
]
