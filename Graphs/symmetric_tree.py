""" https://leetcode.com/problems/symmetric-tree/ """

from calendar import c
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check_sym(root.left, root.right)

    def check_sym(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Both are null
        if not root1 and not root2:
            return True
        # One of them is null
        if not root1 or not root2:
            return False
        # Both are not null
        return (
            (root1.val == root2.val)
            and self.check_sym(root1.left, root2.right)
            and self.check_sym(root1.right, root2.left)
        )
