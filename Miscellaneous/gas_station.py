""" https://leetcode.com/problems/gas-station/ """

from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = diff_sum = i = 0
        while True:
            if diff_sum < 0:
                start = i  # restart cycle
                diff_sum = 0
            diff_sum += gas[i] - cost[i]
            i = (i + 1) % len(gas)
            if i == start:  # cycle complete
                break
        return start
