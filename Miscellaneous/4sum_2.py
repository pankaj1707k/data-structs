""" https://leetcode.com/problems/4sum-ii/ """

from typing import List
from collections import defaultdict


def fourSumCount(
    nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
) -> int:
    f = defaultdict(int)
    for y in nums3:
        for z in nums4:
            f[y + z] += 1

    ans = 0
    for w in nums1:
        for x in nums2:
            ans += f[-(w + x)]

    return ans
