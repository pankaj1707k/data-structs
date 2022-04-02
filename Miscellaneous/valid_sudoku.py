""" https://leetcode.com/problems/valid-sudoku/ """

from typing import *


def is_valid_sudoku(board: List[List[int]]) -> bool:
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue

            # check row
            for k in range(9):
                if k == j:
                    continue
                if board[i][k] == board[i][j]:
                    return False

            # check column
            for k in range(9):
                if k == i:
                    continue
                if board[k][j] == board[i][j]:
                    return False

            # check 3x3 box
            row = (i // 3) * 3
            col = (j // 3) * 3
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if r == i and c == j:
                        continue
                    if board[r][c] == board[i][j]:
                        return False

    return True
