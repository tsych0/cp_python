# Created by Ayush Biswas at 2025/08/09 22:37
# https://codeforces.com/problemset/problem/115/A
from cpio.cpio import sol

# @code begin
from collections import defaultdict, deque


@sol("n; n*int")
def solution(n: int, a: list[int]) -> int:
    graph = defaultdict(list)
    ceos = []
    for i, manager in enumerate(a, 1):
        if manager > 0:
            graph[manager].append(i)
        else:
            ceos.append(i)

    def depth(i: int) -> int:
        res = 0
        stack = deque()
        stack.append((i, 1))
        while stack:
            match stack.popleft():
                case (node, depth):
                    res = max(res, depth)
                    for child in graph[node]:
                        stack.append((child, depth + 1))
        return res

    return max(depth(ceo) for ceo in ceos)


solution()

# @code end
