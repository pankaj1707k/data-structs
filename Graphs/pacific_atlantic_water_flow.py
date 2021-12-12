""" https://leetcode.com/problems/pacific-atlantic-water-flow/ """

from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    m = len(heights)
    n = len(heights[0])
    pacific = [[False for __ in range(n)] for _ in range(m)]
    atlantic = [[False for __ in range(n)] for _ in range(m)]

    def dfs(row: int, col: int, prevHeight: int, visited: List[List[bool]]):
        if (
            row < 0
            or col < 0
            or row >= m
            or col >= n
            or visited[row][col]
            or prevHeight > heights[row][col]
        ):
            return
        visited[row][col] = True
        dfs(row - 1, col, heights[row][col], visited)
        dfs(row, col - 1, heights[row][col], visited)
        dfs(row + 1, col, heights[row][col], visited)
        dfs(row, col + 1, heights[row][col], visited)

    for i in range(m):
        dfs(i, 0, -1, pacific)
        dfs(i, n - 1, -1, atlantic)
    for j in range(n):
        dfs(0, j, -1, pacific)
        dfs(m - 1, j, -1, atlantic)

    result = []

    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])

    return result


tests = [
    [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ],
    [[2, 1], [1, 2]],
]
for t in tests:
    print(pacificAtlantic(t))
