""" https://leetcode.com/problems/single-number/ """

from typing import *
from collections import defaultdict


class Solution:
    # O(n) time and O(1) space
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result

    # O(n*log(n)) time and O(1) space
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i - 1] != nums[i]:
                return nums[i - 1]
        return nums[-1]

    # O(n) time and O(n) space
    def singleNumber(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        for n in freq:
            if freq[n] == 1:
                return n
