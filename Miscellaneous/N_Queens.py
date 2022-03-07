""" https://leetcode.com/problems/n-queens/ """

from typing import *


def n_queens(n: int) -> List[List[str]]:
    board = [["."] * n for _ in range(n)]
    columns = set()
    positive_diagonals = set()
    negative_diagonals = set()
    result = []

    def solve(r: int):
        if r == n:
            board_copy = ["".join(row) for row in board]
            result.append(board_copy)
            return

        for c in range(n):
            if (
                (c in columns)
                or (r + c in positive_diagonals)
                or (r - c in negative_diagonals)
            ):
                continue

            board[r][c] = "Q"
            columns.add(c)
            positive_diagonals.add(r + c)
            negative_diagonals.add(r - c)

            solve(r + 1)

            board[r][c] = "."
            columns.remove(c)
            positive_diagonals.remove(r + c)
            negative_diagonals.remove(r - c)

    solve(0)
    return result
