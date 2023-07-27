from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Using dfs
        max_internal = float("-inf")
        max_branches = float("-inf")
        def max_in_branch(node):
            nonlocal max_internal
            if not node:
                return 0

            internal = max(max_in_branch(node.left) + node.val + max_in_branch(node.right), node.val, max_in_branch(node.left) + node.val, node.val + max_in_branch(node.right))
            max_internal = internal if internal > max_internal else max_internal

            return max(max_in_branch(node.left) + node.val, max_in_branch(node.right) + node.val, node.val)
        return max(max_in_branch(root), max_internal)

# Improved
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        left, right = self.helper(root.left), self.helper(root.right)
        self.res = max(self.res, root.val + left + right)
        return max(root.val + max(left, right), 0)
