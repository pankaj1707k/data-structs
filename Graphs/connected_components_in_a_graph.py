""" https://www.hackerearth.com/problem/algorithm/connected-components-in-a-graph/ """

from collections import defaultdict
from typing import *

def dfs(vertex:int):
    visited[vertex] = True
    for child in graph[vertex]:
        if visited[child]:
            continue
        dfs(child)

# graph input
n, e = map(int, input().split())
graph = defaultdict(list)
visited = defaultdict(bool)
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# find number of connected components
connected_count = 0
for v in range(1,n+1):
    if visited[v]:
        continue
    dfs(v)      # component rooted at v is completely traversed
    connected_count += 1

print(connected_count)