# Created by Ayush Biswas at 2025/08/08 09:55
# https://codeforces.com/problemset/problem/1932/A
from cpio.cpio import sol_n

# @code begin


@sol_n("n; str")
def solution(_: int, s: str) -> int:
    return s.split("**")[0].count("@")


solution()

# @code end
