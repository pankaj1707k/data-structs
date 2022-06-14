""" https://leetcode.com/problems/delete-operation-for-two-strings/ """

from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def lcs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            ans = lcs(i - 1, j - 1) + int(word1[i] == word2[j])
            ans = max(ans, lcs(i - 1, j))
            ans = max(ans, lcs(i, j - 1))
            return ans

        return len(word1) + len(word2) - 2 * lcs(len(word1) - 1, len(word2) - 1)
