""" https://leetcode.com/problems/russian-doll-envelopes/ """

from typing import *
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        self.envelopes = envelopes
        self.envelopes.sort(key=lambda e: (e[0], -e[1]))
        lis = []
        # lis is not the correct sequence but its length is same as the actual sequence
        for i in range(len(envelopes)):
            if not lis or self.envelopes[i][1] > lis[-1]:
                lis.append(self.envelopes[i][1])
                continue
            pos = bisect_left(lis, self.envelopes[i][1])
            lis[pos] = self.envelopes[i][1]  # replace element
        return len(lis)
