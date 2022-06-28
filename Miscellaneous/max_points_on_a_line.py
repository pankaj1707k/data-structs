""" https://leetcode.com/problems/max-points-on-a-line/ """

from typing import *


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1 or n == 2:
            return n
        max_count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                slope_num = points[j][1] - points[i][1]
                slope_den = points[j][0] - points[i][0]
                count = 2
                for k in range(n):
                    if k != i and k != j:
                        # (x2-x1)*(y-y1) == (y2-y1)*(x-x1)
                        count += int(
                            slope_den * (points[k][1] - points[i][1])
                            == slope_num * (points[k][0] - points[i][0])
                        )
                max_count = max(max_count, count)

        return max_count
