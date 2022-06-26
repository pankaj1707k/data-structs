""" https://leetcode.com/problems/minimum-window-substring/ """

from collections import defaultdict
from typing import *


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n or m == 0 or n == 0:
            return ""
        left = right = 0
        start, end = 0, 100009
        fs = defaultdict(int)
        ft = defaultdict(int)

        # Record freq of each char in t
        for char in t:
            ft[char] += 1

        # number of distinct chars that have been completely covered
        # in the current window (covered means char is present with req freq)
        covered = 0
        # number of distinct chars needed to be covered for valid substring
        required = len(ft)

        while right < m:
            # add current character in window
            fs[s[right]] += 1

            # is the current char completely covered
            if s[right] in ft and fs[s[right]] == ft[s[right]]:
                covered += 1

            # decrease window size from left if window remains valid
            while left <= right and covered == required:
                # update window extremes
                if right - left < end - start:
                    start = left
                    end = right
                # remove char from window
                fs[s[left]] -= 1
                # if freq of char in window reduces below threshold then
                # it is not covered
                if s[left] in ft and fs[s[left]] < ft[s[left]]:
                    covered -= 1
                left += 1

            # expand towards right
            right += 1

        return s[start : end + 1] if end - start != 100009 else ""
