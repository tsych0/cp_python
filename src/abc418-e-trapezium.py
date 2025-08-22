# Created by Ayush Biswas at 2025/08/11 21:50
# https://atcoder.jp/contests/abc418/tasks/abc418_e
from cpio.cpio import debug, sol


# @code begin
from collections import defaultdict


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def dist(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def slope(self, other: "Point") -> float:
        if self.x == other.x:
            return float("inf")
        return (self.y - other.y) / (self.x - other.x)


@sol("n; n*ints")
def solution(n: int, a: list[list[int]]) -> int:
    points = [Point(x, y) for [x, y] in a]
    lines = defaultdict(lambda: 0)
    slopes = defaultdict(lambda: 0)
    for i in range(n):
        for j in range(i + 1, n):
            d = points[i].dist(points[j])
            s = points[i].slope(points[j])
            lines[(d, s)] += 1
            slopes[s] += 1

    parallelos = sum((i * (i - 1)) // 2 for i in lines.values())
    trapeziums = sum((i * (i - 1)) // 2 for i in slopes.values())

    return trapeziums - parallelos // 2


solution()

# @code end
