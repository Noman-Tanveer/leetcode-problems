from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p or q) and (not (p and q)):
            return False
        def dfs(root1, root2):
            if root1.val == root2.val:
                if root1.left and root2.left and root1.right and root2.right:
                    return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
                elif root1.left and root2.left and not (root1.right or root2.right):
                    return dfs(root1.left, root2.left)
                elif root1.right and root2.right and not (root1.left or root2.left):
                    return dfs(root1.right, root2.right)
                elif not (root1.left or root2.left or root1.right or root2.right):
                    return True
                else:
                    return False
            return False
        return dfs(p, q)
