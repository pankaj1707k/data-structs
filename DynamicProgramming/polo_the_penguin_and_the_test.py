""" https://www.codechef.com/problems/PPTEST """

import sys
from typing import *
from functools import cache

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline


def pptest(C: List[int], P: List[int], T: List[int], capacity: int) -> int:
    @cache
    def solve(i: int, w: int) -> int:
        if w == 0:
            return 0
        if i < 0:
            return 0
        ans = solve(i - 1, w)
        if w - T[i] >= 0:
            ans = max(ans, C[i] * P[i] + solve(i - 1, w - T[i]))
        return ans

    return solve(len(C) - 1, capacity)


t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    C = [0] * n
    P = [0] * n
    T = [0] * n
    for i in range(n):
        C[i], P[i], T[i] = map(int, input().split())
    print(pptest(C, P, T, w))
