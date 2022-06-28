""" https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/ """

from collections import Counter
from typing import *


class Solution:
    def minDeletions(self, s: str) -> int:
        d = Counter(s)
        freq = {}  # map frequency to character
        deletions = 0
        for char in d:
            # decrease the frequency until it reaches a value
            # which does not exist in `freq`
            while d[char] in freq:
                d[char] -= 1
                deletions += 1
            # add the decreased frequency only if it is not 0
            if d[char] != 0:
                freq[d[char]] = char

        return deletions
