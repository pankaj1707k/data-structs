""" https://leetcode.com/problems/hamming-distance/ """


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        # count set bits in xor
        count = 0
        while xor:
            count += xor & 1
            xor >>= 1
        return count
