""" https://leetcode.com/problems/non-decreasing-array/ """

from typing import *


class Solution:
    def checkPossiblity(self, nums: List[int]) -> bool:
        found = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if found:  # more than one position to modify
                    return False
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    # nums[i+2] may be larger than nums[i]
                    nums[i + 1] = nums[i]
                found = True

        return True
