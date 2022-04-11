""" https://leetcode.com/problems/shift-2d-grid/ """

from typing import *


def shift_grid(grid: List[List[int]], k: int) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    arr = [grid[i][j] for i in range(m) for j in range(n)]
    for _ in range(k):
        last = arr[-1]
        for i in range(m * n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last
    grid = []
    for i in range(m):
        row = [arr[j] for j in range(i * n, i * n + n)]
        grid.append(row)
    return grid
