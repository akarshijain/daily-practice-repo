class Solution:
    def __init__(self):
        self.subset = []
        self.result = []

    def dfs(self, index, nums):
        if index >= len(nums):
            self.result.append(self.subset.copy())
            return

        self.subset.append(nums[index])
        self.dfs(index + 1, nums)

        self.subset.pop()
        self.dfs(index + 1, nums)

        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.dfs(0, nums)
        return self.result
        