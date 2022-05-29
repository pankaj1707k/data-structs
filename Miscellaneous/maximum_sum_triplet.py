""" https://www.interviewbit.com/problems/maximum-sum-triplet/ """

from typing import *
from bisect import *


class Solution:
    def maxSumTriplet(self, A: List[int]) -> int:
        suffix = [0] * len(A)
        suffix[-1] = A[-1]
        for i in range(-2, -len(A) - 1, -1):
            suffix[i] = max(suffix[i + 1], A[i])
        pre = [A[0]]
        max_sum = 0
        for j in range(1, len(A) - 1):
            i = bisect_left(pre, A[j])
            i -= 1
            if i >= 0 and suffix[j + 1] > A[j]:
                max_sum = max(max_sum, pre[i] + A[j] + suffix[j + 1])
            pre.insert(i + 1, A[j])
        return max_sum
