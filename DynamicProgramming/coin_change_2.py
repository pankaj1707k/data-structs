""" https://leetcode.com/problems/coin-change-2/ """

from typing import *


def coinChange(amount: int, coins: List[int]) -> int:
    n = len(coins)
    memo = [[-1] * (303) for _ in range(amount + 1)]

    def solve(amt: int, coinIndex: int) -> int:
        if amt == 0:
            return 1
        if coinIndex < 0:
            return 0
        if memo[amt][coinIndex] != -1:
            return memo[amt][coinIndex]

        ans = 0
        for x in range(0, amt + 1, coins[coinIndex]):
            ans += solve(amt - x, coinIndex - 1)

        memo[amt][coinIndex] = ans
        return ans

    ways = solve(amount, n - 1)
    return ways


L = [[5, [1, 2, 5]], [3, [2]], [10, [10]]]
for l in L:
    print(coinChange(l[0], l[1]))
