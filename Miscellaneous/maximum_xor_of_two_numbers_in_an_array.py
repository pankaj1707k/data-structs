""" https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/ """

from typing import *


def findMaximumXOR(nums: List[int]) -> int:
    maxx, mask = 0, 0
    for i in range(31, -1, -1):
        mask = mask | (1 << i)
        prefixes = {(num & mask) for num in nums}
        temp = maxx | (1 << i)
        for prefix in prefixes:
            if (temp ^ prefix) in prefixes:
                maxx = temp

    return maxx
