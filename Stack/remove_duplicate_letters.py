""" https://leetcode.com/problems/remove-duplicate-letters/ """
""" https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/ """

from collections import defaultdict


def remove_duplicate_letters(s: str) -> str:
    last_index = {}
    visited = defaultdict(bool)
    stack = []
    n = len(s)

    for i in range(n - 1, -1, -1):
        if s[i] in last_index:
            continue
        last_index[s[i]] = i

    for i in range(n):
        if visited[s[i]]:
            continue
        while stack and (s[i] < stack[-1]) and (i < last_index[stack[-1]]):
            visited[stack.pop()] = False
        stack.append(s[i])
        visited[s[i]] = True

    return "".join(stack)
