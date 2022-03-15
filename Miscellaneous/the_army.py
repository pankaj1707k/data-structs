""" https://www.codechef.com/problems/ANUARM """

import sys

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    output = [0] * n
    pos = list(map(int, input().split()))
    min_pos = min(pos)
    max_pos = max(pos)
    for i in range(n):
        output[i] = max(abs(i - min_pos), abs(i - max_pos))
    print(*output)
