# Created by Ayush Biswas at 2025/08/10 20:07
# https://codeforces.com/contest/2131/problem/0
from cpio.cpio import sol_n

# @code begin


@sol_n("n; ints; ints")
def solution(n: int, a: list[int], b: list[int]) -> int:
    r = 1
    for ai, bi in zip(a, b):
        if ai > bi:
            r += ai - bi
    return r


solution()

# @code end
