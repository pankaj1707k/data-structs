""" https://leetcode.com/problems/remove-nth-node-from-end-of-list/ """

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        n = length - n + 1  # node number from beginning
        prev = None
        curr = head
        for _ in range(1, n):
            prev = curr
            curr = curr.next
        # prev is (n-1)th node and curr is nth node after the loop
        if not prev:
            return head.next
        prev.next = curr.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        first = dummy
        second = dummy
        for _ in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
