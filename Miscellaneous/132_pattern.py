""" https://leetcode.com/problems/132-pattern/ """

from typing import *


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        # prefix array with respect to minimum element
        for i in range(1, len(nums)):
            # minimum element upto and including index i
            min_array[i] = min(min_array[i - 1], nums[i])
        for j in range(len(nums) - 1, -1, -1):
            # nums[j] => `3` in pattern
            # min_array[j] => `1` in pattern
            # stack[-1] => `2` in pattern (possibly)
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:  # pattern satisfied
                return True
            # elements ahead of index j that can be considered
            # for number 2 in the pattern are stored in stack
            stack.append(nums[j])
        return False
