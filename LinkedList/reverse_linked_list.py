""" https://leetcode.com/problems/reverse-linked-list/ """

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        # Add values in a stack
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        # Pop values from stack and change the node values
        while stack:
            curr.val = stack.pop()
            curr = curr.next
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def perform_reversal(node: ListNode) -> List[Optional[ListNode]]:
            if node.next == None:
                head = ListNode(node.val)
                return [head, head]
            head, tail = perform_reversal(node.next)
            tail.next = ListNode(node.val)
            tail = tail.next
            return [head, tail]

        if not head:
            return None
        return perform_reversal(head)[0]
