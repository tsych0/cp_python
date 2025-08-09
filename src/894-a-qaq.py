# Created by Ayush Biswas at 2025/08/07 16:37
# https://codeforces.com/problemset/problem/894/A

from cpio.cpio import sol

# @code begin


@sol("str")
def solution(s: str) -> int:
    q_idx = [i for i, c in enumerate(s) if c == "Q"]
    a_idx = [i for i, c in enumerate(s) if c == "A"]

    return sum(1 for q1 in q_idx for a in a_idx for q2 in q_idx if q1 < a < q2)


solution()

# @code end
