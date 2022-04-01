""" Prim's algorithm to find the MST of a weighted graph """

from typing import *
from queue import PriorityQueue
from collections import defaultdict


def primMST(source: int) -> Tuple[int, int]:
    """
    Lazy version
    Time complexity: O(E*log(E))
    Space complexity: O(V)
    """
    visited = defaultdict(bool)
    mst_weight = edge_count = 0
    pq = PriorityQueue()  # To get the edge with lowest cost
    visited[source] = True
    for edge in graph[source]:
        pq.put((edge[1], source, edge[0]))  # (edge_weight, current_node, opposite node)

    while (
        not pq.empty() and edge_count < n - 1
    ):  # edge_count == n-1 means MST is complete
        edge = pq.get()  # get lowest cost edge
        vertex = edge[2]  # opposite end vertex
        if visited[vertex]:
            continue
        edge_count += 1
        mst_weight += edge[0]
        visited[vertex] = True
        # enqueue the unvisited edges connected to `vertex`
        for e in graph[vertex]:
            if not visited[e[0]]:
                pq.put((e[1], vertex, e[0]))

    # MST does not exist because of disconnected graph
    if edge_count != n - 1:
        return (None, None)
    return (edge_count, mst_weight)


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

edge_count, mst_cost = primMST(1)
print("edge count =", edge_count)
print("mst cost =", mst_cost)
