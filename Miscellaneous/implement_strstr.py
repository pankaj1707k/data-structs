""" https://leetcode.com/problems/implement-strstr/ """


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(m):
            k = i
            j = 0
            while k < m and j < n and haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == n:
                return i
        return -1
