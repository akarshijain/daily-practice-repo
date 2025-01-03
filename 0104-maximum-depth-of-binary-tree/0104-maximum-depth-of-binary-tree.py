# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        return 1 + max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)