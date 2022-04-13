""" https://leetcode.com/problems/sqrtx/ """

from typing import *


def my_sqrt(x: int) -> int:
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    return mid if mid * mid < x else mid - 1
