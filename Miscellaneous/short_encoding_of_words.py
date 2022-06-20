""" https://leetcode.com/problems/short-encoding-of-words/ """

from typing import *


class Solution:
    # Time: O(k*(n**2)); Space: O(n); n=len(words); k=len(word[i])
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)  # sort in decreasing order of length
        length = 0  # length of encoded string
        included = [False] * len(words)
        for i in range(len(words)):
            if not included[i]:
                included[i] = True
                length += len(words[i])
                for j in range(i + 1, len(words)):
                    if not included[j] and words[i].endswith(words[j]):
                        included[j] = True
                length += 1  # for '#' at end of word
        return length

    # Time: O(k*n); Space: O(n)
    def minimumLengthEncoding(self, words: List[str]) -> int:
        required = set(words)
        for word in words:
            # remove all suffixes of word
            for i in range(1, len(word)):
                required.discard(word[i:])
        return sum(len(word) + 1 for word in required)
