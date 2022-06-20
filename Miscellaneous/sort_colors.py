""" https://leetcode.com/problems/sort-colors/ """

from typing import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0, 0, 0]  # red, white, blue
        for n in nums:
            colors[n] += 1
        i = 0
        for color, freq in enumerate(colors):
            while freq:
                nums[i] = color
                freq -= 1
                i += 1

    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        # Skip continuous 0s from front
        while left <= right and nums[left] == 0:
            left += 1
        # Skip continuous 2s from rear
        while left <= right and nums[right] == 2:
            right -= 1
        mid = left  # mid will go from left to right
        while mid <= right:
            if nums[mid] == 0:
                # Swap with left
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid -= 1  # recompare with new number at mid
            elif nums[mid] == 2:
                # Swap with right
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
                mid -= 1  # recompare with new number at mid
            mid += 1
            mid = max(left, mid)
