""" https://leetcode.com/problems/move-zeroes/ """

from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = j = 0
        while i < n and j < n:
            if nums[i] == 0:
                while j < n and nums[j] == 0:
                    j += 1
                if j == n:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
