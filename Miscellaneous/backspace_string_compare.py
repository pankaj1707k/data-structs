""" https://leetcode.com/problems/backspace-string-compare/ """


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(string: str) -> str:
            stack = []
            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)

        return build_string(s) == build_string(t)
