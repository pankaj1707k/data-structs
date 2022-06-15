""" https://leetcode.com/problems/min-stack/ """


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.stack[-1][1] if self.stack else (1 << 31) - 1
        self.stack.append((val, min(min_val, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
