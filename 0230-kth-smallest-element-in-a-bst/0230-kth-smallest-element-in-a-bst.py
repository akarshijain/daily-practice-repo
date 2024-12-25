# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def dfs(self, node):
        if not node:
            return None

        left = self.dfs(node.left)

        self.result.append(node.val)

        right = self.dfs(node.right)

        return node

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root)
        print(self.result)
        return self.result[k - 1]