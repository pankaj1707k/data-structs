""" https://leetcode.com/problems/intersection-of-two-arrays-ii/ """

from typing import *
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        for n in freq1:
            if n in freq2:
                result.extend([n] * min(freq1[n], freq2[n]))
        return result
