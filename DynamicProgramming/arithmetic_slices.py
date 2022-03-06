""" https://leetcode.com/problems/arithmetic-slices/ """

from typing import *
from functools import cache


def count_arithmetic_slices(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0

    diff = [(nums[i + 1] - nums[i]) for i in range(n - 1)]

    @cache
    def f(l: int) -> int:
        if l < 3:
            return 0
        return l - 2 + f(l - 1)

    length = 2
    ans = 0
    for i in range(1, n - 1):
        if diff[i] == diff[i - 1]:
            length += 1
        else:
            ans += f(length)
            length = 2

    return ans + f(length)
