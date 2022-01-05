""" https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/areas-0475fb6e/ """

import sys
from typing import List, Tuple

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline


def dfs(i: int, j: int, visited: List[List[bool]]) -> int:
    if i < 0 or j < 0 or i >= r or j >= c:
        return 0
    if grid[i][j] == "#":
        return 0
    if visited[i][j]:
        return 0
    visited[i][j] = True
    return (
        1
        + dfs(i - 1, j, visited)
        + dfs(i + 1, j, visited)
        + dfs(i, j - 1, visited)
        + dfs(i, j + 1, visited)
    )


def solve(rows: int, cols: int) -> Tuple[List[int], int]:
    visited = [[False for __ in range(cols)] for _ in range(rows)]
    areas = []
    num = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "." and not visited[i][j]:
                areas.append(dfs(i, j, visited))
                num += 1

    return areas, num


grid = []
t = int(input())
r = c = 0
for _ in range(t):
    r, c = map(int, input().split())
    for i in range(r):
        grid.append(list(input()))
    ans, n = solve(r, c)
    print(n)
    for a in ans:
        print(a, end=" ")
    grid.clear()
    print()
