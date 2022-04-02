""" https://leetcode.com/problems/sudoku-solver/ """

from typing import *


def solve_sudoku(board: List[List[str]]) -> None:
    def is_valid(n: str, i: int, j: int) -> bool:
        # check row
        for c in range(9):
            if c == j:
                continue
            if board[i][c] == n:
                return False

        # check column
        for r in range(9):
            if r == i:
                continue
            if board[r][j] == n:
                return False

        # check box
        row = (i // 3) * 3
        col = (j // 3) * 3
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if r == i and c == j:
                    continue
                if board[r][c] == n:
                    return False

        return True

    def find_empty_cell() -> Tuple[int, int]:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return (i, j)

    def solver() -> bool:
        pos = find_empty_cell()
        # Sudoku is solved if no empty cell is left
        if not pos:
            return True
        # Check for each value from 1 to 9
        for n in range(1, 10):
            if is_valid(f"{n}", pos[0], pos[1]):
                board[pos[0]][pos[1]] = f"{n}"
                if solver():
                    return True
                board[pos[0]][pos[1]] = "."
        return False

    solver()
