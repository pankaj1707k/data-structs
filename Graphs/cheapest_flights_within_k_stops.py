""" https://leetcode.com/problems/cheapest-flights-within-k-stops/ """

from typing import *
from collections import defaultdict
from queue import Queue


def findCheapestPrice(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    graph = defaultdict(list)
    for f in flights:
        graph[f[0]].append((f[1], f[2]))

    INF = 10 ** 9
    price = [INF] * n
    price[src] = 0
    q = Queue()
    q.put((0, src))
    k += 1

    while not q.empty():
        if k <= 0:
            break
        l = q.qsize()
        while l:
            p, v = q.get()
            for c, cp in graph[v]:
                if p + cp < price[c]:
                    price[c] = p + cp
                    q.put((price[c], c))
            l -= 1

        k -= 1

    if price[dst] == INF:
        return -1
    return price[dst]
