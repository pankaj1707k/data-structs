""" https://leetcode.com/problems/word-search/ """

from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.word = word
        self.visited = [[False] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                # search for word starting from board[i][j]
                if self.search(i, j, 0):
                    return True
        return False

    def search(self, row: int, col: int, index: int) -> bool:
        # index out of bounds
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        # character either visited or does not match char at curr index
        if self.visited[row][col] or self.board[row][col] != self.word[index]:
            return False
        # character matched and is the last character of word
        if index == len(self.word) - 1:
            return True
        self.visited[row][col] = True  # mark current cell as visited
        # search for next character in all 4 directions
        res = (
            self.search(row + 1, col, index + 1)
            or self.search(row - 1, col, index + 1)
            or self.search(row, col + 1, index + 1)
            or self.search(row, col - 1, index + 1)
        )
        self.visited[row][col] = False  # backtracking step
        return res
