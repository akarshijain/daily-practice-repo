class Solution:
    def __init__(self):
        self.sum = 0
        self.subset = []
        self.result = []

    def dfs(self, index, candidates, target):
        if self.sum > target or index >= len(candidates):
            return

        if self.sum == target:
            self.result.append(self.subset.copy())
            return
        
        self.sum += candidates[index]
        self.subset.append(candidates[index])
        self.dfs(index, candidates, target)

        self.sum -= candidates[index]
        self.subset.pop()
        self.dfs(index + 1, candidates, target)

        return
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(0, candidates, target)
        return self.result