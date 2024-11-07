# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, min_val, max_val):
        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        left = self.dfs(node.left, min_val, node.val)
        right = self.dfs(node.right, node.val, max_val)

        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))