# Created by Ayush Biswas at 2025/08/08 10:32
# https://codeforces.com/problemset/problem/2091/B
from cpio import *

# @code begin
from typing import Generator


def strong_teams(a: list[int], x: int) -> Generator[int]:
    a = sorted(a, reverse=True)
    count = 0
    skill = 10**9

    for ai in a:
        skill = min(skill, ai)
        count += 1
        if skill * count >= x:
            yield count
            count = 0


@sol_n("n x; ints")
def solution(_: int, x: int, a: list[int]) -> int:
    # count the strong teams
    return sum(1 for _ in strong_teams(a, x))


solution()

# @code end
