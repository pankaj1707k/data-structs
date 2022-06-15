""" https://leetcode.com/problems/shuffle-an-array/ """

import random
from typing import *


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        result = []
        n = len(self.nums)
        while n:
            i = random.randint(0, len(self.nums) - 1)
            if self.nums[i] not in result:
                result.append(self.nums[i])
                n -= 1
        return result
