""" https://www.codechef.com/CSNS21B/problems/GAMEW """

from typing import *

def numOfBlocks(s: str, l: int) -> int:
    i = 1
    n = 1
    while (i < l):
        if s[i] != s[i-1]:
            n += 1
        i += 1
    return n

def findWinner(s: str, l: int) -> str:
    n = numOfBlocks(s, l)
    if n % 3 == 2:
        return "RAMADHIR"
    return "SAHID"

t = int(input().strip())
result = []
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    result.append(findWinner(s, n))

for r in result:
    print(r)