""" https://leetcode.com/problems/3sum/ """

from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        d = {n: i for i, n in enumerate(nums)}
        n = len(nums)
        for i in range(n):
            target = -nums[i]
            for j in range(i + 1, n):
                if j != i and target - nums[j] in d and d[target - nums[j]] > j:
                    triplet = [nums[i], nums[j], target - nums[j]]
                    if triplet not in result:
                        result.append([nums[i], nums[j], target - nums[j]])
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n - 2:
            while i > 0 and nums[i] == nums[i - 1]:
                i += 1
            j, k = i + 1, n - 1
            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]
                if triplet_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                elif triplet_sum > 0:
                    k -= 1
                else:
                    j += 1
        return result
