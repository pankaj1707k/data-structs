""" https://leetcode.com/problems/path-with-minimum-effort/ """

from typing import *
from queue import Queue
import heapq


class Solution:
    def __init__(self) -> None:
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        left = 0
        right = 1000009
        min_effort = right
        self.heights = heights
        self.rows = len(heights)
        self.cols = len(heights[0])

        while left <= right:
            mid = (left + right) // 2
            if self.isPathValid(mid):
                right = mid - 1
                min_effort = min(min_effort, mid)
            else:
                left = mid + 1

        return min_effort

    def isPathValid(self, upper_bound: int) -> bool:
        visited = [[False] * self.cols for _ in range(self.rows)]
        q = Queue()
        q.put((0, 0))
        visited[0][0] = True

        while not q.empty():
            i, j = q.get()
            if i == self.rows - 1 and j == self.cols - 1:
                return True
            for d in self.dirs:
                di, dj = i + d[0], j + d[1]
                if di < 0 or di >= self.rows:
                    continue
                if dj < 0 or dj >= self.cols:
                    continue
                if visited[di][dj]:
                    continue
                if abs(self.heights[di][dj] - self.heights[i][j]) > upper_bound:
                    continue
                visited[di][dj] = True
                q.put((di, dj))

        return False

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        vis = [[False for i in range(n)] for j in range(m)]
        q = []
        heapq.heappush(q, (0, 0, 0))
        while len(q) > 0:
            cur = heapq.heappop(q)
            if vis[cur[1]][cur[2]]:
                continue
            if cur[1] == m - 1 and cur[2] == n - 1:
                return cur[0]
            vis[cur[1]][cur[2]] = True
            for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = cur[1] + _x, cur[2] + _y
                if 0 <= x < m and 0 <= y < n and not vis[x][y]:
                    heapq.heappush(
                        q,
                        (
                            max(cur[0], abs(heights[x][y] - heights[cur[1]][cur[2]])),
                            x,
                            y,
                        ),
                    )
        return -1
