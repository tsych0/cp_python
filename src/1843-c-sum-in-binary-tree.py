# Created by Ayush Biswas at 2025/08/07 22:28
# https://codeforces.com/problemset/problem/1843/C
from cpio.cpio import sol_n

# @code begin


def parents(n: int):
    while n != 0:
        yield n
        n //= 2


@sol_n("int")
def solution(n: int) -> int:
    return sum(parents(n))


solution()

# @code end
