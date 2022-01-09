""" https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/city-and-fireman-vincent/ """

import sys
from collections import defaultdict

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
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    del size[b]
    min_risk[a] = min(min_risk[a], min_risk[b])
    del min_risk[b]


n = int(input())
e = [0] + list(map(int, input().split()))
k = int(input())

MOD = 10 ** 9 + 7

parent = {i: i for i in range(1, n + 1)}
size = {i: 1 for i in range(1, n + 1)}
min_risk = {i: e[i] for i in range(1, n + 1)}
min_risk_freq = defaultdict(int)

for _ in range(k):
    x, y = map(int, input().split())
    union(x, y)

for v in range(1, n + 1):
    r = find(v)
    if min_risk[r] == e[v]:
        min_risk_freq[r] += 1

ans = 1
for i in range(1, n + 1):
    if i == parent[i]:
        ans *= min_risk_freq[i]

print(ans % MOD)
