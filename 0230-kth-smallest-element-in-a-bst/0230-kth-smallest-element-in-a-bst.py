# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = -1
        self.count = 0

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)

        self.count -= 1
        if self.count == 0:
            self.result = root.val
            return
        
        self.dfs(root.right)

        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.dfs(root)
        return self.result

        