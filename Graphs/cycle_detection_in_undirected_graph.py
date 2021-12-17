from collections import defaultdict
from typing import *


def dfs(vertex: int, parent: int) -> bool:
    visited[vertex] = True
    cycle_exist = False
    for child in graph[vertex]:
        if visited[child]:
            if child == parent:
                continue
            return True  # if child is visited and is not the parent of vertex => cycle found
        cycle_exist = cycle_exist or dfs(child, vertex)
    return cycle_exist


# graph input
n, e = map(int, input().split())
graph = defaultdict(list)
visited = defaultdict(bool)
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for v in range(1, n + 1):
    if visited[v]:
        continue
    if dfs(v, 0):
        print("TRUE")
        break
else:
    print("FALSE")
