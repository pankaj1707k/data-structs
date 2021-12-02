""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/ """

from typing import *

def maxProfit(prices:List[int])->int:
    memo = {}   # key: (i,b), value: max_profit
    def solve(i:int, b:bool)->int:
        if i >= len(prices):
            return 0
        if (i,b) in memo:
            return memo[(i,b)]
        if b:
            branch_1 = solve(i+1, False) - prices[i]    # stock bought
            branch_2 = solve(i+1, True)     # not bought
        else:
            branch_1 = solve(i+2, True) + prices[i]     # stock sold
            branch_2 = solve(i+1, False)    # not sold
        memo[(i,b)] = max(branch_1, branch_2)
        return memo[(i,b)]
    return solve(0,True)

tests = [
    [1,2,3,0,2],
    [1],
    [2,1,2,0,1],
    [6,1,3,2,4,7]
]
for t in tests:
    print(maxProfit(t))