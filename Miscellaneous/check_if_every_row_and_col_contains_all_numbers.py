""" https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/ """

from typing import *


def check_valid(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    for i in range(n):
        s_row = set()
        s_col = set()
        for j in range(n):
            s_row.add(matrix[i][j])
            s_col.add(matrix[j][i])
        if len(s_row) != n or len(s_col) != n:
            return False

    return True
