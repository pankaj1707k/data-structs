""" https://leetcode.com/problems/longest-consecutive-sequence/ """

from typing import *


class UnionFind:
    def __init__(self, arr: List[int]) -> None:
        self.parent = {n: n for n in arr}
        self.size = {n: 1 for n in arr}

    def find(self, u: int) -> int:
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        a = self.find(u)
        b = self.find(v)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        uf = UnionFind(nums)
        for n in nums:
            if n + 1 in uf.parent:
                uf.union(n, n + 1)
        return max(uf.size.values())


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxlength = 0

        for num in nums:
            if num - 1 not in nums:
                # num is the starting point of a sequence
                curr_num = num
                length = 1

                while curr_num + 1 in nums:
                    curr_num += 1
                    length += 1

                maxlength = max(maxlength, length)

        return maxlength
