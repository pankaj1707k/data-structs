""" https://leetcode.com/problems/maximum-depth-of-n-ary-tree/ """

from typing import *
from collections import defaultdict

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def maxDepth(root:Optional[Node])->int:
    depth = defaultdict(int)

    def dfs(node:Optional[Node]):
        if node==None:  return
        for child in node.children:
            if child==None: continue
            depth[child] = depth[node] + 1
            dfs(child)
    
    depth[root] = 0
    dfs(root)
    if root == None:
        return 0
    return 1 + max(depth.values())