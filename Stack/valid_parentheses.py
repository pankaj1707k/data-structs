""" https://leetcode.com/problems/valid-parentheses/ """


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"{": "}", "(": ")", "[": "]"}
        for p in s:
            if p in brackets:
                stack.append(p)
            else:
                if not stack:
                    return False
                if p != brackets[stack[-1]]:
                    return False
                stack.pop()
        if stack:
            return False
        return True
