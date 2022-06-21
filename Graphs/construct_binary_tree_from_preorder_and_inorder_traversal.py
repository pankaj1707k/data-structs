""" https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n); Space: O(n); n = len(preorder) = number of nodes
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder: root, left, right
        # Inorder: left, root, right

        n = len(preorder)
        inorder_index = {num: index for index, num in enumerate(inorder)}

        def build(left: int, right: int, root_index: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = preorder[root_index]
            pivot = inorder_index[root_val]  # index of root in inorder
            root = TreeNode(root_val)
            # Root of left subtree is just ahead of current root
            root.left = build(left, pivot - 1, root_index + 1)
            # For root of right subtree, skip over (pivot-left) number of values
            # in preorder. Those (pivot-left) values belong to the right subtree
            root.right = build(pivot + 1, right, root_index + pivot - left + 1)
            return root

        return build(0, n - 1, 0)
