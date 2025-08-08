# Created by Ayush Biswas at 2025/08/08 10:04
# https://codeforces.com/problemset/problem/2126/B

from cpio import *


# @code begin
from typing import Generator


def hike(a: list[int], k: int) -> Generator[bool]:
    r = 0
    for ai in a:
        if r == k:
            r = 0
            yield True
        elif not ai:
            r += 1
        else:
            r = 0
    if r == k:
        yield True


@sol_n("n k; ints")
def solution(_: int, k: int, a: list[int]) -> int:
    return sum(1 for _ in hike(a, k))


solution()

# @code end
