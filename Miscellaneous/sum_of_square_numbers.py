""" https://leetcode.com/problems/sum-of-square-numbers/ """

from typing import *
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = c - a * a
            sqrt_b = math.sqrt(b)
            if sqrt_b == int(sqrt_b):
                return True
            a += 1
        return False
