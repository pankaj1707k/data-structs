""" https://leetcode.com/problems/coin-change/ """

from typing import *


def coinChange(coins: List[int], amount: int) -> int:
    n = len(coins)
    memo = [-1] * (amount + 1)

    def solve(amt: int):
        if amt == 0:
            return 0
        if memo[amt] != -1:
            return memo[amt]
        min_coins = 10009
        for coin in coins:
            if amt - coin >= 0:
                min_coins = min(min_coins, 1 + solve(amt - coin))

        memo[amt] = min_coins
        return min_coins

    ans = solve(amount)
    if ans >= 10000:
        return -1
    return ans


L = [[[1, 2, 5], 11], [[2], 3], [[1], 0]]
for l in L:
    print(coinChange(l[0], l[1]))
