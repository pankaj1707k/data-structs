""" https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.buildBST(0, len(nums) - 1)

    def buildBST(self, left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(self.nums[mid])
        root.left = self.buildBST(left, mid - 1)
        root.right = self.buildBST(mid + 1, right)
        return root
