""" https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/city-and-campers/ """

import sys
from heapq import *
from sortedcontainers import SortedList

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def find(v: int) -> int:
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])  # path compression
    return parent[v]


def merge(a: int, b: int):
    size_sorted.remove(size[b])
    size_sorted.remove(size[a])
    size_sorted.add(size[a] + size[b])


def union(u: int, v: int):
    a = find(u)
    b = find(v)
    if a == b:
        return
    if size[a] < size[b]:  # Merge smaller into larger
        a, b = b, a
    parent[b] = a
    merge(a, b)
    size[a] += size[b]


n, q = map(int, input().split())
parent = {}
size = {i: 1 for i in range(1, n + 1)}
size_sorted = SortedList([1] * n)

for i in range(1, n + 1):
    parent[i] = i

for _ in range(q):
    u, v = map(int, input().split())
    if len(size_sorted) == 1:
        print("0")
    union(u, v)
    print(size_sorted[-1] - size_sorted[0])
