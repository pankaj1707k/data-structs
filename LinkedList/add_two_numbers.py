""" https://leetcode.com/problems/add-two-numbers/ """

from typing import *


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    head = ListNode(0)
    current = head
    carry = 0
    p = l1
    q = l2

    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        s = x + y + carry
        carry = s // 10
        current.next = ListNode(s % 10)
        current = current.next
        if p:
            p = p.next
        if q:
            q = q.next

    if carry:
        current.next = ListNode(carry)

    return head.next
