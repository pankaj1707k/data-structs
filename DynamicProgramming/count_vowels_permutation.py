""" https://leetcode.com/problems/count-vowels-permutation/ """

from functools import cache
from typing import *


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        self.chars = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }
        result = 0
        for char in self.chars:
            result += self._count(n - 1, char) % 1_000_000_007
        return result % 1_000_000_007

    @cache
    def _count(self, n: int, last_char: str) -> int:
        if n == 0:
            return 1
        total_count = 0
        for char in self.chars[last_char]:
            total_count += self._count(n - 1, char) % 1_000_000_007
        return total_count % 1_000_000_007
