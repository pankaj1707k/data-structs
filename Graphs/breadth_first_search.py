""" Base algorithm of BREADTH FIRST SEARCH """

from collections import defaultdict
from queue import Queue

# Time complexity: O(V+E), V=vertices, E=edges
def bfs(source: int):
    q = Queue()
    q.put(source)
    visited[source] = True

    while not q.empty():
        vertex = q.get()
        print(vertex)
        for child in graph[vertex]:
            if visited[child]:
                continue
            q.put(child)
            visited[child] = True


# Graph input
n, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
bfs(1)
