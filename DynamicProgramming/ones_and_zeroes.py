""" https://leetcode.com/problems/ones-and-zeroes/ """

from typing import *
from functools import cache
from collections import Counter


class Solution:
    @cache
    def solve(self, i: int, m: int, n: int) -> int:
        if m < 0 or n < 0:
            return 0
        if i < 0:
            return 0
        return max(
            1 + self.solve(i - 1, m - self.strs[i]["0"], n - self.strs[i]["1"]),
            self.solve(i - 1, m, n),
        )

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.strs = [Counter(s) for s in strs]
        return self.solve(len(strs) - 1, m, n)
