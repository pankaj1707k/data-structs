""" Find the diameter of a generic tree """

from collections import defaultdict


def dfs(vertex: int, parent: int = 0):
    for child in tree[vertex]:
        if child == parent:
            continue
        depth[child] = depth[vertex] + 1
        dfs(child, vertex)


n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

depth = [0] * (n + 1)
dfs(1)
max_depth = max_depth_node = 0
for i in range(1, n + 1):
    if depth[i] > max_depth:
        max_depth = depth[i]
        max_depth_node = i

depth = [0] * (n + 1)
dfs(max_depth_node)
print(max(depth))
