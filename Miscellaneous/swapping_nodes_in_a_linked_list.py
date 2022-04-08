""" https://leetcode.com/problems/swapping-nodes-in-a-linked-list/ """

from typing import *


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def swap_nodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    arr = []

    # construct array from linked list
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next

    # swap elements
    arr[k - 1], arr[-k] = arr[-k], arr[k - 1]

    # construct linked list from array
    head = ListNode()
    curr = head
    for n in arr:
        curr.next = ListNode(n)
        curr = curr.next

    return head.next
