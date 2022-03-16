""" https://www.codechef.com/problems/BEAUTGAR """

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    red = 0
    green = 0
    for i in range(n):
        if s[i] == s[(i + 1) % n]:
            if s[i] == "R":
                red += 1
            else:
                green += 1

    if (red == 0 and green == 0) or (red == 1 and green == 1):
        print("yes")
    else:
        print("no")
