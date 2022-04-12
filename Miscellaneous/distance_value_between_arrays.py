""" https://leetcode.com/problems/find-the-distance-value-between-two-arrays/ """

from typing import *

# Approach 1: O(arr1.length * arr2.length) time
def find_distance_value(arr1: List[int], arr2: List[int], d: int) -> int:
    dval = 0
    for x in arr1:
        for y in arr2:
            if abs(x - y) <= d:
                break
        else:
            dval += 1

    return dval


# Approach 2: O(arr1.length * log(arr2.length)) time
def find_distance_value_2(arr1: List[int], arr2: List[int], d: int) -> int:
    count = 0
    arr2.sort()
    n = len(arr2)
    for x in arr1:
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            y = arr2[mid]
            if abs(y - x) <= d:
                count += 1
                break
            if x < y:
                right = mid - 1
            else:
                left = mid + 1

    return len(arr1) - count
