# Created by Ayush Biswas at 2025/08/09 18:52
# https://codeforces.com/problemset/problem/1797/A
from cpio.cpio import sol_n

# @code begin


@sol_n("n m; x1 y1 x2 y2")
def solution(n: int, m: int, x1: int, y1: int, x2: int, y2: int) -> int:
    f = 4
    f -= 1 if x1 == 1 or x1 == n else 0
    f -= 1 if y1 == 1 or y1 == m else 0
    s = 4
    s -= 1 if x2 == 1 or x2 == n else 0
    s -= 1 if y2 == 1 or y2 == m else 0

    return min(f, s)


solution()

# @code end
