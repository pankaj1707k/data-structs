""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ """

from typing import *

# Recursive solution with memoization
# Time complexity: O(n)
# Space complexity: O(n)
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


# Iterative solution using valley-peak approach
# Time complexity: O(n)
# Space complexity: O(1)
def maxProfit2(prices: List[int]) -> int:
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit


# Iterative solution 2
# Time complexity: O(n)
# Space complexity: O(1)
def maxProfit3(prices: List[int]) -> int:
    n = len(prices)
    if n == 1:
        return 0
    buy, sell = 0, 1
    mp = 0
    while buy < n - 1 and sell < n:
        if prices[sell] > prices[buy]:
            if sell != n - 1 and prices[sell + 1] < prices[sell]:
                mp += prices[sell] - prices[buy]
                buy = sell + 1
                sell += 2
            elif sell == n - 1:
                mp += prices[sell] - prices[buy]
                break
            else:
                sell += 1
        else:
            buy = sell
            sell += 1

    return mp


tests = [[7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]]
for t in tests:
    print(maxProfit(t))
