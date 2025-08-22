# Created by Ayush Biswas at 2025/08/19 20:50
# https://codeforces.com/problemset/problem/1055/A
from cpio.cpio import sol
from cpio.types import BOOL

# @code begin


@sol("n s; ints; ints")
def solution(n: int, s: int, a: list[int], b: list[int]) -> BOOL:
    if a[0] == 0:
        return BOOL(False)
    if a[s - 1] == 1:
        return BOOL(True)
    if b[s - 1] == 0:
        return BOOL(False)
    for i in range(s, n):
        if a[i] == 1 and b[i] == 1:
            return BOOL(True)
    return BOOL(False)


solution()

# @code end
