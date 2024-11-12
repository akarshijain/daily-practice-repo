class Solution:
    def __init__(self):
        self.subset = []
        self.result = []
        self.sum = 0
    # [1, 1, 1, 2, 2, 3]
    def dfs(self, index, candidates, target):
        if self.sum == target:
            self.result.append(self.subset.copy())
            return

        if index >= len(candidates) or self.sum > target:
            return

        self.sum += candidates[index]
        self.subset.append(candidates[index])
        self.dfs(index + 1, candidates, target)

        self.sum -= candidates[index]
        self.subset.pop()
        
        while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
            index += 1
        
        self.dfs(index + 1, candidates, target)

        return


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(0, candidates, target)
        return self.result