""" https://leetcode.com/problems/unique-paths-ii/ """

from typing import *
from functools import cache


class Solution:
    def in_bounds(self, i: int, j: int) -> bool:
        return i >= 0 and j >= 0 and i < len(self.grid) and j < len(self.grid[0])

    @cache
    def dfs(self, i: int, j: int) -> int:
        if i == 0 and j == 0:
            return 1
        path_count = 0
        if self.in_bounds(i - 1, j) and self.grid[i - 1][j] == 0:
            path_count += self.dfs(i - 1, j)
        if self.in_bounds(i, j - 1) and self.grid[i][j - 1] == 0:
            path_count += self.dfs(i, j - 1)
        return path_count

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.grid = obstacleGrid
        if self.grid[len(self.grid) - 1][len(self.grid[0]) - 1] == 1:
            return 0
        if self.grid[0][0] == 1:
            return 0
        return self.dfs(len(self.grid) - 1, len(self.grid[0]) - 1)
