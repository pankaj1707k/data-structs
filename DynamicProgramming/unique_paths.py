""" https://leetcode.com/problems/unique-paths/ """

from typing import *
from functools import cache


class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        ans = 0
        x, y = m - 1, n
        if x >= 1 and y >= 1 and x <= m and y <= n:
            ans += self.uniquePaths(x, y)
        x, y = m, n - 1
        if x >= 1 and y >= 1 and x <= m and y <= n:
            ans += self.uniquePaths(x, y)
        return ans
