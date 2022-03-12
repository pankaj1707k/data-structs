""" https://leetcode.com/problems/different-ways-to-add-parentheses/ """

from typing import *
from functools import cache


def diff_ways_to_compute(expression: str) -> List[int]:
    @cache
    def solve(e: str) -> List[int]:
        if e.isdigit():
            return [int(e)]
        result = []
        for i, c in enumerate(e):
            if c in ["+", "-", "*"]:
                left = solve(e[:i])
                right = solve(e[i + 1 :])
                for l in left:
                    for r in right:
                        result.append(eval(str(l) + c + str(r)))

        return result

    return solve(expression)
