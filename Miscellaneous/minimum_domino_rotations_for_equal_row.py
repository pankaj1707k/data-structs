""" https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/ """

from typing import *
from collections import defaultdict


def min_domino_rotations(tops: List[int], bottoms: List[int]) -> int:
    n = len(tops)
    ftop = defaultdict(int)
    fbot = defaultdict(int)
    fsame = defaultdict(int)

    for i in range(n):
        ftop[tops[i]] += 1
        fbot[bottoms[i]] += 1
        if tops[i] == bottoms[i]:
            fsame[tops[i]] += 1

    min_rotations = 2 * n
    for num in range(1, 7):
        if ftop[num] + fbot[num] - fsame[num] == n:
            min_rotations = min(min_rotations, ftop[num], fbot[num] - fsame[num])

    return -1 if min_rotations == 2 * n else min_rotations
