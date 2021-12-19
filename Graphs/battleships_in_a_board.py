""" https://leetcode.com/problems/battleships-in-a-board/ """

from typing import *


def countBattleships(board: List[List[str]]) -> int:
    m = len(board)
    n = len(board[0])

    def dfs(r: int, c: int):
        if r < 0 or c < 0 or r >= m or c >= n or vis[r][c] or board[r][c] == ".":
            return
        vis[r][c] = True
        for move in moves:
            dfs(r + move[0], c + move[1])

    vis = [[False] * n for _ in range(m)]
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    battleships = 0
    for i in range(m):
        for j in range(n):
            if not vis[i][j] and board[i][j] == "X":
                dfs(i, j)
                battleships += 1

    return battleships
