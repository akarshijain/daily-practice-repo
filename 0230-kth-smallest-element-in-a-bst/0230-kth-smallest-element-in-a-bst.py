# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder = []
    
    def inorderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.inorderTraversal(root.left)
        self.inorder.append(root.val)
        self.inorderTraversal(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorderTraversal(root)
        return self.inorder[k-1]