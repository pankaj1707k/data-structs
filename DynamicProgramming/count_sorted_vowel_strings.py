""" https://leetcode.com/problems/count-sorted-vowel-strings/ """

from typing import *
from functools import cache


class Solution:
    @cache
    def solve(self, n: int, last_char: int) -> int:
        if n == 0:
            return 1
        ans = 0
        for i in range(last_char, 5):
            ans += self.solve(n - 1, i)
        return ans

    def countVowelStrings(self, n: int) -> int:
        ans = 0
        for i in range(5):
            ans += self.solve(n - 1, i)
        return ans
