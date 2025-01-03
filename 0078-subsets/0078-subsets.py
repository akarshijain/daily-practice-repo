class Solution:
    def __init__(self):
        self.all_subsets = []
        self.subset = []

    def dfs(self, start, nums):
        # Add the current subset to the list of all subsets
        self.all_subsets.append(self.subset.copy())
        
        # Explore further subsets starting from the current index
        for i in range(start, len(nums)):
            self.subset.append(nums[i])  # Include nums[i] in the subset
            self.dfs(i + 1, nums)       # Recur with the next index
            self.subset.pop()           # Backtrack by removing nums[i]
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.dfs(0, nums)
        return self.all_subsets
