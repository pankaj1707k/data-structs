""" Base algorithm of DEPTH FIRST SEARCH """

from collections import defaultdict

# Recursive: more memory consumption
def dfs(vertex:int):
    visited[vertex] = True
    # Operations on vertex just after entering it
    for child in graph[vertex]:
        if visited[child]: continue
        # Operations with child before visiting it
        dfs(child)
        # Operations with child after visiting it
    # Operations on vertex after visiting all children

# Graph input
n, e = map(int, input().split())    # number of vertices and edges
graph = defaultdict(list)           # adjacency list
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)
dfs(1)

"""
Iterative version of dfs:

def dfs():
    stack = [1]
    while stack:
        vertex = stack.pop()
        for child in graph[vertex]:
            if visited[child]: continue
            stack.append(child)
        visited[vertex] = True
"""