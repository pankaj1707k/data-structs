""" https://www.interviewbit.com/problems/delete-edge/ """

from collections import defaultdict

MOD = 1e9+7

def dfs(vertex:int, parent:int=0):
    subtree_sum[vertex] += weight[vertex]
    for child in tree[vertex]:
        if child == parent: continue
        dfs(child,vertex)
        subtree_sum[vertex] += subtree_sum[child]

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

weight = [0] + list(map(int, input().split()))
subtree_sum = defaultdict(int)
dfs(1)

max_product = 0
for v in range(2,n+1):
    s1 = subtree_sum[v]
    s2 = subtree_sum[1] - subtree_sum[v]
    max_product = max(max_product, (s1*s2)%MOD)

print(int(max_product))