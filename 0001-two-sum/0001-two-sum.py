class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in nums_map:
                return [i, nums_map[difference]]
            nums_map[num] = i

        return [] 