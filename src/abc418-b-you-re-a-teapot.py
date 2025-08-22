# Created by Ayush Biswas at 2025/08/11 20:31
# https://atcoder.jp/contests/abc418/tasks/abc418_b
from cpio.cpio import sol

# @code begin


@sol("str")
def solution(s: str) -> float:
    tidxs = [i for i, c in enumerate(s) if c == "t"]
    r = 0
    n = len(tidxs)
    for i in range(n):
        for j in range(i + 1, n):
            t1 = tidxs[i]
            t2 = tidxs[j]
            tbetween = j - i - 1
            lenbetween = t2 - t1 - 1
            if lenbetween > 0:
                r = max(r, tbetween / lenbetween)

    return r


solution()

# @code end
