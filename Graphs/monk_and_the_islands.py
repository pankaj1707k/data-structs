""" https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/monk-and-the-islands/ """

import sys
from typing import *
from queue import Queue
from collections import defaultdict

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def bfs(source: int):
    q = Queue()
    q.put(source)
    vis[source] = True
    while not q.empty():
        vertex = q.get()
        for child in graph[vertex]:
            if not vis[child]:
                lvl[child] = lvl[vertex] + 1
                vis[child] = True
                q.put(child)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for __ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    vis = [False] * (n + 1)
    lvl = [0] * (n + 1)
    bfs(1)
    print(lvl[n])
