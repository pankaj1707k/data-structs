""" https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/ """

from typing import *


def special_array(nums: List[int]) -> int:
    # search for x values in range [0,length]
    left = 0
    right = len(nums)
    while left <= right:
        mid = (left + right) // 2
        # number of elements greater than or equal to mid
        count = sum(1 if v >= mid else 0 for v in nums)
        if count == mid:
            return mid
        if count < mid:
            right = mid - 1
        else:
            left = mid + 1
    return -1
