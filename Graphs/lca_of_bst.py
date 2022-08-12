""" https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ """

from typing import *


class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if (p.val < root.val and q.val > root.val) or (
            p.val > root.val and q.val < root.val
        ):
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)
