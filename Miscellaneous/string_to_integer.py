""" https://leetcode.com/problems/string-to-integer-atoi/ """


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        num = i = 0
        sign = 1

        # Discard leading spaces
        while i < len(s) and s[i] == " ":
            i += 1

        # Check for sign
        if i < len(s) and s[i] == "+":
            sign = 1
            i += 1
        elif i < len(s) and s[i] == "-":
            sign = -1
            i += 1

        # Build number by going through all continuous digit characters
        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord("0")
            # Check for overflow/underflow
            if (num > INT_MAX // 10) or (num == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            # Add digit to num
            num = num * 10 + digit
            i += 1

        return num * sign
