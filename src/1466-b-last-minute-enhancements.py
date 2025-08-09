# Created by Ayush Biswas at 2025/08/08 21:09
# https://codeforces.com/problemset/problem/1466/B

from cpio.cpio import sol_n

# @code begin
from collections import defaultdict
from itertools import groupby


@sol_n("n; ints")
def solution(n: int, a: list[int]) -> int:
    grps = defaultdict(lambda: 0, {i: sum(1 for _ in g) for i, g in groupby(a)})
    for i in range(1, 2 * n + 1):
        if grps[i] > 1:
            grps[i + 1] += 1

    return sum(1 for k in grps if grps[k])


solution()

# @code end
