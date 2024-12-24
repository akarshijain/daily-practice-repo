# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return None

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        node.left = right
        node.right = left

        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)
        