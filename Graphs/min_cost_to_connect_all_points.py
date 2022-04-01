""" https://leetcode.com/problems/min-cost-to-connect-all-points/ """

from typing import *


def min_cost_connect_points(points: List[List[int]]) -> int:
    """Using Kruskal's algorithm"""

    n = len(points)
    points = [
        tuple(point) for point in points
    ]  # convert to tuple based points to store in dictionary

    # Assume graph with all points connected to each other
    edges = [
        (
            abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]),
            points[i],
            points[j],
        )
        for i in range(n)
        for j in range(i + 1, n)
    ]

    def find(point: Tuple[int]) -> Tuple[int]:
        if parent[point] == point:
            return point
        parent[point] = find(parent[point])
        return parent[point]

    def union(A: Tuple[int], B: Tuple[int]) -> None:
        a = find(A)
        b = find(B)
        if a == b:
            return
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

    parent = {}
    size = {}
    for point in points:
        parent[point] = point
        size[point] = 1

    mst_weight = 0
    edges.sort()
    for edge in edges:
        weight, pointA, pointB = edge
        if find(pointA) == find(pointB):
            continue
        union(pointA, pointB)
        mst_weight += weight

    return mst_weight
