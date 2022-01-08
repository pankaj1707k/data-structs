""" https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/city-and-flood-1/ """

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def make(v: int):
    parent[v] = v
    size[v] = 1


def find(v: int) -> int:
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])  # path compression
    return parent[v]


def union(u: int, v: int):
    a = find(u)
    b = find(v)
    if a == b:
        return
    if size[a] < size[b]:  # Merge smaller into larger
        a, b = b, a
    parent[b] = a
    size[a] += size[b]


n = int(input())
k = int(input())
parent = {}
size = {}
for i in range(1, n + 1):
    make(i)

for _ in range(k):
    u, v = map(int, input().split())
    union(u, v)

ans = 0
for i in range(1, n + 1):
    if parent[i] == i:
        ans += 1

print(ans)
