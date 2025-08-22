# Created by Ayush Biswas at 2025/08/19 20:27
# https://codeforces.com/problemset/problem/948/A
from cpio.cpio import sol
from cpio.types import Chars, Lines

# @code begin
from array import array
from typing import Any


@sol("n m; n*chars")
def solution(n: int, m: int, grid: Lines[Chars]) -> Lines[Any] | str:
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "W":
                if j > 0 and grid[i][j - 1] == "S":
                    return "No"
                if j < m - 1 and grid[i][j + 1] == "S":
                    return "No"
                if i > 0 and grid[i - 1][j] == "S":
                    return "No"
                if i < n - 1 and grid[i + 1][j] == "S":
                    return "No"
            elif grid[i][j] != "S":
                grid[i][j] = "D"

    return Lines([Chars(array("w", "Yes")), grid])


solution()

# @code end
