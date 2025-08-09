# Created by Ayush Biswas at 2025/08/08 19:31
# https://codeforces.com/problemset/problem/1549/B
from cpio.cpio import sol_n
from cpio.types import Binary

# @code begin


@sol_n("n; binary; binary")
def solution(n: int, enemy: Binary, greg: Binary) -> int:
    res = 0
    for i in range(n):
        if greg[i]:
            if not enemy[i]:
                enemy[i] = 2
                res += 1
            elif i != 0 and enemy[i - 1] == 1:
                enemy[i - 1] = 0
                res += 1
            elif i < n - 1 and enemy[i + 1] == 1:
                enemy[i + 1] = 0
                res += 1
    return res


solution()

# @code end
