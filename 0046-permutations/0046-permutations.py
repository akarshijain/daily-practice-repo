class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        permutations = self.permute(nums[1:])
        all_permutations = []

        for permutation in permutations:
            for index in range(0, len(permutation) + 1):
                possible_permutes = permutation.copy()
                possible_permutes.insert(index, nums[0])
                all_permutations.append(possible_permutes)

        return all_permutations

