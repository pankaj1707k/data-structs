""" https://leetcode.com/problems/delete-and-earn/ """

from typing import *
from collections import defaultdict


def deleteAndEarn(nums: List[int]) -> int:
    nums.sort()     # sort to avoid running loops within recursive calls to dp()
    freq = defaultdict(int)
    for n in nums:
        freq[n] += 1
    
    memo = {}

    def dp(nums: List[int], n: int):
        if n in memo:
            return memo[n]
        if n <= 0:
            return 0

        # Not earning from the last number
        val_1 = dp(nums, n-1)

        # Earning from the last number
        nn = n - freq[nums[n-1]] - freq[nums[n-1] - 1]
        val_2 = nums[n-1]*freq[nums[n-1]] + dp(nums, nn)
        
        # Get the maximum of the two values
        memo[n] = max(val_1, val_2)
        return memo[n]

    return dp(nums, len(nums))
    

print(deleteAndEarn([3, 4, 2]))
print(deleteAndEarn([2, 2, 3, 3, 3, 4]))
print(deleteAndEarn([1]))
