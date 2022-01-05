""" https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/ """

from collections import defaultdict
from typing import *


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    INF = 10 ** 9
    d = [[INF for __ in range(n)] for _ in range(n)]
    for i in range(n):
        d[i][i] = 0

    for edge in edges:
        d[edge[0]][edge[1]] = edge[2]
        d[edge[1]][edge[0]] = edge[2]

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    ans = [0] * n
    for i in range(n):
        for j in range(n):
            if d[i][j] <= distanceThreshold:
                ans[i] += 1

    min_cities = min(ans)
    for i in range(n - 1, -1, -1):
        if ans[i] == min_cities:
            return i
