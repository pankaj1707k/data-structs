""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ """

from typing import *


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    memo = [[-1] * 2 for _ in range(n + 9)]

    def solve(index: int, can_buy: int) -> int:
        if index >= n:
            return 0
        if memo[index][can_buy] != -1:
            return memo[index][can_buy]
        case_1, case_2 = 0, 0
        if can_buy:
            case_1 = solve(index + 1, 0) - prices[index]
            case_2 = solve(index + 1, 1)
        else:
            case_1 = solve(index + 1, 1) + prices[index]
            case_2 = solve(index + 1, 0)
        memo[index][can_buy] = max(case_1, case_2)
        return memo[index][can_buy]

    return solve(0, 1)


tests = [[7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]]
for t in tests:
    print(maxProfit(t))
