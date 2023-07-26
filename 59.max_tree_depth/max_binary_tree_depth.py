from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        max_depth = 1
        while stack:
            nd = stack.pop()
            cur = nd[0]
            depth = nd[1]
            if cur.right:
                stack.append([cur.right, depth+1])
                max_depth = depth+1 if depth+1 > max_depth else max_depth
            if cur.left:
                stack.append([cur.left, depth+1])
                max_depth = depth+1 if depth+1 > max_depth else max_depth

        return max_depth
