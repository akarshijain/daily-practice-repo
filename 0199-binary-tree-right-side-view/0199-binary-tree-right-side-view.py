# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        node_q = deque()
        node_q.append(root)

        result = []
        result.append(root.val)

        while node_q:
            for i in range(len(node_q)):
                node = node_q.popleft()

                if node.right:
                    node_q.append(node.right)
                
                if node.left:
                    node_q.append(node.left)

            if node_q:
                result.append(node_q[0].val)

        return result