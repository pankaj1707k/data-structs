""" https://leetcode.com/problems/search-suggestions-system/ """

from typing import *


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:

        # Build trie
        self.root = TrieNode()
        for word in products:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.end = True

        result = []
        prefix = ""
        for char in searchWord:
            prefix += char
            # get all words starting with `prefix`
            result.append(self.getWords(prefix))

        return result

    def getWords(self, prefix: str) -> List[str]:
        curr = self.root
        words = []

        # Move curr to the end of prefix in trie
        for char in prefix:
            if char not in curr.children:
                return words
            curr = curr.children[char]

        self.dfs(curr, prefix, words)
        return words

    def dfs(self, curr: TrieNode, prefix: str, result: List[str]) -> None:
        if len(result) == 3:
            return
        if curr.end:
            result.append(prefix)
        # recur for all possible characters
        for char in map(chr, range(ord("a"), ord("z") + 1)):
            if char in curr.children:
                self.dfs(curr.children[char], prefix + char, result)
