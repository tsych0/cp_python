# Created by Ayush Biswas at 2025/08/10 21:38
# https://codeforces.com/contest/2131/problem/F
from cpio.cpio import sol_n
from cpio.types import Binary

# @code begin
from typing import Sequence
from array import array


def prefix_sum(a: Sequence[int]):
    s = 0
    for ai in a:
        yield s
        s += ai
    yield s


@sol_n("n; binary; binary")
def solution(n: int, a: Binary, b: Binary) -> int:
    return 0


solution()

# @code end
