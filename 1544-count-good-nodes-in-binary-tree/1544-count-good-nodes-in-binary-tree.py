# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 1

    def dfs(self, root, max_val):
        if not root:
            return

        if root.val >= max_val:
            max_val = root.val
            self.result += 1
        
        self.dfs(root.left, max_val)
        self.dfs(root.right, max_val)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.dfs(root.left, root.val)
        self.dfs(root.right, root.val)

        return self.result
