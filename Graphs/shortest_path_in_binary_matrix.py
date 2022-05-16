""" https://leetcode.com/problems/shortest-path-in-binary-matrix/ """

from typing import *
from queue import Queue


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[0][0] == 1 or grid[n][n] == 1:
            return -1
        q = Queue()
        q.put([0, 0])
        grid[0][0] = 1
        dirs = [[1, 1], [0, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

        while not q.empty():
            i, j = q.get()
            if i == n and j == n:
                return grid[i][j]
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if x >= 0 and y >= 0 and x <= n and y <= n and grid[x][y] == 0:
                    grid[x][y] = grid[i][j] + 1
                    q.put([x, y])

        return grid[n][n] if grid[n][n] > 0 else -1
