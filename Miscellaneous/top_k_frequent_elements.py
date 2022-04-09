""" https://leetcode.com/problems/top-k-frequent-elements/ """

from collections import Counter
from heapq import *
from typing import *


def top_k_frequent(nums: List[int], k: int) -> int:
    freq = Counter(nums)
    return nlargest(k, freq.keys(), key=freq.get)
