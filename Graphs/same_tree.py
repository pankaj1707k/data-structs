""" https://leetcode.com/problems/same-tree/ """

from typing import *
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    pl = []
    ql = []
    
    def bfs(root: Optional[TreeNode], l: List[int]):
        que = Queue()
        que.put(root)
        while not que.empty():
            node = que.get()
            l.append(node.val) if node else l.append(None)
            if node == None:
                continue
            if node.left==None and node.right==None:
                continue
            que.put(node.left)
            que.put(node.right)
    
    bfs(p, pl)
    bfs(q, ql)
    return pl == ql