""" https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/ """


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][1] == c:
                stack.append([stack[-1][0] + 1, c])
                while stack and stack[-1][0] >= k:
                    for _ in range(k):
                        stack.pop()
            else:
                stack.append([1, c])

        return "".join([l[1] for l in stack])
