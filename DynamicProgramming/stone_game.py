""" https://leetcode.com/problems/stone-game/ """

from typing import *


def stone_game(piles: List[int]) -> bool:
    n = len(piles)
    score = [0, 0]  # [alice, bob]
    memo = [[[-1] * 2 for __ in range(n + 9)] for _ in range(n + 9)]

    # player=0  =>  Alice
    # player=1  =>  Bob
    def game(i: int, j: int, player: int) -> bool:
        if i > j:
            return score[0] > score[1]
        if memo[i][j][player] != -1:
            return memo[i][j][player]

        # Take pile from front
        score[player] += piles[i]
        win = game(i + 1, j, 1 - player)
        score[player] -= piles[i]

        # Take pile from rear
        score[player] += piles[j]
        win = win or game(i, j - 1, 1 - player)
        score[player] -= piles[j]

        memo[i][j][player] = win
        return win

    return game(0, n - 1, 0)
