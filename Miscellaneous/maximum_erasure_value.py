""" https://leetcode.com/problems/maximum-erasure-value/ """

from typing import *


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pos = {}  # maps num -> index
        left = right = curr_sum = max_sum = 0
        while right < len(nums):
            if nums[right] not in pos:
                # nums[right] can be included in the subarray of unique elements
                curr_sum += nums[right]
                pos[nums[right]] = right  # mark position of this element
                right += 1
                max_sum = max(max_sum, curr_sum)
            else:
                # nums[right] has been included in the unique elements subarray
                # increase left until the last encountered position of nums[right]
                # discard elements in between from the sum
                while left < pos[nums[right]]:
                    curr_sum -= nums[left]
                    del pos[nums[left]]
                    left += 1
                curr_sum -= nums[left]
                del pos[nums[left]]
                left += 1

        return max_sum
