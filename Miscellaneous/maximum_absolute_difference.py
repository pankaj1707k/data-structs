""" https://www.interviewbit.com/problems/maximum-absolute-difference/ """

from typing import *


class Solution:
    def maxAbsDiff(self, A: List[int]) -> int:
        S = [A[i] + i for i in range(len(A))]
        D = [A[i] - i for i in range(len(A))]
        max_diff_s = max(S) - min(S)
        max_diff_d = max(D) - min(D)
        return max(max_diff_d, max_diff_s)
