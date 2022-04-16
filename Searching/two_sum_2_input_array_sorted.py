""" https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ """

from typing import *

# Approach 1: O(n*log(n)) time and O(1) space
def two_sum(numbers: List[int], target: int) -> List[int]:
    length = len(numbers)
    for i, n in enumerate(numbers):
        r = target - n  # remaining part of target to search in numbers
        # binary search to search for r in logarithmic time
        left = i + 1  # start from next index because numbers are sorted
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == r:
                return [i + 1, mid + 1]
            if r < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1


# Approach 2: O(log(n)) time and O(1) space
def two_sum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        if s < target:
            left += 1
        else:
            right -= 1
