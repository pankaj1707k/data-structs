""" https://leetcode.com/problems/validate-stack-sequences/ """

from typing import *


def validate_stack_sequences(pushed: List[int], popped: List[int]) -> bool:
    n = len(pushed)
    stack = []
    i = 0  # pushed pointer
    j = 0  # popped pointer
    while stack and i < n and j < n:
        stack.append(pushed[i])
        i += 1
        while popped[j] == stack[-1]:
            stack.pop()
            j += 1

    if stack:
        return False
    return True
