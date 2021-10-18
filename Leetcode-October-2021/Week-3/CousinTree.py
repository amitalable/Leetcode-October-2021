# https://leetcode.com/problems/cousins-in-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = [(root, 0, None)]
        level_x, level_y = -1, -1
        parent_x, parent_y = 0, 0
        while stack:
            curr, level, parent = stack.pop(0)
            if curr.val == x:
                level_x = level
                parent_x = parent.val if parent else None
            elif curr.val == y:
                level_y = level
                parent_y = parent.val if parent else None

            if level_x != -1 and level_y != -1:
                break

            if curr.left:
                stack.append((curr.left, level + 1, curr))

            if curr.right:
                stack.append((curr.right, level+1, curr))

        if level_x == level_y and parent_x != parent_y:
            return True
        return False
