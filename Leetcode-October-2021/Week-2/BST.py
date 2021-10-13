# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(down, up):
            if self.idx >= len(preorder):
                return None
            if not down <= preorder[self.idx] <= up:
                return None
            root = TreeNode(preorder[self.idx])
            self.idx += 1
            root.left = helper(down, root.val)
            root.right = helper(root.val, up)
            return root

        self.idx = 0
        return helper(-float("inf"), float("inf"))
