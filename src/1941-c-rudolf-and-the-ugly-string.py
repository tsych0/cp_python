# Created by Ayush Biswas at 2025/08/09 23:30
# https://codeforces.com/problemset/problem/1941/C
from cpio.cpio import sol_n


# @code begin
import re


@sol_n("n; str")
def solution(n: int, a: str) -> int:
    mapies = len(re.findall("mapie", a))
    maps = len(re.findall("map", a))
    pies = len(re.findall("pie", a))
    return pies + maps - mapies


solution()

# @code end
