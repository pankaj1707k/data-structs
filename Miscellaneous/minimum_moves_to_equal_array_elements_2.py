""" https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/ """

from typing import *


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        n = len(nums)
        median = nums[n // 2] if n & 1 else (nums[n // 2] + nums[n // 2 - 1]) // 2
        for num in nums:
            result += abs(median - num)
        return result
