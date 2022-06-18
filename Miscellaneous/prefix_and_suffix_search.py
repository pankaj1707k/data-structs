""" https://leetcode.com/problems/prefix-and-suffix-search/ """

from typing import *


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.index = None


class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.separator = "#"  # character to separate suffix and prefix

        # Construct prefix tree
        for index, word in enumerate(words):
            length = len(word) + 1  # add 1 for separator
            word = word + self.separator + word

            for i in range(length):
                curr = self.root  # start from root for each prefix
                # insert the prefix starting from index i
                # prefixes starting from character after the separator are ignored
                for j in range(i, len(word)):
                    char = word[j]
                    if char not in curr.children:
                        curr.children[char] = TrieNode()
                    curr = curr.children[char]
                    curr.index = index

    def f(self, prefix: str, suffix: str) -> int:
        curr = self.root
        word = suffix + self.separator + prefix
        for char in word:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        return curr.index
