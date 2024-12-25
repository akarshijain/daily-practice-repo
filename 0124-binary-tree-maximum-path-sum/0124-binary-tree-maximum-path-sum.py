# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float("-inf")

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        node_sum = node.val + left + right
        branch_sum = node.val + max(left, right, 0)

        self.max_sum = max(self.max_sum, node_sum, branch_sum)

        return branch_sum


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_sum