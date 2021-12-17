""" https://leetcode.com/problems/maximum-depth-of-binary-tree/ """

from typing import *
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    depth = defaultdict(int)

    def dfs(node: Optional[TreeNode]):
        if node == None:
            return
        if node.left != None:
            depth[node.left] = depth[node] + 1
            dfs(node.left)
        if node.right != None:
            depth[node.right] = depth[node] + 1
            dfs(node.right)

    depth[root] = 0
    dfs(root)
    if root == None:
        return 0
    return 1 + max(depth.values())
