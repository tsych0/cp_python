// Created by Ayush Biswas at 2025/08/23 19:25
// https://codeforces.com/problemset/problem/2051/C
from cpio.cpio import sol_n

# @code begin


@sol_n("n; ints")
def solution(n: int, a: list[int]) -> int:
    return n * sum(a)


solution()

# @code end
