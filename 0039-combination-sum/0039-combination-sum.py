class Solution:
    def __init__(self):
        self.all_combinations = []
        self.combination = []
        self.combination_sum = 0

    def dfs(self, index, target, nums):
        if index >= len(nums) or self.combination_sum > target:
            return

        if self.combination_sum == target:
            self.all_combinations.append(self.combination.copy())
            return

        self.combination.append(nums[index])
        self.combination_sum += nums[index]
        self.dfs(index, target, nums)

        self.combination.pop()
        self.combination_sum -= nums[index]
        self.dfs(index + 1, target, nums)

        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(0, target, candidates)
        return self.all_combinations