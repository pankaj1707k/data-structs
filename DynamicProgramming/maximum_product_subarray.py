""" https://leetcode.com/problems/maximum-product-subarray/ """

from typing import *

def maxProduct(nums: List[int])->int:
    l = len(nums)
    if l == 1:
        return nums[0]
    p = [0]*l   # positive products
    n = [0]*l   # negative products
    if nums[0] > 0:
        p[0] = nums[0]
    elif nums[0] < 0:
        n[0] = nums[0]
    
    for i in range(1,l):
        if nums[i] > 0:
            if p[i-1]:  # previous product is positive => current product is positive
                p[i] = p[i-1] * nums[i]
            else:   # previous product not positive => save current number as current positive product
                p[i] = nums[i]
            if n[i-1]:  # previous product is negative => current product is negative
                n[i] = n[i-1] * nums[i]
        elif nums[i] < 0:
            if n[i-1]:  # previous product is negative => current product is positive
                p[i] = n[i-1] * nums[i]
            if p[i-1]:  # previous product is positive => current product is negative
                n[i] = p[i-1] * nums[i]
            else:   # previous product not positive => save current number as current negative product
                n[i] = nums[i]
        
    return max(p)   # maximum of the positive products is the answer


tests = [
    [2,3,-2,4],
    [-2,0,-1],
    [-1],
    [-2,-3,-4,5,-6]
]
for t in tests:
    print(maxProduct(t))