from abc import ABC, abstractmethod

from pydantic import BaseModel, model_validator


class PKCEGeneratorBase(BaseModel, ABC):
    verifier: str = None
    challenge: str = None

    @model_validator(mode="after")
    def populate_fields(self):
        if self.verifier is None:
            self.verifier = self.generate_code_verifier()
        if self.challenge is None:
            self.challenge = self.generate_code_challenge(self.verifier)
        return self

    @staticmethod
    @abstractmethod
    def generate_code_verifier(length: int = 64) -> str: ...

    @staticmethod
    @abstractmethod
    def generate_code_challenge(verifier: str) -> str: ...
