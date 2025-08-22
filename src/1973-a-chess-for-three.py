# Created by Ayush Biswas at 2025/08/10 17:52
# https://codeforces.com/problemset/problem/1973/A
from cpio.cpio import sol_n

# @code begin


@sol_n("ints")
def solution(score: list[int]) -> int:
    if sum(score) % 2 == 0:
        p1, p2, p3 = sorted(score)
        if p1 + p2 >= p3:
            return sum(score) // 2
        else:
            return p1 + p2
    else:
        return -1


solution()

# @code end
