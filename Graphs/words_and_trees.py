""" https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/words-and-trees-f9ef202c/ """

from collections import defaultdict, Counter
import sys
from typing import *

sys.stdin = open("../../input.txt", "r")
sys.stdout = open("../../output.txt", "w")
input = sys.stdin.readline

def dfs(vertex:int, parent:int):
    sub[vertex].append(char[vertex])
    for child in tree[vertex]:
        if child == parent: continue
        dfs(child, vertex)
        sub[vertex].extend(sub[child])

n, q = map(int, input().split())
char = [''] + input().split()
tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

sub = [[] for _ in range(n+1)]
dfs(1,0)
sub_counters = [Counter(s) for s in sub]
for _ in range(q):
    i = input().split()
    x = int(i[0])
    s = i[1]
    counts = Counter(s)
    ans = 0
    for c in counts:
        if c not in sub_counters[x]:
            ans += counts[c]
        elif counts[c] > sub_counters[x][c]:
            ans += counts[c] - sub_counters[x][c]
    print(ans)