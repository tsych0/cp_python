# Created by Ayush Biswas at 2025/08/08 15:19
# https://codeforces.com/problemset/problem/1944/A
from cpio import *


# @code begin
@sol_n("n k")
def solution(n: int, k: int) -> int:
    return 1 if k >= n - 1 else n


solution()

# @code end
