""" https://leetcode.com/problems/first-missing-positive/ """

from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] < 1 or nums[i] > n or nums[i] == nums[nums[i] - 1]:
                i += 1
            else:
                # inline swapping does not work
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

        for i in range(n):
            if i != nums[i] - 1:
                return i + 1
        return n + 1
