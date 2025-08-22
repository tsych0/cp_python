# Created by Ayush Biswas at 2025/08/12 20:36
# https://codeforces.com/contest/2125/problem/A
from cpio.cpio import sol_n

# @code begin


@sol_n("str")
def solution(s: str) -> str:
    return "".join(reversed(sorted(s)))


solution()

# @code end
