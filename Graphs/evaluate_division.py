""" https://leetcode.com/problems/evaluate-division/ """

from typing import *
from collections import defaultdict
from queue import Queue


def calcEquation(
    equations: List[List[str]], values: List[float], queries: List[List[str]]
) -> List[float]:
    graph = defaultdict(list)
    for i in range(len(equations)):
        graph[equations[i][0]].append((equations[i][1], values[i]))
        graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

    ans = []
    for [source, destination] in queries:
        if not graph[source] or not graph[destination]:
            ans.append(-1.0)
            continue
        if source == destination:
            ans.append(1.0)
            continue
        q = Queue()
        visited = defaultdict(bool)
        q.put((source, 1))
        prod = -1.0
        while not q.empty():
            vertex, sub_prod = q.get()
            for child, weight in graph[vertex]:
                if visited[child]:
                    continue
                if child == destination:
                    prod = sub_prod * weight
                else:
                    q.put((child, sub_prod * weight))
                visited[child] = True

        ans.append(prod)

    return ans
