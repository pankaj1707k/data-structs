""" https://leetcode.com/problems/spiral-matrix-ii/ """

from typing import *


def generate_matrix(n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    num = 1
    for layer in range((n + 1) // 2):
        for j in range(layer, n - layer):
            matrix[layer][j] = num
            num += 1
        for i in range(layer + 1, n - layer):
            matrix[i][n - layer - 1] = num
            num += 1
        for j in range(n - layer - 2, layer - 1, -1):
            matrix[n - layer - 1][j] = num
            num += 1
        for i in range(n - layer - 2, layer, -1):
            matrix[i][layer] = num
            num += 1

    return matrix
