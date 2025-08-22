# Created by Ayush Biswas at 2025/08/11 20:25
# https://atcoder.jp/contests/abc418/tasks/abc418_a
from cpio.cpio import sol, Bool

# @code begin


@sol("n; str")
def solution(n: int, s: str) -> Bool:
    return Bool(s.endswith("tea"))


solution()

# @code end
