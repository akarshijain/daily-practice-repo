class Solution:
    def __init__(self):
        self.index = 0
        self.subset_sum = 0
        self.subset = []
        self.answer = []

    def dfs(self, candidates, i, target):
        if i >= len(candidates):
            return

        if self.subset_sum > target:
            return

        if self.subset_sum == target:
            self.answer.append(self.subset.copy())
            return
        
        self.subset.append(candidates[i])
        self.subset_sum += candidates[i]
        self.dfs(candidates, i, target)

        self.subset.pop()
        self.subset_sum -= candidates[i]
        self.dfs(candidates, i + 1, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(candidates, self.index, target)
        
        return self.answer