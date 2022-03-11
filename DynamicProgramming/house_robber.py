""" https://leetcode.com/problems/house-robber/ """

from typing import *
from functools import cache


def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    @cache
    def solve(i: int) -> int:
        if i < 0:
            return 0
        if i == 0:
            return nums[i]
        max_amt = max(solve(i - 1), nums[i] + solve(i - 2))
        return max_amt

    return solve(n - 1)
