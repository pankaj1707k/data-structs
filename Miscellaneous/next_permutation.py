""" https://leetcode.com/problems/next-permutation/ """

from typing import *


def next_permutation(nums: List[int]) -> None:
    n = len(nums)
    i = n - 2
    while i >= 0:
        if nums[i + 1] > nums[i]:
            break
        i -= 1
    else:
        nums.sort()
        return

    j = i + 1
    while j < n:
        if nums[j] <= nums[i]:
            break
        j += 1
    j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    for k in range(i + 1, i + (n - i - 1) // 2 + 1):
        nums[k], nums[n - k + i] = nums[n - k + i], nums[k]
