""" https://leetcode.com/problems/permutation-in-string/ """

from collections import defaultdict


def check_inclusion(s1: str, s2: str) -> bool:
    l1 = len(s1)
    l2 = len(s2)

    if l1 > l2:
        return False

    freq1 = defaultdict(int)
    freq2 = defaultdict(int)

    for c in s1:
        freq1[c] += 1

    i = 0
    j = i + l1 - 1

    for k in range(i, j + 1):
        freq2[s2[k]] += 1

    while j < l2:
        for k in range(i, j + 1):
            if freq1[s2[k]] != freq2[s2[k]]:
                break
        else:
            return True
        freq2[s2[i]] -= 1
        i += 1
        j += 1
        if j < l2:
            freq2[s2[j]] += 1

    return False
