""" https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/minimize-the-magic-05a3986c/ """

import sys
from collections import defaultdict
from typing import *
from queue import Queue

sys.stdin = open("../../input.txt", "r")
sys.stdout = open("../../output.txt", "w")
input = sys.stdin.readline

def dfs(vertex:int, parent:int):
    subtree_sum[vertex] += values[vertex]
    for child in tree[vertex]:
        if child == parent: continue
        dfs(child,vertex)
        subtree_sum[vertex] += subtree_sum[child]

n, x = map(int, input().split())
values = [0] + list(map(int, input().split()))
values.append(x)
tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

vis = [False] * (n+2)
q = Queue()
q.put(1)
while not q.empty():
    v = q.get()
    vis[v] = True
    if (v==1 and len(tree[v])<2) or (v!=1 and len(tree[v])<3):
        tree[v].append(n+1)
        tree[n+1].append(v)
        break
    for c in tree[v]:
        if vis[c]: continue
        q.put(c)

subtree_sum = [0] * (n+2)
dfs(1,0)
print(sum(subtree_sum))