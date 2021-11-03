""" https://leetcode.com/problems/jump-game-ii/ """

from typing import *

# recursive
def jump(nums: List[int]):
    n = len(nums)
    memo = {}

    def solve(nums: List[int], n: int):
        if n in memo:
            return memo[n]
        if n == 1:
            return 0
        if n <= 0 or nums[-n] == 0:
            return 10001
        min_steps = set()
        for i in range(nums[-n], 0, -1):
            min_steps.add(solve(nums, n-i))
        memo[n] = 1 + min(min_steps)
        return memo[n]

    return solve(nums, n)

# iterative: slower than recursive but memory usage is less
def jump_2(nums: List[int]):
    n = len(nums)
    if n <= 1:
        return 0
    dp = [10001]*n
    dp[-1] = 0
    dp[-2] = 1
    
    for i in range(-3, -n-1, -1):
        for j in range(1,nums[i]+1):
            x = min(i+j, -1)
            dp[i] = min(dp[i], 1 + dp[x])
    
    return dp[0]


nums_list = [[1,3,2], [2,3,1,1,4], [2,1], [2,3,0,1,4]]
for nums in nums_list:
    print(jump_2(nums))