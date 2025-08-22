# Created by Ayush Biswas at 2025/08/12 20:52
# https://codeforces.com/contest/2125/problem/C
from cpio.cpio import sol_n


# @code begin
from functools import cache


@cache
def good(x):
    return x % 2 > 0 and x % 3 > 0 and x % 5 > 0 and x % 7 > 0


def get_naive(x):
    ans = 0
    for i in range(x):
        if good(i):
            ans += 1
    return ans


def get(r):
    return (r // 210) * get_naive(210) + get_naive(r % 210)


@sol_n("l r")
def solution(l: int, r: int) -> int:
    return get(r + 1) - get(l)


solution()

# @code end
