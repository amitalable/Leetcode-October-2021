# https://leetcode.com/problems/invert-binary-tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = [root]
      
        
        while stack:
            cur = stack.pop(0)
            if cur.left and cur.right:
                x = cur.left
                cur.left = cur.right
                cur.right = x
                stack.append(cur.left)
                stack.append(cur.right)
            elif cur.left:
                cur.right = cur.left
                cur.left = None
                stack.append(cur.right)
            elif cur.right:
                cur.left = cur.right
                cur.right = None
                stack.append(cur.left)
        return root
            
                
        