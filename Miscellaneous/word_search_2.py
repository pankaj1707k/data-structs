""" https://leetcode.com/problems/word-search-ii/ """

from typing import *


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = set()
        self.root = TrieNode()

        # construct trie
        for word in words:
            self.insert(word)

        self.rows = len(board)
        self.cols = len(board[0])
        self.visited = set()
        self.board = board

        for i in range(self.rows):
            for j in range(self.cols):
                self.search(i, j, "", self.root)

        return list(self.result)

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, i: int, j: int, s: str, node: TrieNode) -> None:
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols:
            return
        if (i, j) in self.visited or self.board[i][j] not in node.children:
            return
        parent = node
        node = node.children[self.board[i][j]]
        s += self.board[i][j]
        if node.end:
            self.result.add(s)
            # mark as not end to avoid reconsideration
            node.end = False
            # if node has no children then delete it from the trie
            if not node.children:
                parent.children.pop(self.board[i][j])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.visited.add((i, j))
        for d in dirs:
            self.search(i + d[0], j + d[1], s, node)
        self.visited.remove((i, j))
