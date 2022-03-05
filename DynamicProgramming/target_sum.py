""" https://leetcode.com/problems/target-sum/ """

from typing import *


def find_target_sum_ways(nums: List[int], target: int) -> int:
    n = len(nums)
    memo = [[-1] * (2 * 1010) for _ in range(n + 10)]

    def solve(i: int, s: int) -> int:
        if i == n:
            return 1 if s == target else 0
        if memo[i][s] != -1:
            return memo[i][s]
        memo[i][s] = solve(i + 1, s + nums[i]) + solve(i + 1, s - nums[i])
        return memo[i][s]

    return solve(0, 0)
