""" https://leetcode.com/problems/divide-two-integers/ """


class Solution:
    # Time limit exceeded
    # O(dividend/divisor) time
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if ((dividend > 0) ^ (divisor > 0)) else 1
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        return quotient * sign

    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if ((dividend > 0) ^ (divisor > 0)) else 1
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        temp = 0
        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                quotient |= 1 << i
        quotient = quotient * sign
        if quotient > (1 << 31) - 1:
            return (1 << 31) - 1
        if quotient < -(1 << 31):
            return -(1 << 31)
        return quotient
