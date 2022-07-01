""" https://leetcode.com/problems/sliding-window-maximum/ """

from bisect import *
from collections import deque
from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = sorted(nums[:k])
        result = [max(window)]

        # keep the window in sorted order
        for i in range(k, len(nums)):
            insort_right(window, nums[i])
            window.pop(bisect_left(window, nums[i - k]))
            result.append(window[-1])

        return result

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            # pop from front if number in front is less than nums[i]
            while q and q[-1][0] < nums[i]:
                q.pop()
            # pop from rear if index at rear is out of current window
            while q and q[0][1] <= i - k:
                q.popleft()
            q.append((nums[i], i))
            if i >= k - 1:
                # rear element contains the max of window
                result.append(q[0][0])

        return result
