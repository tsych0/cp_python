from typing import Generic, TypeVar

T = TypeVar("T")
E = TypeVar("E")


class CPResult(Generic[T, E]):
    """Result type similar to Rust's Result"""

    def __init__(self, value: T | E, is_success: bool = True):
        self._value = value
        self._is_success = is_success

    @classmethod
    def success(cls, value: T) -> "CPResult[T, E]":
        return cls(value, True)

    @classmethod
    def failure(cls, error: E) -> "CPResult[T, E]":
        return cls(error, False)

    def is_success(self) -> bool:
        return self._is_success

    def unwrap(self) -> T:
        if not self._is_success:
            raise Exception(f"Called unwrap on failure: {self._value}")
        return self._value

    def __str__(self) -> str:
        return str(self._value)


class Bool:
    """Boolean type that displays as Yes/No"""

    def __init__(self, value: bool):
        self.value = value

    def __str__(self) -> str:
        return "Yes" if self.value else "No"


class BOOL:
    """Boolean type that displays as YES/NO"""

    def __init__(self, value: bool):
        self.value = value

    def __str__(self) -> str:
        return "YES" if self.value else "NO"


class Lines(Generic[T]):
    """Newline-separated list"""

    def __init__(self, items: list[T]):
        self.items = items

    def __str__(self) -> str:
        return "\n".join(str(item) for item in self.items)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


class Words(Generic[T]):
    """Space-separated list"""

    def __init__(self, items: list[T]):
        self.items = items

    def __str__(self) -> str:
        return " ".join(str(item) for item in self.items)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


class Binary:
    """Binary string (0s and 1s) type"""

    def __init__(self, bits: list[int]):
        self.bits = bits

    def __str__(self) -> str:
        return "".join(str(bit) for bit in self.bits)

    def __iter__(self):
        return iter(self.bits)


class Chars:
    """Character array type"""

    def __init__(self, chars: list[str]):
        self.chars = chars

    def __str__(self) -> str:
        return "".join(self.chars)

    def __iter__(self):
        return iter(self.chars)

    def __getitem__(self, index):
        return self.chars[index]
