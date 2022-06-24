""" https://leetcode.com/problems/fraction-to-recurring-decimal/ """

from typing import *


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        result = ""
        if (numerator / denominator) < 0:
            result += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        result += str(numerator // denominator)
        numerator %= denominator
        if numerator == 0:
            return result
        result += "."
        remainders = {}  # key=remainder; value=position in result
        remainders[numerator] = len(result)
        while numerator != 0:
            numerator *= 10
            result += str(numerator // denominator)
            numerator %= denominator
            # check if repetition has begun
            if numerator in remainders:
                pos = remainders[numerator]
                result = result[:pos] + "(" + result[pos:] + ")"
                break
            remainders[numerator] = len(result)
        return result
