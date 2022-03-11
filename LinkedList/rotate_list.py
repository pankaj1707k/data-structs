""" https://leetcode.com/problems/rotate-list/ """

from typing import *


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head == None or head.next == None:
        return head

    counter = head
    n = 0
    while counter:
        n += 1
        counter = counter.next

    # List returns to original state after n rotations
    k = k % n

    while k:
        tail = head.next
        tail_pred = head
        while tail.next:
            tail = tail.next
            tail_pred = tail_pred.next
        # Rotate
        tail_pred.next = None
        tail.next = head
        head = tail
        k -= 1

    return head
