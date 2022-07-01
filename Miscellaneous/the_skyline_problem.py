""" https://leetcode.com/problems/the-skyline-problem/ """

from bisect import *
from typing import *


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for b in buildings:
            points.append([b[0], -b[2]])  # neg height marks start point of building
            points.append([b[1], b[2]])  # pos height marks end point of building

        # sort points based on x coordinates in asc order
        # if x coordinates are same, sort wrt height in asc order
        points.sort()

        curr_height = 0
        q = [0]
        key_points = []

        for p in points:
            if p[1] < 0:
                # start point of a building
                insort_right(q, -p[1])  # add height in priority queue
            elif p[1] > 0:
                # end point of a building
                q.pop(bisect_left(q, p[1]))

            # add point to result if it causes a height change
            max_height = q[-1]
            if curr_height != max_height:
                curr_height = max_height
                key_points.append([p[0], curr_height])

        return key_points
