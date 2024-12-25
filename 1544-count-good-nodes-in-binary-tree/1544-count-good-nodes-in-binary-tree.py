# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.good_nodes_count = 0

    def dfs(self, max_val, curr_node):
        if not curr_node:
            return

        if curr_node.val >= max_val:
            self.good_nodes_count += 1
            max_val = max(max_val, curr_node.val)

        self.dfs(max_val, curr_node.left)
        self.dfs(max_val, curr_node.right)

        return

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(float("-inf"), root)
        return self.good_nodes_count