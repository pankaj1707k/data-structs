""" https://leetcode.com/problems/divisor-game/ """

from typing import *


def divisorGame(n: int) -> bool:
    memo = [[-1, -1] for _ in range(n + 1)]

    # player=0 -> Alice; player=1 -> Bob
    def solve(num: int, player: int) -> bool:
        if num == 2:
            if player == 0:
                return True
            return False
        if num < 2:
            if player == 0:
                return False
            return True
        if memo[num][player] != -1:
            return memo[num][player]

        if num % 2 == 0:
            if player == 0:
                memo[num][player] = solve(num - 2, 1 - player) or solve(
                    num - 1, 1 - player
                )
            else:
                memo[num][player] = solve(num - 2, 1 - player) and solve(
                    num - 1, 1 - player
                )
        else:
            memo[num][player] = solve(num - 1, 1 - player)
        return memo[num][player]

    return solve(n, 0)


nums = [2, 3]
for n in nums:
    print(divisorGame(n))
