""" https://leetcode.com/problems/number-of-1-bits/ """


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1
            n = n >> 1
        return count
