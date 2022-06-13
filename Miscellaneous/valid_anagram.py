""" https://leetcode.com/problems/valid-anagram/ """

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs = Counter(s)
        ft = Counter(t)
        return fs == ft
