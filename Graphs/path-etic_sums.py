""" https://www.codechef.com/problems/PATHSUMS """

import sys
from collections import defaultdict

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def dfs(vertex: int, parent: int):
    if parent == 0 or values[parent] == 2:
        values[vertex] = 1
    else:
        values[vertex] = 2
    for child in tree[vertex]:
        if child == parent:
            continue
        dfs(child, vertex)


t = int(input())
for _ in range(t):
    n = int(input())
    tree = defaultdict(list)
    for __ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    values = [0] * (n + 1)
    dfs(1, 0)
    print(" ".join(map(str, values))[2:])
