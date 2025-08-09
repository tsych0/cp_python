# Created by Ayush Biswas at 2025/08/08 09:14
# https://codeforces.com/problemset/problem/1519/B
from cpio.cpio import sol_n
from cpio.types import BOOL

# @code begin
from dataclasses import dataclass


@dataclass
class State:
    x: int
    y: int
    cost: int


@sol_n("n m k")
def solution(n: int, m: int, k: int) -> BOOL:
    return BOOL(k == n * m - 1)


solution()

# @code end
