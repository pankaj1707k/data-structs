""" https://leetcode.com/problems/sort-list/ """

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time: O(nlogn); Space: O(logn)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid = self.get_mid_node(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def get_mid_node(self, head: ListNode) -> ListNode:
        mid_prev = None
        while head and head.next:
            # head moves two steps and mid_prev moves one step at a time
            # so when head reaches the end, mid_prev reaches mid-1 pos
            mid_prev = mid_prev.next if mid_prev else head
            head = head.next.next
        mid = mid_prev.next
        mid_prev.next = None
        return mid

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy_head = ListNode()
        tail = dummy_head
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        return dummy_head.next
