""" https://www.codechef.com/problems/PROBLEMS """

import sys

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

p, s = map(int, input().split())
diff = []

for i in range(p):
    sc = list(map(int, input().split()))
    ns = list(map(int, input().split()))
    sc_ns = [[sc[j], ns[j]] for j in range(s)]
    sc_ns.sort()
    n = 0
    for k in range(s - 1):
        if sc_ns[k][1] > sc_ns[k + 1][1]:
            n += 1
    diff.append((n, i + 1))

diff.sort()
for d in diff:
    print(d[1])
