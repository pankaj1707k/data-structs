"""
You are at the IIITA campus which is in the form of an N * M grid. 
Here people travel from one place to another by jumping over the 
buildings which are present in each cell of the grid. It is Christmas 
eve, and one of your Teachers wants to give you gifts and chocolates. 
You live in the building which is present at the cell (N - 1, M - 1). 
Initially, Your teacher is present on cell (0, 0). Since your teacher 
also has to do his research work and is in hurry you must help him 
find a path from starting point to the endpoint with the least amount of time.

Your teacher may go only from one building to any of its adjacent 
buildings which are present either to the right or to the bottom or 
bottom right cell i.e. if the current position is (x, y), he may go 
to (x + 1, y + 1) or (x + 1, y) or (x, y + 1) given that the new 
coordinates are in the grid. The time taken to reach from one building 
to another is equal to the absolute difference between the heights of buildings.
"""

from typing import *
import sys

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline


def minimumTime(campus: List[List[int]], n: int, m: int) -> int:
    memo = [[-1] * m for _ in range(n)]

    def solve(i: int, j: int) -> int:
        if (i, j) == (n - 1, m - 1):
            return 0
        if memo[i][j] != -1:
            return memo[i][j]

        diagonal = 10 ** 9
        down = 10 ** 9
        right = 10 ** 9
        if i + 1 < n and j + 1 < m:
            diagonal = solve(i + 1, j + 1) + abs(campus[i][j] - campus[i + 1][j + 1])
        if i + 1 < n and j < m:
            down = solve(i + 1, j) + abs(campus[i][j] - campus[i + 1][j])
        if i < n and j + 1 < m:
            right = solve(i, j + 1) + abs(campus[i][j] - campus[i][j + 1])

        memo[i][j] = min(diagonal, down, right)
        return memo[i][j]

    return solve(0, 0)


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [list(map(int, input().split())) for __ in range(n)]
        print(minimumTime(grid, n, m))


main()
