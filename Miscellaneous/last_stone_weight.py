""" https://leetcode.com/problems/last-stone-weight/ """

from typing import *
from bisect import insort


def last_stone_weight(stones: List[int]) -> int:
    stones.append(0)
    stones.sort()
    n = len(stones)
    while n > 1:
        y = stones.pop()
        x = stones.pop()
        if x == y:
            n -= 2
            continue
        insort(stones, y - x)
        n -= 1
    return stones.pop()
