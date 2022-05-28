""" https://leetcode.com/problems/missing-number/ """

from typing import *


class Solution:
    # O(n) time and O(1) space
    def missingNumber(self, nums: List[int]) -> int:
        for n in range(len(nums) + 2):
            if n not in nums:
                return n

    # O(n*log(n)) time and O(1) space
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    # O(n) time and O(1) space
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums) * (len(nums) + 1) // 2
        return total - sum(nums)
