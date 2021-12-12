""" https://leetcode.com/problems/island-perimeter/ """

from typing import List

def islandPerimeter(grid: List[List[int]])->int:
    m = len(grid)
    n = len(grid[0])
    visited = [[False for __ in range(n)] for _ in range(m)]

    def dfs(row:int, col:int)->int:
        if row<0 or col<0 or row>=m or col>=n: return 1
        if grid[row][col]==0: return 1
        if visited[row][col]: return 0
        visited[row][col] = True
        return dfs(row-1,col) + dfs(row,col-1) + dfs(row+1,col) + dfs(row,col+1)

    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                return dfs(i,j)

tests = [
    [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]],
    [[1]],
    [[1,0]]
]
for t in tests:
    print(islandPerimeter(t))