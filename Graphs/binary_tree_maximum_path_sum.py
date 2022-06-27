""" https://leetcode.com/problems/binary-tree-maximum-path-sum/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS with Kadane's algorithm
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.overall_sum = -1000000009
        self.local_sum = 1000000009
        self.dfs(root)
        return self.overall_sum

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        # either start a new sequence from root going up the tree
        # or extend max of left and right by root going up
        self.local_sum = max(root.val, root.val + max(left, right))
        # the sequence could end up within this subtree starting at root
        non_extending_sum = max(self.local_sum, left + right + root.val)
        self.overall_sum = max(self.overall_sum, non_extending_sum)
        # return local_sum to extend sequence up the tree
        return self.local_sum
