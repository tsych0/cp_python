# Created by Ayush Biswas at 2025/08/11 20:41
# https://atcoder.jp/contests/abc418/tasks/abc418_c
from cpio.cpio import debug, sol
from cpio.types import Lines

# @code begin
from array import array
from bisect import bisect_left
from typing import Iterable


def prefix_sum(a: Iterable[int]):
    s = 0
    for ai in a:
        s += ai
        yield s


@sol("n q; ints; q*int")
def solution(n: int, q: int, a: list[int], b: list[int]) -> Lines:
    a = sorted(a)
    aprefix = array("q", prefix_sum(a))
    debug(aprefix)

    def gen():
        for bi in b:
            idx = bisect_left(a, bi)
            if idx == n:
                yield -1
            elif idx == 0:
                yield (bi - 1) * n + 1
            else:
                yield aprefix[idx - 1] + (bi - 1) * (n - idx) + 1

    return Lines(array("q", gen()))


solution()

# @code end
