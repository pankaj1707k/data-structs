""" https://leetcode.com/problems/letter-combinations-of-a-phone-number/ """

from itertools import product
from typing import *


class Solution:
    def __init__(self) -> None:
        self.letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        letter_sets = [self.letter_map[d] for d in digits]
        result_list = list(product(*letter_sets))
        return ["".join(t) for t in result_list if "".join(t)]

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []

        def generate(i: int, s: str) -> None:
            if i == len(digits):
                result.append(s)
                return
            for char in self.letter_map[digits[i]]:
                generate(i + 1, s + char)

        generate(0, "")
        return result
