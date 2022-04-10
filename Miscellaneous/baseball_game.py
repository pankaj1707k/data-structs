""" https://leetcode.com/problems/baseball-game/ """

from typing import *


def cal_points(ops: List[str]) -> int:
    scores = []
    for i, op in enumerate(ops):
        if op == "+":
            scores.append(scores[-1] + scores[-2])
        elif op == "D":
            scores.append(scores[-1] * 2)
        elif op == "C":
            scores.pop()
        else:
            scores.append(int(op))

    return sum(scores)
