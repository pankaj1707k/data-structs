""" https://leetcode.com/problems/roman-to-integer/ """


class Solution:
    def romanToInt(self, s: str) -> int:
        value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)):
            if i < len(s) - 1 and value[s[i]] < value[s[i + 1]]:
                num -= value[s[i]]
            else:
                num += value[s[i]]
        return num
