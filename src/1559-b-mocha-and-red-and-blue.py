# Created by Ayush Biswas at 2025/08/11 10:57
# https://codeforces.com/problemset/problem/1559/B
from cpio.cpio import sol_n
from cpio.types import Chars


# @code begin
@sol_n("n; chars")
def solution(n: int, s: Chars) -> Chars:
    if set(s) == set("?"):
        s[0] = "B"
    prev = "?"
    opp = lambda c: "B" if c == "R" else "R"

    for i in range(n):
        if prev != "?" and s[i] == "?":
            s[i] = opp(prev)
        prev = s[i]
    for i in reversed(range(n)):
        if prev != "?" and s[i] == "?":
            s[i] = opp(prev)
        prev = s[i]

    return s


solution()
# @code end
