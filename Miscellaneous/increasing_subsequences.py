""" https://leetcode.com/problems/increasing-subsequences/ """

from typing import *


def find_subsequences(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = set()

    def generate(i: int, seq: Tuple[int]):
        if i == n:
            if len(seq) > 1:
                result.add(seq)
            return
        if not seq or nums[i] >= seq[-1]:
            generate(i + 1, seq + (nums[i],))
        generate(i + 1, seq)

    generate(0, tuple())
    return list(result)
