""" https://leetcode.com/problems/queue-reconstruction-by-height/ """

from typing import *


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort wrt desc in height and asc in k
        people.sort(key=lambda l: (-l[0], l[1]))
        self.result = []

        # insert all people with max height
        i = 0
        while i < len(people) and people[i][0] == people[0][0]:
            self.result.append(people[i])
            i += 1
        # insert remaining people in order of decreasing height
        # at positions marked by k
        for j in range(i, len(people)):
            self.result.insert(people[j][1], people[j])
        return self.result
