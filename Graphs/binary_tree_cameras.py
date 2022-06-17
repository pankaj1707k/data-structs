""" https://leetcode.com/problems/binary-tree-cameras/ """

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # add a camera on root if it is still uncovered
        return self.dfs(root) + int(root.val == 0)

    # value of node determines the state of coverage
    # node.val = 0 => node is unconvered
    # node.val = 1 => node is covered and has a camera
    # node.val = 2 => node is covered but does not have a camera
    # Return the number of cameras required for subtree starting at `root`
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # Get the number of cameras required for left and right subtrees
        cameras = self.dfs(root.left) + self.dfs(root.right)
        # check if `root` needs a camera or not
        state = min(
            root.left.val if root.left else float("inf"),
            root.right.val if root.right else float("inf"),
        )
        if state == 0:
            # At least one of the children is uncovered, so `root` needs camera
            cameras += 1
            root.val = 1
        elif state == 1:
            # At least one the children has a camera, so `root` is already covered
            root.val = 2
        # state==inf implies that `root` is a leaf node, so prefer putting a camera on its parent.
        # state==2 implies that children are covered, but none has a camera,
        # so treat `root` as a leaf node and let its parent handle its cover.
        return cameras
