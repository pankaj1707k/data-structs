""" https://www.codechef.com/CSNS21B/problems/MAXDMGE """

from typing import *

def maxDamage(a: List[int], n: int) -> List:
    rv = []
    rv.append(a[0]&a[1])
    for i in range(1, n-1):
        rv.append(max(a[i-1]&a[i], a[i]&a[i+1]))
    rv.append(a[-1]&a[-2])
    return rv

t = int(input().strip())
result = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result.append(maxDamage(a, n))

for r in result:
    for n in r:
        print(n, end=' ')
    print()