""" https://www.codechef.com/problems/ODDSUM """

import sys

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n < 3:
        print("1")
    else:
        ans = 1 + (n - 1) * (n - 2)
        print(ans)
