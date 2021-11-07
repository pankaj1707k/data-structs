""" https://leetcode.com/problems/maximum-subarray/ """

from typing import *

# Method 1: O(n) [bottom-up DP approach]
def maxSubArray(nums: List[int]) -> int:
    cm = nums[0]
    mx = nums[0]
    for i in range(1,len(nums)):
        cm = max(nums[i], cm + nums[i])
        mx = max(mx, cm)
    return mx

# Method 2: Divide and conquer (recursive)
def maxSubArray2(nums: List[int]) -> int:
    n = len(nums)

    def solve(arr: List[int], l: int, r: int) -> int:
        if l == r:
            return arr[l]

        mid = (l+r) // 2

        # find max of left subarray including mid
        lm = -100001    # left maximum
        cs = 0          # cumulative sum
        for i in range(mid, l-1, -1):
            cs += nums[i]
            lm = max(lm, cs)
        
        # find max of right subarray excluding mid
        rm = -100001    # right maximum
        cs = 0          # cumulative sum
        for i in range(mid+1, r+1):
            cs += nums[i]
            rm = max(rm, cs)
        
        return max([
            solve(nums, l, mid),
            solve(nums, mid+1, r),
            lm + rm
        ])
        
    return solve(nums, 0, n-1)

lists = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8], [-2,-3,-1]]
for l in lists:
    print(maxSubArray2(l))