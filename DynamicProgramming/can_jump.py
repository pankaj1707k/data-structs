""" https://leetcode.com/problems/jump-game/ """

from typing import *

# Recursive solution (TLE)
def canJump(nums: List[int]) -> bool:
    memo = [-1] * 100009
    n = len(nums)

    # Is it possible to reach last index from i-th index
    def solve(i: int) -> bool:
        if i >= n - 1:
            return True
        if nums[i] == 0:
            return False
        if memo[i] != -1:
            return memo[i]
        for j in range(1, nums[i] + 1):
            if solve(i + j):
                memo[i] = True
                return True

        memo[i] = False
        return False

    return solve(0)


# Optimal solution
def canJump_opt(nums: List[int]):
    f = 1
    for i in range(len(nums) - 1):
        f = max(nums[i], f - 1)
        if f == 0:
            return False
    return True


print(canJump([2, 3, 1, 1, 4]))
print(canJump_opt([3, 2, 1, 0, 4]))
