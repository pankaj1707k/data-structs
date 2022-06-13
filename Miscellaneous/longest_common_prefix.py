""" https://leetcode.com/problems/longest-common-prefix/ """

from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 209
        for s in strs:
            min_length = min(min_length, len(s))

        # Check index i in all strings
        # If all strings have the same character at index i,
        # add that character to the result
        # return the result on first difference
        result = ""
        for i in range(min_length):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return result
            result += char
        return result
