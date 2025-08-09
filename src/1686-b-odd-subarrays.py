# Created by Ayush Biswas at 2025/08/09 16:46
# https://codeforces.com/problemset/problem/1686/B
from cpio.cpio import sol_n


# @code begin
def max_inversions(a: list[int]):
    curr = -1
    for ai in a:
        if ai > curr:
            curr = ai
        else:
            curr = -1
            yield True


@sol_n("n; ints")
def solution(_: int, a: list[int]) -> int:
    return sum(1 for _ in max_inversions(a))


solution()

# @code end
