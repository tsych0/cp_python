from typing import Generic, TypeVar, Sequence
from array import array

T = TypeVar("T")


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

    def __init__(self, items: Sequence[T]):
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

    def __init__(self, items: Sequence[T]):
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

    def __init__(self, bits: array):
        self.bits = bits

    def __str__(self) -> str:
        return "".join(str(bit) for bit in self.bits)

    def __iter__(self):
        return iter(self.bits)

    def __getitem__(self, index):
        return self.bits[index]

    def __setitem__(self, key, value):
        self.bits[key] = value


class Chars:
    """Character array type"""

    def __init__(self, chars: array):
        self.chars = chars

    def __str__(self) -> str:
        return "".join(self.chars)

    def __iter__(self):
        return iter(self.chars)

    def __getitem__(self, index):
        return self.chars[index]
