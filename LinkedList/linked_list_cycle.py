""" https://leetcode.com/problems/linked-list-cycle/ """

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's turtle-hare algorithm
        turtle = hare = head
        while hare and hare.next:
            hare = hare.next.next  # move two steps at a time
            turtle = turtle.next  # move one step at a time
            if hare == turtle:  # cycle detected
                return True
        return False
