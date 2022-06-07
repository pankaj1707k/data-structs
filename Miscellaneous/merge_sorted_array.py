""" https://leetcode.com/problems/merge-sorted-array/ """

from typing import *


class Solution:
    def shift_right(self, arr: List[int], start: int) -> None:
        for i in range(len(arr) - 2, start - 1, -1):
            arr[i + 1] = arr[i]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = k = 0
        while j < n and k < m:
            if nums1[i] <= nums2[j]:
                i += 1
                k += 1
            else:
                self.shift_right(nums1, i)
                nums1[i] = nums2[j]
                j += 1
                i += 1
        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
