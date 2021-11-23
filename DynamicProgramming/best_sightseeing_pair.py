""" https://leetcode.com/problems/best-sightseeing-pair/ """

from typing import *

def maxScoreSightseeingPair(values: List[int])->int:
    m = values[0]
    ans = 0
    for i in range(1,len(values)):
        s = values[i] - i + m
        ans = max(ans, s)
        m = max(m, values[i] + i)
    return ans


tests = [
    [8,1,5,2,6],
    [1,2]
]

for t in tests:
    print(maxScoreSightseeingPair(t))