# Created by Ayush Biswas at 2025/08/12 20:45
# https://codeforces.com/contest/2125/problem/B
from cpio.cpio import sol_n

# @code begin
from math import gcd


@sol_n("a b k")
def solution(a: int, b: int, k: int) -> int:
    g = gcd(a, b)
    if a // g > k or b // g > k:
        return 2
    return 1


solution()

# @code end
