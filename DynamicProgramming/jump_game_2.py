""" https://leetcode.com/problems/jump-game-ii/ """

from typing import *

# recursive
def jump(nums: List[int]):
    n = len(nums)
    memo = {}

    def solve(i: int):
        if i in memo:
            return memo[i]
        if i == 1:
            return 0
        if i <= 0 or nums[-i] == 0:
            return 10001
        min_steps = 100001
        for j in range(nums[-i], 0, -1):
            min_steps = min(min_steps, solve(i - j))
        memo[i] = 1 + min_steps
        return memo[i]

    return solve(n)


# iterative: slower than recursive but memory usage is less
def jump_2(nums: List[int]):
    n = len(nums)
    if n <= 1:
        return 0
    dp = [10001] * n
    dp[-1] = 0
    dp[-2] = 1

    for i in range(-3, -n - 1, -1):
        for j in range(1, nums[i] + 1):
            x = min(i + j, -1)
            dp[i] = min(dp[i], 1 + dp[x])

    return dp[0]


nums_list = [[1, 3, 2], [2, 3, 1, 1, 4], [2, 1], [2, 3, 0, 1, 4]]
for nums in nums_list:
    print(jump_2(nums))
