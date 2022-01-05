""" https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/zero-path-a7d370fd/ """

import sys

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    degree = [0] * (n + 1)
    for __ in range(n - 1):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1
    w = [0] + list(map(int, input().split()))
    num_of_ops = 0
    for v in range(1, n + 1):
        if degree[v] > 1 and w[v] != 0:
            num_of_ops += 1
    print(num_of_ops)
