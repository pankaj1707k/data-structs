""" https://leetcode.com/problems/most-frequent-subtree-sum/ """

from collections import defaultdict
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findFrequentTreeSum(root: Optional[TreeNode]) -> List[int]:
    subtree_sum = defaultdict(int)

    def dfs(node:Optional[TreeNode]):
        if node==None:  return
        subtree_sum[node] += node.val
        dfs(node.left)
        subtree_sum[node] += subtree_sum[node.left]
        dfs(node.right)
        subtree_sum[node] += subtree_sum[node.right]
    
    dfs(root)

    freq = defaultdict(int)
    for node,ssum in subtree_sum.items():
        if node==None: continue
        freq[ssum] += 1
    
    max_freq = max(freq.values())
    ans = [m for m in freq if freq[m]==max_freq]
    
    return ans