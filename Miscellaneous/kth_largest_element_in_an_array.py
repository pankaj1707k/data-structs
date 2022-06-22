""" https://leetcode.com/problems/kth-largest-element-in-an-array/ """

import heapq
from typing import *


class Solution:
    # Time: O(nlogn)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    # Time: O(nlogn)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  # O(n)
        for _ in range(len(nums) - k):  # worst case: O(nlogn)
            heapq.heappop(nums)  # pop operation is O(logn)
        return heapq.heappop(nums)
