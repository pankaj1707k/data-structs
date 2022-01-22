""" Given a undirected weighted graph, find its minimium spanning tree """

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def find(v: int) -> int:
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]


def union(u: int, v: int):
    a = find(u)
    b = find(v)
    if a == b:
        return
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]


n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

parent = {}
size = {}
for v in range(1, n + 1):
    parent[v] = v
    size[v] = 1

edges.sort()
total_weight = 0
for edge in edges:
    w, u, v = edge
    if find(u) == find(v):
        continue
    union(u, v)
    total_weight += w
    print(u, v, w)

print(total_weight)
