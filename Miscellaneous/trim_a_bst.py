""" https://leetcode.com/problems/trim-a-binary-search-tree/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def trim_BST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    dummy = TreeNode(-1, None, root)

    def dfs(v: Optional[TreeNode], p: Optional[TreeNode]) -> None:
        if not v:
            return
        if v.val < low:
            if v.right:
                if v.right.val > p.val:
                    p.right = v.right
                else:
                    p.left = v.right
                dfs(v.right, p)
            else:
                if v.val > p.val:
                    p.right = None
                else:
                    p.left = None
        elif v.val > high:
            if v.left:
                if v.left.val > p.val:
                    p.right = v.left
                else:
                    p.left = v.left
                dfs(v.left, p)
            else:
                if v.val > p.val:
                    p.right = None
                else:
                    p.left = None
        else:
            dfs(v.left, v)
            dfs(v.right, v)

    dfs(root, dummy)
    return dummy.right
