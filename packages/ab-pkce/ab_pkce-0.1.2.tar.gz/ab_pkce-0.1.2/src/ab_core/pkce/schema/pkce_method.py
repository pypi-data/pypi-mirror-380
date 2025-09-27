from enum import StrEnum


class PKCEMethod(StrEnum):
    S256 = "S256"
    PLAIN = "plain"
    TEMPLATE = "TEMPLATE"
