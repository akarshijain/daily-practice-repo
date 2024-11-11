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
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.dfs(index + 1, nums)

        return 

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.dfs(0, nums)
        return self.result