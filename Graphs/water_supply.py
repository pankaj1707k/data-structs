""" https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/water-flow-4-38cea6c6/ """

import sys
from collections import defaultdict
from typing import *

sys.stdin = open("../../input.txt", "r")
sys.stdout = open("../../output.txt", "w")
input = sys.stdin.readline


def dfs(vertex: int):
    global count
    count += 1
    if blockages[vertex]:
        return
    visited[vertex] = True
    for child in graph[vertex]:
        if visited[child]:
            continue
        dfs(child)


n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

blockages = [0] + list(map(int, input().split()))
count = result = 0
visited = [False] * (n + 1)
for v in range(1, n + 1):
    if visited[v]:
        continue
    result = max(result, count)
    count = 0
    dfs(v)

print(result)
