""" 
    You are given an N * N matrix of integers where each row and each column 
    is sorted in increasing order. You are given a target integer 'X'. Find 
    the position of 'X' in the matrix, if it exists then return the pair {i, j} 
    where 'i' represents the row and 'j' represents the column of the array, 
    otherwise return {-1,-1} 
"""

import sys
from typing import List

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline


def searchMatrix(matrix: List[List[int]], n: int, target: int) -> List[int]:
    i = 0
    j = n - 1
    while i < n:
        if matrix[i][j] == target:
            return [i, j]
        if target > matrix[i][j]:
            i += 1
        else:
            j -= 1

    return [-1, -1]


def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        matrix = [list(map(int, input().split())) for __ in range(n)]
        ans = searchMatrix(matrix, n, x)
        print(ans[0], ans[1])


main()
