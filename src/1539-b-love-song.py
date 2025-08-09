# Created by Ayush Biswas at 2025/08/08 18:51
# https://codeforces.com/problemset/problem/1539/B

from cpio.cpio import sol
from cpio.types import Words, Lines

# @code begin
from string import ascii_lowercase
from array import array
from typing import Iterable


def prefix_sum(a: Iterable[int]):
    s = 0
    for ai in a:
        yield s
        s += ai
    yield s


@sol("n q; str; q*ints")
def solution(_: int, __: int, a: str, queries: list[Words[int]]) -> Lines[int]:
    w = {c: i for i, c in enumerate(ascii_lowercase, 1)}
    ai = array("i", (w[ai] for ai in a))
    ax = array("i", prefix_sum(ai))
    return Lines([ax[r] - ax[l - 1] for [l, r] in queries])


solution()

# @code end
