""" https://leetcode.com/problems/longest-palindromic-substring/ """

from collections import defaultdict
from typing import *


# bottom-up dp approach
def longest_palindrome(s: str) -> str:
    n = len(s)
    dp = defaultdict(bool)
    start = 0
    end = 0

    for j in range(n):
        for i in range(j + 1):
            if i == j:
                dp[(i, j)] = True
            elif i + 1 == j:
                dp[(i, j)] = s[i] == s[j]
            else:
                dp[(i, j)] = (s[i] == s[j]) and dp[(i + 1, j - 1)]

            if dp[(i, j)] and j - i + 1 > end - start + 1:
                start = i
                end = j

    return s[start : end + 1]


# Improved space complexity
def longest_palindrome_2(s: str) -> str:
    n = len(s)
    dp = [None for i in range(n)]
    max_len = 0
    lps = ""

    for j in range(n):
        for i in range(j + 1):
            if i == j:
                dp[i] = True
            elif j == i + 1:
                dp[i] = s[i] == s[j]
            else:
                dp[i] = dp[i + 1] and s[i] == s[j]

            if dp[i] and j - i + 1 > max_len:
                max_len = j - i + 1
                lps = s[i : j + 1]

    return lps


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = end = 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i + 1)
            maxlen = max(len1, len2)
            if maxlen > end - start:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2

        return s[start : end + 1]

    def expand(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
