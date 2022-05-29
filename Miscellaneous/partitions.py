""" https://www.interviewbit.com/problems/partitions/ """

from typing import *


class Solution:
    def partitionCount(self, A: int, B: List[int]) -> int:
        if len(B) < 3:
            return 0
        total = sum(B)
        if total % 3:
            return 0
        partsum = total // 3
        ps1 = ps2 = ans = 0
        for i in range(len(B) - 2):
            ps1 += B[i]
            if ps1 == partsum:
                ps2 = 0
                for j in range(i + 1, len(B) - 1):
                    ps2 += B[j]
                    if ps2 == partsum:
                        ans += 1
        return ans
