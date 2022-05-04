""" https://leetcode.com/problems/max-number-of-k-sum-pairs/ """

from typing import *
from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        max_ops = 0
        freq = Counter(nums)
        for n in freq:
            if freq[n] == 0:
                continue
            if k % 2 == 0 and n == k // 2:
                pairs = freq[n] // 2
                max_ops += pairs
                freq[n] -= pairs
            else:
                if k - n in freq or freq[k - n] > 0:
                    pairs = min(freq[n], freq[k - n])
                    max_ops += pairs
                    freq[n] -= pairs
                    freq[k - n] -= pairs

        return max_ops
