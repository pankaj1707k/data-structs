""" https://leetcode.com/problems/combination-sum-iii/ """

from typing import *
from itertools import combinations


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        valid_combinations = []

        def solve(k: int, n: int, combination: List[int], num: int) -> None:
            if k == 0:
                if n == 0:
                    valid_combinations.append(combination)
                return
            if num > 9:
                return
            solve(k - 1, n - num, combination + [num], num + 1)
            solve(k, n, combination, num + 1)

        solve(k, n, [], 1)
        return valid_combinations

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        all_combs = list(map(list, list(combinations(list(range(1, 10)), k))))
        return [c for c in all_combs if sum(c) == n]
