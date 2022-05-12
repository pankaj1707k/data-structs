""" https://leetcode.com/problems/permutations-ii/ """

from typing import *


class Solution:
    def add_permutation(self, n: int, permutation: List[int], visited: List[int]):
        if n == 0:
            if permutation not in self.result:
                self.result.append(permutation)
            return
        for i in range(len(self.nums)):
            if not visited[i]:
                visited[i] = True
                self.add_permutation(n - 1, permutation + [self.nums[i]], visited)
                visited[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []
        visited = [False] * len(nums)
        self.add_permutation(len(nums), [], visited)
        return self.result
