""" https://leetcode.com/problems/kth-missing-positive-number/ """

from typing import *

# Approach 1: O(n) time and O(n) space
def find_kth_positive_number(arr: List[int], k: int) -> int:
    missing = [n for n in range(1, 2001) if n not in arr]
    return missing[k - 1]


# Approach 2: O(n) time and O(1) space
def find_kth_positive_num(arr: List[int], k: int) -> int:
    for n in arr:
        if n <= k:
            k += 1
        else:
            break
    return k
