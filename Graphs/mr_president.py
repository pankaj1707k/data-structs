""" https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/mr-president/ """

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


n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

parent = [v for v in range(n + 1)]
size = [1] * (n + 1)

edges.sort()
total_weight = 0
min_weights = []
mn = 0
for edge in edges:
    if find(edge[1]) == find(edge[2]):
        continue
    union(edge[1], edge[2])
    total_weight += edge[0]
    min_weights.append(edge[0])
    mn += 1

p = find(1)
for v in range(1, n + 1):
    if find(v) != p:
        print("-1")
        exit(0)

min_weights.sort(reverse=True)
num_transform = 0
for i in range(mn):
    if total_weight <= k:
        break
    total_weight = total_weight - min_weights[i] + 1
    num_transform += 1

if total_weight > k:
    print("-1")
else:
    print(num_transform)
