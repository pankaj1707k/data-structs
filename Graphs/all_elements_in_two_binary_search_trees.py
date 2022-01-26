""" https://leetcode.com/problems/all-elements-in-two-binary-search-trees/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getAllElements(root1: TreeNode, root2: TreeNode) -> List[int]:
    list1 = []
    list2 = []

    def inorderTraversal(root: TreeNode, l: List[int]):
        if root == None:
            return
        inorderTraversal(root.left, l)
        l.append(root.val)
        inorderTraversal(root.right, l)

    inorderTraversal(root1, list1)
    inorderTraversal(root2, list2)

    result = sorted(list1 + list2)
    return result
