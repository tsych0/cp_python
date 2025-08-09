# Created by Ayush Biswas at 2025/08/08 21:01
# https://codeforces.com/problemset/problem/1598/A
from cpio.cpio import sol_n
from cpio.types import Binary, BOOL

# @code begin


@sol_n("n; 2*binary")
def solution(_: int, a: list[Binary]) -> BOOL:
    return BOOL(not any(i and j for i, j in zip(a[0], a[1])))


solution()

# @code end
