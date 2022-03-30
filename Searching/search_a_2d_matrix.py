""" https://leetcode.com/problems/search-a-2d-matrix/ """

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    for i in range(len(matrix)):
        if target <= matrix[i][-1]:
            break
    left = 0
    right = len(matrix[0]) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == matrix[i][mid]:
            return True
        if target < matrix[i][mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False
