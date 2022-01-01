""" https://leetcode.com/problems/network-delay-time/ """

from typing import *
from collections import defaultdict
from queue import PriorityQueue


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for time in times:
        u, v, w = time
        graph[u].append((v, w))

    # Dijkstra's algorithm
    source = k
    visited = [False] * (n + 1)
    INF = 10 ** 9
    distance = [INF] * (n + 1)
    distance[source] = 0
    pq = PriorityQueue()
    pq.put((0, source))

    while not pq.empty():
        d, v = pq.get()
        if visited[v]:
            continue
        visited[v] = True
        for child in graph[v]:
            child_v, weight = child
            if d + weight < distance[child_v]:
                distance[child_v] = d + weight
                pq.put((distance[child_v], child_v))
    # Dijkstra's algorithm end

    ans = max(distance[1:])
    if ans == INF:
        return -1
    return ans


print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(networkDelayTime([[1, 2, 1]], 2, 1))
print(networkDelayTime([[1, 2, 1]], 2, 2))
