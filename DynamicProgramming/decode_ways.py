""" https://leetcode.com/problems/decode-ways/ """

from functools import cache
from typing import *


class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def count(i: int) -> int:
            # string with leading zero is invalid
            if i < len(s) and s[i] == "0":
                return 0
            if i >= len(s) - 1:
                return 1
            # combining 2 adjacent digits results in num >26 (invalid code)
            if i < len(s) - 1 and int(s[i] + s[i + 1]) > 26:
                return count(i + 1)
            return count(i + 1) + count(i + 2)

        return count(0)
