# Created by Ayush Biswas at 2025/08/10 20:24
# https://codeforces.com/contest/2131/problem/C
from cpio.cpio import sol_n
from cpio.types import BOOL

# @code begin
fuck
from collections import defaultdict
from random import getrandbits

RD = getrandbits(31)


@sol_n("n k; ints; ints")
def solution(n: int, k: int, s: list[int], t: list[int]) -> BOOL:
    ts = defaultdict(int)

    for ti in t:
        tx = min(k - ti % k, ti % k)
        ts[tx ^ RD] += 1

    for si in s:
        sx = min(k - si % k, si % k)
        ts[sx ^ RD] -= 1

    return BOOL(all(v == 0 for v in ts.values()))


solution()

# @code end
