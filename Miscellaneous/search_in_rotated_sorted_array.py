""" https://leetcode.com/problems/search-in-rotated-sorted-array/ """

from typing import List


def search(nums: List[int], target: int) -> int:
    def binsearch(left: int, right: int) -> int:
        if left > right:
            return -1
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            return binsearch(left, mid - 1)
        return binsearch(mid + 1, right)

    n = len(nums)
    pivot = n - 1
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            pivot = i
            break

    return max(binsearch(0, pivot), binsearch(pivot + 1, n - 1))
