import secrets
from typing import Literal, override

from ab_core.pkce.schema.pkce_method import PKCEMethod

from .base import PKCEGeneratorBase


class PlainPKCE(PKCEGeneratorBase):
    """Legacy PKCE implementation using `plain` method (verifier == challenge)."""

    method: Literal[PKCEMethod.PLAIN] = PKCEMethod.PLAIN

    @staticmethod
    @override
    def build_verifier(length: int = 64) -> str:
        return secrets.token_urlsafe(length)[:128]

    @staticmethod
    @override
    def build_challenge(verifier: str) -> str:
        return verifier
