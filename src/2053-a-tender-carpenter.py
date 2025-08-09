# Created by Ayush Biswas at 2025/08/08 23:58
# https://codeforces.com/problemset/problem/2053/A
from cpio.cpio import sol_n
from cpio.types import BOOL


# @code begin
@sol_n("n; ints")
def solution(n: int, a: list[int]) -> BOOL:
    for i in range(1, n):
        x, y = a[i - 1], a[i]
        if 2 * x > y and 2 * y > x:
            return BOOL(True)
    return BOOL(False)


solution()

# @code end
