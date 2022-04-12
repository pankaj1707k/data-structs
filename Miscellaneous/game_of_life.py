""" https://leetcode.com/problems/game-of-life/ """

from typing import *


def game_of_life(board: List[List[int]]) -> None:
    m = len(board)
    n = len(board[0])
    original = [[board[i][j] for j in range(n)] for i in range(m)]

    def is_valid(i: int, j: int) -> bool:
        return i >= 0 and j >= 0 and i < m and j < n

    def live_neighbor_count(r: int, c: int) -> int:
        live_count = 0
        dr = [0, 0, 1, 1, 1, -1, -1, -1]
        dc = [1, -1, 0, 1, -1, 0, 1, -1]
        for k in range(8):
            if is_valid(r + dr[k], c + dc[k]) and original[r + dr[k]][c + dc[k]]:
                live_count += 1

        return live_count

    for i in range(m):
        for j in range(n):
            live_neighbors = live_neighbor_count(i, j)
            if original[i][j]:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = 0
            else:
                if live_neighbors == 3:
                    board[i][j] = 1
