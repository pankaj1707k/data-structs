""" https://leetcode.com/problems/pascals-triangle-ii/ """

from typing import *


def getRow(rowIndex: int) -> List[int]:
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]
    prevRow = [1, 1]
    currRow = [1]
    rnum = 2
    while rnum <= rowIndex:
        for cnum in range(1, rnum):
            currRow.append(prevRow[cnum - 1] + prevRow[cnum])
        currRow.append(1)
        prevRow = currRow
        currRow = [1]
        rnum += 1

    return prevRow
