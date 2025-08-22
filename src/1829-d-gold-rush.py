# Created by Ayush Biswas at 2025/08/19 21:05
# https://codeforces.com/problemset/problem/1829/D
from cpio.cpio import sol_n
from cpio.types import BOOL

# @code begin
from functools import cache


@cache
def gold_rush(n: int, m: int) -> bool:
    if n == m:
        return True

    if n < m or n % 3 != 0:
        return False

    return gold_rush(n / 3, m) or gold_rush(2 * n / 3, m)


@sol_n("n m")
def solution(n: int, m: int) -> BOOL:
    return BOOL(gold_rush(n, m))


solution()

# @code end
