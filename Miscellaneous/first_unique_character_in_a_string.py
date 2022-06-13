""" https://leetcode.com/problems/first-unique-character-in-a-string/ """

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for index, char in enumerate(s):
            if freq[char] == 1:
                return index
        return -1
