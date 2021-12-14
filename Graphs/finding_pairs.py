""" https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/find-pairs-4-699bc085/ """

from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(vertex:int, parent:int):
    for child in tree[vertex]:
        if child==parent: continue
        depth[child] = depth[vertex] + 1
        dfs(child,vertex)

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

depth = [0]*(n+1)
dfs(1,0)

ans = 0
for v in range(1,n+1):
    ans += depth[v] + 1

print(ans)