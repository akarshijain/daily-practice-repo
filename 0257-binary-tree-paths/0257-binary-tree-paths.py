# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []
        self.unique_paths = []

    def dfs(self, node):
        if not node:
            return

        self.path.append(str(node.val))

        if not node.left and not node.right:
            self.unique_paths.append("->".join(self.path))

        self.dfs(node.left)
        self.dfs(node.right)

        self.path.pop()
        return

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.dfs(root)
        return self.unique_paths