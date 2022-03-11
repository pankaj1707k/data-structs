""" https://leetcode.com/problems/house-robber-ii/ """

from typing import *
from functools import cache


def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    @cache
    def solve(i: int, lower_limit: int) -> int:
        if i < lower_limit:
            return 0
        if i == lower_limit:
            return nums[i]
        max_amt = max(solve(i - 1, lower_limit), nums[i] + solve(i - 2, lower_limit))
        return max_amt

    return max(solve(n - 1, 1), solve(n - 2, 0))
