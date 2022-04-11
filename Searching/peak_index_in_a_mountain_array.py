""" https://leetcode.com/problems/peak-index-in-a-mountain-array/ """

from typing import *

# Approach 1: O(n) time and O(1) space
def peak_index_in_mountain_array(arr: List[int]) -> int:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return i


# Approach 2: O(n*log(n)) time and O(1) space
def peak_index_in_mountain_array(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        if arr[mid] > arr[mid + 1]:
            right = mid - 1
        else:
            left = mid + 1
