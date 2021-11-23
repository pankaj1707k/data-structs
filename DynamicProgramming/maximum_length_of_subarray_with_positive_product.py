""" https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/ """

from typing import *

def getMaxLen(nums: List[int])->int:
    """
    1. Split nums into subarrays at 0s
    2. For each subarray find number of negatives
    3. If even number of negatives, complete subarray is a candidate for the final answer
    4. If odd number of negatives, two cases:
        (a) Part of subarray excluding elements from starting till first negative number
        (b) Part of subarray excluding elements from last negative number till the end
    """
    n = len(nums)
    if n == 1:
        return 0 if nums[0]<=0 else 1
    sub = []
    start = 0
    for i in range(n):
        if nums[i]==0:
            if (i-start)>0:
                sub.append(nums[start:i])
            start = i+1
    if start<n:
        sub.append(nums[start:])
    max_len = 0
    for s in sub:
        l = len(s)
        neg_count = len(list(filter(lambda x: x<0, s)))
        if neg_count % 2 == 0:
            max_len = max(max_len, l)
            continue
        l1, l2 = 0, 0
        for i in range(l):
            if s[i]<0:
                l1 = l-i-1
                break
        for i in range(-1,-l-1,-1):
            if s[i]<0:
                l2 = l+i
                break
        max_len = max(max_len, l1, l2)
    
    return max_len


tests = [
    [1,-2,-3,4],
    [0,1,-2,-3,-4],
    [-1,-2,-3,0,1],
    [-1,2],
    [1,2,3,5,-6,4,0,10]
]

for t in tests:
    print(getMaxLen(t))