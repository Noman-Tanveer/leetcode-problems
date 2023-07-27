from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        que = []
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            if len(que) == k:
                return
            que.append(node.val)
            in_order(node.right)
        in_order(root)
        return que[-1]
