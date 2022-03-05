""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ """

from typing import *


def maxProfit(prices: List[int]) -> int:
    min_price = 10009
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


tests = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
for t in tests:
    print(maxProfit(t))
