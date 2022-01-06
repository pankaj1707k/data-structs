""" https://leetcode.com/problems/car-pooling/ """

from typing import *
from collections import defaultdict


def carPooling(trips: List[List[int]], capacity: int) -> bool:
    locations = defaultdict(lambda: {"pick": 0, "drop": 0})
    for trip in trips:
        locations[trip[1]]["pick"] += trip[0]
        locations[trip[2]]["drop"] += trip[0]

    locs = sorted(locations.keys())
    onboard = 0
    for loc in locs:
        onboard += locations[loc]["pick"] - locations[loc]["drop"]
        if onboard < 0 or onboard > capacity:
            return False

    return True
