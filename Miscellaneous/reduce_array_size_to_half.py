""" https://leetcode.com/problems/reduce-array-size-to-the-half/ """

from collections import *
from typing import *


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        result = 0
        freq = Counter(arr)
        total_count = 0
        for count in sorted(freq.values(), reverse=True):
            result += 1
            total_count += count
            if total_count >= len(arr) // 2:
                break
        return result
