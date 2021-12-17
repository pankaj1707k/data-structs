""" Given a tree, find the lowest common ancestor of two nodes """

from typing import *
from collections import defaultdict


def dfs(vertex: int, parent: int = -1):
    par[vertex] = parent
    for child in tree[vertex]:
        if child == parent:
            continue
        dfs(child, vertex)


def findLCA(v1: int, v2: int) -> int:
    path1 = []
    while v1 != -1:
        path1.append(v1)
        v1 = par[v1]
    path1.reverse()
    path2 = []
    while v2 != -1:
        path2.append(v2)
        v2 = par[v2]
    path2.reverse()

    min_len = min(len(path1), len(path2))
    lca = path1[0]
    for i in range(min_len):
        if path1[i] == path2[i]:
            lca = path1[i]
        else:
            break

    return lca


n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

par = defaultdict(int)
dfs(1)
v1, v2 = map(int, input().split())
lca = findLCA(v1, v2)
print(lca)
