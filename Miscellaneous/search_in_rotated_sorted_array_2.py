""" https://leetcode.com/problems/search-in-rotated-sorted-array-ii/ """

from typing import List


def search(nums: List[int], target: int) -> bool:
    def binsearch(left: int, right: int) -> bool:
        if left > right:
            return False
        mid = (left + right) // 2
        if target == nums[mid]:
            return True
        if target < nums[mid]:
            return binsearch(left, mid - 1)
        return binsearch(mid + 1, right)

    n = len(nums)
    pivot = n - 1
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            pivot = i
            break

    return binsearch(0, pivot) or binsearch(pivot + 1, n - 1)
