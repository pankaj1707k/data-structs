""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/ """

from typing import *

def maxProfit(prices:List[int], fee:int)->int:
    memo = {}   # key: (i,b), value: max_profit
    n = len(prices)
    def solve(i:int, b:bool)->int:
        if i >= n:
            return 0
        if (i,b) in memo:
            return memo[(i,b)]
        if b:
            branch_1 = solve(i+1, False) - prices[i]    # bought
            branch_2 = solve(i+1, True)     # did not buy
        else:
            branch_1 = solve(i+1, True) + prices[i] - fee   # sold
            branch_2 = solve(i+1, False)    # did not sell
        memo[(i,b)] = max(branch_1, branch_2)
        return memo[(i,b)]
    return solve(0,True)

tests = [
    [[1,3,2,8,4,9], 2],
    [[1,3,7,5,10,3], 3]
]
for t in tests:
    print(maxProfit(t[0], t[1]))