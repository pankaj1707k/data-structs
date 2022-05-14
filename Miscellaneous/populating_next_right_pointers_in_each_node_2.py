""" https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/ """

from typing import *


class Node:
    def __init__(self, val=0, left=None, right=None, next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # O(N) time and O(maxlen(queue)) space
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        q = []
        q.append(root)
        dummy = Node(-777)

        while q:
            n = len(q)
            previous = dummy
            for _ in range(n):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    previous.next = node.left
                    previous = previous.next
                if node.right:
                    q.append(node.right)
                    previous.next = node.right
                    previous = previous.next

        return root

    # O(N) time and O(1) space
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        curr = root
        head = root
        dummy = Node(-777)

        while head:
            curr = head
            previous = dummy
            while curr:
                if curr.left:
                    previous.next = curr.left
                    previous = previous.next
                if curr.right:
                    previous.next = curr.right
                    previous = previous.next
                curr = curr.next
            head = dummy.next
            dummy.next = None

        return root
