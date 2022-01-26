""" https://leetcode.com/problems/is-subsequence/ """

from typing import *


def isSubsequence(s: str, t: str) -> bool:
    i = 0
    j = 0
    sn = len(s)
    tn = len(t)
    while i < sn and j < tn:
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == sn
