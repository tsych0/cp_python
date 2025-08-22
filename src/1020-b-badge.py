# Created by Ayush Biswas at 2025/08/19 21:14
# https://codeforces.com/problemset/problem/1020/B
from cpio.cpio import sol
from cpio.types import Words

# @code begin


@sol("n; ints")
def solution(n: int, p: list[int]) -> Words:
    def dfs(i):
        visited = [False for _ in range(n)]
        while True:
            visited[i - 1] = True
            i = p[i - 1]
            if visited[i - 1]:
                return i

    return Words([dfs(i + 1) for i in range(n)])


solution()

# @code end
