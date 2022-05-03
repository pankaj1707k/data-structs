""" https://leetcode.com/problems/shortest-unsorted-continuous-subarray/ """

import sys
from typing import *


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_element, max_element = 100009, -100009
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                min_element = min(min_element, nums[i])
        flag = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                max_element = max(max_element, nums[i])
        left = 0
        for i in range(len(nums)):
            if nums[i] > min_element:
                left = i
                break
        right = 0
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] < max_element:
                right = j
                break
        return 0 if right - left <= 0 else right - left + 1
