import re
from enum import StrEnum
from maleo.types.string import ListOfStrings


class Case(StrEnum):
    CAMEL = "camel"
    PASCAL = "pascal"
    SNAKE = "snake"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


def to_camel(text: str) -> str:
    """Converts snake_case or PascalCase to camelCase."""
    words = re.split(r"[_\s]", text)  # Handle snake_case and spaces
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def to_pascal(text: str) -> str:
    """Converts snake_case or camelCase to PascalCase."""
    words = re.split(r"[_\s]", text)
    return "".join(word.capitalize() for word in words)


def to_snake(text: str) -> str:
    """Converts camelCase or PascalCase to snake_case."""
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text).lower()


def convert(text: str, target: Case) -> str:
    """Converts text to the specified case format."""
    if target is Case.CAMEL:
        return to_camel(text)
    elif target is Case.PASCAL:
        return to_pascal(text)
    elif target is Case.SNAKE:
        return to_snake(text)
