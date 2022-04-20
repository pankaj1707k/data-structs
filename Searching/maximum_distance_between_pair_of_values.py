""" https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/ """

from typing import *


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_distance = 0
        n = len(nums2)
        # for each i (nums1) find valid j (nums2) farthest from i using binary search
        for i in range(len(nums1)):
            left = i
            right = n - 1
            while left <= right:
                j = (left + right) // 2
                if nums2[j] >= nums1[i]:
                    left = j + 1
                else:
                    right = j - 1
            j = left - 1
            max_distance = max(max_distance, j - i)
        return max_distance
