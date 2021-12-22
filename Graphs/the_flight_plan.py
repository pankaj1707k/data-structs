""" https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/traffic-light-2-ee27ba45/ """

import sys
from typing import *
from queue import Queue
from collections import defaultdict

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def bfs(source: int):
    q = Queue()
    q.put(source)
    parent[source] = 0
    vis[source] = True
    while not q.empty():
        v = q.get()
        for child in routes[v]:
            if vis[child]:
                continue
            q.put(child)
            parent[child] = v
            vis[child] = True


n, m, t, c = map(int, input().split())
routes = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    routes[u].append(v)
    routes[v].append(u)
x, y = map(int, input().split())
for v in range(1, n + 1):
    routes[v] = sorted(routes[v])
path = []
parent = [0] * (n + 1)
vis = [False] * (n + 1)
bfs(x)
k = 0
while y != 0:
    k += 1
    path.append(y)
    y = parent[y]
print(k)
print(" ".join(map(str, path[::-1])))
