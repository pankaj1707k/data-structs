""" https://leetcode.com/problems/minimum-size-subarray-sum/ """

from typing import *
from itertools import accumulate
from bisect import bisect_left


class Solution:
    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        """
        Two pointer approach
        Time complexity => O(n)
        Space complexity => O(1)
        """
        min_length = 100009
        curr_sum = 0
        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target and left <= right:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return min_length if min_length <= len(nums) else 0

    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        """
        Prefix sum and binary search
        Time complexity => O(n*log(n))
        Space complexity => O(n)
        """
        min_length = 100009
        prefix = list(accumulate(nums))
        for i, p in enumerate(prefix):
            rem = p - target
            if rem < 0:
                continue
            j = bisect_left(prefix, rem, 0, i)  # Uses binary search
            if prefix[j] != rem:
                j -= 1
            min_length = min(min_length, i - j)
        return min_length if min_length <= len(nums) else 0
