""" https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/waves-b18625d7/ """

import sys
from queue import Queue

sys.stdin = open("../../input.txt", "r")
sys.stdout = open("../../output.txt", "w")
input = sys.stdin.readline


def bfs(src_i: int, src_j: int):
    q = Queue()
    q.put((src_i, src_j))
    vis = [[False] * c for _ in range(r)]
    vis[src_i][src_j] = True
    while not q.empty():
        i, j = q.get()
        for move in moves:
            x = i + move[0]
            y = j + move[1]
            if x >= 0 and y >= 0 and x < r and y < c and not vis[x][y]:
                q.put((x, y))
                matrix[x][y] = matrix[i][j] + 1
                vis[x][y] = True


r, c, ci, cj = map(int, input().split())
matrix = [[0] * c for _ in range(r)]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
bfs(ci, cj)
for i in range(r):
    print(" ".join(map(str, matrix[i])))
