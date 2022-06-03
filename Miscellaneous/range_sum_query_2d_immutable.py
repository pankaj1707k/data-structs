""" https://leetcode.com/problems/range-sum-query-2d-immutable/ """

from typing import *

# O(m) time per query, O(mn) space
# class NumMatrix:
#     def __init__(self, matrix: List[List[int]]):
#         self.rows = len(matrix)
#         self.cols = len(matrix[0])
#         self.prefix = []
#         for i in range(self.rows):
#             prefix_row = [matrix[i][0]]
#             for j in range(1, self.cols):
#                 prefix_row.append(prefix_row[-1] + matrix[i][j])
#             self.prefix.append(prefix_row)

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         result = 0
#         for i in range(row1, row2 + 1):
#             result += self.prefix[i][col2] - (
#                 self.prefix[i][col1 - 1] if col1 > 0 else 0
#             )
#         return result

# O(1) time per query, O(mn) space
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.prefix = [[0] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.prefix[i][j] = (
                    matrix[i][j]
                    + (self.prefix[i][j - 1] if j > 0 else 0)
                    + (self.prefix[i - 1][j] if i > 0 else 0)
                    - (self.prefix[i - 1][j - 1] if i > 0 and j > 0 else 0)
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2][col2]
            - (self.prefix[row1 - 1][col2] if row1 > 0 else 0)
            - (self.prefix[row2][col1 - 1] if col1 > 0 else 0)
            + (self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0)
        )
