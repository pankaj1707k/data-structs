""" https://leetcode.com/problems/two-city-scheduling/ """

from typing import List
from functools import cache


# Approach 1: DP
# Time: O(N**2), Space: O(N**3)
def two_city_sched_cost(costs: List[List[int]]) -> int:
    n = len(costs) // 2

    @cache
    def min_cost(i: int, j: int, k: int) -> int:
        if k < 0:
            return 0
        if i == 0:
            if j == 0:
                return 0
            return costs[k][1] + min_cost(i, j - 1, k - 1)
        if j == 0:
            if i == 0:
                return 0
            return costs[k][0] + min_cost(i - 1, j, k - 1)
        return min(
            costs[k][1] + min_cost(i, j - 1, k - 1),
            costs[k][0] + min_cost(i - 1, j, k - 1),
        )

    return min_cost(n, n, 2 * n - 1)


# Approach 2: Sorting
# Time: O(N), Space: O(1)
def two_city_sched_cost_2(costs: List[List[int]]) -> int:
    costs.sort(key=lambda x: x[0] - x[1])
    n = len(costs) // 2
    ans = 0
    for i in range(2 * n):
        if i < n:
            ans += costs[i][0]
        else:
            ans += costs[i][1]
    return ans
