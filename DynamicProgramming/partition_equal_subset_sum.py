""" https://leetcode.com/problems/partition-equal-subset-sum/ """

from typing import *


def canPartition(nums: List[int]) -> bool:
    s = sum(nums)
    if s % 2 != 0:
        return False
    s //= 2
    n = len(nums)
    dp = [[-1] * (s + 9) for _ in range(n)]

    def solve(index: int, target_sum: int) -> bool:
        if dp[index][target_sum] != -1:
            return dp[index][target_sum]
        if target_sum == 0:
            return True
        if index < 0:
            return False

        # Do not select the current element
        is_possible = solve(index - 1, target_sum)

        # Select the current element
        if target_sum - nums[index] >= 0:
            is_possible = is_possible or solve(index - 1, target_sum - nums[index])

        dp[index][target_sum] = is_possible
        return dp[index][target_sum]

    return solve(n - 1, s)
