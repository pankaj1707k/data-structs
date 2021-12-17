""" https://leetcode.com/problems/range-sum-of-bst/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    def solve(node: Optional[TreeNode]):
        if node == None:
            return 0
        if node.val < low:
            return solve(node.right)
        if node.val > high:
            return solve(node.left)
        return node.val + solve(node.left) + solve(node.right)

    return solve(root)
