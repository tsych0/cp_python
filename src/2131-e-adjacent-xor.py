# Created by Ayush Biswas at 2025/08/10 21:04
# https://codeforces.com/contest/2131/problem/E
from cpio.cpio import sol_n, BOOL

# @code begin


@sol_n("n; ints; ints")
def solution(n: int, a: list[int], b: list[int]) -> BOOL:
    if a[-1] != b[-1]:
        return BOOL(False)
    for i in range(n - 1):
        if (a[i] ^ a[i + 1] == b[i]) or (a[i] ^ b[i + 1] == b[i]) or a[i] == b[i]:
            continue
        else:
            return BOOL(False)
    return BOOL(True)


solution()

# @code end
