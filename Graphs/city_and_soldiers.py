""" https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/city-and-soldiers/ """

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def find(v: int) -> int:
    if v == parent[v]:
        return v
    parent[v] = find(parent[v])
    return parent[v]


def union(u: int, v: int):
    a = find(u)
    b = find(v)
    if a == b:
        return
    parent[a] = b


n, q = map(int, input().split())
parent = {i: i for i in range(1, n + 1)}

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        union(query[1], query[2])
    elif query[0] == 2:
        a = query[1]
        p = find(a)
        if a != p:
            parent[p] = a
            parent[a] = a
    else:
        print(find(query[1]))
