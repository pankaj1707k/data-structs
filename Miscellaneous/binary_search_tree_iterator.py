""" https://leetcode.com/problems/binary-search-tree-iterator/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        self.inorder(root)
        self.length = len(self.values)
        self.ptr = None

    def next(self) -> int:
        if self.ptr == None:
            self.ptr = 0
        else:
            self.ptr += 1
        return self.values[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr == None or self.ptr < self.length - 1

    def inorder(self, root: Optional[TreeNode]):
        if root:
            self.inorder(root.left)
            self.values.append(root.val)
            self.inorder(root.right)
