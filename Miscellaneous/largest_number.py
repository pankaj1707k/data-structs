""" https://leetcode.com/problems/largest-number/ """

from typing import *


class Comparator(str):
    def __lt__(self, __x: str) -> bool:
        return self + __x > __x + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))  # convert each number to string
        nums.sort(key=Comparator)  # sort based on concatenation
        result = "".join(nums)
        return "0" if result[0] == "0" else result
