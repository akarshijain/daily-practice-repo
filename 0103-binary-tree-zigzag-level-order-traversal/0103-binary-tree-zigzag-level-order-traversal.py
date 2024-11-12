# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        nodes_q = deque()
        nodes_q.append(root)

        level = -1
        while nodes_q:
            traversal = []
            level += 1
            for i in range(len(nodes_q)):
                curr = nodes_q.popleft()
                traversal.append(curr.val)

                if curr.left:
                    nodes_q.append(curr.left)

                if curr.right:
                    nodes_q.append(curr.right)

            if level % 2 == 0:
                result.append(traversal)
            else:
                result.append(traversal[-1::-1])

        return result



        