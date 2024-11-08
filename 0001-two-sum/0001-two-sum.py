class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_map:
                return [i, num_map[difference]]
            else:
                num_map[num] = i

        