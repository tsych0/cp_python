# Created by Ayush Biswas at 2025/08/08 16:07
# https://codeforces.com/problemset/problem/2019/A
from cpio.cpio import sol_n


# @code begin
@sol_n("n; ints")
def solution(n: int, a: list[int]) -> int:
    if n == 1:
        return a[0] + 1

    odds = a[::2]
    evens = a[1::2]

    return max(max(odds) + len(odds), max(evens) + len(evens))


solution()
# @code end
