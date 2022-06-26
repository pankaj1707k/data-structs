""" https://leetcode.com/problems/wildcard-matching/ """

from functools import cache
from typing import *


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def match(i: int, j: int) -> bool:
            # Base cases
            if i == len(s) - 1 and j == len(p) - 1:
                return s[i] == p[j] or p[j] == "?" or p[j] == "*"
            if i == len(s):
                while j < len(p) and p[j] == "*":
                    j += 1
                return j == len(p)
            if i == len(s) or j == len(p):
                return False

            # Recursive cases
            if p[j] in {s[i], "?"}:
                # match exactly one character
                return match(i + 1, j + 1)
            if p[j] == "*":
                # match either empty string or at least one character from s
                return match(i, j + 1) or match(i + 1, j)
            return False

        return match(0, 0)
