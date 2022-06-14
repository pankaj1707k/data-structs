""" https://leetcode.com/problems/palindrome-linked-list/ """

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find length of linked list
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        stack = []
        curr = head
        for _ in range(length // 2):
            stack.append(curr.val)
            curr = curr.next
        # If length is odd, skip middle element
        if length % 2:
            curr = curr.next
        while curr:
            if curr.val != stack[-1]:
                return False
            curr = curr.next
            stack.pop()
        return True
