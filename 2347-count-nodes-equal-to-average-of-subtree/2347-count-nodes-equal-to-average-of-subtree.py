# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.num_average_nodes = 0

    def dfs(self, node):
        if not node:
            return 0, 0

        left_val, num_left_nodes = self.dfs(node.left)
        right_val, num_right_nodes = self.dfs(node.right)

        total_val = node.val + left_val + right_val
        total_nodes = 1 + num_left_nodes + num_right_nodes
        average_val = total_val // total_nodes

        if node.val == average_val:
            self.num_average_nodes += 1

        return total_val, total_nodes

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.num_average_nodes