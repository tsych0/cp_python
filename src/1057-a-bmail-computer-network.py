# Created by Ayush Biswas at 2025/08/19 20:55
# https://codeforces.com/problemset/problem/1057/A
from cpio.cpio import sol
from cpio.types import Words

# @code begin


@sol("n; ints")
def solution(n: int, a: list[int]) -> Words:
    res = []
    curr = n
    while curr != 1:
        res.append(curr)
        curr = a[curr - 2]
    res.append(curr)
    return Words(reversed(res))  # type: ignore


solution()

# @code end
