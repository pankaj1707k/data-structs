""" https://leetcode.com/problems/minimum-number-of-refueling-stops/ """

from heapq import *
from typing import *


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        stations.append([target, 0])
        missed_stations = []  # heap storing fuel in missed gas stations
        fuel = startFuel
        prev_pos = stops = 0

        for pos, fuel_capacity in stations:
            distance = pos - prev_pos
            prev_pos = pos
            while missed_stations and fuel < distance:
                # get missed station with highest fuel (time travel!)
                fuel += -heappop(missed_stations)
                stops += 1
            if fuel < distance:
                return -1
            fuel -= distance
            heappush(missed_stations, -fuel_capacity)

        return stops
