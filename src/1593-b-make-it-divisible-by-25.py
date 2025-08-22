# Created by Ayush Biswas at 2025/08/10 10:35
# https://codeforces.com/problemset/problem/1593/B
from cpio.cpio import sol_n


# @code begin
def find_subseq(n: str, s: str) -> int:
    r = 0
    n = n[::-1]
    for c in s[::-1]:
        while n and n[0] != c:
            n = n[1:]
            r += 1
        if not n:
            return r * 10
        n = n[1:]
    return r


@sol_n("str")
def solution(n: str) -> int:
    return min(
        find_subseq(n, "00"),
        find_subseq(n, "75"),
        find_subseq(n, "50"),
        find_subseq(n, "25"),
    )


solution()

# @code end
