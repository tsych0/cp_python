# Created by Ayush Biswas at 2025/08/08 20:52
# https://codeforces.com/problemset/problem/2069/A
from cpio.cpio import sol_n
from cpio.types import BOOL, Binary

# @code begin
from array import array


@sol_n("n; ints")
def solution(_: int, a: array) -> BOOL:
    return BOOL(str(Binary(a)).find("101") == -1)


solution()

# @code end
