from collections import defaultdict
from typing import *

def dfs(vertex:int, parent:int=0):
    for child in tree[vertex]:
        if child == parent: continue
        depth[child] = depth[vertex] + 1
        dfs(child,vertex)
        height[vertex] = max(height[vertex], height[child] + 1)


n = int(input())    # number of nodes
tree = defaultdict(list)
for i in range(1,n):    # number of edges = n-1
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

depth = [0]*(n+1)
height = [0]*(n+1)
dfs(1)

for i in range(1,n+1):
    print(i, depth[i], height[i])