""" https://leetcode.com/problems/pascals-triangle/ """

from typing import *


def generate(numRows: int) -> List[int]:
    rows = [[1] for _ in range(numRows)]
    for rnum in range(1, numRows):
        for cnum in range(1, rnum):
            rows[rnum].append(rows[rnum - 1][cnum - 1] + rows[rnum - 1][cnum])
        rows[rnum].append(1)

    return rows
