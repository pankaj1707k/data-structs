""" https://leetcode.com/problems/is-graph-bipartite/ """

from typing import *
from queue import Queue


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        node_color = [-1] * n  # valid: 0 or 1; -1 means not yet visited
        is_bipartite = True
        q = Queue()

        for s in range(n):
            if node_color[s] != -1:  # already visited
                continue
            q.put(s)
            node_color[s] = 0
            while not q.empty():
                u = q.get()
                for v in graph[u]:
                    if node_color[v] == -1:  # not yet visited
                        # assign color opposite to neighbor/parent
                        node_color[v] = 1 - node_color[u]
                        q.put(v)
                    else:  # already visited, check if both neighbors have different color
                        is_bipartite = is_bipartite and (node_color[u] != node_color[v])

        return is_bipartite
