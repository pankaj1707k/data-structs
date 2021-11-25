""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ """

from typing import *

def maxProfit(prices: List[int])->int:
    n = len(prices)
    if n==1:
        return 0
    buy, sell = 0,1
    mp = 0
    while buy<n-1 and sell<n:
        if prices[sell] > prices[buy]:
            if sell!=n-1 and prices[sell+1] < prices[sell]:
                mp += prices[sell]-prices[buy]
                buy = sell+1
                sell += 2
            elif sell == n-1:
                mp += prices[sell]-prices[buy]
                break
            else:
                sell += 1
        else:
            buy = sell
            sell += 1
    
    return mp
        

tests = [
    [7,1,5,3,6,4],
    [1,2,3,4,5],
    [7,6,4,3,1]
]
for t in tests:
    print(maxProfit(t))