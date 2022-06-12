""" https://leetcode.com/problems/remove-duplicates-from-sorted-array/ """

from typing import *


class Solution:
    # Does not work if arrays cannot be shrinked
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i - 1]:
                del nums[i]
            i += 1
        return len(nums)

    # Without shrinking the array
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        while j < len(nums):
            nums[i] = nums[j]
            # after first encounter, skip over the duplicates
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            i += 1
        return i
