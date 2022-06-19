""" https://leetcode.com/problems/count-and-say/ """

from typing import *


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        curr = ""
        i = 0
        while i < len(prev):
            num = prev[i]
            freq = 1
            i += 1
            while i < len(prev) and prev[i] == prev[i - 1]:
                freq += 1
                i += 1
            curr += f"{freq}{num}"
        return curr

    def countAndSay(self, n: int) -> str:
        result = "1"
        for k in range(1, n):
            curr = ""
            i = 0
            while i < len(result):
                num = result[i]
                freq = 1
                i += 1
                while i < len(result) and result[i] == result[i - 1]:
                    freq += 1
                    i += 1
                curr += f"{freq}{num}"
            result = curr
        return result
