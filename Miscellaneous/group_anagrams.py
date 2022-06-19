""" https://leetcode.com/problems/group-anagrams/ """

from collections import Counter, defaultdict
from typing import *


class Solution:
    # TLE: O(k*(n**2)); k=len(strs[i]); n=len(strs)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        visited = [False] * len(strs)
        for i in range(len(strs)):
            if visited[i]:
                continue
            group = [strs[i]]
            visited[i] = True
            freq = Counter(strs[i])
            for j in range(i + 1, len(strs)):
                if not visited[j] and Counter(strs[j]) == freq:
                    group.append(strs[j])
                    visited[j] = True
            groups.append(group)
        return groups

    # O(n*k) time
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # maps tuple of character counts to list of strings
        groups = defaultdict(list)
        for string in strs:
            counts = [0] * 26
            for char in string:
                counts[ord(char) - ord("a")] += 1
            groups[tuple(counts)].append(string)
        return list(groups.values())
