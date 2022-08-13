""" https://leetcode.com/problems/substring-with-concatenation-of-all-words/ """

from collections import Counter
from typing import *


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N, L = len(s), len(words)
        word_length = len(words[0])  # length of each word in list
        word_count = Counter(words)  # frequency map of words
        result = []

        for start in range(word_length):
            left = start
            used_count = 0  # count of words used (<= L)
            excess_word = False  # denotes if a word is in excess in current window
            window_word_count = Counter()  # frequency of each word in current window
            substr_length = L * word_length

            # both right and left move with jumps of word_length
            for right in range(left, N, word_length):
                word = s[right : right + word_length]
                if word not in word_count:
                    # Invalid word, reset everything
                    left = right + word_length
                    used_count = 0
                    excess_word = False
                    window_word_count.clear()
                else:
                    while right - left == substr_length or excess_word == True:
                        # window size is beyond allowed or there is an excess word
                        # in the current window, update window parameters by shrinking
                        # the window from left
                        left_word = s[left : left + word_length]
                        window_word_count[left_word] -= 1
                        left += word_length
                        if window_word_count[left_word] == word_count[left_word]:
                            excess_word = False
                        else:
                            used_count -= 1
                    window_word_count[word] += 1
                    if window_word_count[word] <= word_count[word]:
                        used_count += 1
                    else:
                        excess_word = True
                if used_count == L and excess_word == False:
                    result.append(left)

        return result
