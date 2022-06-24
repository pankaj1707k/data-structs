""" https://leetcode.com/problems/construct-target-array-with-multiple-sums/ """

from heapq import *
from typing import *


class Solution:
    # TLE; Worst case: when one element is very large compared to others
    # example: [1, 1000000000]
    def isPossible(self, target: List[int]) -> bool:
        # negate numbers for use in max heap
        for i in range(len(target)):
            target[i] = -target[i]

        heapify(target)
        total = -sum(target)
        while True:
            num = -heappop(target)  # get max num
            if num == 1:  # all elements are 1
                return True
            new_num = 2 * num - total  # num - (total - num)
            if new_num < 1:
                return False
            heappush(target, -new_num)
            total = total - num + new_num  # update total

    # Optimized
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        # negate numbers for use in max heap
        for i in range(len(target)):
            target[i] = -target[i]

        heapify(target)
        total = -sum(target)
        while True:
            num = -heappop(target)  # get max num
            if num == 1:  # all elements are 1
                return True
            if total - num == 1:  # only happens if len(target)==2
                return True
            new_num = num % (total - num)  # skip repetitive subtraction
            if new_num < 1 or new_num == num:
                return False
            heappush(target, -new_num)
            total = total - num + new_num  # update total
