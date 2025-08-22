# Created by Ayush Biswas at 2025/08/19 23:07
# https://codeforces.com/problemset/problem/3/A
from cpio.cpio import sol
from cpio.types import Lines

# @code begin


@sol("str; str")
def solution(src: str, dest: str) -> Lines:
    c1, r1 = ord(src[0]), int(src[1])
    c2, r2 = ord(dest[0]), int(dest[1])
    downMoves = max(0, r1 - r2) * "D"
    upMoves = max(0, r2 - r1) * "U"
    leftMoves = max(0, c1 - c2) * "L"
    rightMoves = max(0, c2 - c1) * "R"
    upDown = upMoves + downMoves
    rightLeft = rightMoves + leftMoves
    combined = [c1 + c2 for c1, c2 in zip(rightLeft, upDown)]
    res = combined + list(upDown)[len(combined) :] + list(rightLeft)[len(combined) :]
    return Lines([len(res), Lines(res)])


solution()

# @code end
