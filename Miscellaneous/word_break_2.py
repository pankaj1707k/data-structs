""" https://leetcode.com/problems/word-break-ii/ """

from typing import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)  # for constant time lookup
        result = []

        def generate_sentence(s: str, sentence: List[str]) -> None:
            if s == "":  # valid sentence formed
                result.append(" ".join(sentence))
                return
            # for each prefix of s (starting from index 0)
            # check if it exists in wordDict
            # if yes, recursively generate sentence for remaining part of s
            for i in range(len(s)):
                curr_word = s[: i + 1]
                if curr_word in wordDict:
                    generate_sentence(s[i + 1 :], sentence + [s[: i + 1]])

        generate_sentence(s, [])
        return result
