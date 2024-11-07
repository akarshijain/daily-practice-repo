# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node, max_val):
        if not node:
            return None

        if node.val >= max_val:
            max_val = node.val
            self.count += 1

        self.dfs(node.left, max_val)
        self.dfs(node.right, max_val)

        return None

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, float("-inf"))
        return self.count