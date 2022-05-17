""" https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/ """

from typing import *


class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generate_path(self, root: TreeNode, target: TreeNode) -> bool:
        if root == target:
            return True
        if root.left:
            self.path.append(0)
            if self.generate_path(root.left, target):
                return True
            self.path.pop()
        if root.right:
            self.path.append(1)
            if self.generate_path(root.right, target):
                return True
            self.path.pop()
        return False

    def find_target(self, root: TreeNode, path_index: int) -> TreeNode:
        if path_index == len(self.path):
            return root
        if self.path[path_index] == 0:
            return self.find_target(root.left, path_index + 1)
        return self.find_target(root.right, path_index + 1)

    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        self.path = []
        self.generate_path(original, target)
        return self.find_target(cloned, 0)
