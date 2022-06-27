""" https://leetcode.com/problems/largest-rectangle-in-histogram/ """

from typing import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []  # store [index, height] pairs
        # index is the position from which height can be included
        max_area = 0
        for i in range(n):
            if not stack:
                stack.append([i, heights[i]])
            elif heights[i] > stack[-1][1]:
                # height in increasing order
                stack.append([i, heights[i]])
            index = None
            # decreasing order encountered
            while stack and heights[i] < stack[-1][1]:
                # pop heights and update max_area
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
            # at least one height is popped
            if index != None:
                # `heights[i]` can be extended towards left upto `index`
                stack.append([index, heights[i]])

        # heights remaining in the stack can be stretched
        # from `index` upto the end of the list
        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height * (n - index))

        return max_area
