""" https://leetcode.com/problems/binary-trees-with-factors/ """

from collections import defaultdict
from typing import *


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        numset = set(arr)
        arr.sort()
        memo = defaultdict(int)
        result = 0
        for root_num in arr:
            result = (result + self._recur(root_num, memo, numset)) % 1_000_000_007
        return result

    def _recur(self, root: int, memo: dict, numset: set) -> int:
        if memo[root] != 0:
            return memo[root]
        factors = self._get_factors(root, numset)
        memo[root] = 1
        # recursively find the result for all factors of num
        for f in factors:
            left = self._recur(f, memo, numset)
            right = self._recur(root // f, memo, numset) if root // f in factors else 0
            memo[root] = (memo[root] + left * right) % 1_000_000_007
        return memo[root]

    def _get_factors(self, num: int, numset: set) -> set:
        factors = set()
        for x in numset:
            if x != num and num % x == 0:
                factors.add(x)
        return factors


test_arg = [15, 13, 22, 7, 11]
result = Solution().numFactoredBinaryTrees(test_arg)
print(result)
