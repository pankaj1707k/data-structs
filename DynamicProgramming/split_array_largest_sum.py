""" https://leetcode.com/problems/split-array-largest-sum/ """

from typing import *
from functools import cache
from itertools import accumulate

# Dynamic programming
# Time: O((n**2)*m), Space: O(n*m)
def split_array(nums: List[int], m: int) -> int:
    n = len(nums)
    prefix_sum = [0] + list(accumulate(nums))

    @cache
    def solve(curr_index: int, rem_sub: int) -> int:
        if rem_sub == 1:
            return prefix_sum[n] - prefix_sum[curr_index]
        min_largest = prefix_sum[n]
        for i in range(curr_index, n - rem_sub + 1):
            first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]
            largest = max(first_split_sum, solve(i + 1, rem_sub - 1))
            min_largest = min(min_largest, largest)
            if first_split_sum >= min_largest:
                break
        return min_largest

    return solve(0, m)


# Binary search
# Time: O(n*log(s)) [s = sum of nums]
# Space: O(1)
def split_array_bin(nums: List[int], m: int) -> int:
    def min_subs_req(max_allowed_sum: int) -> int:
        curr_sum = 0  # sum of numbers in current subarray
        splits = 0  # number of splits required
        for num in nums:
            if curr_sum + num <= max_allowed_sum:
                curr_sum += num
            else:
                curr_sum = num
                splits += 1
        return splits + 1  # number of subarrays required is 1 more than splits

    left = max(nums)
    right = sum(nums)
    while left <= right:
        mid = (left + right) // 2  # maximum allowed sum
        if min_subs_req(mid) <= m:
            min_largest_sum = mid
            right = mid - 1
        else:
            left = mid + 1
    return min_largest_sum
