# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, min_val, max_val, node):
        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        left = self.dfs(min_val, node.val, node.left)
        right = self.dfs(node.val, max_val, node.right)

        return left and right


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(float("-inf"), float("inf"), root)
        