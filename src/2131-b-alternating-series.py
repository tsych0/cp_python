# Created by Ayush Biswas at 2025/08/10 20:13
# https://codeforces.com/contest/2131/problem/B
from cpio.cpio import sol_n
from cpio.types import Words

# @code begin
from itertools import cycle
from array import array


@sol_n("n")
def solution(n: int) -> Words:
    res = array("q", [0] * n)
    for i, v in zip(range(n), cycle([-1, 3])):
        res[i] = v
    if res[-1] == 3:
        res[-1] = 2
    return Words(res)


solution()

# @code end
