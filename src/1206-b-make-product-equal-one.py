# Created by Ayush Biswas at 2025/08/10 17:02
# https://codeforces.com/problemset/problem/1206/B
from cpio.cpio import sol

# @code begin


@sol("n; ints")
def solution(n: int, a: list[int]) -> int:
    one_cost = sum(abs(abs(ai) - 1) for ai in a)
    extra_cost = 2 if sum(1 for ai in a if ai < 0) % 2 != 0 else 0
    extra_cost *= 0 if any(ai == 0 for ai in a) else 1
    return one_cost + extra_cost


solution()

# @code end
