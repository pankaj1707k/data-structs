""" https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/approximate/jp-and-the-escape-planapprox/ """

import sys
from typing import *

sys.stdin = open("../../input.txt", "r")
sys.stdout = open("../../output.txt", "w")
input = sys.stdin.readline


def dfs(i: int, j: int) -> bool:
    if i == 0 or i == N - 1 or j == 0 or j == M - 1:
        return True
    vis[i][j] = True
    for move in moves:
        r, c = i + move[0], j + move[1]
        if (
            vis[r][c]
            or grid[r][c] > grid[dx - 1][dy - 1]
            or grid[r][c] < grid[i][j] - J
        ):
            continue
        path.append((r + 1, c + 1))
        if dfs(r, c):
            return True
        path.pop()
    return False


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dx, dy, J = map(int, input().split())

path = [(dx, dy)]  # stack to store the path
vis = [[False for __ in range(M)] for _ in range(N)]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
if dfs(dx - 1, dy - 1):
    print("YES")
    print(len(path))
    for p in path:
        print(p[0], p[1])
else:
    print("NO")
