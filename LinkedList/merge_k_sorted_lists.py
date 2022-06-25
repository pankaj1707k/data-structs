""" https://leetcode.com/problems/merge-k-sorted-lists/ """

from typing import *


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        # attach each list to form a single list
        for lst in lists:
            curr.next = lst
            while curr.next:
                curr = curr.next

        head = head.next
        return self.merge_sort(head)

    def merge_sort(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        mid = self.get_mid(head)
        left = self.merge_sort(head)
        right = self.merge_sort(mid)
        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        head = ListNode()
        tail = head
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return head.next

    def get_mid(self, head: ListNode) -> ListNode:
        mid_prev = None
        while head and head.next:
            mid_prev = mid_prev.next if mid_prev else head
            head = head.next.next
        mid = mid_prev.next
        mid_prev.next = None
        return mid


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Store all nodes in an array
        nodes = []
        for lst in lists:
            curr = lst
            while curr:
                nodes.append(curr)
                curr = curr.next

        # Sort based on values
        nodes.sort(key=lambda node: node.val)

        # reattach the nodes in new sorted order
        head = curr = ListNode()
        for node in nodes:
            curr.next = node
            curr = curr.next

        return head.next
