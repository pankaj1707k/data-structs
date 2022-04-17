""" https://leetcode.com/problems/increasing-order-search-tree/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node: TreeNode, values: List[int]):
        if not node:
            return
        self.inorder(node.left, values)
        values.append(node.val)
        self.inorder(node.right, values)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = []
        self.inorder(root, values)
        newroot = TreeNode()
        curr = newroot
        for v in values:
            curr.right = TreeNode(v)
            curr = curr.right
        return newroot.right
