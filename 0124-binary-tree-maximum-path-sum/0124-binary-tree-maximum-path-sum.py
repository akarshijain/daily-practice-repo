# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def dfs(self, root):
        if not root:
            return 0

        rightSum = self.dfs(root.right)

        leftSum = self.dfs(root.left)

        subtreeSum = root.val + leftSum + rightSum
        maxBranchSum = root.val + max(leftSum, rightSum, 0)

        if subtreeSum >= maxBranchSum:
            subSum = subtreeSum
        else:
            subSum = maxBranchSum

        self.maxSum = max(self.maxSum, subSum)

        print(root.val, subtreeSum, maxBranchSum, self.maxSum)

        return maxBranchSum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxSum