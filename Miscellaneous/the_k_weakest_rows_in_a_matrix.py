""" https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/ """

from typing import List
from collections import defaultdict


def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
    f = defaultdict(int)
    m = len(mat)
    n = len(mat[0])

    for i in range(m):
        for j in range(n):
            f[i] += mat[i][j]

    items = f.items()
    items = sorted(items, key=lambda t: t[1])
    k_weakest = []

    for i in range(k):
        k_weakest.append(items[i][0])

    return k_weakest
