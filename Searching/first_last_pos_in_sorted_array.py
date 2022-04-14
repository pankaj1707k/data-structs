""" https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ """

from typing import *


def search_range(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = right = mid
            while left >= 0 and nums[left] == target:
                left -= 1
            while right < len(nums) and nums[right] == target:
                right += 1
            return [left + 1, right - 1]
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return [-1, -1]
