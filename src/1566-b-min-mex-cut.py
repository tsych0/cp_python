# Created by Ayush Biswas at 2025/08/08 21:21
# https://codeforces.com/problemset/problem/1566/B

from cpio.cpio import sol_n
from cpio.types import Binary

# @code begin
from itertools import groupby


@sol_n("binary")
def solution(a: Binary) -> int:
    return min(2, sum(1 - i for i, g in groupby(a.bits)))


solution()

# @code end
