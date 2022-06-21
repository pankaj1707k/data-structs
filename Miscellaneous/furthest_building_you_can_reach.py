""" https://leetcode.com/problems/furthest-building-you-can-reach/ """

import heapq
from functools import cache
from typing import *


class Solution:
    # TLE [Time: O(2**max(bricks, ladders))]
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        @cache
        def solve(i: int, b: int, l: int) -> int:
            if i == len(heights) - 1 or (b == 0 and l == 0):
                return i
            index = i
            if heights[i] >= heights[i + 1]:
                # no need to use anything
                index = max(index, solve(i + 1, b, l))
            else:
                if l > 0:
                    # use a ladder
                    index = max(index, solve(i + 1, b, l - 1))
                if heights[i + 1] - heights[i] <= b:
                    # use bricks
                    diff = heights[i + 1] - heights[i]
                    index = max(index, solve(i + 1, b - diff, l))
            return index

        return solve(0, bricks, ladders)

    # Time: O(n*log(n)); Space: O(n)
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff = []
        heapq.heapify(diff)

        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d <= 0:
                continue
            bricks -= d  # use bricks
            heapq.heappush(diff, -d)  # (-d) is added to simulate max heap
            if bricks < 0:
                # replace the bricks used in max height till now with a ladder
                bricks += -heapq.heappop(diff)
                if ladders > 0:
                    ladders -= 1
                else:
                    return i

        return len(heights) - 1
