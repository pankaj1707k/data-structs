""" https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/ """

from typing import *


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # initially take all cards from beginning
        score = sum(cardPoints[i] for i in range(k))
        max_score = score
        n = len(cardPoints)
        for i in range(k - 1, -1, -1):
            # remove one element already in sum
            # and add one element from the end
            score = score - cardPoints[i] + cardPoints[i + n - k]
            max_score = max(max_score, score)
        return max_score
