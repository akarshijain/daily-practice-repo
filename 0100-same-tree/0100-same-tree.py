# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, first_tree, second_tree):
        if not first_tree and not second_tree:
            return True

        if not first_tree or not second_tree:
            return False

        if first_tree.val != second_tree.val:
            return False

        left = self.dfs(first_tree.left, second_tree.left)
        right = self.dfs(first_tree.right, second_tree.right)

        if not left or not right:
            return False

        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)