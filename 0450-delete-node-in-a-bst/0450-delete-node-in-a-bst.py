# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMinNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node.left:
            return node

        return self.findMinNode(node.left)
        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        head = root

        if not root:
            return
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.findMinNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        return head

        