""" https://leetcode.com/problems/populating-next-right-pointers-in-each-node/ """

from typing import *


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        level = [root]
        while level:
            n = len(level)
            for i in range(n - 1):
                level[i].next = level[i + 1]
            for _ in range(n):
                node = level.pop(0)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return root
