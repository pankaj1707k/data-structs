""" https://leetcode.com/problems/regular-expression-matching/ """

from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def match(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)
            curr_match = i < len(s) and (p[j] == "." or p[j] == s[i])
            if j + 1 < len(p) and p[j + 1] == "*":
                # Match zero characters or match at least one character for *
                return match(i, j + 2) or (curr_match and match(i + 1, j))
            return curr_match and match(i + 1, j + 1)

        return match(0, 0)
