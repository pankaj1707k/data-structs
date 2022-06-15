""" https://leetcode.com/problems/longest-string-chain/ """

from typing import *


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        memo = {}
        max_length = 1
        for word in words:
            memo[word] = 1
            for i in range(len(word)):
                # predecessor by removing i-th character
                pred = word[:i] + word[i + 1 :]
                if pred in memo:
                    memo[word] = max(memo[word], memo[pred] + 1)
                    max_length = max(max_length, memo[word])
        return max_length
