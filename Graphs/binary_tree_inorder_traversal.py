""" https://leetcode.com/problems/binary-tree-inorder-traversal/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root == None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
