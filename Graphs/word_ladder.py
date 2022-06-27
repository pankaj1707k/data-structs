""" https://leetcode.com/problems/word-ladder/ """

from collections import defaultdict, deque
from typing import *


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(set)  # key = word pattern, value = set of matching words
        q = deque()  # q[i] = (word, level)
        visited = set()

        # preprocess generic patterns of each word
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                d[pattern].add(word)

        q.append((beginWord, 1))
        visited.add(beginWord)
        word_len = len(beginWord)  # each word is of the same length

        # BFS
        while q:
            curr_word, level = q.popleft()
            # generate all patterns from curr_word
            for i in range(word_len):
                pattern = curr_word[:i] + "*" + curr_word[i + 1 :]
                # search all words mapped by the pattern
                for word in d[pattern]:
                    # return current level + 1 id endWord is found
                    if word == endWord:
                        return level + 1
                    # add word to queue if it is not visited
                    if word not in visited:
                        q.append((word, level + 1))
                        visited.add(word)
        # endWord was never found
        return 0
