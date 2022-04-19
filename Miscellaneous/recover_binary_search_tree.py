""" https://leetcode.com/problems/recover-binary-search-tree/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recover_tree(self, root: Optional[TreeNode]) -> None:
        self.previous = TreeNode(-(2 ** 32))
        self.first_mistake = self.second_mistake = None
        self.inorder(root)
        self.first_mistake.val, self.second_mistake.val = (
            self.second_mistake.val,
            self.first_mistake.val,
        )

    def inorder(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return
        # Traverse the left subtree
        self.inorder(root.left)
        # No mistake found in left subtree and current node value is less than previous node value
        if self.first_mistake == None and root.val < self.previous.val:
            self.first_mistake = self.previous
        # First mistake already found and current node value is less than previous node value
        if self.first_mistake and root.val < self.previous.val:
            self.second_mistake = root
        self.previous = root  # update previous to current node
        # Traverse right subtree
        self.inorder(root.right)
