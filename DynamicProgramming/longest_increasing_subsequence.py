""" https://leetcode.com/problems/longest-increasing-subsequence/ """

from typing import *


def lengthofLIS(nums: List[int]) -> int:
    n = len(nums)
    memo = [0] * n

    # Return the longest subsequence ending at "index"
    def solve(index: int) -> int:
        if index == 0:
            return 1
        if memo[index] != 0:
            return memo[index]

        length = 1
        for j in range(index):
            if nums[j] < nums[index]:
                length = max(length, 1 + solve(j))

        memo[index] = length
        return length

    ans = 1
    for i in range(n):
        ans = max(ans, solve(i))

    return ans


L = [[10, 9, 2, 5, 3, 7, 101, 18], [0, 1, 0, 3, 2, 3], [7, 7, 7, 7, 7, 7, 7]]
for l in L:
    print(lengthofLIS(l))
