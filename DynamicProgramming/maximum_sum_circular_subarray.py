""" https://leetcode.com/problems/maximum-sum-circular-subarray/ """

from typing import *

def maxSumCircularSubarray(nums: List[int]) -> int:
    """
    Apply kadane's algorithm. To handle the wrap around case, 
    keep evaluating minimum sum subarray similarly to the 
    maximum sum subarray. The wrapped around maximum sum 
    subarray is obtained by removing the minimum sum subarray 
    from the circular array. Minimum sum is calculated by inverting 
    the signs of all elements of the array and applying kadane's 
    algo to find the maximum for this inverted array.
    """
    n = len(nums)
    s = nums[0]     # total sum of array
    mx = nums[0]    # maximum sum
    cmx = nums[0]    # cumulative maximum sum
    mn = -nums[0]    # minimum sum
    cmn = -nums[0]    # cumulative minimum sum
    for i in range(1, n):
        s += nums[i]
        cmx = max(nums[i], cmx + nums[i])
        mx = max(mx, cmx)
        cmn = max(-1 * nums[i], cmn - nums[i])
        mn = max(mn, cmn)
    
    if mx < 0:
        # if all elements of the array are negative, return mx (represents the max element of array)
        return mx
    return max(mx, s + mn)  
    # Since, sign was inverted to calculated mn, it has to be added instead of subtracting

tests = [
    [1,-2,3,-2],
    [5,-3,5],
    [3,-1,2,-1],
    [3,-2,2,-3],
    [-2,-3,-1],
    [-2],
    [0,5,8,-9,9,-7,3,-2]
]

for l in tests:
    print(maxSumCircularSubarray(l))