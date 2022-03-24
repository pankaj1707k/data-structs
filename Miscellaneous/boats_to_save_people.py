""" https://leetcode.com/problems/boats-to-save-people/ """

from typing import List


def num_rescue_boats(people: List[int], limit: int) -> int:
    people.sort()
    boats = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        boats += 1
        j -= 1
    return boats
