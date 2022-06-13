""" https://leetcode.com/problems/triangle/ """

from typing import *
from functools import cache


class Solution:
    @cache
    def solve(self, i: int, j: int) -> int:
        if i == len(self.triangle):
            return 0
        return self.triangle[i][j] + min(self.solve(i + 1, j), self.solve(i + 1, j + 1))

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        return self.solve(0, 0)
