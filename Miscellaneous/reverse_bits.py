""" https://leetcode.com/problems/reverse-bits/ """


class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for _ in range(32):
            rev = (rev << 1) | (n & 1)
            n >>= 1
        return rev
