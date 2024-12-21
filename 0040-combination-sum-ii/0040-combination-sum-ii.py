class Solution:
    def __init__(self):
        self.all_subsets = []
        self.subset = []
        self.combination_sum = 0

    def dfs(self, index, nums, target):
        if self.combination_sum == target:
            self.all_subsets.append(self.subset.copy())
            return

        if index >= len(nums) or self.combination_sum > target:
            return

        self.subset.append(nums[index])
        self.combination_sum += nums[index]
        self.dfs(index + 1, nums, target)

        self.subset.pop()
        self.combination_sum -= nums[index]
        while (index + 1) < len(nums) and nums[index] == nums[index + 1]:
            index += 1

        self.dfs(index + 1, nums, target)
        return
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(0, candidates, target)
        return self.all_subsets
