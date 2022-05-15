""" https://leetcode.com/problems/deepest-leaves-sum/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_max_depth(self, root: Optional[TreeNode]) -> int:
        if root == None:  # No contribution to depth
            return 0
        # get max depth from left and right subtrees and add 1
        return 1 + max(self.get_max_depth(root.left), self.get_max_depth(root.right))

    def calc_sum(self, root: Optional[TreeNode], depth: int) -> int:
        if root == None:
            return
        if depth == self.max_depth:
            self.sum += root.val
            return  # condition guarantees that it's a leaf node
        self.calc_sum(root.left, depth + 1)
        self.calc_sum(root.right, depth + 1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_depth = self.get_max_depth(root)
        self.sum = 0
        self.calc_sum(root, 1)  # minimum depth can be 1 with only the root node
        return self.sum
