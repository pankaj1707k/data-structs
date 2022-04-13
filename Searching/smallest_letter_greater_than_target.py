""" https://leetcode.com/problems/find-smallest-letter-greater-than-target/ """

from typing import *


def next_greatest_letter(letters: List[str], target: str) -> str:
    n = len(letters)
    for i in range((ord(target) + 1 - ord("a")) % 26 + ord("a"), ord("z") + 1):
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if ord(letters[mid]) == i:
                return letters[mid]
            if ord(letters[mid]) > i:
                right = mid - 1
            else:
                left = mid + 1

    return letters[0]
