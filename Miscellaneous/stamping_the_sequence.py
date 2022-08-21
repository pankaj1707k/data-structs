""" https://leetcode.com/problems/stamping-the-sequence/ """

from typing import *


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        S = len(stamp)
        T = len(target)
        target = list(target)
        result = []
        visited = set()  # store start positions already considered
        wild_count = 0  # count of wild card character '?' in string

        while wild_count < T:
            # find `stamp` or its part with wild card char in target
            pos = self.find_pos(stamp, target, visited)
            if pos == -1:  # stamp not found
                return []
            result.append(pos)
            visited.add(pos)
            # replace substring with wild card character
            for i in range(pos, pos + S):
                if target[i] == "?":
                    continue
                target[i] = "?"
                wild_count += 1

        result.reverse()
        return result

    def find_pos(self, stamp: str, target: str, visited: Set) -> int:
        S = len(stamp)
        T = len(target)
        for i in range(T - S + 1):
            if i in visited:
                continue
            # check if substring from i to i+S-1 follows stamp pattern
            j = i
            while j < i + S and (target[j] == stamp[j - i] or target[j] == "?"):
                j += 1
            if j == i + S:
                return i
        return -1
