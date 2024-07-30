# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return (self.isSame(root.right, subRoot.right) \
                    and self.isSame(root.left, subRoot.left))

        return False
 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        if self.isSame(root, subRoot):
            return True

        return (self.isSubtree(root.right, subRoot) \
                    or self.isSubtree(root.left, subRoot))
