class Solution:
    def __init__(self):
        self.path = []
        self.permutations = []
        self.lookup = set()

    def dfs(self, index, nums):
        if index >= len(nums):
            self.permutations.append(self.path.copy())
            return

        for i in range(len(nums)):
            if nums[i] not in self.lookup:
                self.path.append(nums[i])
                self.lookup.add(nums[i])

                self.dfs(index + 1, nums)

                self.path.pop()
                self.lookup.remove(nums[i])
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.dfs(0, nums)
        return self.permutations