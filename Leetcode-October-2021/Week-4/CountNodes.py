# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_left_height(self, root):
        return 0 if root is None else 1 + self.get_left_height(root.left)

    def get_right_height(self, root):
        return 0 if root is None else 1 + self.get_right_height(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        left_height, right_height = self.get_left_height(
            root), self.get_right_height(root)

        if left_height == right_height:  # tree is 100% filled
            return 2**left_height - 1  # or 2**right_height - 1, they're equal

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)

obj = Solution()
res = obj.countNodes(tree)
print(res)
