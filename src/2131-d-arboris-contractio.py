# Created by Ayush Biswas at 2025/08/10 20:40
# https://codeforces.com/contest/2131/problem/D
from cpio.cpio import sol_n

# @code begin


@sol_n("n; (n-1)*ints")
def solution(n: int, edges: list[list[int]]) -> int:
    graph = [[] for _ in range(n + 1)]
    deg = [0 for _ in range(n + 1)]
    for [a, b] in edges:
        graph[a].append(b)
        graph[b].append(a)
        deg[a] += 1
        deg[b] += 1

    total_leaves = min(sum(1 for d in deg if d == 1), n - 1)
    res = 10**9
    for i in range(1, n + 1):
        neighbor_leaves = 0
        for neighbor in graph[i]:
            if deg[neighbor] == 1:
                neighbor_leaves += 1
        res = min(res, total_leaves - neighbor_leaves)

    return res


solution()

# @code end
