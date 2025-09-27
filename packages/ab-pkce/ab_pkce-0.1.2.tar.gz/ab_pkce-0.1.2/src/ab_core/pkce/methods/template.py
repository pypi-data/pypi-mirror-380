from typing import Literal, override

from ab_core.pkce.schema.pkce_method import PKCEMethod

from .base import PKCEGeneratorBase


class TemplatePKCE(PKCEGeneratorBase):
    """Generate PKCE code verifier & code challenge."""

    method: Literal[PKCEMethod.TEMPLATE] = PKCEMethod.TEMPLATE

    @staticmethod
    @override
    def generate_code_verifier(length: int = 64) -> str:
        raise NotImplementedError()

    @staticmethod
    @override
    def generate_code_challenge(verifier: str) -> str:
        raise NotImplementedError()
