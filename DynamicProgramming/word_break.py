""" https://leetcode.com/problems/word-break/ """

from typing import *

def wordBreak(s:str, wordDict:List[str])->bool:
    wordLength = len(s)
    memo = [False]*(wordLength+1)
    memo[wordLength] = True
    for i in range(wordLength-1, -1, -1):
        for word in wordDict:
            wl = len(word)
            if (i+wl) <= wordLength and s[i:i+wl] == word:
                memo[i] = memo[i+wl]
            if memo[i]:
                break
    return memo[0]

tests = [
    ["leetcode", ["leet", "code"]],
    ["applepenapple", ["apple", "pen"]],
    ["catsandog", ["cats", "dog", "sand", "and", "cat"]]
]
for t in tests:
    print(wordBreak(t[0], t[1]))