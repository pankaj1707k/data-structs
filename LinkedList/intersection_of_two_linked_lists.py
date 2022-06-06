""" https://leetcode.com/problems/intersection-of-two-linked-lists/ """

from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(m+n) time and O(m) space
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        seen = set()
        curr = headA
        while curr:
            seen.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in seen:
                return curr
            curr = curr.next
        return None

    # O(m+n) time and O(1) space
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        first = headA
        second = headB
        while first != second:
            first = headB if not first else first.next
            second = headA if not second else second.next
        return first
