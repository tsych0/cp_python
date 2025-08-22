# Created by Ayush Biswas at 2025/08/13 18:21
# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b
from cpio.cpio import sol
from cpio.types import Bool, Lines


# @code begin
def qualified(a: int, b: int, s: str):
    m = a + b
    jp = 0
    ab = 0
    for c in s:
        if jp == m:
            yield False
        elif c == "a":
            jp += 1
            yield True
        elif c == "b" and ab < b:
            jp += 1
            ab += 1
            yield True
        else:
            yield False


@sol("n a b; str")
def solution(n: int, a: int, b: int, s: str) -> Lines:
    return Lines([Bool(v) for v in qualified(a, b, s)])


solution()

# @code end
