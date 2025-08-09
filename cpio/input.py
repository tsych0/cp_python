from cpio.types import Chars, Binary

# @code begin
import sys
from array import array


class CPInput:
    """Enhanced input reader"""

    def __init__(self, input_stream=None):
        self.stream = input_stream or sys.stdin
        if hasattr(self.stream, "read"):
            self.lines = self.stream.read().splitlines()
        else:
            self.lines = self.stream.readlines()
        self.index = 0

    def read_line(self) -> str:
        if self.index >= len(self.lines):
            return ""
        line = self.lines[self.index].strip()
        self.index += 1
        return line

    def read_int(self) -> int:
        return int(self.read_line())

    def read_ints(self) -> array:
        return array("q", map(int, self.read_line().split()))

    def read_str(self) -> str:
        return self.read_line()

    def read_strs(self) -> list[str]:
        return self.read_line().split()

    def read_chars(self) -> Chars:
        return Chars(array("B", self.read_line()))

    def read_binary(self) -> Binary:
        return Binary(array("h", (int(c) for c in self.read_line() if c in "01")))

    def read_floats(self) -> array:
        return array("d", map(float, self.read_line().split()))


# @code end
