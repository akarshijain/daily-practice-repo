# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer = []
        binary_tree_nodes_q = deque()

        if root:
            binary_tree_nodes_q.append(root)

        while len(binary_tree_nodes_q) > 0:
            level_order_traversal = []
            for i in range(len(binary_tree_nodes_q)):
                curr = binary_tree_nodes_q.popleft()
                level_order_traversal.append(curr.val)

                if curr.left:
                    binary_tree_nodes_q.append(curr.left)
                
                if curr.right:
                    binary_tree_nodes_q.append(curr.right)

            answer.append(level_order_traversal)

        return answer