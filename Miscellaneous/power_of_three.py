""" https://leetcode.com/problems/power-of-three/ """

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

    def isPowerOfThree(self, n: int) -> bool:
        # maximum power of 3 number in the 32-bit signed integer range is
        # 3**19 = 1162261467
        return n > 0 and 1162261467 % n == 0
