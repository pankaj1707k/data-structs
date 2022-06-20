""" https://leetcode.com/problems/subsets/ """

from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def add_subset(i: int, subset: List[int]) -> None:
            if i == len(nums):
                result.append(subset)
                return
            add_subset(i + 1, subset)  # Not including nums[i]
            add_subset(i + 1, subset + [nums[i]])  # Including nums[i]

        add_subset(0, [])
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            result.append(subset)

        return result
