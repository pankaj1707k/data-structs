""" https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ """

from typing import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        # Complete array is in sorted order
        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1  # inflection point is in left half
            else:
                right = mid - 1  # inflection point is in right half
