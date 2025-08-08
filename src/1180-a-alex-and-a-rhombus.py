# Created by Ayush Biswas at 2025/08/08 15:14
# https://codeforces.com/problemset/problem/1180/A
from cpio import *

# @code begin


@sol("n")
def solution(n: int) -> int:
    return 1 + sum(4 * i for i in range(n))


solution()

# @code end
