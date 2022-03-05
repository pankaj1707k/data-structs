""" https://leetcode.com/problems/01-matrix/ """

from typing import *


def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])

    distance = [[10000009] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                distance[i][j] = 0
                continue
            if i > 0:
                distance[i][j] = min(distance[i - 1][j] + 1, distance[i][j])
            if j > 0:
                distance[i][j] = min(distance[i][j - 1] + 1, distance[i][j])

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if mat[i][j] != 0:
                if i + 1 < m:
                    distance[i][j] = min(distance[i + 1][j] + 1, distance[i][j])
                if j + 1 < n:
                    distance[i][j] = min(distance[i][j + 1] + 1, distance[i][j])

    return distance
