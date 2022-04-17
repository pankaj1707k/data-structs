""" https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/ """

from typing import *

# Approach 1: Brute force O(m*n)
def count_negatives(grid: List[List[int]]) -> int:
    count = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] < 0:
                count += 1
    return count


# Approach 2: Using binary search optimization
def count_negatives_bs(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0

    for i in range(m):
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if grid[i][mid] < 0:
                right = mid - 1
            else:
                left = mid + 1
        if left < n:
            count += n - left

    return count
