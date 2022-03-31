""" https://leetcode.com/problems/insertion-sort-list/ """

from typing import *


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next


def insertion_sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel_head = ListNode()

    while head:
        compare_node = sentinel_head

        while compare_node.next and head.val > compare_node.next.val:
            compare_node = compare_node.next

        head_next = head.next
        head.next = compare_node.next
        compare_node.next = head
        head = head_next

    return sentinel_head.next
