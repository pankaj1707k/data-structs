""" https://leetcode.com/problems/stone-game-ii/ """

from typing import *
from functools import cache


def stone_game_II(piles: List[int]) -> int:
    n = len(piles)
    suffix_sum = [0] * n
    suffix_sum[n - 1] = piles[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + piles[i]

    INF = 10 ** 9

    @cache
    def game(i: int, m: int) -> int:
        # Take all remaining piles if available
        if (i + 2 * m) >= n:
            return suffix_sum[i]

        min_rival_score = INF
        for x in range(1, 2 * m + 1):
            # Rival starts taking piles from (i+x) index
            # Minimize the rival's score by going over all x
            curr_rival_score = game(i + x, max(m, x))
            min_rival_score = min(min_rival_score, curr_rival_score)

        # current player's max possible score
        return suffix_sum[i] - min_rival_score

    return game(0, 1)
