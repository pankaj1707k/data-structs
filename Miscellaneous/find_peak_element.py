""" https://leetcode.com/problems/find-peak-element/ """

from typing import *


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and mid < n - 1:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid] < nums[mid + 1]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                left = mid + 1
            else:
                if nums[mid] > nums[mid - 1]:
                    return mid
                right = mid - 1
