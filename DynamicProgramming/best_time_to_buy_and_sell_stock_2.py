""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ """

from typing import *

def maxProfit(prices: List[int])->int:
    # Method 1
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

    # Method 2
    
    # memo = {}   # key: (i,b), value: max_profit
    # n = len(prices)
    # def solve(i:int, b:bool)->int:
    #     if i >= n:
    #         return 0
    #     if (i,b) in memo:
    #         return memo[(i,b)]
    #     if b:
    #         branch_1 = solve(i+1, False) - prices[i]    # bought
    #         branch_2 = solve(i+1, True)     # did not buy
    #     else:
    #         branch_1 = solve(i+1, True) + prices[i]   # sold
    #         branch_2 = solve(i+1, False)    # did not sell
    #     memo[(i,b)] = max(branch_1, branch_2)
    #     return memo[(i,b)]
    # return solve(0,True)
        

tests = [
    [7,1,5,3,6,4],
    [1,2,3,4,5],
    [7,6,4,3,1]
]
for t in tests:
    print(maxProfit(t))