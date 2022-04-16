""" https://leetcode.com/problems/convert-bst-to-greater-tree/ """
""" https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.total = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root
