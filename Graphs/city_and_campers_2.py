""" https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/city-and-campers-2/ """

import sys
from heapq import *
from collections import defaultdict

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def find(v: int) -> int:
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]


def merge(a: int, b: int):
    freq[size[a]] -= 1
    if freq[size[a]] == 0:
        size_sorted.remove(size[a])

    freq[size[b]] -= 1
    if freq[size[b]] == 0:
        size_sorted.remove(size[b])

    freq[size[a] + size[b]] += 1
    if freq[size[a] + size[b]] == 1:
        heappush(size_sorted, size[a] + size[b])


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
parent = {i: i for i in range(1, n + 1)}
size = {i: 1 for i in range(1, n + 1)}
freq = defaultdict(int)
freq[1] = n
size_sorted = [1]
heapify(size_sorted)

for _ in range(q):
    u, v = map(int, input().split())
    union(u, v)

    size_sorted_copy = size_sorted.copy()
    previous = -1
    min_diff = n + 1
    while size_sorted_copy:
        current = heappop(size_sorted_copy)
        if freq[current] > 1:
            min_diff = 0
            break
        if previous != -1:
            min_diff = min(min_diff, current - previous)
        previous = current

    if min_diff == n + 1:
        min_diff = 0
    print(min_diff)
