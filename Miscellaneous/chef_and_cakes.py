""" https://www.codechef.com/problems/EGRCAKE """

import sys
from math import gcd

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == 1:
        print("Yes")
        continue
    if m == 0:
        print("No 1")
        continue
    v = gcd(n, m)
    if v == 1:
        print("Yes")
    else:
        print(f"No {n//v}")
