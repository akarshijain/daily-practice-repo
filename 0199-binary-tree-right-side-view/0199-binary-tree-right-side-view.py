# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes_q = deque()
        answer = []

        if root:
            nodes_q.append(root)

        while len(nodes_q) > 0:
            nodes_at_level = []
            for i in range(len(nodes_q)):
                curr = nodes_q.popleft()
                nodes_at_level.append(curr.val)

                if curr.right:
                    nodes_q.append(curr.right)

                if curr.left:
                    nodes_q.append(curr.left)

            answer.append(nodes_at_level[0])

        return answer

            
