""" https://leetcode.com/problems/set-matrix-zeroes/ """

from typing import *


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = False  # marks if first column should be set to 0
        # matrix[0][0] marks if the first row should be set to 0
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col = True
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Leave first row and first column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row to 0
        if matrix[0][0] == 0:
            for j in range(1, len(matrix[0])):
                matrix[0][j] = 0

        # Set first column to 0
        if col:
            for i in range(1, len(matrix)):
                matrix[i][0] = 0
