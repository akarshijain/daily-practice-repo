# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        node_q = deque()
        node_q.append(root)

        level_order_values = []

        while node_q:
            nodes_in_level = []

            for i in range(len(node_q)):
                node = node_q.popleft()
                nodes_in_level.append(node.val)

                if node.left:
                    node_q.append(node.left)
                
                if node.right:
                    node_q.append(node.right)

            level_order_values.append(nodes_in_level)

        return level_order_values

