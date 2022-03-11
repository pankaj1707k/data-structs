""" https://leetcode.com/problems/house-robber-iii/ """

from typing import *
from functools import cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def rob(root: Optional[TreeNode]) -> int:
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return root.val

    @cache
    def solve(node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return node.val

        return max(
            solve(node.left) + solve(node.right),
            node.val
            + solve(node.left.left if node.left else None)
            + solve(node.left.right if node.left else None)
            + solve(node.right.left if node.right else None)
            + solve(node.right.right if node.right else None),
        )

    return solve(root)
