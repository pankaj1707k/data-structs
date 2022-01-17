""" https://leetcode.com/problems/word-pattern/ """

from typing import *
from collections import defaultdict


def wordPattern(pattern: str, s: str) -> bool:
    d_char_word = defaultdict(set)
    d_word_char = defaultdict(set)
    words = s.split()
    if len(words) != len(pattern):
        return False
    for index, char in enumerate(pattern):
        d_char_word[char].add(words[index])
        d_word_char[words[index]].add(char)
        if len(d_char_word[char]) > 1 or len(d_word_char[words[index]]) > 1:
            return False

    return True
