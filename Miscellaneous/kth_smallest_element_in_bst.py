""" https://leetcode.com/problems/kth-smallest-element-in-a-bst/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    def inorder(node: Optional[TreeNode]) -> None:
        if node:
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

    values = []
    inorder(root)
    return values[k - 1]
