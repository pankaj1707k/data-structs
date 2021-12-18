""" https://www.codechef.com/problems/FIRESC """

import sys
from collections import defaultdict

MOD = 10 ** 9 + 7
sys.stdin = open("../../input.txt", "r")
sys.stdout = open("../../output.txt", "w")
input = sys.stdin.readline


def dfs(vertex: int):
    vis[vertex] = True
    global num_vertices
    num_vertices += 1
    for child in graph[vertex]:
        if vis[child]:
            continue
        dfs(child)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for __ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    vis = [False] * (N + 1)
    num_of_routes = 0
    captain_ways = 1
    for v in range(1, N + 1):
        if not vis[v]:
            num_vertices = 0
            dfs(v)
            num_of_routes += 1
            captain_ways = ((captain_ways % MOD) * (num_vertices % MOD)) % MOD
    print(num_of_routes, captain_ways)
