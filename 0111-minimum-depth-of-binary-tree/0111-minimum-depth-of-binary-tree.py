# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_depth = 1

        nodes_q = deque()
        nodes_q.append(root)
        
        while nodes_q:
            for i in range(len(nodes_q)):
                node = nodes_q.popleft()

                if not node.right and not node.left:
                    return min_depth

                if node.left:
                    nodes_q.append(node.left)

                if node.right:
                    nodes_q.append(node.right)

            min_depth += 1

        return min_depth
