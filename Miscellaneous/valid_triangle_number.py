""" https://leetcode.com/problems/valid-triangle-number/ """

from typing import *


class Solution:
    def triangle_number(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1, 1, -1):  # loop for `c`
            j = 0  # index of `a`
            k = i - 1  # index of `b`
            while j < k:
                if nums[j] + nums[k] > nums[i]:  # a + b > c
                    ans += k - j
                    k -= 1
                else:
                    j += 1
        return ans
