# Created by Ayush Biswas at 2025/08/10 21:28
# https://codeforces.com/contest/2131/problem/H
from cpio.cpio import sol_n

# @code begin
from math import gcd


@sol_n("n; ints")
def solution(n: int, a: list[int]) -> int:

    return n * sum(a)


solution()

# @code end
