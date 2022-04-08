""" https://leetcode.com/problems/kth-largest-element-in-a-stream/ """

from typing import *
from bisect import insort


class KthLargest:
    def __init__(self, k: int, nums: List[int]) -> None:
        self.k = k
        self.nums = sorted(nums)
        self.length = len(nums)

    def add(self, val: int) -> int:
        insort(self.nums, val)
        return self.nums[-self.k]
