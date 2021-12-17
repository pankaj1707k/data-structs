""" https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/minimum-nodes-e023e51e/ """

import sys
from typing import *
from collections import defaultdict

sys.stdin = open("../../input.txt", "r")
sys.stdout = open("../../output.txt", "w")
input = sys.stdin.readline


def dfs(vertex: int, parent: int, s=0):
    s += values[vertex]
    level[vertex] = level[parent] + 1
    if s >= k:
        sums.append((s, vertex))
    for child in tree[vertex]:
        if child == parent:
            continue
        dfs(child, vertex, s)


n, q = map(int, input().split())
values = [0] + list(map(int, input().split()))
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

sums = []
level = [0] * (n + 1)
for _ in range(q):
    x, k = map(int, input().split())
    dfs(x, 0)
    min_lvl = n + 1
    for t in sums:
        if level[t[1]] < min_lvl:
            min_lvl = level[t[1]]
    if min_lvl == n + 1:
        print(-1)
    else:
        print(min_lvl)
    sums.clear()
    level = [0] * (n + 1)
