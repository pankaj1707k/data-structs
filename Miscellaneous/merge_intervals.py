""" https://leetcode.com/problems/merge-intervals/ """

from typing import *


class Solution:
    # Time: O(n*log(n)) (for sorting)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        start, end = intervals[0]
        for interval in intervals:
            if max(start, interval[0]) > min(end, interval[1]):
                # no overlap
                result.append([start, end])
                start, end = interval
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        result.append([start, end])
        return result
