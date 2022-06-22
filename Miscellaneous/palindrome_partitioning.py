""" https://leetcode.com/problems/palindrome-partitioning/ """

from typing import *


class Solution:
    # Time: O(n*(2^n)); Space: O(n)
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.dfs(s, 0, [])
        return self.result

    def dfs(self, s: str, start: int, part_list: List[str]) -> None:
        if start >= len(s):
            # a possible partition is ready
            self.result.append(part_list)
            return
        for end in range(start, len(s)):
            # check all substrings starting from `start`
            # if palindrome is found, recur for remaining part
            if self.is_palindrome(s, start, end):
                self.dfs(s, end + 1, part_list + [s[start : end + 1]])

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


class Solution2:
    # Same time and space complexity with small optimization
    # Palindrome check is O(1)
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        self.result = []
        self.palindrome = [[False] * N for _ in range(N)]
        self.dfs(s, 0, [])
        return self.result

    def dfs(self, s: str, start: int, part_list: List[str]) -> None:
        if start >= len(s):
            # a possible partition is ready
            self.result.append(part_list)
            return
        for end in range(start, len(s)):
            # check all substrings starting from `start`
            # if palindrome is found, recur for remaining part
            if self.is_palindrome(s, start, end):
                self.palindrome[start][end] = True
                self.dfs(s, end + 1, part_list + [s[start : end + 1]])

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        if end - start == 0:
            return True
        if end - start == 1:
            return s[start] == s[end]
        return s[start] == s[end] and self.palindrome[start + 1][end - 1]
