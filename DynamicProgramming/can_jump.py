""" https://leetcode.com/problems/jump-game/ """

from typing import *

# Using standard DP approach
def canJump(nums: List[int], n: int, memo: Dict = {}) -> bool:
    if n in memo:
        return memo[n]
    if n == 1:
        return True
    if nums[-n] >= n-1:
        return True
    for i in range(nums[-n], 0, -1):
        r = canJump(nums, n-i)
        if r:
            memo[n] = True
            return True
    memo[n] = False
    return False

# Optimal solution
def canJump_opt(nums: List[int]):
    f = 1
    for i in range(len(nums)-1):
        f = max(nums[i], f-1)
        if f==0:
            return False
    return True

print(canJump([2,3,1,1,4], 5))
print(canJump_opt([3,2,1,0,4]))
