class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in num_index_map:
                return [i, num_index_map[difference]]

            else:
                num_index_map[num] = i