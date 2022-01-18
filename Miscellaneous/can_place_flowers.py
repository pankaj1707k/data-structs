""" https://leetcode.com/problems/can-place-flowers/ """

from typing import *


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    l = len(flowerbed)
    if l == 1 and flowerbed[0] == 0:
        n -= 1
        return n <= 0
    for i in range(l):
        if flowerbed[i] == 1:
            continue
        if (i == 0 and flowerbed[i + 1] == 0) or (i == l - 1 and flowerbed[i - 1] == 0):
            flowerbed[i] = 1
            n -= 1
            continue
        if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1

    return n <= 0
