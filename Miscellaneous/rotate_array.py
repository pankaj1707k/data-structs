""" https://leetcode.com/problems/rotate-array/ """

from typing import *


class Solution:
    # O(n) time and O(k%n) space
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # shifting by n places has no effect on nums
        temp = []  # to store last k elements of nums
        for i in range(n - k, n):
            temp.append(nums[i])
        # shift n-k elements in nums
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]
        # assign elements in temp as first k elements in nums
        for i in range(k):
            nums[i] = temp[i]

    # O(n) time and O(1) space
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
