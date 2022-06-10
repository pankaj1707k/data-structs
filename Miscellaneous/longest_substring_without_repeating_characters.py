""" https://leetcode.com/problems/longest-substring-without-repeating-characters/ """


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        left = right = length = max_length = 0
        while right < len(s):
            if s[right] not in pos:
                pos[s[right]] = right
                right += 1
                length += 1
                max_length = max(max_length, length)
            else:
                while left < pos[s[right]]:
                    del pos[s[left]]
                    left += 1
                    length -= 1
                del pos[s[left]]
                left += 1
                length -= 1

        return max_length
