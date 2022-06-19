""" https://leetcode.com/problems/spiral-matrix/ """

from typing import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top = left = 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
