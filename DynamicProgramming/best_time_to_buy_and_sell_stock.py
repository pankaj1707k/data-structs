""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ """

from typing import *

def maxProfit(prices: List[int])->int:
    n = len(prices)
    if n == 1:
        return 0
    mp = 0  # max profit
    b,s = 0,1   # b: buy, s: sell
    while s<n and b<n-1:
        if prices[s] < prices[b]:
            b += 1
        else:
            mp = max(mp, prices[s]-prices[b])
            s += 1
    
    return mp

tests = [
    [7,1,5,3,6,4],
    [7,6,4,3,1]
]
for t in tests:
    print(maxProfit(t))