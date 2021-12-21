""" https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/strange-matrix-8b96f2ab/ """

import sys
from typing import *

sys.stdin = open("../../input.txt", "r")
sys.stdout = open("../../output.txt", "w")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(i: int, j: int) -> bool:
    # Recursive code ran out of stack memory
    # if i == N - 1 and j == M - 1:
    #     return True
    # vis[i][j] = True
    # for move in moves:
    #     x = i + move[0]
    #     y = j + move[1]
    #     if x < 0 or y < 0 or x >= N or y >= M or vis[x][y] or mtrx[x][y] != mtrx[0][0]:
    #         continue
    #     if dfs(x, y):
    #         return True
    # return False
    stack = [(0, 0)]
    while stack:
        i, j = stack.pop()
        if i == N - 1 and j == M - 1:
            return True
        for move in moves:
            x = i + move[0]
            y = j + move[1]
            if (
                x < 0
                or y < 0
                or x >= N
                or y >= M
                or vis[x][y]
                or mtrx[x][y] != mtrx[0][0]
            ):
                continue
            stack.append((x, y))
            vis[x][y] = True
    return False


def validPath(k: int) -> bool:
    for i in range(N):
        for j in range(M):
            mtrx[i][j] = min(matrix[i][j] + k, C)
            vis[i][j] = False
    return dfs(0, 0)


N, M, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
vis = [[False] * M for _ in range(N)]
l = 0
h = C
ans = None
mid = None
while l <= h:
    mid = (l + h) // 2
    mtrx = [[0] * M for _ in range(N)]
    if validPath(mid):
        ans = mid
        h = mid - 1
    else:
        l = mid + 1

print(ans)
