# Created by Ayush Biswas at 2025/08/07 23:03
# https://codeforces.com/problemset/problem/1862/A
from cpio import *

# @code begin


@sol_n("n m; n*chars")
def solution(n: int, m: int, carpet: Lines[Chars]) -> BOOL:
    v_idx = min([i for l in carpet for i, c in enumerate(l) if c == "v"], default=20)
    i_idx = [i for l in carpet for i, c in enumerate(l) if c == "i"]
    k_idx = [i for l in carpet for i, c in enumerate(l) if c == "k"]
    a_idx = max([i for l in carpet for i, c in enumerate(l) if c == "a"], default=-1)
    return BOOL(any([1 for j in i_idx for k in k_idx if v_idx < j < k < a_idx]))


solution()

# @code end
