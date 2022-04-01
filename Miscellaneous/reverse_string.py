""" https://leetcode.com/problems/reverse-string/ """

from typing import List

# Constraint: In-place reverse and O(1) space
def reverse_string(s: List[str]) -> None:
    n = len(s)
    for i in range(n // 2):
        s[i], s[n - i - 1] = s[n - i - 1], s[i]
