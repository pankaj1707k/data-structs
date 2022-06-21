""" https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        level = [root]
        direction = 1  # left: 1; right: -1
        while level:
            result.append([node.val for node in level])
            next_level = []
            direction = -direction
            for node in reversed(level):
                if direction == 1:
                    # left to right
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    # right to left
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
            level = next_level

        return result
