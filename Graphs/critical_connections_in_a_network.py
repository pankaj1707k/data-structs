""" https://leetcode.com/problems/critical-connections-in-a-network/ """

from typing import *
from collections import defaultdict


class Solution:
    def dfs(self, vertex: int, parent: int) -> None:
        self.visited[vertex] = True
        self.low[vertex] = self.in_time[vertex] = self.curr_time
        self.curr_time += 1
        for child in self.graph[vertex]:
            if child == parent:
                continue
            if self.visited[child]:
                self.low[vertex] = min(self.low[vertex], self.in_time[child])
            else:
                self.dfs(child, vertex)
                self.low[vertex] = min(self.low[vertex], self.low[child])
                if self.low[child] > self.in_time[vertex]:
                    self.critical_conns.append([vertex, child])

    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        # build graph (adjacency list)
        self.graph = defaultdict(list)
        for conn in connections:
            self.graph[conn[0]].append(conn[1])
            self.graph[conn[1]].append(conn[0])

        # initialize required variables
        self.curr_time = 0
        self.low = [-1] * n
        self.in_time = [-1] * n
        self.visited = [False] * n
        self.critical_conns = []  # output list

        # Start DFS [initially there is only 1 connected component]
        self.dfs(0, -1)
        return self.critical_conns
