# Created by Ayush Biswas at 2025/08/13 18:09
# https://atcoder.jp/contests/abc156/tasks/abc156_c
from cpio.cpio import sol

# @code begin
from statistics import mean
from math import ceil, floor


@sol("n; ints")
def solution(n: int, a: list[int]) -> int:
    m = mean(a)
    mceil = ceil(m)
    mfloor = floor(m)
    return min(sum((ai - mceil) ** 2 for ai in a), sum((ai - mfloor) ** 2 for ai in a))


solution()

# @code end
