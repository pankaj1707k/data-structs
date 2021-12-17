""" Find the sum of each subtree of the given tree """

from collections import defaultdict


def dfs(vertex: int, parent: int = 0):
    subtree_sum[vertex] += vertex
    for child in tree[vertex]:
        if child == parent:
            continue
        dfs(child, vertex)
        subtree_sum[vertex] += subtree_sum[child]


n = int(input())
tree = defaultdict(list)
for i in range(1, n):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

subtree_sum = defaultdict(int)
dfs(1)
for i in range(1, n + 1):
    print(i, subtree_sum[i])

"""
If q (<=10**5) queries are given, instead of calling dfs for each query,
it is efficient to pre-compute the sum of all subtrees by calling dfs only once. 
"""
