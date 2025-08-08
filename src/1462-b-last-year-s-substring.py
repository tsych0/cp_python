# Created by Ayush Biswas at 2025/08/08 10:46
# https://codeforces.com/problemset/problem/1462/B
from cpio import *

# @code begin
from itertools import takewhile


@sol_n("n; str")
def solution(_: int, s: str) -> BOOL:
    first_part = "".join(
        a for a, b in takewhile(lambda pair: pair[0] == pair[1], zip(s, "2020"))
    )
    second_part = s[len(first_part) - 4 :]
    return BOOL(first_part == "2020" or first_part + second_part == "2020")


solution()

# @code end
