""" https://leetcode.com/problems/number-of-islands/ """

from typing import *


def numIslands(grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    visited = [[False for j in range(n)] for i in range(m)]

    def dfs(row: int, col: int):
        if row < 0 or row >= m or col < 0 or col >= n:
            return
        if grid[row][col] == "0":
            return
        if visited[row][col]:
            return
        visited[row][col] = True
        dfs(row - 1, col)
        dfs(row, col - 1)
        dfs(row + 1, col)
        dfs(row, col + 1)

    num_islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                if visited[i][j]:
                    continue
                dfs(i, j)
                num_islands += 1

    return num_islands


tests = [
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ],
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ],
]
for t in tests:
    print(numIslands(t))
