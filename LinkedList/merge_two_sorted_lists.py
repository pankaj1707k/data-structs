""" https://leetcode.com/problems/merge-two-sorted-lists/ """

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = ListNode()
        curr = head
        a = list1
        b = list2

        while a and b:
            if a.val <= b.val:
                curr.next = ListNode(a.val)
                curr = curr.next
                a = a.next
            else:
                curr.next = ListNode(b.val)
                curr = curr.next
                b = b.next

        while a:
            curr.next = ListNode(a.val)
            curr = curr.next
            a = a.next

        while b:
            curr.next = ListNode(b.val)
            curr = curr.next
            b = b.next

        return head.next
