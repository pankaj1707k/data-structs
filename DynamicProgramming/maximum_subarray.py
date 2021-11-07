""" https://leetcode.com/problems/maximum-subarray/ """

from typing import *

def maxSubArray(nums: List[int]) -> int:
    cm = nums[0]
    mx = nums[0]
    for i in range(1,len(nums)):
        cm = max(nums[i], cm + nums[i])
        mx = max(mx, cm)
    return mx


lists = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8], [-2,-3,-1]]
for l in lists:
    print(maxSubArray(l))