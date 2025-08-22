# Created by Ayush Biswas at 2025/08/09 21:51
# https://codeforces.com/problemset/problem/910/A
from cpio.cpio import sol
from cpio.types import Binary

# @code begin
from array import array


@sol("n d; binary")
def solution(n: int, d: int, s: Binary) -> int:
    dp = array("q", (10**9 for _ in range(n + 1)))
    dp[1] = 0

    for i in range(1, n + 1):
        for j in range(1, d + 1):
            if i + j > n:
                break
            if s[i + j - 1]:
                dp[i + j] = min(dp[i + j], dp[i] + 1)

    return -1 if dp[n] == 10**9 else dp[n]


solution()

# @code end
