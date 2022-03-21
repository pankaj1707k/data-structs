""" https://leetcode.com/problems/partition-labels/ """

from typing import *


def partition_labels(s: str) -> List[int]:
    n = len(s)
    last = {}

    for i, c in enumerate(s):
        last[c] = i

    i = 0
    j = 0
    parts = []
    while i < n and j < n:
        j = last[s[i]]
        k = i + 1
        while k < j:
            j = max(j, last[s[k]])
            k += 1
        parts.append(j - i + 1)
        i = j + 1

    return parts
