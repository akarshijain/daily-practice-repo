# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0, True

        left, isBalanced_left = self.dfs(node.left)
        right, isBalanced_right = self.dfs(node.right)

        if not isBalanced_left or not isBalanced_right or abs(left - right) > 1:
            return 0, False

        return 1 + max(left, right), True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]