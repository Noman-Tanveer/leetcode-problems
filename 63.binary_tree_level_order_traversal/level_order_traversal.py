from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        res = []
        nds = [[root]]
        while nds:
            nxt_lvl = []
            lvl_res = []
            lvl_nds = nds.pop()
            for node in lvl_nds:
                lvl_res.append(node.val)
                if node.left:
                    nxt_lvl.append(node.left)
                if node.right:
                    nxt_lvl.append(node.right)
            res.append(lvl_res)
            if nxt_lvl:
                nds.insert(0, nxt_lvl)
        return res
