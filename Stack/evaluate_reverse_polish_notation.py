""" https://leetcode.com/problems/evaluate-reverse-polish-notation/ """

from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                elif token == "/":
                    stack.append(int(x / y))

        return stack.pop()
