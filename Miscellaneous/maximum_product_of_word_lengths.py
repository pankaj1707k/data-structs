""" https://leetcode.com/problems/maximum-product-of-word-lengths/ """

from typing import *


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_masks = []
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord("a"))
            bit_masks.append(mask)
        max_prod = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bit_masks[i] & bit_masks[j] == 0:
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
        return max_prod
