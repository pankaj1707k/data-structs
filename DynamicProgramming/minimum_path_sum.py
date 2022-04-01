""" https://leetcode.com/problems/minimum-path-sum/ """

from typing import *
from functools import cache


def min_path_sum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    @cache
    def solve(i: int, j: int) -> int:
        if i == 0 and j == 0:
            return grid[i][j]
        if j == 0:
            return grid[i][j] + solve(i - 1, j)
        if i == 0:
            return grid[i][j] + solve(i, j - 1)
        return grid[i][j] + min(solve(i, j - 1), solve(i - 1, j))

    return solve(m - 1, n - 1)
