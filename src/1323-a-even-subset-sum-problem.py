# Created by Ayush Biswas at 2025/08/09 16:33
# https://codeforces.com/problemset/problem/1323/A
from cpio.cpio import sol_n
from cpio.types import Words, Lines


# @code begin
def even_subset(a: list[int]):
    for i, ai in enumerate(a, 1):
        if ai % 2 == 0:
            yield [i]
            return

    if len(a) < 2:
        return

    yield [1, 2]


@sol_n("n; ints")
def solution(_: int, a: list[int]) -> Lines | int:
    try:
        res = next(even_subset(a))
        return Lines([len(res), Words(res)])
    except StopIteration:
        return -1


solution()

# @code end
