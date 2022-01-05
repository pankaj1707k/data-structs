""" https://leetcode.com/problems/path-with-maximum-probability/ """

from typing import *
from collections import defaultdict
from queue import PriorityQueue
from math import log, exp


def maxProbability(
    n: int, edges: List[List[int]], succProb: List[float], start: int, end: int
) -> float:
    graph = defaultdict(list)
    m = len(edges)
    for i in range(m):
        graph[edges[i][0]].append((edges[i][1], (-1) * log(succProb[i])))
        graph[edges[i][1]].append((edges[i][0], (-1) * log(succProb[i])))

    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, start))
    INF = 10 ** 9
    dist = [INF] * n
    dist[start] = 0

    while not pq.empty():
        d, v = pq.get()
        if visited[v]:
            continue
        visited[v] = True
        for child in graph[v]:
            cv, wt = child
            if d + wt < dist[cv]:
                dist[cv] = d + wt
                pq.put((dist[cv], cv))

    if dist[end] == INF:
        return 0
    return exp((-1) * dist[end])
