""" https://leetcode.com/problems/find-the-duplicate-number/ """

from typing import *

# Binary search: Time -> O(n*log(n)); Space -> O(1)
def find_duplicate(nums: List[int]) -> int:
    left = 1
    right = len(nums) - 1
    duplicate = 0

    while left <= right:
        mid = (left + right) // 2
        count = sum(num <= mid for num in nums)
        if count > mid:
            right = mid - 1
            duplicate = mid
        else:
            left = mid + 1

    return duplicate


def aliter(nums: List[int]) -> int:
    n = len(nums) - 1
    bits = n.bit_length()
    duplicate = 0
    for bit in range(bits):
        # Set bit at position 'bit'
        mask = 1 << bit
        base_count = 0
        nums_count = 0
        for i in range(n + 1):
            # if 'bit' positioned bit is set in i then increment base_count
            if i & mask:
                base_count += 1
            # if 'bit' positioned bit is set in nums[i] then increment nums_count
            if nums[i] & mask:
                nums_count += 1
            # if nums_count > base_count then the bit at position 'bit' must be set in the duplicate
        if nums_count > base_count:
            duplicate |= mask

    return duplicate
