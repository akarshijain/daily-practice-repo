# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inRange(self, root, leftBoundary, rightBoundary):
        if not root:
            return True

        if not (leftBoundary < root.val < rightBoundary):
            return False

        return self.inRange(root.right, root.val, rightBoundary) \
               and self.inRange(root.left, leftBoundary, root.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.inRange(root, float("-inf"), float("inf"))