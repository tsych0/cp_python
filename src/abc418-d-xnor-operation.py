# Created by Ayush Biswas at 2025/08/11 21:16
# https://atcoder.jp/contests/abc418/tasks/abc418_d
from cpio.cpio import sol

# @code begin
from array import array


@sol("n; str")
def solution(n: int, s: str) -> int:
    b = array("q", [0] * (n + 1))
    u = array("q", [0] * (n + 1))
    for i in range(n):
        if s[i] == "1":
            b[i + 1] = b[i] + 1
            u[i + 1] = u[i]
        else:
            b[i + 1] = u[i]
            u[i + 1] = b[i] + 1
    return sum(b)


solution()

# @code end
