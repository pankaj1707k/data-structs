""" https://leetcode.com/problems/plus-one/ """

from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = (digits[-1] + 1) % 10
        carry = (digits[-1] + 1) // 10
        digits[-1] = s
        i = len(digits) - 2
        while carry and i >= 0:
            s = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            digits[i] = s
            i -= 1
        if carry:
            digits = [carry] + digits
        return digits
