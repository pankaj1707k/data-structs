""" https://leetcode.com/problems/two-sum/ """

from typing import *


def two_sum(nums: List[int], target: int) -> List[int]:
    indexes = {}

    for index, num in enumerate(nums):
        indexes[num] = index

    for index, num in enumerate(nums):
        if target - num in indexes and indexes[target - num] != index:
            return [index, indexes[target - num]]
