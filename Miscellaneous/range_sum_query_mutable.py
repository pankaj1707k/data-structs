from typing import *


class NumArray:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        # Binary indexed tree
        self.bitree = [0] * (len(nums) + 9)

        # Store initial sums in bitree
        for i in range(len(nums)):
            j = i + 1
            while j <= len(nums):
                self.bitree[j] += nums[i]
                j += j & (-j)

    # Time: O(log(n))
    def update(self, index: int, value: int) -> None:
        old_value = self.nums[index]
        self.nums[index] = value
        # update bitree
        index += 1  # bitree has 1-based indexing
        while index <= len(self.nums):
            self.bitree[index] += value - old_value
            index += index & (-index)

    # Time: O(log(n))
    def sumRange(self, left: int, right: int) -> int:
        # find sum of range [1, right]
        upper_bound = 0
        right += 1  # bitree is
        while right > 0:
            upper_bound += self.bitree[right]
            right -= right & (-right)

        # find sum of range [1, left-1]
        lower_bound = 0
        while left > 0:
            lower_bound += self.bitree[left]
            left -= left & (-left)

        return upper_bound - lower_bound
