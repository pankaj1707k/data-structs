""" https://leetcode.com/problems/longest-increasing-path-in-a-matrix/ """

from typing import *
from functools import cache


class Solution:
    def is_valid(self, i: int, j: int) -> bool:
        return i >= 0 and j >= 0 and i < self.m and j < self.n

    @cache
    def dfs(self, i: int, j: int) -> int:
        max_len = 0
        for d in self.dirs:
            x, y = i + d[0], j + d[1]
            if self.is_valid(x, y) and self.matrix[x][y] > self.matrix[i][j]:
                max_len = max(max_len, self.dfs(x, y))
        return max_len + 1

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        max_len = 0
        for i in range(self.m):
            for j in range(self.n):
                max_len = max(max_len, self.dfs(i, j))
        return max_len
