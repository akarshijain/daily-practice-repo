# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0

    def getMaxDiameter(self, node):
        if not node:
            return 0

        left = self.getMaxDiameter(node.left)
        right = self.getMaxDiameter(node.right)

        self.max_diameter = max(self.max_diameter, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getMaxDiameter(root)
        return self.max_diameter
