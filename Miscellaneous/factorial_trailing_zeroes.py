""" https://leetcode.com/problems/factorial-trailing-zeroes/ """

from typing import *


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # count how many 5s can be extracted from
        # each multiple of 5
        for x in range(5, n + 1, 5):
            while x % 5 == 0:
                count += 1
                x //= 5
        return count
