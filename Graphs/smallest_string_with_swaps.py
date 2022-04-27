""" https://leetcode.com/problems/smallest-string-with-swaps/ """

from typing import *
from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)

        # construct graph (adjacency list)
        for pair in pairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        # DFS to create a component
        def dfs(vertex: int, chars: List[str], indexes: List[int]):
            chars.append(s[vertex])
            indexes.append(vertex)
            visited[vertex] = True
            for child in graph[vertex]:
                if not visited[child]:
                    dfs(child, chars, indexes)

        # create separate components by calling DFS
        visited = [False] * len(s)
        result = [" "] * len(s)
        for vertex in range(len(s)):
            if not visited[vertex]:
                chars = []
                indexes = []
                dfs(vertex, chars, indexes)
                chars.sort(key=ord)
                indexes.sort()
                for i, index in enumerate(indexes):
                    result[index] = chars[i]

        return "".join(result)
