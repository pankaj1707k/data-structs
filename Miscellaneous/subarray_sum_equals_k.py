""" https://leetcode.com/problems/subarray-sum-equals-k/ """

from typing import *
from collections import defaultdict


def subarraySum(nums: List[int], k: int) -> int:
    n = len(nums)
    prefix = [0] * n
    prefix[0] = nums[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]

    count = 0
    d = defaultdict(int)  # store frequencies of prefix sums in dictionary
    for i in range(n):
        # if prefix[i] itself is the required sum increment count
        if prefix[i] == k:
            count += 1

        # prefix[i] - prefix[j] = k => prefix[i] - k = prefix[j]
        # so check for existence of prefix[i] - k
        # if (prefix[i]-k) exists in frequency map, add its frequency to count
        if prefix[i] - k in d:
            count += d[prefix[i] - k]

        # increment the frequency of prefix[i]
        d[prefix[i]] += 1

    return count
