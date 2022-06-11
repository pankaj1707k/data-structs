""" https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/ """

from typing import *


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Approach: Instead of finding minimum length prefix+suffix,
        find maximum length of subarray with sum=total-x
        """
        target = sum(nums) - x
        left = max_len = curr_sum = 0
        found = False

        for right in range(len(nums)):
            curr_sum += nums[right]
            # Reduce window from left side while curr_sum is more than target
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            # Update max_len if target is reached
            if curr_sum == target:
                found = True
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if found else -1
