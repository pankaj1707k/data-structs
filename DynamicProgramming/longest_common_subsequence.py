""" https://leetcode.com/problems/longest-common-subsequence/ """

from typing import *


def longestCommonSubsequence(text1: str, text2: str) -> int:
    memo = [[-1] * 1005 for _ in range(1005)]

    def solve(i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        ans = solve(i - 1, j)
        ans = max(ans, solve(i, j - 1))
        ans = max(ans, solve(i - 1, j - 1) + (1 if text1[i] == text2[j] else 0))
        memo[i][j] = ans
        return ans

    return solve(len(text1) - 1, len(text2) - 1)
