""" https://leetcode.com/problems/surrounded-regions/ """

from typing import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i: int, j: int) -> None:
            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[0])
                or visited[i][j]
                or board[i][j] == "X"
            ):
                return
            visited[i][j] = True
            board[i][j] = "Y"
            d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for k in d:
                dfs(i + k[0], j + k[1])

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        # Mark all regions connected to boundary as 'Y's
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0 or r == m - 1 or c == n - 1:
                    if not visited[r][c] and board[r][c] == "O":
                        dfs(r, c)

        # Mark all 'O's as 'X' and all 'Y's as 'O'
        for r in range(m):
            for c in range(n):
                if board[r][c] == "Y":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
