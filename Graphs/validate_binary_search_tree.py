""" https://leetcode.com/problems/validate-binary-search-tree/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def solve(root: Optional[TreeNode], smallest: int, largest: int):
        if root == None:
            return True
        if root.val >= largest or root.val <= smallest:
            return False
        return solve(root.left, smallest, root.val) and solve(
            root.right, root.val, largest
        )

    return solve(root, -(2 ** 31) - 1, 2 ** 31)
