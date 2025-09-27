import base64
import hashlib
import secrets
from typing import Literal, override

from ab_core.pkce.schema.pkce_method import PKCEMethod

from .base import PKCEGeneratorBase


class S256PKCE(PKCEGeneratorBase):
    """Generate PKCE code verifier & code challenge."""

    method: Literal[PKCEMethod.S256] = PKCEMethod.S256

    @staticmethod
    @override
    def generate_code_verifier(length: int = 64) -> str:
        return secrets.token_urlsafe(length)[:128]  # max PKCE length = 128

    @staticmethod
    @override
    def generate_code_challenge(verifier: str) -> str:
        digest = hashlib.sha256(verifier.encode()).digest()
        return base64.urlsafe_b64encode(digest).decode().rstrip("=")
